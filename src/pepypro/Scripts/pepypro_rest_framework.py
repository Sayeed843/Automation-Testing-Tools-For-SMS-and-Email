import requests
import json

ENDPOINT1 = "http://127.0.0.1:8000/api/pepypro/emails/"
ENDPOINT2 = "http://127.0.0.1:8000/api/pepypro/messages/"


def email_do (method = 'get', data={}, id=3, is_json=True):
    headers = {}
    if is_json:
        headers['content-type']='application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT1, data=data, headers= headers)
    print(r.text)
    print(r.status_code)
    return r

email_do(method='post', data={"user_name":"Mamun",
                              "campaign_name":"Sayeed New Campaign",
                              "api_key":"ksjbdlknbakjdsndsakn",
                              "sender_email":"sayeed@gmail.com",
                              "receiver_email":"lead@gmail.com",
                              "email_subject":"New Subject",
                              "email_body":"Email Body"})

print("\n\n Now Message")

def message_do (method = 'get', data={}, id=2, is_json=True):
    headers = {}
    if is_json:
        headers['content-type']='application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT2, data=data, headers= headers)
    print(r.text)
    print(r.status_code)
    return r

message_do(method='post', data={"user_name":"Sayeed",
                              "campaign_name":"Sayeed New Campaign",
                              "api_key":"ksjbdlknbakjdsndsakn",
                              "sender_number":"1234567890",
                              "receiver_number":"1023456789",
                              "mess_body":"Email Body"})
