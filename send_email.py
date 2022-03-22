import smtplib
from email.message import EmailMessage


def send_email(content):
    msg = EmailMessage()
    msg.set_content(content)
    recipients = ['x@x.x']
    msg['From'] = 'x@x.x'
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = 'New Bill(s)'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('email address', 'password')
    server.send_message(msg)
    server.quit()
