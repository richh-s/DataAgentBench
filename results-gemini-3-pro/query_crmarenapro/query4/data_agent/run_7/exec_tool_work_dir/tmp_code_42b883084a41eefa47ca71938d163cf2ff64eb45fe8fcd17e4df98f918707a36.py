code = """import pandas as pd
import json

# Access variables using locals() because of hyphens in keys
order_items = locals()['var_function-call-1163680895361236878']
cases_file_path = locals()['var_function-call-2618497939888766397']

# Clean OrderItem IDs
target_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    if oid:
        oid = oid.strip()
        if oid.startswith('#'):
            oid = oid[1:]
        target_order_item_ids.add(oid)

# Load cases
with open(cases_file_path, 'r') as f:
    cases_data = json.load(f)

cases_df = pd.DataFrame(cases_data)

# Clean Case OrderItem IDs
def clean_id(x):
    if x is None:
        return ""
    x = str(x).strip()
    if x.startswith('#'):
        return x[1:]
    return x

cases_df['clean_orderitemid'] = cases_df['orderitemid__c'].apply(clean_id)

# Filter cases by product (join logic)
cases_df = cases_df[cases_df['clean_orderitemid'].isin(target_order_item_ids)]

# Parse dates
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'])

# Filter date range: Past 10 months from 2021-04-10
end_date = pd.Timestamp('2021-04-10').tz_localize('UTC')
start_date = end_date - pd.DateOffset(months=10)

# Ensure createddate is timezone aware or handle it (it looks like it has +0000)
# pd.to_datetime usually handles ISO8601 with offset
# The dataset preview showed "2023-07-02T11:00:00.000+0000"
# Just to be safe, convert to UTC
if cases_df['createddate'].dt.tz is None:
    cases_df['createddate'] = cases_df['createddate'].dt.tz_localize('UTC')
else:
    cases_df['createddate'] = cases_df['createddate'].dt.tz_convert('UTC')

cases_df = cases_df[(cases_df['createddate'] >= start_date) & (cases_df['createddate'] <= end_date)]

# Group by Month
cases_df['month_year'] = cases_df['createddate'].dt.to_period('M').astype(str)
cases_df['month_name'] = cases_df['createddate'].dt.month_name()

counts = cases_df.groupby(['month_year', 'month_name']).size().reset_index(name='count')

print("__RESULT__:")
print(counts.to_json(orient='records'))"""

env_args = {'var_function-call-1163680895361236878': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-2618497939888766397': 'file_storage/function-call-2618497939888766397.json'}

exec(code, env_args)
