code = """import pandas as pd
import json

# Load order items
order_items = json.loads(var_function_call_1163680895361236878)
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
with open(var_function_call_2618497939888766397, 'r') as f:
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
# 10 months ago is approx 2020-06-10
end_date = pd.Timestamp('2021-04-10')
start_date = end_date - pd.DateOffset(months=10)

cases_df = cases_df[(cases_df['createddate'] >= start_date) & (cases_df['createddate'] <= end_date)]

# Group by Month
# We need the month name.
cases_df['month_year'] = cases_df['createddate'].dt.to_period('M')
cases_df['month_name'] = cases_df['createddate'].dt.month_name()

counts = cases_df.groupby(['month_year', 'month_name']).size().reset_index(name='count')

print("__RESULT__:")
print(counts.to_json(orient='records'))"""

env_args = {'var_function-call-1163680895361236878': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-2618497939888766397': 'file_storage/function-call-2618497939888766397.json'}

exec(code, env_args)
