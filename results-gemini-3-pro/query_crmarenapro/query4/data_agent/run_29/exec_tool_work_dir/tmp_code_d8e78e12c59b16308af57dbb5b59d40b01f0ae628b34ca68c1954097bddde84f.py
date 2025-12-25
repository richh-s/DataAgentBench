code = """import json
import pandas as pd

# Load OrderItem data
order_items = locals()['var_function-call-17981461665015701643']
clean_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    # Clean: stringify, strip whitespace, remove leading #
    oid = str(oid).strip()
    if oid.startswith('#'):
        oid = oid[1:]
    clean_order_item_ids.add(oid)

print(f"DEBUG: Number of clean OrderItem IDs: {len(clean_order_item_ids)}")

# Load Case data
case_file_path = locals()['var_function-call-15708709062430009873']
with open(case_file_path, 'r') as f:
    cases = json.load(f)

# Process Cases
case_data = []
for c in cases:
    raw_oid = c.get('orderitemid__c')
    if raw_oid:
        clean_oid = str(raw_oid).strip()
        if clean_oid.startswith('#'):
            clean_oid = clean_oid[1:]
        
        if clean_oid in clean_order_item_ids:
            case_data.append(c)

print(f"DEBUG: Number of matched Cases: {len(case_data)}")

df = pd.DataFrame(case_data)
if not df.empty:
    df['createddate'] = pd.to_datetime(df['createddate'])

    # Filter for past 10 months from 2021-04-10
    end_date = pd.Timestamp('2021-04-10').tz_localize('UTC')
    start_date = end_date - pd.DateOffset(months=10)

    df_filtered = df[(df['createddate'] >= start_date) & (df['createddate'] <= end_date)]
    
    # Group by month
    df_filtered['MonthName'] = df_filtered['createddate'].dt.month_name()
    df_filtered['Year'] = df_filtered['createddate'].dt.year
    # Create a sortable month string
    df_filtered['MonthSort'] = df_filtered['createddate'].dt.strftime('%Y-%m')
    
    monthly_counts = df_filtered.groupby(['Year', 'MonthName']).size().reset_index(name='count')
    # Sort by count desc
    monthly_counts = monthly_counts.sort_values(by='count', ascending=False)
    
    print("__RESULT__:")
    print(monthly_counts.to_json(orient='records'))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-17981461665015701643': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-15708709062430009873': 'file_storage/function-call-15708709062430009873.json', 'var_function-call-4524556861012458299': {'2020-November': 2, '2021-January': 1, '2020-September': 1, '2021-March': 1}, 'var_function-call-11887533739256296881': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}]}

exec(code, env_args)
