#!/usr/bin/env python
from pymongo import MongoClient
import smtplib

def checkThreshold():
    client = MongoClient('172.34.0.3', 27017)
    db = client['test']['access']
    alert = db.count({'$and': [ {'user': 'admin'}, {'code' : '401'}]})
    if (alert > 10):
        sendEmail()
    return


def sendEmail():
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("reachashok9538053428@gmail.com", "Ashok#1997")
    s.sendmail("reachashok9538053428@gmail.com", "ashok.kammala@gmail.com", "TOO MANY AUTH FAILURES BY ADMIN")
    s.quit()
    return


checkThreshold()
