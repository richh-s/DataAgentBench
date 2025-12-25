code = """import json
from datetime import datetime
import collections

# Load OrderItems
with open(locals()['var_function-call-13465245641380238800'], 'r') as f:
    order_items = json.load(f)

target_product_id = '01tWt000006hVJdIAM'
valid_order_item_ids = set()

for item in order_items:
    pid = item.get('Product2Id')
    oid = item.get('Id')
    if pid and oid:
        # Clean Product ID
        if pid.startswith('#'):
            pid = pid[1:]
        
        if pid == target_product_id:
            # Clean Order Item ID
            if oid.startswith('#'):
                oid = oid[1:]
            valid_order_item_ids.add(oid)

# Load Cases
with open(locals()['var_function-call-14716890772645570036'], 'r') as f:
    cases = json.load(f)

case_counts = collections.defaultdict(int)

start_date = datetime(2020, 6, 1)
end_date = datetime(2021, 4, 10)

for case in cases:
    oid = case.get('orderitemid__c')
    cdate_str = case.get('createddate')
    
    if oid and cdate_str:
        if oid.startswith('#'):
            oid = oid[1:]
        
        if oid in valid_order_item_ids:
            try:
                date_part = cdate_str[:10]
                dt = datetime.strptime(date_part, '%Y-%m-%d')
                
                if start_date <= dt <= end_date:
                    month_name = dt.strftime('%B')
                    case_counts[month_name] += 1
            except:
                pass

print("__RESULT__:")
print(json.dumps(case_counts))"""

env_args = {'var_function-call-647088612482234381': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-647088612482233272': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-14716890772645570036': 'file_storage/function-call-14716890772645570036.json', 'var_function-call-5639678163244169573': {'January': 1, 'November': 2, 'September': 1, 'March': 1}, 'var_function-call-13465245641380238800': 'file_storage/function-call-13465245641380238800.json'}

exec(code, env_args)
