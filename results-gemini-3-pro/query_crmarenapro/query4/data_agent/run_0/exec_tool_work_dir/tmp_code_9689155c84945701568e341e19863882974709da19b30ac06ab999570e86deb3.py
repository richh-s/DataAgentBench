code = """import json
import pandas as pd
import datetime

# Load OrderItem IDs
order_items = locals()['var_function-call-16950200408850617220']
valid_ids = set()
for item in order_items:
    raw_id = item.get('Id')
    if isinstance(raw_id, str):
        clean = raw_id.lstrip('#').strip()
        valid_ids.add(clean)

# Load Cases
file_path = locals()['var_function-call-5359725997570772964']
with open(file_path, 'r') as f:
    cases_data = json.load(f)

# Process Cases
cases = []
for case in cases_data:
    raw_oid = case.get('orderitemid__c')
    if not raw_oid:
        continue
    clean_oid = raw_oid.lstrip('#').strip()
    
    if clean_oid in valid_ids:
        cases.append(case)

df = pd.DataFrame(cases)
if not df.empty:
    df['createddate'] = pd.to_datetime(df['createddate'])

    # Filter by date range: Past 10 months from 2021-04-10
    start_date = pd.Timestamp('2020-06-10', tz='UTC')
    end_date = pd.Timestamp('2021-04-10', tz='UTC')

    df = df[(df['createddate'] >= start_date) & (df['createddate'] <= end_date)]

    df['YearMonth'] = df['createddate'].dt.to_period('M')
    monthly_counts = df.groupby('YearMonth').size()

    # Find max
    max_count = monthly_counts.max()
    max_period = monthly_counts.idxmax()
    
    result = max_period.strftime('%B')
else:
    result = "None"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16950200408850617220': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-5359725997570772964': 'file_storage/function-call-5359725997570772964.json'}

exec(code, env_args)
