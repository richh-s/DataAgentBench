code = """import pandas as pd, json

rows = var_call_1NsguBoGUnXCoueT5tW2wmpj

# Convert to DataFrame
df = pd.DataFrame(rows)

# Clean AgentId by stripping whitespace (and keep leading '#', as it may be meaningful)
df['AgentId'] = df['AgentId'].astype(str).str.strip()

# Ensure numeric types
df['Quantity'] = pd.to_numeric(df['Quantity'])
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'])

# Compute sales amount per row
df['SalesAmount'] = df['Quantity'] * df['UnitPrice']

# Aggregate by AgentId
agg = df.groupby('AgentId', as_index=False)['SalesAmount'].sum()

# Find the AgentId with the maximum sales
top_row = agg.sort_values('SalesAmount', ascending=False).iloc[0]
result = top_row['AgentId']

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_1NsguBoGUnXCoueT5tW2wmpj': [{'OrderId': '#801Wt00000PFt7UIAT', 'AgentId': '005Wt000003NIiUIAW', 'Quantity': '10.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-09-15'}, {'OrderId': '#801Wt00000PFt7UIAT', 'AgentId': '005Wt000003NIiUIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PFyITIA1', 'AgentId': '005Wt000003NDJ0IAO', 'Quantity': '15.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-07-10'}, {'OrderId': '801Wt00000PFyITIA1', 'AgentId': '005Wt000003NDJ0IAO', 'Quantity': '8.0', 'UnitPrice': '503.4905', 'EffectiveDate': '2022-07-10'}, {'OrderId': '801Wt00000PGGhBIAX', 'AgentId': '005Wt000003NIaRIAW', 'Quantity': '10.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-10-01'}, {'OrderId': '801Wt00000PGGhBIAX', 'AgentId': '005Wt000003NIaRIAW', 'Quantity': '14.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-10-01'}, {'OrderId': '801Wt00000PGGhBIAX', 'AgentId': '005Wt000003NIaRIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-10-01'}, {'OrderId': '#801Wt00000PGbdMIAT', 'AgentId': '#005Wt000003NGtcIAG', 'Quantity': '20.0', 'UnitPrice': '450.4915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '#801Wt00000PGbdMIAT', 'AgentId': '#005Wt000003NGtcIAG', 'Quantity': '30.0', 'UnitPrice': '390.9915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PH4FMIA1', 'AgentId': '#005Wt000003NJmbIAG', 'Quantity': '10.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PH8yvIAD', 'AgentId': '005Wt000003NIXCIA4', 'Quantity': '20.0', 'UnitPrice': '390.9915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PH8yvIAD', 'AgentId': '005Wt000003NIXCIA4', 'Quantity': '30.0', 'UnitPrice': '552.4915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PH8yvIAD', 'AgentId': '005Wt000003NIXCIA4', 'Quantity': '50.0', 'UnitPrice': '450.4915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'AgentId': '005Wt000003NJ9uIAG', 'Quantity': '1.0', 'UnitPrice': '399.99', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'AgentId': '005Wt000003NJ9uIAG', 'Quantity': '3.0', 'UnitPrice': '499.99', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'AgentId': '005Wt000003NJ9uIAG', 'Quantity': '5.0', 'UnitPrice': '427.4905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'AgentId': '005Wt000003NJ9uIAG', 'Quantity': '7.0', 'UnitPrice': '455.9905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHhDIAX', 'AgentId': '#005Wt000003NITxIAO', 'Quantity': '12.0', 'UnitPrice': '314.991', 'EffectiveDate': '2022-08-01'}, {'OrderId': '801Wt00000PHLzNIAX', 'AgentId': '005Wt000003NEoYIAW', 'Quantity': '10.0', 'UnitPrice': '449.991', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PHLzNIAX', 'AgentId': '005Wt000003NEoYIAW', 'Quantity': '12.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PHLzNIAX', 'AgentId': '005Wt000003NEoYIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PHRFAIA5', 'AgentId': '#005Wt000003NIx1IAG', 'Quantity': '16.0', 'UnitPrice': '440.991', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHRFAIA5', 'AgentId': '#005Wt000003NIx1IAG', 'Quantity': '5.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHRFAIA5', 'AgentId': '#005Wt000003NIx1IAG', 'Quantity': '7.0', 'UnitPrice': '379.9905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHRFAIA5', 'AgentId': '#005Wt000003NIx1IAG', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '#801Wt00000PHVkDIAX', 'AgentId': '005Wt000003NJt3IAG', 'Quantity': '3.0', 'UnitPrice': '599.99', 'EffectiveDate': '2022-08-15'}, {'OrderId': '801Wt00000PHVqfIAH', 'AgentId': '005Wt000003NDEBIA4', 'Quantity': '10.0', 'UnitPrice': '539.991', 'EffectiveDate': '2022-09-20'}, {'OrderId': '#801Wt00000PHWptIAH', 'AgentId': '005Wt000003NJ0EIAW', 'Quantity': '2.0', 'UnitPrice': '339.99', 'EffectiveDate': '2022-09-25'}, {'OrderId': '#801Wt00000PHWptIAH', 'AgentId': '005Wt000003NJ0EIAW', 'Quantity': '3.0', 'UnitPrice': '529.99', 'EffectiveDate': '2022-09-25'}]}

exec(code, env_args)
