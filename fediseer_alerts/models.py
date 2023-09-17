import enum


class Report_Type(enum.Enum):
    GUARANTEE = "GUARANTEE"
    ACTIVITY = "ACTIVITY"
    CENSURE = "CENSURE"
    HESITATION = "HESITATION"


class Report_Activity(enum.Enum):
    ADDED = "ADDED"
    DELETED = "DELETED"
    MODIFIED = "MODIFIED"


class ActivityReport:
    source_domain: str
    target_domain: str
    report_type: Report_Type
    report_activity: Report_Activity
    created: str

    def __init__(
        self,
        source_domain: str,
        target_domain: str,
        report_type: Report_Type,
        report_activity: Report_Activity,
        created: str,
    ):
        self.source_domain = source_domain
        self.target_domain = target_domain
        self.report_type = report_type
        self.report_activity = report_activity
        self.created = created
