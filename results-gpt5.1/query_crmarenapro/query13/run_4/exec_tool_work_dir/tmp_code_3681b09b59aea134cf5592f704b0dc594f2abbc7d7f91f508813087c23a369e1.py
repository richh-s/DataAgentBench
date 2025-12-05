code = """import json, pandas as pd, os

# Load full Opportunity, Order, OrderItem data from files
with open(var_call_ECUeg1BiwN9h13Bv3Wqn2P4n, 'r') as f:
    opp = pd.DataFrame(json.load(f))
with open(var_call_AlHvFcCqhqT9kJITZPbRiJak, 'r') as f:
    orders = pd.DataFrame(json.load(f))
with open(var_call_ykcvd5HfK76dN8dxbpMZ6ms3, 'r') as f:
    items = pd.DataFrame(json.load(f))

con = pd.DataFrame(var_call_LqWUMQrd4xDc6NLBzJnEEugL)

# Clean leading '#' in ID fields for joins
for df in [opp, orders, con]:
    for col in df.columns:
        if col.endswith('Id') or col.endswith('ID__c') or col == 'Id':
            df[col] = df[col].astype(str).str.strip().str.lstrip('#')

for df in [items]:
    if 'OrderId' in df.columns:
        df['OrderId'] = df['OrderId'].astype(str).str.strip().str.lstrip('#')

# Filter opportunities whose contracts are in the signed window
eligible_con_ids = set(con['Id'])
opp_elig = opp[opp['ContractID__c'].isin(eligible_con_ids)]

# Join eligible opportunities to orders via AccountId
merged = opp_elig.merge(orders, on='AccountId', how='inner', suffixes=('_opp', '_ord'))

# Compute order sales amounts
items['Quantity'] = items['Quantity'].astype(float)
items['UnitPrice'] = items['UnitPrice'].astype(float)
items_sum = items.copy()
items_sum['SalesAmount'] = items_sum['Quantity'] * items_sum['UnitPrice']
items_sum = items_sum.groupby('OrderId', as_index=False)['SalesAmount'].sum()

merged2 = merged.merge(items_sum, left_on='Id_ord', right_on='OrderId', how='inner')

result = merged2.groupby('OwnerId')['SalesAmount'].sum().reset_index().sort_values('SalesAmount', ascending=False).head(1)

answer = None
if not result.empty:
    answer = result.iloc[0]['OwnerId']

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ldV4lBuwJO5NBpRhNOm5rMLW': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_call_ECUeg1BiwN9h13Bv3Wqn2P4n': 'file_storage/call_ECUeg1BiwN9h13Bv3Wqn2P4n.json', 'var_call_LqWUMQrd4xDc6NLBzJnEEugL': [{'Id': '800Wt00000DDNlnIAH', 'AccountId': '#001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDe3OIAT', 'AccountId': '001Wt00000PGYx5IAH', 'CompanySignedDate': '2022-09-20'}, {'Id': '800Wt00000DDeg6IAD', 'AccountId': '#001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-07-18'}, {'Id': '800Wt00000DDzZLIA1', 'AccountId': '001Wt00000PHVqdIAH', 'CompanySignedDate': '2022-10-26'}, {'Id': '#800Wt00000DDzvrIAD', 'AccountId': '001Wt00000PHHXXIA5', 'CompanySignedDate': '2022-08-30'}, {'Id': '800Wt00000DE0FHIA1', 'AccountId': '#001Wt00000PGZZoIAP', 'CompanySignedDate': '2022-08-02'}, {'Id': '800Wt00000DE0TiIAL', 'AccountId': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2022-09-10'}, {'Id': '800Wt00000DE2vLIAT', 'AccountId': '#001Wt00000PGovMIAT', 'CompanySignedDate': '2022-06-29'}, {'Id': '800Wt00000DE98oIAD', 'AccountId': '001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-11-10'}, {'Id': '800Wt00000DE9GrIAL', 'AccountId': '#001Wt00000PGRnYIAX', 'CompanySignedDate': '2022-06-30'}, {'Id': '#800Wt00000DE9ITIA1', 'AccountId': '#001Wt00000PGzM9IAL', 'CompanySignedDate': '2022-09-11'}, {'Id': '#800Wt00000DE9SAIA1', 'AccountId': '001Wt00000PGdzxIAD', 'CompanySignedDate': '2022-09-30'}, {'Id': '800Wt00000DE9YbIAL', 'AccountId': '001Wt00000PHRTfIAP', 'CompanySignedDate': '2022-11-22'}, {'Id': '#800Wt00000DE9lVIAT', 'AccountId': '#001Wt00000PFsjOIAT', 'CompanySignedDate': '2022-06-26'}, {'Id': '800Wt00000DE9qLIAT', 'AccountId': '001Wt00000PGzSaIAL', 'CompanySignedDate': '2022-09-01'}, {'Id': '800Wt00000DE9rxIAD', 'AccountId': '001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-09-19'}], 'var_call_AlHvFcCqhqT9kJITZPbRiJak': 'file_storage/call_AlHvFcCqhqT9kJITZPbRiJak.json', 'var_call_ykcvd5HfK76dN8dxbpMZ6ms3': 'file_storage/call_ykcvd5HfK76dN8dxbpMZ6ms3.json', 'var_call_6uqRMv2JUlMVNMCdVSIq9mMg': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem']}

exec(code, env_args)
