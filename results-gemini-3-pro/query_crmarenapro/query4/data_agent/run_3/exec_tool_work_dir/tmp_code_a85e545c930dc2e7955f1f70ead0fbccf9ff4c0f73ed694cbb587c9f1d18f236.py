code = """import json
import pandas as pd
import datetime

# Load OrderItem IDs
# The variable is already a list
order_items = locals()['var_function-call-174254281076829396']
target_ids = set()
for item in order_items:
    oid = item['Id']
    if oid:
        target_ids.add(oid.lstrip('#'))

# Load Cases
with open(locals()['var_function-call-11873204265821133797'], 'r') as f:
    cases = json.load(f)

# Filter and Process
filtered_cases = []
# "Past 10 months" relative to 2021-04-10
# Usually means [2020-06-10, 2021-04-10]
end_date = pd.to_datetime('2021-04-10').tz_localize('UTC')
start_date = end_date - pd.DateOffset(months=10)

for case in cases:
    oid = case.get('orderitemid__c')
    cdate_str = case.get('createddate')
    
    if oid and cdate_str:
        clean_oid = oid.lstrip('#')
        if clean_oid in target_ids:
            try:
                cdate = pd.to_datetime(cdate_str)
                # Check timezone
                if cdate.tzinfo is None:
                    cdate = cdate.tz_localize('UTC')
                # Normalize to UTC if different
                cdate = cdate.astimezone(datetime.timezone.utc)
                
                if start_date <= cdate <= end_date:
                    filtered_cases.append({'createddate': cdate})
            except Exception as e:
                pass

df = pd.DataFrame(filtered_cases)

if not df.empty:
    df['month'] = df['createddate'].dt.strftime('%B')
    df['year_month'] = df['createddate'].dt.strftime('%Y-%m')
    counts = df.groupby(['year_month', 'month']).size().reset_index(name='count')
    counts = counts.sort_values('year_month')
    
    print("__RESULT__:")
    print(counts.to_json(orient='records'))
else:
    print("__RESULT__:")
    print(json.dumps([]))"""

env_args = {'var_function-call-174254281076829396': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-11873204265821133797': 'file_storage/function-call-11873204265821133797.json'}

exec(code, env_args)
