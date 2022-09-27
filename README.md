# ONLY FOR WINDOWS OPERATING SYSTEM
# Youtube Mix Url Capture

A python script that mails the external ip changes using gmail

## Requirements

This script has been written for and only Windows.

- [requests]
- [smtplib]
- [ssl]
- [email.message]
- [time]

# Install

Install Python --> download the latest version from python.org

OPEN A CMD COMMAND LINE

````
py -m pip install requests
py -m pip install smtplib
py -m pip install ssl
py -m pip install email.message
````

## Usage

in Windows Powershell
```
~\> py .\ip_change_mail.py
```
in CMD
```
~\> py ip_change_mail.py
```

### Arguments

NO ARGUMENTS NEEDED

### Warnings

Please make sure you change "email_sender" and "email_password" to your gmail and password. 
For more please follow "https://towardsdev.com/using-python-to-send-email-using-gmail-38afce31174a" guide

