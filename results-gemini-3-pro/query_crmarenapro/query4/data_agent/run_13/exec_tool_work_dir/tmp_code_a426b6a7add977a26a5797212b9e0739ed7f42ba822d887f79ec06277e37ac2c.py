code = """import json
from datetime import datetime

order_items = locals()['var_function-call-10888803579691069025']
cases_file = locals()['var_function-call-2174225455058142858']

with open(cases_file, 'r') as f:
    cases = json.load(f)

def clean_id(val):
    if not val:
        return ""
    s = str(val).strip()
    if s.startswith("#"):
        s = s[1:]
    return s

target_product_id = "01tWt000006hVJdIAM"
target_order_item_ids = set()

for oi in order_items:
    pid = clean_id(oi.get("Product2Id"))
    oid = clean_id(oi.get("Id"))
    if pid == target_product_id:
        target_order_item_ids.add(oid)

match_count = 0
date_mismatch_count = 0
matches_per_month = {}

start_date = datetime(2020, 6, 10)
end_date = datetime(2021, 4, 10, 23, 59, 59)

for c in cases:
    c_oid = clean_id(c.get("orderitemid__c"))
    if c_oid in target_order_item_ids:
        match_count += 1
        c_date_str = c.get("createddate")
        if c_date_str:
            try:
                dt = datetime.strptime(c_date_str[:19], "%Y-%m-%dT%H:%M:%S")
                m_key = dt.strftime("%Y-%m")
                matches_per_month[m_key] = matches_per_month.get(m_key, 0) + 1
            except:
                pass

debug_info = {
    "target_order_item_count": len(target_order_item_ids),
    "total_case_matches": match_count,
    "matches_per_month": matches_per_month
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-10888803579691069025': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-10888803579691066634': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-2174225455058142858': 'file_storage/function-call-2174225455058142858.json', 'var_function-call-9786930371562019834': {'2021-01': 1, '2020-11': 2, '2020-09': 1, '2021-03': 1}}

exec(code, env_args)
