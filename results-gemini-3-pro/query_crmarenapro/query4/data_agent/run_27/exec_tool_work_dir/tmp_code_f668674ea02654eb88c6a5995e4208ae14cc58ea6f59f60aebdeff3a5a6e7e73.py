code = """import json
import pandas as pd

# Access variables from locals
order_items_json = locals()['var_function-call-3562023347462174956']
cases_file_path = locals()['var_function-call-7329632320469133909']

# Load OrderItem IDs
order_items = json.loads(order_items_json)
target_item_ids = set()
for item in order_items:
    # Clean ID: remove leading '#'
    clean_id = item['Id'].lstrip('#').strip()
    target_item_ids.add(clean_id)

# Load Cases
with open(cases_file_path, 'r') as f:
    cases = json.load(f)

df = pd.DataFrame(cases)

# Clean orderitemid__c
# Handle potential NaN or non-string
df['clean_orderitemid'] = df['orderitemid__c'].astype(str).apply(lambda x: x.lstrip('#').strip())

# Filter by target OrderItem IDs
df_filtered = df[df['clean_orderitemid'].isin(target_item_ids)].copy()

# Convert createddate to datetime
# Format seems to be ISO 8601 like "2023-07-02T11:00:00.000+0000"
df_filtered['created_dt'] = pd.to_datetime(df_filtered['createddate'])

# Filter by date range: past 10 months from 2021-04-10
# 10 months ago from April 2021 is roughly June 2020.
# Let's say range is 2020-06-10 to 2021-04-10.
start_date = pd.Timestamp('2020-06-10', tz='UTC')
end_date = pd.Timestamp('2021-04-10', tz='UTC')

df_in_range = df_filtered[(df_filtered['created_dt'] >= start_date) & (df_filtered['created_dt'] <= end_date)].copy()

# Extract month name
df_in_range['month_name'] = df_in_range['created_dt'].dt.month_name()
df_in_range['year_month'] = df_in_range['created_dt'].dt.to_period('M')

# Count per month
counts = df_in_range.groupby('month_name')['id'].count()
counts_ym = df_in_range.groupby('year_month')['id'].count()

print("__RESULT__:")
print(json.dumps({
    "counts_by_month_name": counts.to_dict(),
    "counts_by_year_month": {str(k): v for k, v in counts_ym.to_dict().items()}
}))"""

env_args = {'var_function-call-3562023347462174956': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-7329632320469133909': 'file_storage/function-call-7329632320469133909.json'}

exec(code, env_args)
