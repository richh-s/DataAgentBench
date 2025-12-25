code = """import json
import pandas as pd
from datetime import datetime, timedelta

# Load data
contracts = pd.DataFrame(json.loads(locals()['var_function-call-16165289132143861962']))
with open(locals()['var_function-call-16165289132143863109'], 'r') as f:
    orders = pd.DataFrame(json.load(f))
with open(locals()['var_function-call-16165289132143864256'], 'r') as f:
    order_items = pd.DataFrame(json.load(f))

# Clean IDs
def clean_id(x):
    if isinstance(x, str):
        return x.lstrip('#').strip()
    return x

contracts['AccountId'] = contracts['AccountId'].apply(clean_id)
orders['AccountId'] = orders['AccountId'].apply(clean_id)
orders['Id'] = orders['Id'].apply(clean_id)
orders['OwnerId'] = orders['OwnerId'].apply(clean_id)
order_items['OrderId'] = order_items['OrderId'].apply(clean_id)

# Convert dates
def parse_date(x):
    try:
        return pd.to_datetime(x)
    except:
        return pd.NaT

contracts['StartDate'] = parse_date(contracts['StartDate'])
contracts['CompanySignedDate'] = parse_date(contracts['CompanySignedDate'])
orders['EffectiveDate'] = parse_date(orders['EffectiveDate'])

# Filter Contracts (already filtered in SQL, but good to be safe/explicit if needed, here SQL did it)
# SQL: CompanySignedDate >= '2022-06-25' AND <= '2022-11-25'

# Match Orders to Contracts
# Strategy: For each contract, find order with same AccountId and EffectiveDate close to StartDate
eligible_order_ids = []

for _, contract in contracts.iterrows():
    cid = contract['AccountId'] # Using AccountId as link key
    c_start = contract['StartDate']
    c_sign = contract['CompanySignedDate']
    
    # Candidates
    candidates = orders[orders['AccountId'] == cid].copy()
    
    if candidates.empty:
        continue
        
    # Calculate date diff with StartDate (or SignedDate if StartDate is NaT)
    # Prefer StartDate match
    target_date = c_start if pd.notnull(c_start) else c_sign
    
    if pd.isnull(target_date):
        continue
        
    candidates['diff'] = (candidates['EffectiveDate'] - target_date).abs()
    
    # Filter by reasonable window (e.g. +/- 30 days)
    # The sample showed exact match. Let's allow 15 days.
    # Note: Some data might be corrupted or shifted.
    matches = candidates[candidates['diff'] <= timedelta(days=30)].sort_values('diff')
    
    if not matches.empty:
        best_match = matches.iloc[0]
        eligible_order_ids.append(best_match['Id'])

# Calculate Sales Amount
# Filter items
eligible_items = order_items[order_items['OrderId'].isin(eligible_order_ids)].copy()

# Calculate amount
# Clean UnitPrice and Quantity (strings -> float)
def to_float(x):
    try:
        return float(x)
    except:
        return 0.0

eligible_items['Quantity'] = eligible_items['Quantity'].apply(to_float)
eligible_items['UnitPrice'] = eligible_items['UnitPrice'].apply(to_float)
eligible_items['Amount'] = eligible_items['Quantity'] * eligible_items['UnitPrice']

# Aggregation
# We need OwnerId from Order
# Join eligible items with orders to get OwnerId
eligible_orders = orders[orders['Id'].isin(eligible_order_ids)][['Id', 'OwnerId']]
merged = pd.merge(eligible_items, eligible_orders, left_on='OrderId', right_on='Id', how='left')

# Group by OwnerId
sales_by_agent = merged.groupby('OwnerId')['Amount'].sum().reset_index()
sales_by_agent = sales_by_agent.sort_values('Amount', ascending=False)

print("__RESULT__:")
print(sales_by_agent.to_json(orient='records'))"""

env_args = {'var_function-call-2499348873779837984': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-2499348873779836323': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}], 'var_function-call-6447918121010576454': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-6447918121010573491': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Status', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StartDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CustomerSignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CompanySignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractTerm', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-6447918121010574624': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractID__c', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContactId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OwnerId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Probability', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Amount', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StageName', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Name', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CreatedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CloseDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-13131393751477626964': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'Status': 'Activated  ', 'EffectiveDate': '2020-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'Status': 'Activated', 'EffectiveDate': '2023-06-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_function-call-5097305656981981825': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OpportunityId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Product2Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'PricebookEntryId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Quantity', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'TotalPrice', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-14267851576542656403': [{'Id': '#800Wt00000DDfKTIA1', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'StartDate': '2023-06-25', 'CustomerSignedDate': '2023-06-20', 'CompanySignedDate': '2023-06-21', 'Description': 'This contract covers the provision of AI-powered EDA solutions tailored for media production enhancement for Digital Horizon Media. TechPulse Solutions ensures product integration, training, and ongoing support as part of a 12-month term.', 'ContractTerm': '12'}, {'Id': '800Wt00000DDt8uIAD', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated   ', 'StartDate': '2024-01-01', 'CustomerSignedDate': '2023-12-20', 'CompanySignedDate': '2023-12-20', 'Description': "This contract outlines the integration of TechPulse Solutions' AI-powered EDA solutions into Digital Horizon Media's existing systems. The contract ensures comprehensive implementation, training, and support services to enhance Digital Horizon Media's media production capabilities.", 'ContractTerm': '24'}], 'var_function-call-14267851576542657102': [{'Id': '802Wt000007906kIAA', 'OrderId': '801Wt00000PFsjPIAT', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '15.0', 'UnitPrice': '359.991', 'PriceBookEntryId': '01uWt0000027P6zIAE'}, {'Id': '802Wt00000796qEIAQ', 'OrderId': '801Wt00000PFsjPIAT', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '10.0', 'UnitPrice': '539.991', 'PriceBookEntryId': '01uWt0000027P5NIAU'}, {'Id': '802Wt000007996VIAQ', 'OrderId': '801Wt00000PFsjPIAT', 'Product2Id': '01tWt000006hVebIAE', 'Quantity': '8.0', 'UnitPrice': '522.4905', 'PriceBookEntryId': '01uWt0000027PjhIAE'}, {'Id': '#802Wt0000079A0vIAE', 'OrderId': '801Wt00000PFsjPIAT', 'Product2Id': '#01tWt000006hUgwIAE', 'Quantity': '10.0', 'UnitPrice': '539.991', 'PriceBookEntryId': '01uWt0000027Q34IAE'}], 'var_function-call-14267851576542657801': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OpportunityId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContactId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Name', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Status', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CreatedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ExpirationDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-16165289132143861962': [{'AccountId': '#001Wt00000PGtdJIAT', 'StartDate': '2022-09-15', 'CompanySignedDate': '2022-09-02'}, {'AccountId': '001Wt00000PGYx5IAH', 'StartDate': '2022-09-25', 'CompanySignedDate': '2022-09-20'}, {'AccountId': '#001Wt00000PHVtpIAH', 'StartDate': '2022-08-01', 'CompanySignedDate': '2022-07-18'}, {'AccountId': '001Wt00000PHVqdIAH', 'StartDate': '2022-12-01', 'CompanySignedDate': '2022-10-26'}, {'AccountId': '001Wt00000PHHXXIA5', 'StartDate': '2022-09-01', 'CompanySignedDate': '2022-08-30'}, {'AccountId': '#001Wt00000PGZZoIAP', 'StartDate': '2022-08-15', 'CompanySignedDate': '2022-08-02'}, {'AccountId': '001Wt00000PGZmfIAH', 'StartDate': '2022-09-15', 'CompanySignedDate': '2022-09-10'}, {'AccountId': '#001Wt00000PGovMIAT', 'StartDate': '2022-07-01', 'CompanySignedDate': '2022-06-29'}, {'AccountId': '001Wt00000PGtdJIAT', 'StartDate': '2022-12-15', 'CompanySignedDate': '2022-11-10'}, {'AccountId': '#001Wt00000PGRnYIAX', 'StartDate': '2022-07-10', 'CompanySignedDate': '2022-06-30'}, {'AccountId': '#001Wt00000PGzM9IAL', 'StartDate': '2022-09-20', 'CompanySignedDate': '2022-09-11'}, {'AccountId': '001Wt00000PGdzxIAD', 'StartDate': '2022-10-15', 'CompanySignedDate': '2022-09-30'}, {'AccountId': '001Wt00000PHRTfIAP', 'StartDate': '2022-12-01', 'CompanySignedDate': '2022-11-22'}, {'AccountId': '#001Wt00000PFsjOIAT', 'StartDate': '2022-07-01', 'CompanySignedDate': '2022-06-26'}, {'AccountId': '001Wt00000PGzSaIAL', 'StartDate': '2022-09-15', 'CompanySignedDate': '2022-09-01'}, {'AccountId': '001Wt00000PHVtpIAH', 'StartDate': '2022-10-01', 'CompanySignedDate': '2022-09-19'}], 'var_function-call-16165289132143863109': 'file_storage/function-call-16165289132143863109.json', 'var_function-call-16165289132143864256': 'file_storage/function-call-16165289132143864256.json'}

exec(code, env_args)
