code = """import json

contracts = locals()['var_function-call-3368095588372396259']
orders = locals()['var_function-call-1184197430398516886']
order_items = locals()['var_function-call-1184197430398514381']

def clean_id(i):
    if i and isinstance(i, str):
        return i.lstrip('#')
    return i

# 1. Eligible Account IDs
eligible_account_ids = set()
for c in contracts:
    if c.get('AccountId'):
        eligible_account_ids.add(clean_id(c['AccountId']))

# 2. Eligible Orders and Map to Owner
eligible_orders = {} # order_id -> owner_id
for o in orders:
    acc_id = clean_id(o.get('AccountId'))
    if acc_id in eligible_account_ids:
        order_id = clean_id(o.get('Id'))
        owner_id = clean_id(o.get('OwnerId'))
        eligible_orders[order_id] = owner_id

# 3. Calculate Totals
owner_sales = {}

for item in order_items:
    order_id = clean_id(item.get('OrderId'))
    if order_id in eligible_orders:
        owner_id = eligible_orders[order_id]
        
        try:
            qty = float(item.get('Quantity', 0))
            price = float(item.get('UnitPrice', 0))
            amount = qty * price
        except:
            amount = 0
            
        owner_sales[owner_id] = owner_sales.get(owner_id, 0) + amount

# 4. Find Top Agent
top_agent = None
max_sales = -1

for agent, sales in owner_sales.items():
    if sales > max_sales:
        max_sales = sales
        top_agent = agent

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_function-call-18111864696704650149': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-18111864696704649474': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}], 'var_function-call-12590192217909324180': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-2953279664057868323': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Status', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StartDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CustomerSignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CompanySignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractTerm', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-2953279664057872282': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractID__c', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContactId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OwnerId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Probability', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Amount', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StageName', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Name', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CreatedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CloseDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-3368095588372396259': [{'AccountId': '#001Wt00000PGtdJIAT'}, {'AccountId': '001Wt00000PGYx5IAH'}, {'AccountId': '#001Wt00000PHVtpIAH'}, {'AccountId': '001Wt00000PHVqdIAH'}, {'AccountId': '001Wt00000PHHXXIA5'}, {'AccountId': '#001Wt00000PGZZoIAP'}, {'AccountId': '001Wt00000PGZmfIAH'}, {'AccountId': '#001Wt00000PGovMIAT'}, {'AccountId': '001Wt00000PGtdJIAT'}, {'AccountId': '#001Wt00000PGRnYIAX'}, {'AccountId': '#001Wt00000PGzM9IAL'}, {'AccountId': '001Wt00000PGdzxIAD'}, {'AccountId': '001Wt00000PHRTfIAP'}, {'AccountId': '#001Wt00000PFsjOIAT'}, {'AccountId': '001Wt00000PGzSaIAL'}, {'AccountId': '001Wt00000PHVtpIAH'}], 'var_function-call-1184197430398516886': [{'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFyITIA1', 'AccountId': '001Wt00000PGRnYIAX', 'OwnerId': '005Wt000003NDJ0IAO'}, {'Id': '801Wt00000PGGhBIAX', 'AccountId': '001Wt00000PHVtpIAH', 'OwnerId': '005Wt000003NIaRIAW'}, {'Id': '#801Wt00000PGbLTIA1', 'AccountId': '001Wt00000PHHXXIA5', 'OwnerId': '005Wt000003NFRKIA4'}, {'Id': '#801Wt00000PGbdMIAT', 'AccountId': '#001Wt00000PGZgHIAX', 'OwnerId': '#005Wt000003NGtcIAG'}, {'Id': '#801Wt00000PGtiAIAT', 'AccountId': '#001Wt00000PGdzxIAD', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PH4FMIA1', 'AccountId': '#001Wt00000PGZmfIAH', 'OwnerId': '#005Wt000003NJmbIAG'}, {'Id': '801Wt00000PH8yvIAD', 'AccountId': '001Wt00000PGovMIAT', 'OwnerId': '005Wt000003NIXCIA4'}, {'Id': '801Wt00000PHHMFIA5', 'AccountId': '001Wt00000PFsjOIAT', 'OwnerId': '005Wt000003NJ9uIAG'}, {'Id': '801Wt00000PHHhDIAX', 'AccountId': '#001Wt00000PHVtpIAH', 'OwnerId': '#005Wt000003NITxIAO'}, {'Id': '801Wt00000PHLzNIAX', 'AccountId': '001Wt00000PGtdJIAT', 'OwnerId': '005Wt000003NEoYIAW'}, {'Id': '801Wt00000PHRFAIA5', 'AccountId': '001Wt00000PGdwiIAD', 'OwnerId': '#005Wt000003NIx1IAG'}, {'Id': '#801Wt00000PHVkDIAX', 'AccountId': '001Wt00000PGZZoIAP', 'OwnerId': '005Wt000003NJt3IAG'}, {'Id': '801Wt00000PHVqfIAH', 'AccountId': '#001Wt00000PGzM9IAL', 'OwnerId': '005Wt000003NDEBIA4'}, {'Id': '#801Wt00000PHWptIAH', 'AccountId': '#001Wt00000PGYx5IAH', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-1184197430398514381': [{'OrderId': '#801Wt00000PFt7UIAT', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '7.0', 'UnitPrice': '379.9905'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '12.0', 'UnitPrice': '476.991'}, {'OrderId': '#801Wt00000PGbdMIAT', 'Quantity': '30.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PHVqfIAH', 'Quantity': '10.0', 'UnitPrice': '539.991'}, {'OrderId': '#801Wt00000PGbdMIAT', 'Quantity': '20.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '20.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '14.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '3.0', 'UnitPrice': '499.99'}, {'OrderId': '#801Wt00000PHWptIAH', 'Quantity': '2.0', 'UnitPrice': '339.99'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '50.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '16.0', 'UnitPrice': '440.991'}, {'OrderId': '801Wt00000PH4FMIA1', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '1.0', 'UnitPrice': '399.99'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '10.0', 'UnitPrice': '449.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '5.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PFyITIA1', 'Quantity': '15.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PFyITIA1', 'Quantity': '8.0', 'UnitPrice': '503.4905'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'OrderId': '801Wt00000PHHhDIAX', 'Quantity': '12.0', 'UnitPrice': '314.991'}, {'OrderId': '#801Wt00000PHWptIAH', 'Quantity': '3.0', 'UnitPrice': '529.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '7.0', 'UnitPrice': '455.9905'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '5.0', 'UnitPrice': '427.4905'}, {'OrderId': '#801Wt00000PFt7UIAT', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '#801Wt00000PHVkDIAX', 'Quantity': '3.0', 'UnitPrice': '599.99'}]}

exec(code, env_args)
