from os import getenv
from time import sleep

from dotenv import load_dotenv
from pymongo import MongoClient

from fediseer_alerts.models import ActivityReport, Report_Type, Report_Activity

load_dotenv()

from requests import get

from slack_sdk.webhook import WebhookClient

webhook = False

if getenv('SLACK_WEBHOOK_URL'):
    webhook = WebhookClient(getenv('SLACK_WEBHOOK_URL'))

db = MongoClient(getenv('MONGO_URI'))['fediseer-notifications']['censures']


def start():
    print("Starting...")
    while True:
        censures = get_censures()
        if len(censures) > 0:
            print("Censures found")
            for c in censures:
                censure = ActivityReport(
                    source_domain=c['source_domain'],
                    target_domain=c['target_domain'],
                    report_type=Report_Type(c['report_type']),
                    report_activity=Report_Activity(c['report_activity']),
                    created=c['created'],
                )
                found_censure = db.find_one(
                    {
                        "$and": [
                            {"created": censure.created},
                            {"source_domain": censure.source_domain},
                            {"target_domain": censure.target_domain},
                            {"report_type": censure.report_type.value},
                            {"report_activity": censure.report_activity.value},
                        ]
                    }
                )
                if not found_censure:
                    db.insert_one(
                        {
                            "created": censure.created,
                            "source_domain": censure.source_domain,
                            "target_domain": censure.target_domain,
                            "report_type": censure.report_type.value,
                            "report_activity": censure.report_activity.value,
                        }
                    )
                    print(f"New censure found: {str(censure)}")
                    if webhook:
                        webhook.send(
                            text=f"From: {censure.source_domain}\n"
                            f"To: {censure.report_activity.value}\n"
                            f"Action{censure.target_domain}"
                        )

        else:
            print("No censures found")
        print("Waiting 60 seconds...")
        sleep(60)


def get_censures():
    response = get('https://fediseer.com/api/v1/reports?report_type=CENSURE&page=1')
    if response.status_code == 200:
        return response.json()
    else:
        return []
