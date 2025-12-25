code = """import json
from datetime import datetime

file_path = locals()['var_function-call-15840550546839219915']
with open(file_path, 'r') as f:
    history_data = json.load(f)

# Last 12 months
start_date = datetime(2022, 4, 10)
end_date = datetime(2023, 4, 10, 23, 59, 59)

handled_counts = {}
transfer_counts = {}

def clean_id(val):
    if not val or val == 'None':
        return None
    val = val.strip()
    if val.startswith('#'):
        val = val[1:]
    if len(val) < 5:
        return None
    return val

def parse_date(date_str):
    try:
        dt_str = date_str.split('+')[0]
        return datetime.strptime(dt_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
    except:
        return None

for record in history_data:
    d_str = record.get('createddate')
    dt = parse_date(d_str)
    
    if dt and start_date <= dt <= end_date:
        old_val = clean_id(record.get('oldvalue__c'))
        new_val = clean_id(record.get('newvalue__c'))
        
        if new_val:
            handled_counts[new_val] = handled_counts.get(new_val, 0) + 1
        if old_val:
            transfer_counts[old_val] = transfer_counts.get(old_val, 0) + 1

candidates = []
for agent, h_count in handled_counts.items():
    t_count = transfer_counts.get(agent, 0)
    candidates.append({"id": agent, "handled": h_count, "transfers": t_count})

candidates.sort(key=lambda x: (x['transfers'], -x['handled']))

print("__RESULT__:")
print(json.dumps(candidates[:10]))"""

env_args = {'var_function-call-3045517057883522603': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5940713645896962222': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-2920167374087173322': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-6188298989589663829': [{'id': 'a04Wt00000534p0IAA', 'caseid__c': '500Wt00000DDzRCIA1', 'oldvalue__c': '005Wt000003NFhOIAW', 'newvalue__c': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:38:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000535UwIAI', 'caseid__c': '500Wt00000DDzW3IAL', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NIfHIAW', 'createddate': '2021-11-02T13:31:14.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537riIAA', 'caseid__c': '500Wt00000DDzSnIAL', 'oldvalue__c': '005Wt000003NHuUIAW', 'newvalue__c': '005Wt000003NJ9tIAG', 'createddate': '2021-10-15T13:58:32.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt0000053831IAA', 'caseid__c': '500Wt00000DDnt7IAD', 'oldvalue__c': '005Wt000003NHGAIA4', 'newvalue__c': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T15:47:56.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-15840550546839219915': 'file_storage/function-call-15840550546839219915.json', 'var_function-call-17968858354395597536': {'min_count': 0, 'agents': ['005Wt000003NJD9IAO', '005Wt000003NJ0DIAW', '005Wt000003NInLIAW', '005Wt000003NIwzIAG', '005Wt000003NIvNIAW', '005Wt000003NEzqIAG', '005Wt000003NJhlIAG', '005Wt000003NJEjIAO', '005Wt000003NJ6gIAG', '005Wt000003NGjuIAG', '005Wt000003NIc2IAG', '005Wt000003NIVZIA4', '005Wt000003NFr4IAG', '005Wt000003NBykIAG', '005Wt000003NJTFIA4', '005Wt000003NFKoIAO', '005Wt000003NHsrIAG', '005Wt000003NISLIA4', '005Wt000003NJoDIAW', '005Wt000003NBcAIAW', '005Wt000003NJcvIAG', '005Wt000003NJ8HIAW', '005Wt000003NIaQIAW', '005Wt000003NHpeIAG', '005Wt000003NDsUIAW', '005Wt000003NEGhIAO', '005Wt000003NINVIA4', '005Wt000003NDqFIAW', '005Wt000003NI2XIAW', '005Wt000003NDJ1IAO', '005Wt000003NJrRIAW'], 'total_candidates': 32}, 'var_function-call-10733184246661407943': [{'id': '005Wt000003NFKoIAO', 'handled': 3, 'transfers': 0}, {'id': '005Wt000003NHsrIAG', 'handled': 2, 'transfers': 0}, {'id': '005Wt000003NINVIA4', 'handled': 2, 'transfers': 0}, {'id': '005Wt000003NJhlIAG', 'handled': 2, 'transfers': 0}, {'id': '005Wt000003NJ8HIAW', 'handled': 2, 'transfers': 0}, {'id': '005Wt000003NJcvIAG', 'handled': 1, 'transfers': 0}, {'id': '005Wt000003NDqFIAW', 'handled': 1, 'transfers': 0}, {'id': '005Wt000003NEzqIAG', 'handled': 1, 'transfers': 0}, {'id': '005Wt000003NEGhIAO', 'handled': 1, 'transfers': 0}, {'id': '005Wt000003NJ6gIAG', 'handled': 1, 'transfers': 0}]}

exec(code, env_args)
