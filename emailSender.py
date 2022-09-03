from email.message import EmailMessage
import ssl
import smtplib
from password import appPassword

email_sender = 'kleierferris@gmail.com'
email_password = appPassword
email_reciever = 'ferris@uldagon.com'

subject = "Hello there"
body = """
This was sent via Python
"""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())