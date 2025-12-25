code = """import json
import pandas as pd
from datetime import datetime, timedelta

# Load Order Items
order_items = locals()['var_function-call-538766658491964125']
# Create set of valid IDs, handling leading '#'
target_ids = set()
for item in order_items:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    target_ids.add(oid)

# Load Cases
file_path = locals()['var_function-call-1872938474651528192']
with open(file_path, 'r') as f:
    cases = json.load(f)

# Process Cases
filtered_cases = []
ref_date = datetime(2021, 4, 10)
start_date = ref_date - timedelta(days=30*10) # Approximately 10 months

for case in cases:
    c_date_str = case['createddate']
    # Parse date (format: 2023-07-02T11:00:00.000+0000)
    # Using pandas to parse is easier but let's try basic string slicing first or pd.to_datetime later
    # Format seems ISO8601-like
    
    # ID cleaning
    c_oid = case.get('orderitemid__c')
    if not c_oid:
        continue
    if c_oid.startswith('#'):
        c_oid = c_oid[1:]
    
    if c_oid in target_ids:
        filtered_cases.append({'date': c_date_str, 'id': c_oid})

df = pd.DataFrame(filtered_cases)
if not df.empty:
    df['date'] = pd.to_datetime(df['date'])
    # Filter by date range: Past 10 months from 2021-04-10
    # Let's say June 2020 to April 2021
    # 2020-06-10 to 2021-04-10
    mask = (df['date'] >= '2020-06-10') & (df['date'] <= '2021-04-10')
    df_filtered = df[mask].copy()
    
    df_filtered['month_year'] = df_filtered['date'].dt.strftime('%Y-%B')
    counts = df_filtered['month_year'].value_counts().sort_index()
    
    print('__RESULT__:')
    print(counts.to_json())
else:
    print('__RESULT__:')
    print(json.dumps({}))"""

env_args = {'var_function-call-7545720086494888731': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-538766658491964125': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-1872938474651528192': 'file_storage/function-call-1872938474651528192.json'}

exec(code, env_args)
