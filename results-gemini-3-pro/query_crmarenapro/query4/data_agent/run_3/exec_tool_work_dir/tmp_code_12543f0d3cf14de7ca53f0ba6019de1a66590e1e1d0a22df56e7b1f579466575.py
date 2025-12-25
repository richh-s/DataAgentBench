code = """import json
import pandas as pd

# Load OrderItem IDs
order_items = locals()['var_function-call-174254281076829396']
target_ids = set()
for item in order_items:
    oid = item['Id']
    if oid:
        target_ids.add(oid.lstrip('#'))

# Load Cases
with open(locals()['var_function-call-11873204265821133797'], 'r') as f:
    cases = json.load(f)

matched_cases = []
for case in cases:
    oid = case.get('orderitemid__c')
    if oid:
        clean_oid = oid.lstrip('#')
        if clean_oid in target_ids:
            matched_cases.append(case)

debug_info = {}
debug_info['total_cases'] = len(cases)
debug_info['matched_count'] = len(matched_cases)

if matched_cases:
    df = pd.DataFrame(matched_cases)
    df['dt'] = pd.to_datetime(df['createddate'])
    # Group by month
    df['month_year'] = df['dt'].dt.to_period('M').astype(str)
    counts = df['month_year'].value_counts().to_dict()
    debug_info['counts'] = counts

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-174254281076829396': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-11873204265821133797': 'file_storage/function-call-11873204265821133797.json', 'var_function-call-14776065568724950520': [{'year_month': '2020-09', 'month': 'September', 'count': 1}, {'year_month': '2020-11', 'month': 'November', 'count': 2}, {'year_month': '2021-01', 'month': 'January', 'count': 1}, {'year_month': '2021-03', 'month': 'March', 'count': 1}], 'var_function-call-17039264448365346050': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-49142100613548160': 'Done'}

exec(code, env_args)
