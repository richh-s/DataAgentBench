code = """import json
# Get the account ID from the previous query
contact_result = locals()['var_functions.query_db:7']
account_id = contact_result[0]['AccountId']
print('__RESULT__:')
print(json.dumps({'account_id': account_id}))"""

env_args = {'var_functions.query_db:7': [{'AccountId': '#001Wt00000PGXrNIAX'}], 'var_functions.list_db:8': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:10': [], 'var_functions.query_db:12': []}

exec(code, env_args)
