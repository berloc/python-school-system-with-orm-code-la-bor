import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models import *


class EmailSender:
    user = 'codelabor1@gmail.com'
    password = 'Codelabor1234'
    to_address = 'codelabor1@gmail.com'
    body = "\r\n".join([
      "Why, oh why",
      "Why, oh why",
      "Why, oh why"
      ])

    @classmethod
    def email_send(cls):
        user = cls.user
        to_address = cls.to_address
        password = cls.password
        body = cls.body
        message = MIMEMultipart()
        message['From'] = user
        message['To'] = to_address
        message['Subject'] = "Welcome"
        body = cls.body
        message.attach(MIMEText(body, 'plain'))
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(user, password)
            server.sendmail(user, to_address, message.as_string())
            print("Send")
            server.quit()
        except:
            print("Sending failed!")

EmailSender.email_send()
