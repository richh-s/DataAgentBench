code = """import pandas as pd
data = locals()['var_function-call-5218675286338104934']
df = pd.DataFrame(data)

# Clean OwnerId by removing '#' if present
df['OwnerId'] = df['OwnerId'].astype(str).str.replace('#', '')

df['Quantity'] = pd.to_numeric(df['Quantity'])
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'])

df['SalesAmount'] = df['Quantity'] * df['UnitPrice']

agent_sales = df.groupby('OwnerId')['SalesAmount'].sum().reset_index()

top_agent = agent_sales.loc[agent_sales['SalesAmount'].idxmax()]

print("__RESULT__:")
print(top_agent['OwnerId'])"""

env_args = {'var_function-call-10929918150490677000': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-5218675286338104934': [{'OwnerId': '005Wt000003NIiUIAW', 'Quantity': '10.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-09-15'}, {'OwnerId': '005Wt000003NIiUIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-09-15'}, {'OwnerId': '005Wt000003NDJ0IAO', 'Quantity': '15.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-07-10'}, {'OwnerId': '005Wt000003NDJ0IAO', 'Quantity': '8.0', 'UnitPrice': '503.4905', 'EffectiveDate': '2022-07-10'}, {'OwnerId': '005Wt000003NIaRIAW', 'Quantity': '10.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-10-01'}, {'OwnerId': '005Wt000003NIaRIAW', 'Quantity': '14.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-10-01'}, {'OwnerId': '005Wt000003NIaRIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-10-01'}, {'OwnerId': '#005Wt000003NGtcIAG', 'Quantity': '20.0', 'UnitPrice': '450.4915', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '#005Wt000003NGtcIAG', 'Quantity': '30.0', 'UnitPrice': '390.9915', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '#005Wt000003NJmbIAG', 'Quantity': '10.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-09-15'}, {'OwnerId': '005Wt000003NIXCIA4', 'Quantity': '20.0', 'UnitPrice': '390.9915', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '005Wt000003NIXCIA4', 'Quantity': '30.0', 'UnitPrice': '552.4915', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '005Wt000003NIXCIA4', 'Quantity': '50.0', 'UnitPrice': '450.4915', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '1.0', 'UnitPrice': '399.99', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '3.0', 'UnitPrice': '499.99', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '5.0', 'UnitPrice': '427.4905', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '7.0', 'UnitPrice': '455.9905', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '#005Wt000003NITxIAO', 'Quantity': '12.0', 'UnitPrice': '314.991', 'EffectiveDate': '2022-08-01'}, {'OwnerId': '005Wt000003NEoYIAW', 'Quantity': '10.0', 'UnitPrice': '449.991', 'EffectiveDate': '2022-09-15'}, {'OwnerId': '005Wt000003NEoYIAW', 'Quantity': '12.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-09-15'}, {'OwnerId': '005Wt000003NEoYIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-09-15'}, {'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '16.0', 'UnitPrice': '440.991', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '5.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '7.0', 'UnitPrice': '379.9905', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-07-01'}, {'OwnerId': '005Wt000003NJt3IAG', 'Quantity': '3.0', 'UnitPrice': '599.99', 'EffectiveDate': '2022-08-15'}, {'OwnerId': '005Wt000003NDEBIA4', 'Quantity': '10.0', 'UnitPrice': '539.991', 'EffectiveDate': '2022-09-20'}, {'OwnerId': '005Wt000003NJ0EIAW', 'Quantity': '2.0', 'UnitPrice': '339.99', 'EffectiveDate': '2022-09-25'}, {'OwnerId': '005Wt000003NJ0EIAW', 'Quantity': '3.0', 'UnitPrice': '529.99', 'EffectiveDate': '2022-09-25'}]}

exec(code, env_args)
