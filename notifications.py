##########################################################
# Slack notifications
##########################################################
from config import *
import requests
import json
def slack_notification(message):
    slack_data = {'text': "{}".format(message)}
    response = requests.post(slack["slack_webhook"], data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})

##########################################################
# E-mail notifications
##########################################################
def email_notification(message):
    import smtplib

    smtpObj = smtplib.SMTP(email_smtp_server)
    smtpObj.sendmail(email_sender, email_receiver, message)
