code = """import json

order_items = locals()['var_function-call-15960168675309596331']
target_ids = set()
for item in order_items:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    target_ids.add(oid)

file_path = locals()['var_function-call-5822691755495783972']
with open(file_path, 'r') as f:
    cases = json.load(f)

match_count = 0
total_cases = len(cases)
matched_dates = []

for case in cases:
    oid = case.get('orderitemid__c')
    if oid:
        if oid.startswith('#'):
            oid = oid[1:]
        if oid in target_ids:
            match_count += 1
            matched_dates.append(case.get('createddate'))

print("__RESULT__:")
print(json.dumps({"total_cases_in_file": total_cases, "matches": match_count, "sample_dates": matched_dates[:10]}))"""

env_args = {'var_function-call-1114849343674935655': [], 'var_function-call-1114849343674935754': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-10923393815479506923': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-15960168675309596331': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-5822691755495783972': 'file_storage/function-call-5822691755495783972.json', 'var_function-call-4105337430942002585': {'January': 1, 'November': 2, 'September': 1, 'March': 1}}

exec(code, env_args)
