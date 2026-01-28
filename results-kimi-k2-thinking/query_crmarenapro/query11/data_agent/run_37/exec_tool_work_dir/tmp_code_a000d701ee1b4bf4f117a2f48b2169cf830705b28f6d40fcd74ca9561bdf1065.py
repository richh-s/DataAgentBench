code = """import json

# Get data from storage
rl1 = locals()['var_functions.query_db:0']  # AI products
rl2 = locals()['var_functions.query_db:5']  # Contact info
rl4 = locals()['var_functions.query_db:8']  # Product IDs from orders

# Extract contact's account ID (handle potential # prefix)
contact_account_id = rl2[0]['AccountId'].lstrip('#')

# Identify AI products from the orders
ai_product_ids = [item['Product2Id'] for item in rl4]

# Find which AI products match our list of AI-related products
ai_products_in_catalog = {item['Id']: item['Name'] for item in rl1}
matching_ai_products = []

for product_id in ai_product_ids:
    if product_id in ai_products_in_catalog:
        matching_ai_products.append({
            'ProductId': product_id,
            'ProductName': ai_products_in_catalog[product_id]
        })

print('__RESULT__:')
print(json.dumps(matching_ai_products[0]['ProductId'] if matching_ai_products else None))"""

env_args = {'var_functions.query_db:0': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift', 'Description': 'Dynamic AI-powered design tool shifting paradigms in circuit creation.'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision', 'Description': 'AI-powered optical design tool for developing efficient light-based components.'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator', 'Description': 'AI-enhanced circuit design tool for innovative electronic development.'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro', 'Description': 'AI-enhanced design tool for seamless circuit synchronization and development.'}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy', 'Description': 'All-inclusive training platform for EDA tools with interactive learning modules.'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance', 'Description': 'Advanced educational platform providing expert training in modern EDA tools.'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub', 'Description': 'Innovative training platform offering advanced EDA courses and certifications.'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager', 'Description': 'Enhanced power optimization tools for sustainable electronics development.'}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  ', 'Description': 'Eco-conscious PCB design platform focusing on sustainable materials.'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite', 'Description': 'Robust training platform for mastering EDA tools with hands-on labs.'}], 'var_functions.query_db:2': [{'Id': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'Status': 'Activated  ', 'EffectiveDate': '2021-06-15', 'OwnerId': '#005Wt000003NJ53IAG'}, {'Id': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'Status': 'Activated', 'EffectiveDate': '2021-06-01', 'OwnerId': '005Wt000003NJmcIAG'}, {'Id': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'Status': 'Activated', 'EffectiveDate': '2021-06-01', 'OwnerId': '005Wt000003NHzJIAW'}], 'var_functions.query_db:5': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_functions.query_db:6': [{'Id': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'Status': 'Activated  ', 'EffectiveDate': '2021-06-15', 'OwnerId': '#005Wt000003NJ53IAG', 'OrderItemId': '802Wt0000079AU1IAM', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'Id': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'Status': 'Activated', 'EffectiveDate': '2021-06-01', 'OwnerId': '005Wt000003NJmcIAG', 'OrderItemId': '#802Wt00000797O2IAI', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '5.0', 'UnitPrice': '379.9905'}, {'Id': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'Status': 'Activated', 'EffectiveDate': '2021-06-01', 'OwnerId': '005Wt000003NJmcIAG', 'OrderItemId': '802Wt00000795XxIAI', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '7.0', 'UnitPrice': '569.9905'}, {'Id': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'Status': 'Activated', 'EffectiveDate': '2021-06-01', 'OwnerId': '005Wt000003NHzJIAW', 'OrderItemId': '#802Wt0000079AQlIAM', 'Product2Id': '01tWt000006hV57IAE', 'Quantity': '20.0', 'UnitPrice': '424.9915'}, {'Id': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'Status': 'Activated', 'EffectiveDate': '2021-06-01', 'OwnerId': '005Wt000003NHzJIAW', 'OrderItemId': '802Wt00000796euIAA', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '15.0', 'UnitPrice': '539.991'}], 'var_functions.query_db:8': [{'Product2Id': '01tWt000006hV8LIAU'}]}

exec(code, env_args)
