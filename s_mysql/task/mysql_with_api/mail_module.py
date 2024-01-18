# 구글 앱 비번 - rpwr mtuf kdne iudu
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email, certification_number):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "ghk495892@gmail.com"
    receiver_email = email
    password = "rpwr mtuf kdne iudu"
    message = f"<h1>{certification_number}</h1>"

    msg = MIMEText(message, 'html')
    data = MIMEMultipart()
    data.attach(msg)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, data.as_string())
