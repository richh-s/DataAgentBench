code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-13900309014079849120'], 'r') as f:
    orders = json.load(f)
with open(locals()['var_function-call-10501813386352291870'], 'r') as f:
    order_items = json.load(f)

df_orders = pd.DataFrame(orders)
df_items = pd.DataFrame(order_items)

# Clean IDs
def clean_id(x):
    if x is None: return None
    return str(x).strip().lstrip('#')

df_orders['Id'] = df_orders['Id'].apply(clean_id)
df_orders['OwnerId'] = df_orders['OwnerId'].apply(clean_id)
df_items['OrderId'] = df_items['OrderId'].apply(clean_id)

# Clean Dates
df_orders['EffectiveDate'] = pd.to_datetime(df_orders['EffectiveDate'], errors='coerce')

# Filter Dates
# Past 5 months from 2022-11-25: 2022-06-25 to 2022-11-25
start_date = pd.to_datetime('2022-06-25')
end_date = pd.to_datetime('2022-11-25')

# Filter orders
mask = (df_orders['EffectiveDate'] >= start_date) & (df_orders['EffectiveDate'] <= end_date)
df_filtered_orders = df_orders[mask].copy()

# Join
df_merged = pd.merge(df_filtered_orders, df_items, left_on='Id', right_on='OrderId', how='inner')

# Calculate Amount
# Quantity and UnitPrice are strings in JSON, need conversion
df_merged['Quantity'] = pd.to_numeric(df_merged['Quantity'], errors='coerce')
df_merged['UnitPrice'] = pd.to_numeric(df_merged['UnitPrice'], errors='coerce')
df_merged['SalesAmount'] = df_merged['Quantity'] * df_merged['UnitPrice']

# Group by OwnerId
sales_by_agent = df_merged.groupby('OwnerId')['SalesAmount'].sum().reset_index()
sales_by_agent = sales_by_agent.sort_values(by='SalesAmount', ascending=False)

top_agent = sales_by_agent.head(1).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_function-call-2295826410917181573': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-11560358009096936411': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'Status': 'Activated  ', 'EffectiveDate': '2020-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'Status': 'Activated', 'EffectiveDate': '2023-06-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_function-call-8471173522553135376': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}, {'Id': '802Wt0000078wz4IAA', 'OrderId': '801Wt00000PHVkDIAX', 'Product2Id': '01tWt000006hVDBIA2', 'Quantity': '3.0', 'UnitPrice': '549.99', 'PriceBookEntryId': '01uWt0000027PF3IAM'}, {'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '9.0', 'UnitPrice': '503.4905', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '#802Wt0000078xABIAY', 'OrderId': '801Wt00000PHVicIAH', 'Product2Id': '01tWt000006hVMrIAM', 'Quantity': '1.0', 'UnitPrice': '299.99', 'PriceBookEntryId': '01uWt0000027POjIAM'}], 'var_function-call-13900309014079849120': 'file_storage/function-call-13900309014079849120.json', 'var_function-call-10501813386352291870': 'file_storage/function-call-10501813386352291870.json'}

exec(code, env_args)
