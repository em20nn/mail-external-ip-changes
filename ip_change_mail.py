from requests import get
import requests
import smtplib
import ssl
from email.message import EmailMessage
import time
email_sender = 'your@mail.com'
email_password = 'yourpassword'
email_receiver = email_sender
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = 'IP'

startup=True
while startup:
    try:
        ip_startup = get('https://api.ipify.org').content.decode('utf8')
    except:
        try:
            ip_startup = requests.get('https://www.wikipedia.org').headers['X-Client-IP']
        except:
            ip_startup = "ERROR"
    if ip_startup=="ERROR":
        time.sleep(120)
    elif ip_startup!="ERROR":
        startup=False


body = f"""Ip adress : {ip_startup}"""
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
time.sleep(120)

first=True
while True:
    try:
        ip = get('https://api.ipify.org').content.decode('utf8')
    except:
        try:
            ip = requests.get('https://www.wikipedia.org').headers['X-Client-IP']
        except:
            ip = "ERROR"
    if ip=="ERROR":
        while first:
            body = f"""Ip adress : {ip}"""
            em.set_content(body)
            context = ssl.create_default_context()
            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())
            except:
                time.sleep(0)
            ip_startup=ip
            is_error=True
            time.sleep(120)
            first=False
    elif ip_startup==ip:
        first=True
        time.sleep(120)
        continue
    elif ip_startup!=ip:
        first=True
        if is_error==True:
            body = f"""IP: AFTER ERROR"""
            em.set_content(body)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            is_error=False
        ip_startup=ip
        body = f"""Ip adress : {ip}"""
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        time.sleep(120)