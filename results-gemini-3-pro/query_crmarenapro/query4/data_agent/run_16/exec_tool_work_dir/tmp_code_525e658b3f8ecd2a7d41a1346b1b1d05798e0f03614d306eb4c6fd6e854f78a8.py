code = """import json
from collections import Counter
from datetime import datetime

order_items = locals()['var_function-call-15960168675309596331']
target_ids_15 = set()
for item in order_items:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    target_ids_15.add(oid[:15])

file_path = locals()['var_function-call-5822691755495783972']
with open(file_path, 'r') as f:
    cases = json.load(f)

# Date range: 2020-06-10 to 2021-04-10
start_date = datetime(2020, 6, 10)
end_date = datetime(2021, 4, 10)

counts = Counter()

for case in cases:
    oid = case.get('orderitemid__c')
    if not oid:
        continue
    if oid.startswith('#'):
        oid = oid[1:]
    
    # Match on 15 chars
    if oid[:15] in target_ids_15:
        c_date_str = case.get('createddate')
        try:
            dt = datetime.strptime(c_date_str[:10], '%Y-%m-%d')
            if start_date <= dt <= end_date:
                month_name = dt.strftime('%B')
                counts[month_name] += 1
        except:
            pass

print("__RESULT__:")
print(json.dumps(counts))"""

env_args = {'var_function-call-1114849343674935655': [], 'var_function-call-1114849343674935754': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-10923393815479506923': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-15960168675309596331': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-5822691755495783972': 'file_storage/function-call-5822691755495783972.json', 'var_function-call-4105337430942002585': {'January': 1, 'November': 2, 'September': 1, 'March': 1}, 'var_function-call-12135099683109002930': {'total_cases_in_file': 153, 'matches': 6, 'sample_dates': ['2021-01-25T09:30:00.000+0000', '2020-11-05T08:19:00.000+0000', '2023-06-30T13:03:00.000+0000', '2020-09-29T01:59:00.000+0000', '2021-03-07T11:25:00.000+0000', '2020-11-09T19:02:00.000+0000']}, 'var_function-call-12049651236594350279': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-9275372129351384085': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
