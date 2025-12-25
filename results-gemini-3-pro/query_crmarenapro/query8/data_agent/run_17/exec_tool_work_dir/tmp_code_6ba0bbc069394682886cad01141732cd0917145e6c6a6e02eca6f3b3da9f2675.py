code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-4761739676269309166'], 'r') as f:
    cases = json.load(f)
with open(locals()['var_function-call-4045250952106322466'], 'r') as f:
    history = json.load(f)

start_date = pd.Timestamp("2022-04-01", tz="UTC")
end_date = pd.Timestamp("2023-03-31", tz="UTC")

def normalize_id(i):
    if i is None or i == "None":
        return None
    s = str(i).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

agent_cases = {} # agent -> set of case IDs
transfer_counts = {} # agent -> count

# Helper to add case to agent
def add_case(agent, cid):
    if not agent: return
    if agent not in agent_cases:
        agent_cases[agent] = set()
    agent_cases[agent].add(cid)

# 1. From Case (Active cases)
for c in cases:
    try:
        c_create = pd.Timestamp(c['createddate'])
    except:
        continue
    c_close = None
    if c['closeddate'] and c['closeddate'] != "None":
        try:
            c_close = pd.Timestamp(c['closeddate'])
        except:
            pass
            
    if c_close is not None and c_close < start_date:
        continue
    if c_create > end_date:
        continue
        
    oid = normalize_id(c['ownerid'])
    cid = c['id']
    add_case(oid, cid)

# 2. From History
for h in history:
    try:
        h_date = pd.Timestamp(h['createddate'])
    except:
        continue
        
    if start_date <= h_date <= end_date:
        if h['field__c'] in ["Owner Assignment", "Owner"]:
            old_v = normalize_id(h['oldvalue__c'])
            new_v = normalize_id(h['newvalue__c'])
            cid = h['caseid__c']
            
            if old_v:
                add_case(old_v, cid)
                transfer_counts[old_v] = transfer_counts.get(old_v, 0) + 1
            if new_v:
                add_case(new_v, cid)

# Prepare list
results = []
for agent, cases_set in agent_cases.items():
    h_count = len(cases_set)
    if h_count > 0:
        t_count = transfer_counts.get(agent, 0)
        results.append({
            "id": agent,
            "handled": h_count,
            "transfers": t_count
        })

# Sort: Primary = transfers (asc), Secondary = handled (desc)
results.sort(key=lambda x: (x['transfers'], -x['handled']))

print("__RESULT__:")
print(json.dumps(results[:10])) # Top 10"""

env_args = {'var_function-call-6749587193675572085': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-181915633783256925': 'file_storage/function-call-181915633783256925.json', 'var_function-call-4045250952106322466': 'file_storage/function-call-4045250952106322466.json', 'var_function-call-4761739676269309166': 'file_storage/function-call-4761739676269309166.json', 'var_function-call-13565731729749787714': ['#005Wt000003NBcAIAW', '#005Wt000003NDu7IAG', '#005Wt000003NEtOIAW', '#005Wt000003NEzqIAG', '#005Wt000003NFKoIAO', '#005Wt000003NFr4IAG', '#005Wt000003NGjuIAG', '#005Wt000003NH3GIAW', '#005Wt000003NIDqIAO', '#005Wt000003NIYnIAO', '#005Wt000003NIfHIAW', '#005Wt000003NInLIAW', '#005Wt000003NJEjIAO', '#005Wt000003NJQ1IAO', '#005Wt000003NJWTIA4', '#005Wt000003NJeXIAW', '#005Wt000003NJoDIAW', '005Wt000003NBcAIAW', '005Wt000003NBykIAG', '005Wt000003NDJ1IAO', '005Wt000003NDqFIAW', '005Wt000003NDsUIAW', '005Wt000003NEGhIAO', '005Wt000003NEdKIAW', '005Wt000003NEzqIAG', '005Wt000003NFKoIAO', '005Wt000003NFKpIAO', '005Wt000003NFW6IAO', '005Wt000003NFhOIAW', '005Wt000003NFr4IAG', '005Wt000003NGjuIAG', '005Wt000003NHGAIA4', '005Wt000003NHfyIAG', '005Wt000003NHpeIAG', '005Wt000003NHsrIAG', '005Wt000003NHuUIAW', '005Wt000003NI2XIAW', '005Wt000003NINVIA4', '005Wt000003NISLIA4', '005Wt000003NIVZIA4', '005Wt000003NIXBIA4', '005Wt000003NIaQIAW', '005Wt000003NIc2IAG', '005Wt000003NIk7IAG', '005Wt000003NInJIAW', '005Wt000003NInLIAW', '005Wt000003NIvNIAW', '005Wt000003NIwzIAG', '005Wt000003NJ0DIAW', '005Wt000003NJ3RIAW', '005Wt000003NJ6gIAG', '005Wt000003NJ8HIAW', '005Wt000003NJ9tIAG', '005Wt000003NJD9IAO', '005Wt000003NJEjIAO', '005Wt000003NJJaIAO', '005Wt000003NJLBIA4', '005Wt000003NJTFIA4', '005Wt000003NJWTIA4', '005Wt000003NJcvIAG', '005Wt000003NJcwIAG', '005Wt000003NJhlIAG', '005Wt000003NJoDIAW', '005Wt000003NJrRIAW', '005Wt000003NJufIAG'], 'var_function-call-6802526502515180070': ['005Wt000003NBcAIAW', '005Wt000003NBykIAG', '005Wt000003NDJ1IAO', '005Wt000003NDqFIAW', '005Wt000003NDsUIAW', '005Wt000003NDu7IAG', '005Wt000003NEGhIAO', '005Wt000003NEdKIAW', '005Wt000003NEtOIAW', '005Wt000003NEzqIAG', '005Wt000003NFKoIAO', '005Wt000003NFKpIAO', '005Wt000003NFW6IAO', '005Wt000003NFhOIAW', '005Wt000003NFr4IAG', '005Wt000003NGjuIAG', '005Wt000003NH3GIAW', '005Wt000003NHGAIA4', '005Wt000003NHfyIAG', '005Wt000003NHpeIAG', '005Wt000003NHsrIAG', '005Wt000003NHuUIAW', '005Wt000003NI2XIAW', '005Wt000003NIDqIAO', '005Wt000003NINVIA4', '005Wt000003NISLIA4', '005Wt000003NIVZIA4', '005Wt000003NIXBIA4', '005Wt000003NIYnIAO', '005Wt000003NIaQIAW', '005Wt000003NIc2IAG', '005Wt000003NIfHIAW', '005Wt000003NIk7IAG', '005Wt000003NInJIAW', '005Wt000003NInLIAW', '005Wt000003NIvNIAW', '005Wt000003NIwzIAG', '005Wt000003NJ0DIAW', '005Wt000003NJ3RIAW', '005Wt000003NJ6gIAG', '005Wt000003NJ8HIAW', '005Wt000003NJ9tIAG', '005Wt000003NJD9IAO', '005Wt000003NJEjIAO', '005Wt000003NJJaIAO', '005Wt000003NJLBIA4', '005Wt000003NJQ1IAO', '005Wt000003NJTFIA4', '005Wt000003NJWTIA4', '005Wt000003NJcvIAG', '005Wt000003NJcwIAG', '005Wt000003NJeXIAW', '005Wt000003NJhlIAG', '005Wt000003NJoDIAW', '005Wt000003NJrRIAW', '005Wt000003NJufIAG']}

exec(code, env_args)
