code = """import json
import pandas as pd

# Load Order Items
order_items_raw = locals()['var_function-call-17685673552228500933']
order_item_ids = set()
for item in order_items_raw:
    # Normalize: strip whitespace, remove leading '#'
    oid = item['Id'].strip()
    if oid.startswith('#'):
        oid = oid[1:]
    order_item_ids.add(oid)

# Load Cases
cases_file = locals()['var_function-call-3593888098400294967']
with open(cases_file, 'r') as f:
    cases_data = json.load(f)

filtered_cases = []
current_date = pd.to_datetime('2021-04-10').tz_localize('UTC')
start_date = current_date - pd.DateOffset(months=10)

print(f"Targeting Order Item IDs (count {len(order_item_ids)})")

for case in cases_data:
    oid_c = case.get('orderitemid__c')
    if not oid_c:
        continue
    # Normalize
    oid_c = oid_c.strip()
    if oid_c.startswith('#'):
        oid_c = oid_c[1:]
    
    if oid_c in order_item_ids:
        cdate_str = case.get('createddate')
        if not cdate_str:
            continue
        try:
            c_date = pd.to_datetime(cdate_str)
            if c_date.tzinfo is None:
                c_date = c_date.tz_localize('UTC')
            
            if c_date >= start_date and c_date <= current_date:
                filtered_cases.append({
                    'id': case['id'],
                    'month': c_date.strftime('%Y-%m'),
                    'month_name': c_date.strftime('%B')
                })
        except:
            pass

df = pd.DataFrame(filtered_cases)
if not df.empty:
    counts = df['month_name'].value_counts()
    print("__RESULT__:")
    print(counts.to_json())
else:
    print("__RESULT__:")
    print(json.dumps({}))"""

env_args = {'var_function-call-3903120554950776209': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-8688839653892335344': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-3593888098400294967': 'file_storage/function-call-3593888098400294967.json', 'var_function-call-15006923841398303866': {'November': 2, 'January': 1, 'September': 1, 'March': 1}, 'var_function-call-7712524867755978802': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'External_ID__c': 'Data Analytics Platforms,Security and Compliance Modules_13'}], 'var_function-call-17685673552228500933': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
