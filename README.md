# Abuse Mail Checker

This script will check for the given email ( unread, all folders ) for lemmy URLs, comments or posts.  
It will automatically remove those preemtively and send out a slack(optional) and email notification.  

To configure it rename .env_example to .env and put your wanted variables in it.

# Install
pip install . --upgrade

# Run Docker
task docker
