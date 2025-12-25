code = """import json
import pandas as pd

with open(locals()['var_function-call-13900309014079849120'], 'r') as f:
    orders = json.load(f)

df_orders = pd.DataFrame(orders)
# Check statuses
print("__RESULT__:")
print(json.dumps(df_orders['Status'].unique().tolist()))"""

env_args = {'var_function-call-2295826410917181573': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-11560358009096936411': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'Status': 'Activated  ', 'EffectiveDate': '2020-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'Status': 'Activated', 'EffectiveDate': '2023-06-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_function-call-8471173522553135376': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}, {'Id': '802Wt0000078wz4IAA', 'OrderId': '801Wt00000PHVkDIAX', 'Product2Id': '01tWt000006hVDBIA2', 'Quantity': '3.0', 'UnitPrice': '549.99', 'PriceBookEntryId': '01uWt0000027PF3IAM'}, {'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '9.0', 'UnitPrice': '503.4905', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '#802Wt0000078xABIAY', 'OrderId': '801Wt00000PHVicIAH', 'Product2Id': '01tWt000006hVMrIAM', 'Quantity': '1.0', 'UnitPrice': '299.99', 'PriceBookEntryId': '01uWt0000027POjIAM'}], 'var_function-call-13900309014079849120': 'file_storage/function-call-13900309014079849120.json', 'var_function-call-10501813386352291870': 'file_storage/function-call-10501813386352291870.json', 'var_function-call-15249243181633914201': [{'OwnerId': '005Wt000003NIXCIA4', 'SalesAmount': 46919.149999999994}]}

exec(code, env_args)
