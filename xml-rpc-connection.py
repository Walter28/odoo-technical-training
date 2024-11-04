import xmlrpc.client

url = 'http://localhost:8069'
username = 'admin'
password = 'admin'
db = 'odoo_db'

# end point that odoo use for xmlrpc conn
# this endpoint is used to fetch version info and to make auth calls
# DONNOT NEED TO AUTH BFR MAKING REQUEST
# endpoint => 'xmlrpc/2/common'

# Connexion au server
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
print(f"Common : {common}")

# Authentication
user_uid = common.authenticate(db, username, password, {})
print("User ID:", user_uid)

# Used to call method of odoo via the 'execute_kw' func
# Params of execute_rpc => (db, uid, pwd, model_name, method_name:str, [], {})
# endpoint => 'xmlrpc/2/object'
# here we'll use the "search" method in ou estate.property
# [[]] => for showing all, [[[]]] => i u wanna add search conding, put it inside the 3th braquet

models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
# search method
property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search', [[]])
print('Properties list : ', property_ids)
# count method
count_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search_count', [[]])
print('Properties count : ', count_property_ids)
# read method, with needed field setup for output [HERE WE USE READ WHEN ALREADY SEARCH BFR
read_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'read', [property_ids], {'fields': ['name']})
print('Read properties : ', read_property_ids)
# read method + search in the same time
search_read_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search_read', [], {'fields': ['name']})
print('Search Read properties : ', search_read_property_ids)
# create method
# sales_id => mandatory field [the id of the sales person]
# create_property_id = models.execute_kw(db, user_uid, password, 'estate.property', 'create', [{'name' : 'Property from RPC', 'res_users_id' : 6, 'expected_price' : 5000}])
# print('Create property : ', create_property_id)
# write method
# write_property_id = models.execute_kw(db, user_uid, password, 'estate.property', 'write', [[8], {'name': 'Property from RPC Updated'}])
# read_name_get = models.execute_kw(db, user_uid, password, 'estate.property', 'name_get', [[8]])
# print('Write property : ', read_name_get)
# unlink method
# unlink_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'unlink', [[8]])
# print('Unlink property : ', unlink_property_ids)


# USE PAGINATION WHEN U HAV A THOUSAND OF RECORD

# search method
property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search', [[]], {'offset': 0, 'limit': 1})
print('Properties list : ', property_ids)