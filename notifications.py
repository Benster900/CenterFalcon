##########################################################
# Slack notifications
##########################################################
import config
def slack_notification(message):
    import requests
    data = urllib.urlencode({'payload': '{"text": {}"}'.format(message)})
    r = requests.post(slack_webhook, json=data)

##########################################################
# E-mail notifications
##########################################################
def email_notification(message):
    import smtplib

    smtpObj = smtplib.SMTP(email_smtp_server)
    smtpObj.sendmail(email_sender, email_receiver, message)
