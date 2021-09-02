"""
135. Sending Emails with Python
"""
from smtplib import SMTP
from getpass import getpass

if __name__ == "__main__":
    smtp_object = SMTP("smtp.gmail.com", 587)
    print(smtp_object.ehlo())
    print(smtp_object.starttls())
    password = getpass("Email password: ")
