import logging
import smtplib
from email.mime.text import MIMEText

logging.config.fileConfig('config/logging.yaml')
logger = logging.getLogger('advertisex')

def send_alert_email(subject, message, recipient):
    sender = "alerts@advertisex.com"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        with smtplib.SMTP('localhost') as server:
            server.sendmail(sender, [recipient], msg.as_string())
    except Exception as e:
        logger.error(f"Failed to send alert email: {e}")

def monitor_errors(log_file):
    with open(log_file) as f:
        for line in f:
            if 'ERROR' in line:
                send_alert_email("Error Alert", line, "alerts@advertisex.com")

if __name__ == "__main__":
    monitor_errors("logs/error.log")
