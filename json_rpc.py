import json
import random
import urllib.request
from http.client import responses

odoo_url = 'http://localhost:8069'
username = 'admin'
password = 'admin'
db = 'odoo_db'

def json_rpc(url, method, params):
    data = {
        'jsonrpc': '2.0',
        'method': method,
        'params': params,
        'id': random.randint(0, 1000000000)
    }

    headers = {
        'Content-Type': 'application/json'
    }

    # make the call
    req = urllib.request.Request(
        url=url,
        data=json.dumps(data).encode(),
        headers=headers
    )

    res = json.loads(
        urllib.request.urlopen(req).read().decode("UTF-8")
    )

    if res.get('error'):
        raise Exception(res['error'])
    return res['result']

def call(url, service, method, *args):
    return json_rpc(f"{url}/jsonrpc", "call", {'service': service, 'method': method, 'args': args})

# authenticate, we use "common" service to authenticate
user_id = call(odoo_url, "common", "login", db, username, password)
print("User id : ", user_id)

# Create a property using this jsonrpc
vals = {
    "name" : "Property from JSON",
    "res_users_id": 6,
    "expected_price": 10000
}
## we use "object" service to male ORM calls
# create_property = call(odoo_url, "object", "execute", db, user_id, password, 'estate.property', 'create', vals)
# print("Create property : ", create_property)
## Read the property we have just finish to create
read_property = call(odoo_url, "object", "execute", db, user_id, password, 'estate.property', 'read', [9])
print("Read property : ", read_property)
