
from dotenv import load_dotenv
import os
import time


# DEPRECATED:
# File no longer used in server.py 

load_dotenv()

def load_cookies():
    cookie_data = cookie_data = [
        {
            "key": "uid",
            "value": os.getenv("UID"),
            "domain": ".medium.com",
            "path": "/",
            "expires": None
        },
        {
            "key": "sid",
            "value": os.getenv("SID"),
            "domain": ".medium.com",
            "path": "/",
            "expires": None
        }
    ]
    uid_exp = os.getenv("UID_EXP").split(",")
    sid_exp = os.getenv("SID_EXP").split(",")
    cookie_data[0]["expires"] = str(time.mktime((int(uid_exp[0]), int(uid_exp[1]), int(
        uid_exp[2]), int(uid_exp[3]), int(uid_exp[4]), int(uid_exp[5]), 0, 0, 0)))
    cookie_data[1]["expires"] = str(time.mktime((int(sid_exp[0]), int(sid_exp[1]), int(
        sid_exp[2]), int(sid_exp[3]), int(sid_exp[4]), int(sid_exp[5]), 0, 0, 0)))
    return cookie_data
