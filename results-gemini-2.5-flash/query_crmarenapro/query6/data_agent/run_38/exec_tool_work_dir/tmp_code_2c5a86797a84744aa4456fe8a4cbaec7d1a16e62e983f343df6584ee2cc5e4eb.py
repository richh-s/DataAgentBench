code = """quote_line_items = locals()['var_function-call-2266200642641341188']
product_active_status = locals()['var_function-call-8748175222428396554']

product_ids_in_quote = {item['Product2Id'].replace('#', '') for item in quote_line_items}
active_product_ids = {item['Id'].replace('#', '') for item in product_active_status if item['IsActive'] == '1'}

inactive_products_in_quote = product_ids_in_quote - active_product_ids

# Print the list of inactive products in the quote
print('__RESULT__:')
print(list(inactive_products_in_quote))"""

env_args = {'var_function-call-2266200642641341188': [{'Quantity': '3.0', 'UnitPrice': '349.99', 'Product2Id': '#01tWt000006hV6jIAE'}, {'Quantity': '2.0', 'UnitPrice': '529.99', 'Product2Id': '01tWt000006hV8LIAU'}, {'Quantity': '4.0', 'UnitPrice': '299.99', 'Product2Id': '#01tWt000006hPffIAE'}, {'Quantity': '35.0', 'UnitPrice': '399.99', 'Product2Id': '01tWt000006hVczIAE'}], 'var_function-call-16172532657386427047': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-6439532908540786458': [], 'var_function-call-8748175222428396554': [{'Id': '01tWt000006hV8LIAU', 'IsActive': '1'}, {'Id': '01tWt000006hVczIAE', 'IsActive': '1'}]}

exec(code, env_args)
