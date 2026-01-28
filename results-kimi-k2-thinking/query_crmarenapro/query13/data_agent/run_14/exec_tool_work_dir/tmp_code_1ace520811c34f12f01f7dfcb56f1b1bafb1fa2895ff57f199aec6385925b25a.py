code = """import json
result = var_functions.query_db:2
# If result is a string path to a JSON file, read it.
if isinstance(result, str):
    with open(result, 'r') as f:
        data = json.load(f)
else:
    data = result

# Compute sales per agent
from collections import defaultdict
sales_by_agent = defaultdict(float)
for row in data:
    # Clean OwnerId: remove leading # and whitespace
    owner_id = row['OwnerId']
    if isinstance(owner_id, str):
        owner_id = owner_id.lstrip('#').strip()
    # Convert quantity and unit price to float
    try:
        qty = float(row['Quantity'])
        up = float(row['UnitPrice'])
    except Exception as e:
        # skip if conversion fails
        continue
    amount = qty * up
    sales_by_agent[owner_id] += amount

# Find agent with max sales
if not sales_by_agent:
    top_agent = None
else:
    top_agent = max(sales_by_agent, key=lambda k: sales_by_agent[k])

# Return top_agent as JSON string
print('__RESULT__:')
print(json.dumps(top_agent))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'Quantity': '10.0', 'UnitPrice': '359.991', 'AccountId': '001Wt00000PGzSaIAL', 'EffectiveDate': '2022-09-15', 'Status': 'Activated'}, {'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'AccountId': '001Wt00000PGzSaIAL', 'EffectiveDate': '2022-09-15', 'Status': 'Activated'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'Quantity': '15.0', 'UnitPrice': '359.991', 'AccountId': '001Wt00000PGRnYIAX', 'EffectiveDate': '2022-07-10', 'Status': 'Activated'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'Quantity': '8.0', 'UnitPrice': '503.4905', 'AccountId': '001Wt00000PGRnYIAX', 'EffectiveDate': '2022-07-10', 'Status': 'Activated'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'Quantity': '10.0', 'UnitPrice': '359.991', 'AccountId': '001Wt00000PHVtpIAH', 'EffectiveDate': '2022-10-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'Quantity': '14.0', 'UnitPrice': '476.991', 'AccountId': '001Wt00000PHVtpIAH', 'EffectiveDate': '2022-10-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'AccountId': '001Wt00000PHVtpIAH', 'EffectiveDate': '2022-10-01', 'Status': 'Activated'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'Quantity': '20.0', 'UnitPrice': '450.4915', 'AccountId': '#001Wt00000PGZgHIAX', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'Quantity': '30.0', 'UnitPrice': '390.9915', 'AccountId': '#001Wt00000PGZgHIAX', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG', 'Quantity': '10.0', 'UnitPrice': '476.991', 'AccountId': '#001Wt00000PGZmfIAH', 'EffectiveDate': '2022-09-15', 'Status': 'Activated'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'Quantity': '20.0', 'UnitPrice': '390.9915', 'AccountId': '001Wt00000PGovMIAT', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'Quantity': '30.0', 'UnitPrice': '552.4915', 'AccountId': '001Wt00000PGovMIAT', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'Quantity': '50.0', 'UnitPrice': '450.4915', 'AccountId': '001Wt00000PGovMIAT', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '1.0', 'UnitPrice': '399.99', 'AccountId': '001Wt00000PFsjOIAT', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '3.0', 'UnitPrice': '499.99', 'AccountId': '001Wt00000PFsjOIAT', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '5.0', 'UnitPrice': '427.4905', 'AccountId': '001Wt00000PFsjOIAT', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '7.0', 'UnitPrice': '455.9905', 'AccountId': '001Wt00000PFsjOIAT', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PHHhDIAX', 'OwnerId': '#005Wt000003NITxIAO', 'Quantity': '12.0', 'UnitPrice': '314.991', 'AccountId': '#001Wt00000PHVtpIAH', 'EffectiveDate': '2022-08-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'Quantity': '10.0', 'UnitPrice': '449.991', 'AccountId': '001Wt00000PGtdJIAT', 'EffectiveDate': '2022-09-15', 'Status': 'Activated  '}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'Quantity': '12.0', 'UnitPrice': '476.991', 'AccountId': '001Wt00000PGtdJIAT', 'EffectiveDate': '2022-09-15', 'Status': 'Activated  '}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'AccountId': '001Wt00000PGtdJIAT', 'EffectiveDate': '2022-09-15', 'Status': 'Activated  '}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '16.0', 'UnitPrice': '440.991', 'AccountId': '001Wt00000PGdwiIAD', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '5.0', 'UnitPrice': '569.9905', 'AccountId': '001Wt00000PGdwiIAD', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '7.0', 'UnitPrice': '379.9905', 'AccountId': '001Wt00000PGdwiIAD', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'AccountId': '001Wt00000PGdwiIAD', 'EffectiveDate': '2022-07-01', 'Status': 'Activated'}, {'OrderId': '#801Wt00000PHVkDIAX', 'OwnerId': '005Wt000003NJt3IAG', 'Quantity': '3.0', 'UnitPrice': '599.99', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2022-08-15', 'Status': 'Activated'}, {'OrderId': '801Wt00000PHVqfIAH', 'OwnerId': '005Wt000003NDEBIA4', 'Quantity': '10.0', 'UnitPrice': '539.991', 'AccountId': '#001Wt00000PGzM9IAL', 'EffectiveDate': '2022-09-20', 'Status': 'Activated '}, {'OrderId': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'Quantity': '2.0', 'UnitPrice': '339.99', 'AccountId': '#001Wt00000PGYx5IAH', 'EffectiveDate': '2022-09-25', 'Status': 'Activated'}, {'OrderId': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'Quantity': '3.0', 'UnitPrice': '529.99', 'AccountId': '#001Wt00000PGYx5IAH', 'EffectiveDate': '2022-09-25', 'Status': 'Activated'}]}

exec(code, env_args)
