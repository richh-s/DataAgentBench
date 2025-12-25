code = """import json
from datetime import datetime

order_items = locals()['var_function-call-16064184842318411823']
with open(locals()['var_function-call-8702892083309368303'], 'r') as f:
    cases = json.load(f)

def clean_id(val):
    if not val:
        return ""
    val = str(val).strip()
    if val.startswith('#'):
        val = val[1:]
    return val

valid_order_item_ids = set()
for item in order_items:
    valid_order_item_ids.add(clean_id(item['Id']))

debug_counts = {}
total_matches = 0

for case in cases:
    case_oid = clean_id(case.get('orderitemid__c'))
    if case_oid in valid_order_item_ids:
        total_matches += 1
        c_date_str = case.get('createddate')
        try:
            c_date = datetime.strptime(c_date_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            month_key = c_date.strftime("%B %Y")
            debug_counts[month_key] = debug_counts.get(month_key, 0) + 1
        except ValueError:
            pass

print("__RESULT__:")
print(json.dumps({
    "num_order_items": len(valid_order_item_ids),
    "total_matches": total_matches,
    "all_month_counts": debug_counts
}))"""

env_args = {'var_function-call-16064184842318411823': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-8702892083309368303': 'file_storage/function-call-8702892083309368303.json', 'var_function-call-7519533941935195638': {'January 2021': 1, 'November 2020': 2, 'September 2020': 1, 'March 2021': 1}}

exec(code, env_args)
