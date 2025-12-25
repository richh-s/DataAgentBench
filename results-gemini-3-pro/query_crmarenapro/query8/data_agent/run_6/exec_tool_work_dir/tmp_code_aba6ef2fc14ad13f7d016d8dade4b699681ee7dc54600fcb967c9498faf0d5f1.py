code = """import json
from datetime import datetime

# Load data
with open(locals()['var_function-call-4741343475108631162'], 'r') as f:
    history = json.load(f)

with open(locals()['var_function-call-3312263680111285021'], 'r') as f:
    cases = json.load(f)

with open(locals()['var_function-call-12179606321985110018'], 'r') as f:
    users = json.load(f)

def clean_id(i):
    if i and isinstance(i, str):
        if i.startswith('#'):
            return i[1:]
        return i
    return None

def parse_date(d):
    if not d: return None
    try:
        return datetime.strptime(d[:19], "%Y-%m-%dT%H:%M:%S")
    except:
        return None

START_DATE = datetime(2022, 4, 10)
END_DATE = datetime(2023, 4, 10)

# 1. Process Users
valid_users = {} # Id -> Name
excluded_names = [
    "Integration User", "Automated Process", "Platform Integration User", 
    "Chatter Expert", "Data.com Clean", "Security User", "Insights Integration",
    "B2BMA Integration", "SalesforceIQ Integration", "Commerce", "System"
]

for u in users:
    uid = clean_id(u.get('Id'))
    fname = u.get('FirstName') or ""
    lname = u.get('LastName') or ""
    full_name = f"{fname} {lname}".strip()
    
    is_excluded = False
    for ex in excluded_names:
        if ex in full_name:
            is_excluded = True
            break
    
    if not is_excluded and uid:
        valid_users[uid] = full_name

# 2. Calculate Handled Cases & Transfers
handled_cases = {} # Agent -> Set(CaseID)
transfer_counts = {} # Agent -> Int

# From Case (Current Owner)
for c in cases:
    cid = clean_id(c.get('id')) # Note: Case file has lower case 'id' from query? 
    # Query was SELECT Id... Postgres returns what? Usually case sensitive to query?
    # Inspecting previous output: "id": "#500..." (lowercase keys in JSON from tool?)
    # Tool output usually standardizes or keeps DB driver output.
    # Previous preview showed lowercase keys: "id", "ownerid".
    
    oid = clean_id(c.get('ownerid'))
    cd = parse_date(c.get('createddate'))
    cld = parse_date(c.get('closeddate'))
    
    if not oid or oid not in valid_users: continue
    
    # Check window overlap
    # If case created before End AND (not closed OR closed after Start)
    if cd and cd <= END_DATE:
        if not cld or cld >= START_DATE:
            if oid not in handled_cases: handled_cases[oid] = set()
            handled_cases[oid].add(cid)

# From History
for h in history:
    if h.get('field__c') != 'Owner Assignment': continue
    
    cid = clean_id(h.get('caseid__c'))
    old_val = clean_id(h.get('oldvalue__c'))
    new_val = clean_id(h.get('newvalue__c'))
    date = parse_date(h.get('createddate'))
    
    if not date: continue
    
    # Metric: Transfer Count (in window)
    if START_DATE <= date <= END_DATE:
        if old_val in valid_users:
            transfer_counts[old_val] = transfer_counts.get(old_val, 0) + 1
            # Also implies they handled it (gave it up)
            if old_val not in handled_cases: handled_cases[old_val] = set()
            handled_cases[old_val].add(cid)
        
        if new_val in valid_users:
            # They received it -> handled it
            if new_val not in handled_cases: handled_cases[new_val] = set()
            handled_cases[new_val].add(cid)
            
    # If transferred after window, they held it during window (likely)
    if date > END_DATE:
        if old_val in valid_users:
            # They gave it up after window, so they held it.
            # But do we check if they held it *in* window?
            # If date > END, and they gave it up, they must have had it before.
            # Did they have it before END?
            # If they got it after END, then NO.
            # If they got it before END, then YES.
            # This is hard to prove without full chain. 
            # But relying on the 'handled' sets from strictly inside window events + open cases is safer.
            pass

# 3. Candidates
candidates = []
for agent_id, cases_set in handled_cases.items():
    if len(cases_set) > 0:
        t_count = transfer_counts.get(agent_id, 0)
        candidates.append({
            'id': agent_id,
            'name': valid_users[agent_id],
            'transfers': t_count,
            'handled': len(cases_set)
        })

# Sort: Fewest transfers, then Most handled (tie breaker logic)
candidates.sort(key=lambda x: (x['transfers'], -x['handled']))

print("__RESULT__:")
print(json.dumps(candidates[:10]))"""

env_args = {'var_function-call-5260945133747048414': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-4004111035141208110': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-4741343475108631162': 'file_storage/function-call-4741343475108631162.json', 'var_function-call-1467132616485381509': 'file_storage/function-call-1467132616485381509.json', 'var_function-call-11938786780876158215': [{'id': '005Wt000003NIDqIAO', 'count': 0}, {'id': '005Wt000003NJcwIAG', 'count': 0}, {'id': '005Wt000003NJ0DIAW', 'count': 0}, {'id': '005Wt000003NIc2IAG', 'count': 0}, {'id': '005Wt000003NJD9IAO', 'count': 0}, {'id': '005Wt000003NBcAIAW', 'count': 0}, {'id': '005Wt000003NJoDIAW', 'count': 0}, {'id': '005Wt000003NJhlIAG', 'count': 0}, {'id': '005Wt000003NInLIAW', 'count': 0}, {'id': '005Wt000003NIaQIAW', 'count': 0}, {'id': '005Wt000003NHGAIA4', 'count': 0}, {'id': '005Wt000003NIk7IAG', 'count': 0}, {'id': '005Wt000003NFKpIAO', 'count': 0}, {'id': '005Wt000003NHsrIAG', 'count': 0}, {'id': '005Wt000003NHpeIAG', 'count': 0}, {'id': '005Wt000003NIVZIA4', 'count': 0}, {'id': '005Wt000003NIvNIAW', 'count': 0}, {'id': '005Wt000003NFKoIAO', 'count': 0}, {'id': '005Wt000003NJeXIAW', 'count': 0}, {'id': '005Wt000003NJ6gIAG', 'count': 0}, {'id': '005Wt000003NIXBIA4', 'count': 0}, {'id': '005Wt000003NJrRIAW', 'count': 0}, {'id': '005Wt000003NJTFIA4', 'count': 0}, {'id': '005Wt000003NDJ1IAO', 'count': 0}, {'id': '005Wt000003NISLIA4', 'count': 0}, {'id': '005Wt000003NH3GIAW', 'count': 0}, {'id': '005Wt000003NFr4IAG', 'count': 0}, {'id': '005Wt000003NJWTIA4', 'count': 0}, {'id': '005Wt000003NDu7IAG', 'count': 0}, {'id': '005Wt000003NJ9tIAG', 'count': 0}, {'id': '005Wt000003NJQ1IAO', 'count': 0}, {'id': '005Wt000003NJ8HIAW', 'count': 0}, {'id': '005Wt000003NJJaIAO', 'count': 0}, {'id': '005Wt000003NJ3RIAW', 'count': 0}, {'id': '005Wt000003NJEjIAO', 'count': 0}, {'id': '005Wt000003NJcvIAG', 'count': 0}, {'id': '005Wt000003NIwzIAG', 'count': 0}, {'id': '005Wt000003NI2XIAW', 'count': 0}, {'id': '005Wt000003NINVIA4', 'count': 0}, {'id': '005Wt000003NDqFIAW', 'count': 0}, {'id': '005Wt000003NHuUIAW', 'count': 0}, {'id': '005Wt000003NGjuIAG', 'count': 0}, {'id': '005Wt000003NDsUIAW', 'count': 0}, {'id': '005Wt000003NFhOIAW', 'count': 0}, {'id': '005Wt000003NBykIAG', 'count': 0}, {'id': '005Wt000003NEGhIAO', 'count': 0}, {'id': '005Wt000003NEtOIAW', 'count': 0}, {'id': '005Wt000003NJLBIA4', 'count': 0}, {'id': '005Wt000003NIfHIAW', 'count': 0}, {'id': '005Wt000003NEzqIAG', 'count': 0}, {'id': '005Wt000003NHfyIAG', 'count': 0}, {'id': '005Wt000003NEdKIAW', 'count': 0}, {'id': '005Wt000003NIYnIAO', 'count': 0}, {'id': '005Wt000003NFW6IAO', 'count': 0}, {'id': '005Wt000003NJufIAG', 'count': 0}, {'id': '005Wt000003NIliIAG', 'count': 0}, {'id': '005Wt000003NInJIAW', 'count': 0}], 'var_function-call-3312263680111285021': 'file_storage/function-call-3312263680111285021.json', 'var_function-call-12179606321985110018': 'file_storage/function-call-12179606321985110018.json'}

exec(code, env_args)
