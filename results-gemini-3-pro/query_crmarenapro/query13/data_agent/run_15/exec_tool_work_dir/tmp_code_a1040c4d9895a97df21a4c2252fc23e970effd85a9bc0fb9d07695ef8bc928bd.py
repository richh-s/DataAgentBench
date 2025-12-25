code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-5246262777296140197'], 'r') as f:
    orders_data = json.load(f)
with open(locals()['var_function-call-1819836885715432581'], 'r') as f:
    order_items_data = json.load(f)
with open(locals()['var_function-call-8177256188524283242'], 'r') as f:
    contracts_data = json.load(f)

df_orders = pd.DataFrame(orders_data)
df_items = pd.DataFrame(order_items_data)
df_contracts = pd.DataFrame(contracts_data)

# Clean IDs
def clean_id(x):
    if pd.isna(x): return x
    x = str(x).strip()
    if x.startswith('#'):
        return x[1:]
    return x

for col in ['Id', 'AccountId', 'OwnerId']:
    df_orders[col] = df_orders[col].apply(clean_id)
for col in ['OrderId']:
    df_items[col] = df_items[col].apply(clean_id)
for col in ['Id', 'AccountId']:
    df_contracts[col] = df_contracts[col].apply(clean_id)

# Convert dates
df_contracts['CompanySignedDate'] = pd.to_datetime(df_contracts['CompanySignedDate'])
df_orders['EffectiveDate'] = pd.to_datetime(df_orders['EffectiveDate'])

# Date range: 2022-11-25 minus 5 months -> 2022-06-25
start_date = pd.Timestamp('2022-06-25')
end_date = pd.Timestamp('2022-11-25')

# Filter Contracts
valid_contracts = df_contracts[(df_contracts['CompanySignedDate'] >= start_date) & 
                               (df_contracts['CompanySignedDate'] <= end_date)]

# Link Orders to Valid Contracts
# Attempt 1: Merge on AccountId and check date proximity
# Since we suspect Order date ~ Contract date
merged = pd.merge(df_orders, valid_contracts, on='AccountId', suffixes=('_ord', '_con'))

# Check date difference
merged['diff'] = (merged['EffectiveDate'] - merged['CompanySignedDate']).abs().dt.days

# Assuming the Order corresponds to the Contract if dates are close (e.g. within 7 days)
# Or maybe they are exactly same?
close_matches = merged[merged['diff'] <= 7].copy()

# Calculate amount
# Need to calculate amount per Order
df_items['Quantity'] = pd.to_numeric(df_items['Quantity'])
df_items['UnitPrice'] = pd.to_numeric(df_items['UnitPrice'])
df_items['Amount'] = df_items['Quantity'] * df_items['UnitPrice']
order_amounts = df_items.groupby('OrderId')['Amount'].sum().reset_index()

# Join with valid orders
# Use close_matches IDs
valid_order_ids = close_matches['Id_ord'].unique()
final_df = order_amounts[order_amounts['OrderId'].isin(valid_order_ids)]

# We need OwnerId
final_df = pd.merge(final_df, df_orders[['Id', 'OwnerId']], left_on='OrderId', right_on='Id')

# Group by OwnerId
agent_sales = final_df.groupby('OwnerId')['Amount'].sum().sort_values(ascending=False)

print("__RESULT__:")
print(json.dumps({
    "top_agent": agent_sales.index[0] if not agent_sales.empty else None,
    "top_amount": agent_sales.iloc[0] if not agent_sales.empty else 0,
    "matches_count": len(close_matches),
    "sample_matches": close_matches[['Id_ord', 'EffectiveDate', 'CompanySignedDate', 'diff']].head().to_dict(orient='records')
}))"""

env_args = {'var_function-call-7212038207275055750': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-7061368504917844034': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractID__c', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContactId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OwnerId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Probability', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Amount', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StageName', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Name', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CreatedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CloseDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-4272444095834979724': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Status', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StartDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CustomerSignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CompanySignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractTerm', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-282923766105866510': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'OrderId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Product2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Quantity', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'UnitPrice', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'PriceBookEntryId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-11993477465646944350': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_function-call-4001687328399682540': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1'}, {'Id': '006Wt000007Aw3WIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGzsMIAT'}, {'Id': '006Wt000007Aw3XIAS', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGYx5IAH'}, {'Id': '006Wt000007Aya9IAC', 'ContractID__c': 'None', 'AccountId': '001Wt00000PHViXIAX'}, {'Id': '006Wt000007AyaAIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PHVk9IAH'}], 'var_function-call-14389848337500588640': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'AccountId': '001Wt00000PGXrLIAX', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'AccountId': '001Wt00000PGXrLIAX', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'AccountId': '001Wt00000PGYgxIAH', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'AccountId': '#001Wt00000PGeJIIA1', 'CompanySignedDate': '2023-07-02'}], 'var_function-call-12139086474376387824': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OpportunityId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Product2Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'PricebookEntryId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Quantity', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'TotalPrice', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-16988569871816016717': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OpportunityId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContactId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Name', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Status', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CreatedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ExpirationDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-13551659079118002765': [{'Id': '801Wt00000PFsjPIAT', 'EffectiveDate': '2023-06-25', 'AccountId': '001Wt00000PFttwIAD'}, {'Id': '801Wt00000PFsjQIAT', 'EffectiveDate': '2021-09-30', 'AccountId': '#001Wt00000PHVqdIAH'}, {'Id': '#801Wt00000PFt7UIAT', 'EffectiveDate': '2022-09-15', 'AccountId': '001Wt00000PGzSaIAL'}, {'Id': '801Wt00000PFtAmIAL', 'EffectiveDate': '2020-09-01', 'AccountId': '001Wt00000PHVdhIAH'}, {'Id': '801Wt00000PFtAnIAL', 'EffectiveDate': '2023-06-01', 'AccountId': '#001Wt00000PGaNjIAL'}], 'var_function-call-17292982521410444723': [{'Count(*)': '163'}], 'var_function-call-8236583732082515205': [{'Count(*)': '689'}], 'var_function-call-11703446667301998711': [{'count_star()': '163'}], 'var_function-call-5246262777296140197': 'file_storage/function-call-5246262777296140197.json', 'var_function-call-1819836885715432581': 'file_storage/function-call-1819836885715432581.json', 'var_function-call-8177256188524283242': 'file_storage/function-call-8177256188524283242.json'}

exec(code, env_args)
