code = """import pandas as pd
import json

# Load data from files
with open(locals()['var_function-call-866280973453821019'], 'r') as f:
    orders = pd.DataFrame(json.load(f))
with open(locals()['var_function-call-866280973453821924'], 'r') as f:
    contracts = pd.DataFrame(json.load(f))
with open(locals()['var_function-call-866280973453822829'], 'r') as f:
    items = pd.DataFrame(json.load(f))

# Clean IDs
def clean_id(x):
    if isinstance(x, str):
        return x.lstrip('#').strip()
    return x

orders['Id'] = orders['Id'].apply(clean_id)
orders['AccountId'] = orders['AccountId'].apply(clean_id)
orders['OwnerId'] = orders['OwnerId'].apply(clean_id)

contracts['Id'] = contracts['Id'].apply(clean_id)
contracts['AccountId'] = contracts['AccountId'].apply(clean_id)

items['OrderId'] = items['OrderId'].apply(clean_id)
items['Quantity'] = pd.to_numeric(items['Quantity'])
items['UnitPrice'] = pd.to_numeric(items['UnitPrice'])

# Dates
orders['EffectiveDate'] = pd.to_datetime(orders['EffectiveDate'])
contracts['CompanySignedDate'] = pd.to_datetime(contracts['CompanySignedDate'])

# Time range
start_date = pd.to_datetime('2022-06-25')
end_date = pd.to_datetime('2022-11-25')

# Calculate Order Amounts
items['Amount'] = items['Quantity'] * items['UnitPrice']
order_amounts = items.groupby('OrderId')['Amount'].sum().reset_index()

# Merge Order Amounts with Orders
orders_merged = orders.merge(order_amounts, left_on='Id', right_on='OrderId', how='left')
orders_merged['Amount'] = orders_merged['Amount'].fillna(0)

# Check linkage
# Join on AccountId
merged = orders_merged.merge(contracts, on='AccountId', suffixes=('_order', '_contract'))

# Check exact date match
matched_exact = merged[merged['EffectiveDate'] == merged['CompanySignedDate']]

print(f"Total Orders: {len(orders)}")
print(f"Total Contracts: {len(contracts)}")
print(f"Matched Exact Date: {len(matched_exact)}")

if len(matched_exact) > 100: # Good overlap
    print("Using Linked Contracts Logic")
    # Filter by Contract Date
    final_df = matched_exact[
        (matched_exact['CompanySignedDate'] >= start_date) & 
        (matched_exact['CompanySignedDate'] <= end_date)
    ]
else:
    print("Using Order Logic Only")
    # Filter by Order EffectiveDate
    final_df = orders_merged[
        (orders_merged['EffectiveDate'] >= start_date) & 
        (orders_merged['EffectiveDate'] <= end_date)
    ]

# Group by OwnerId (Agent)
agent_sales = final_df.groupby('OwnerId')['Amount'].sum().reset_index()
top_agent = agent_sales.sort_values('Amount', ascending=False).head(1)

print("__RESULT__:")
print(json.dumps(top_agent['OwnerId'].values[0] if not top_agent.empty else "No agent found"))"""

env_args = {'var_function-call-14569660899065673844': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-14569660899065674983': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-8780357929761332681': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-8780357929761331016': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'OrderId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Product2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Quantity', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'UnitPrice', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'PriceBookEntryId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-8780357929761329351': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractID__c', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContactId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OwnerId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Probability', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Amount', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StageName', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Name', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CreatedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CloseDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-8780357929761331782': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OpportunityId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Product2Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'PricebookEntryId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Quantity', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'TotalPrice', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-8780357929761330117': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Status', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StartDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CustomerSignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CompanySignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractTerm', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-17710962792532811662': [{'Id': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDe3OIAT', 'CompanySignedDate': '2022-09-20'}, {'Id': '800Wt00000DDeg6IAD', 'CompanySignedDate': '2022-07-18'}, {'Id': '800Wt00000DDzZLIA1', 'CompanySignedDate': '2022-10-26'}, {'Id': '#800Wt00000DDzvrIAD', 'CompanySignedDate': '2022-08-30'}], 'var_function-call-17710962792532807777': [{'Id': '#801Wt00000PFt7UIAT', 'EffectiveDate': '2022-09-15'}, {'Id': '801Wt00000PFyITIA1', 'EffectiveDate': '2022-07-10'}, {'Id': '801Wt00000PGGhBIAX', 'EffectiveDate': '2022-10-01'}, {'Id': '#801Wt00000PGbLTIA1', 'EffectiveDate': '2022-09-01'}, {'Id': '#801Wt00000PGbdMIAT', 'EffectiveDate': '2022-07-01'}], 'var_function-call-16116184336827387428': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OpportunityId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContactId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Name', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Status', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CreatedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ExpirationDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-16116184336827384331': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'QuoteId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OpportunityLineItemId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Product2Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'PricebookEntryId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Quantity', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'UnitPrice', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Discount', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'TotalPrice', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-8960523078503114000': [{'Count(*)': '163'}], 'var_function-call-8960523078503116731': [{'count_star()': '163'}], 'var_function-call-8960523078503115366': [{'count_star()': '1170'}], 'var_function-call-866280973453821019': 'file_storage/function-call-866280973453821019.json', 'var_function-call-866280973453821924': 'file_storage/function-call-866280973453821924.json', 'var_function-call-866280973453822829': 'file_storage/function-call-866280973453822829.json'}

exec(code, env_args)
