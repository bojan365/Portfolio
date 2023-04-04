import yagmail
import os
import smtplib
import ssl


HOST_NAME = "mail.stojkovici.com"
HOST_PORT = 465
MAIL_FROM = "bojan@stojkovici.com"
MAIL_TO = "bojan@stojkovici.com"
MAIL_PASS = "SavaNikiMiki88"
MAIL_SUBJECT = "Contact Form Portfolio Bojan"


def send_email_smtplib(result):
    host = "mail.stojkovici.com"
    port = 465
    username = "bojan@stojkovici.com"
    password = "SavaNikiMiki88"
    receiver = "bojan@stojkovici.com"

    message = result['message']
    name = result['name']
    email_sender = result['email']
    msg = f"""Dobili ste poruku sa Portfolio Bojan stranice:\n
    Ime: {name}
    Email-sender: {email_sender}\n\n
    Poruka: \n{message}"""

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg)


def yag_mail(result):
    sender = MAIL_FROM
    receiver = MAIL_TO
    subject = MAIL_SUBJECT

    contents = result['message']
    yag = yagmail.SMTP(user=sender, password=MAIL_PASS)
    yag.send(to=receiver, subject=subject, contents=contents)
