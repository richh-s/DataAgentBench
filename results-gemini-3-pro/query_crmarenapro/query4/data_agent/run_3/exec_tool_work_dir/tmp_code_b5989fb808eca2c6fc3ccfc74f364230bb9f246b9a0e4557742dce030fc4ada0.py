code = """import json
import pandas as pd

# Load OrderItem IDs
order_items = locals()['var_function-call-174254281076829396']
target_ids = set()
for item in order_items:
    oid = item['Id']
    if oid:
        # Strip whitespace and #
        target_ids.add(oid.strip().lstrip('#'))

# Load Cases
with open(locals()['var_function-call-11873204265821133797'], 'r') as f:
    cases = json.load(f)

matched_cases = []
start_date = pd.Timestamp('2020-06-10', tz='UTC')
end_date = pd.Timestamp('2021-04-10', tz='UTC')

for case in cases:
    oid = case.get('orderitemid__c')
    cdate_str = case.get('createddate')
    
    if oid and cdate_str:
        clean_oid = oid.strip().lstrip('#')
        if clean_oid in target_ids:
            try:
                cdate = pd.to_datetime(cdate_str)
                if cdate.tzinfo is None:
                    cdate = cdate.tz_localize('UTC')
                cdate = cdate.astimezone(pd.Timestamp.now().tz) # Align to UTC
                # Actually just convert to UTC
                cdate = cdate.tz_convert('UTC')

                if start_date <= cdate <= end_date:
                    matched_cases.append({'date': cdate})
            except:
                pass

if matched_cases:
    df = pd.DataFrame(matched_cases)
    df['month'] = df['date'].dt.strftime('%B')
    df['year_month'] = df['date'].dt.to_period('M')
    counts = df['year_month'].value_counts().sort_index()
    print("__RESULT__:")
    # Convert to string for printing
    print(counts.to_json())
else:
    print("__RESULT__:")
    print(json.dumps({}))"""

env_args = {'var_function-call-174254281076829396': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-11873204265821133797': 'file_storage/function-call-11873204265821133797.json', 'var_function-call-14776065568724950520': [{'year_month': '2020-09', 'month': 'September', 'count': 1}, {'year_month': '2020-11', 'month': 'November', 'count': 2}, {'year_month': '2021-01', 'month': 'January', 'count': 1}, {'year_month': '2021-03', 'month': 'March', 'count': 1}], 'var_function-call-17039264448365346050': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-49142100613548160': 'Done', 'var_function-call-1015091591446595413': {'total_cases': 153, 'matched_count': 6, 'counts': {'2020-11': 2, '2021-01': 1, '2023-06': 1, '2020-09': 1, '2021-03': 1}}, 'var_function-call-2304885649518893948': [{'count': '153'}], 'var_function-call-4117866771748014130': [{'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000'}], 'var_function-call-18446502841409028470': []}

exec(code, env_args)
