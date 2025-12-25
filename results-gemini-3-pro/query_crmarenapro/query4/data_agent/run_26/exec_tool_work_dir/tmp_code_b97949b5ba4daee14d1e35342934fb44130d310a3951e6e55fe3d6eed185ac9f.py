code = """import json
from datetime import datetime
import collections

# Load OrderItems
with open(locals()['var_function-call-4366002142693380250'], 'r') as f:
    order_items = json.load(f)

target_product_id = '01tWt000006hVJdIAM'
target_pbe_id = '01uWt0000027PJtIAM'

valid_order_item_ids = set()

for item in order_items:
    pid = item.get('Product2Id', '')
    pbe = item.get('PriceBookEntryId', '') # Key from preview
    oid = item.get('Id', '')
    
    if oid:
        # Clean IDs
        pid = pid.strip()
        if pid.startswith('#'):
            pid = pid[1:]
            
        pbe = pbe.strip()
        if pbe.startswith('#'):
            pbe = pbe[1:]
            
        oid = oid.strip()
        if oid.startswith('#'):
            oid = oid[1:]
        
        if pid == target_product_id or pbe == target_pbe_id:
            valid_order_item_ids.add(oid)

# Load Cases
with open(locals()['var_function-call-14716890772645570036'], 'r') as f:
    cases = json.load(f)

case_counts = collections.defaultdict(int)
all_counts = 0

start_date = datetime(2020, 6, 1)
end_date = datetime(2021, 4, 10)

for case in cases:
    oid = case.get('orderitemid__c')
    cdate_str = case.get('createddate')
    
    if oid and cdate_str:
        oid = oid.strip()
        if oid.startswith('#'):
            oid = oid[1:]
        
        if oid in valid_order_item_ids:
            try:
                date_part = cdate_str[:10]
                dt = datetime.strptime(date_part, '%Y-%m-%d')
                
                # Check date range
                if start_date <= dt <= end_date:
                    month_name = dt.strftime('%B')
                    case_counts[month_name] += 1
                    all_counts += 1
            except:
                pass

print("__RESULT__:")
print(json.dumps(case_counts))"""

env_args = {'var_function-call-647088612482234381': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-647088612482233272': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-14716890772645570036': 'file_storage/function-call-14716890772645570036.json', 'var_function-call-5639678163244169573': {'January': 1, 'November': 2, 'September': 1, 'March': 1}, 'var_function-call-13465245641380238800': 'file_storage/function-call-13465245641380238800.json', 'var_function-call-8790806689710718268': {'January': 1, 'November': 2, 'September': 1, 'March': 1}, 'var_function-call-3392742827441771171': [{'Name': 'SecureAnalytics Pro'}], 'var_function-call-11060956755486869955': {'filtered': {'January': 1, 'November': 2, 'September': 1, 'March': 1}, 'total_matches': 6}, 'var_function-call-11191345530562564092': [{'Id': '#01tWt000006hVJdIAM'}], 'var_function-call-729858300381811242': [], 'var_function-call-729858300381814469': [{'count': '153'}], 'var_function-call-729858300381813600': [{'count': '153'}], 'var_function-call-2312998877449157181': [{'Id': '01uWt0000027PJtIAM'}], 'var_function-call-4366002142693380250': 'file_storage/function-call-4366002142693380250.json'}

exec(code, env_args)
