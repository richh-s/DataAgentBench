code = """import pandas as pd, json, re

# Recalculate from scratch with better cleaning
orders = locals()['var_functions.query_db:0']
items = locals()['var_functions.query_db:4']

df_o = pd.DataFrame(orders)
df_i = pd.DataFrame(items)

# Clean all ID fields - strip whitespace and remove leading #
clean_id = lambda x: str(x).strip().replace('#', '') if pd.notnull(x) else x
for col in df_o.columns:
    if 'Id' in col:
        df_o[col] = df_o[col].apply(clean_id)

for col in df_i.columns:
    if 'Id' in col:
        df_i[col] = df_i[col].apply(clean_id)

# Convert numeric fields
df_i['Quantity'] = pd.to_numeric(df_i['Quantity'])
df_i['UnitPrice'] = pd.to_numeric(df_i['UnitPrice'])

# Calculate sales
df_i['SalesAmount'] = df_i['Quantity'] * df_i['UnitPrice']

# Group by OrderId
df_order_totals = df_i.groupby('OrderId')['SalesAmount'].sum().reset_index()

# Merge with orders
df_merged = pd.merge(df_order_totals, df_o[['Id', 'OwnerId']], left_on='OrderId', right_on='Id', how='inner')

# Group by OwnerId to get agent totals
df_agent_totals = df_merged.groupby('OwnerId')['SalesAmount'].sum().reset_index()

# Sort and get top
df_agent_totals = df_agent_totals.sort_values('SalesAmount', ascending=False)

top_agent_id = df_agent_totals.iloc[0]['OwnerId']
top_agent_sales = df_agent_totals.iloc[0]['SalesAmount']

# Verify by listing top 3 agents
print('__RESULT__:')
print(json.dumps({
    'top_agent_id': top_agent_id,
    'top_agent_sales': float(top_agent_sales),
    'top_3_agents': df_agent_totals.head(3).to_dict('records')
}))"""

env_args = {'var_functions.query_db:0': [{'Id': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO'}, {'Id': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW'}, {'Id': '#801Wt00000PGbLTIA1', 'OwnerId': '005Wt000003NFRKIA4'}, {'Id': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG'}, {'Id': '#801Wt00000PGtiAIAT', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG'}, {'Id': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4'}, {'Id': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG'}, {'Id': '801Wt00000PHHhDIAX', 'OwnerId': '#005Wt000003NITxIAO'}, {'Id': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW'}, {'Id': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG'}, {'Id': '#801Wt00000PHVkDIAX', 'OwnerId': '005Wt000003NJt3IAG'}, {'Id': '801Wt00000PHVqfIAH', 'OwnerId': '005Wt000003NDEBIA4'}, {'Id': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_functions.query_db:2': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'Status': 'Activated  ', 'EffectiveDate': '2020-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'Status': 'Activated', 'EffectiveDate': '2023-06-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_functions.query_db:4': [{'OrderId': '#801Wt00000PFt7UIAT', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '7.0', 'UnitPrice': '379.9905'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '12.0', 'UnitPrice': '476.991'}, {'OrderId': '#801Wt00000PGbdMIAT', 'Quantity': '30.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PHVqfIAH', 'Quantity': '10.0', 'UnitPrice': '539.991'}, {'OrderId': '#801Wt00000PGbdMIAT', 'Quantity': '20.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '20.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '14.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '3.0', 'UnitPrice': '499.99'}, {'OrderId': '#801Wt00000PHWptIAH', 'Quantity': '2.0', 'UnitPrice': '339.99'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '50.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '16.0', 'UnitPrice': '440.991'}, {'OrderId': '801Wt00000PH4FMIA1', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '1.0', 'UnitPrice': '399.99'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '10.0', 'UnitPrice': '449.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '5.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PFyITIA1', 'Quantity': '15.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PFyITIA1', 'Quantity': '8.0', 'UnitPrice': '503.4905'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'OrderId': '801Wt00000PHHhDIAX', 'Quantity': '12.0', 'UnitPrice': '314.991'}, {'OrderId': '#801Wt00000PHWptIAH', 'Quantity': '3.0', 'UnitPrice': '529.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '7.0', 'UnitPrice': '455.9905'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '5.0', 'UnitPrice': '427.4905'}, {'OrderId': '#801Wt00000PFt7UIAT', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '#801Wt00000PHVkDIAX', 'Quantity': '3.0', 'UnitPrice': '599.99'}], 'var_functions.execute_python:6': '005Wt000003NIXCIA4'}

exec(code, env_args)
