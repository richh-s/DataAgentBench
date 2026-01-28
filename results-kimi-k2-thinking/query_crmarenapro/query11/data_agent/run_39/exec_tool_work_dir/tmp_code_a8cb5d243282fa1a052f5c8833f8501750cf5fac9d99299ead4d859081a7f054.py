code = """import json
# Get the orders from storage
orders = locals().get('var_functions.query_db:2', [])

# Print the search information we have
print('__RESULT__:')
print(json.dumps({'contact_id': '003Wt00000Jqy8SIAR', 
                  'account_id': '#001Wt00000PGXrNIAX',
                  'orders_found': orders,
                  'message': 'No June 2021 orders found for this account'}))"""

env_args = {'var_functions.query_db:0': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_functions.query_db:2': []}

exec(code, env_args)
