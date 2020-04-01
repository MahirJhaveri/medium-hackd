import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

# code which runs upon import of this module
def init_connection():
    creds = credentials.Certificate('./keys/medium-hackd-analytics-firebase-adminsdk-key.json')
    firebase_admin.initialize_app(creds)
    db = firestore.client()
    return db

### Variables

# The database object
db = init_connection()
stats_ref = db.collection(u'requests').document(u'statistics')

### Methods

@firestore.transactional
def write_request_transaction(transaction, ip, article, status_code):
    snapshot = stats_ref.get(transaction=transaction)
    transaction.update(stats_ref, {
        u'count': snapshot.get(u'count') + 1
    })
    new_doc_ref = db.collection(u'requests').document()
    transaction.set(new_doc_ref, {
        u'ip': ip,
        u'date': datetime.datetime.now(),
        u'article': article,
        u'status_code': status_code
    })

# Write request data
# Called in server.py
def write_request_data(ip, article, status_code):
    write_request_transaction(db.transaction(), ip, article, status_code)



