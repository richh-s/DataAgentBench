code = """import json
import pandas as pd
from datetime import datetime

# Load OrderItem data
order_items = locals()['var_function-call-17981461665015701643']
clean_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    clean_order_item_ids.add(oid)

# Load Case data
# accessing the file path from the storage key
case_file_path = locals()['var_function-call-15708709062430009873']
with open(case_file_path, 'r') as f:
    cases = json.load(f)

# Process Cases
case_data = []
for c in cases:
    # Clean orderitemid__c
    raw_oid = c.get('orderitemid__c')
    if raw_oid:
        clean_oid = raw_oid
        if clean_oid.startswith('#'):
            clean_oid = clean_oid[1:]
        
        if clean_oid in clean_order_item_ids:
            case_data.append(c)

df = pd.DataFrame(case_data)
df['createddate'] = pd.to_datetime(df['createddate'])

# Filter for past 10 months from 2021-04-10
end_date = pd.Timestamp('2021-04-10').tz_localize('UTC')
start_date = end_date - pd.DateOffset(months=10)

df_filtered = df[(df['createddate'] >= start_date) & (df['createddate'] <= end_date)]

# Group by month
# Format month as 'YYYY-MM'
df_filtered['Month'] = df_filtered['createddate'].dt.strftime('%Y-%B')
monthly_counts = df_filtered['Month'].value_counts()

print("__RESULT__:")
print(monthly_counts.to_json())"""

env_args = {'var_function-call-17981461665015701643': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-15708709062430009873': 'file_storage/function-call-15708709062430009873.json'}

exec(code, env_args)
