code = """import pandas as pd
import json

with open(locals()['var_function-call-8334225719153154105'], 'r') as f:
    cases_data = json.load(f)
with open(locals()['var_function-call-7458872839498508585'], 'r') as f:
    history_data = json.load(f)
users_data = locals()['var_function-call-18179623810098580225']

valid_users = set()
for u in users_data:
    valid_users.add(u['Id'].strip().replace('#',''))

# Global Processed Count
global_processed = {} # Agent -> Set(CaseId)

# From Current Owners
for c in cases_data:
    cid = c['id'].strip().replace('#','')
    oid = c['ownerid'].strip().replace('#','')
    if oid in valid_users:
        if oid not in global_processed: global_processed[oid] = set()
        global_processed[oid].add(cid)

# From History
for h in history_data:
    cid = h['caseid__c'].strip().replace('#','')
    ov = h['oldvalue__c']
    nv = h['newvalue__c']
    
    if ov:
        ov = ov.strip().replace('#','')
        if ov in valid_users:
            if ov not in global_processed: global_processed[ov] = set()
            global_processed[ov].add(cid)
            
    if nv:
        nv = nv.strip().replace('#','')
        if nv in valid_users:
            if nv not in global_processed: global_processed[nv] = set()
            global_processed[nv].add(cid)

agents_gt_1 = [a for a, cases in global_processed.items() if len(cases) > 1]

# Handle Time in Window
# Window: 2023-05-02 to 2023-09-02
start_date = pd.Timestamp('2023-05-02', tz='UTC')
end_date = pd.Timestamp('2023-09-02', tz='UTC')

# Identify Transferred Cases (Global)
# A case is transferred if it appears in history with Owner Assignment (implying > 1 owner or change)
# Wait, strict definition: "For cases that have NOT been transferred ..., there will be only ONE 'Owner Assignment'".
# I'll count Owner Assignment records per case.
case_assignment_counts = {}
for h in history_data:
    # Filter for Owner Assignment if needed?
    # Assuming the loaded history_data is already filtered for 'Owner Assignment' (it was).
    cid = h['caseid__c'].strip().replace('#','')
    case_assignment_counts[cid] = case_assignment_counts.get(cid, 0) + 1

handle_times = {} # Agent -> List[seconds]

for c in cases_data:
    if not c['closeddate']: continue
    
    closed_dt = pd.to_datetime(c['closeddate'], utc=True)
    if not (start_date <= closed_dt <= end_date + pd.Timedelta(days=1)):
        continue
        
    cid = c['id'].strip().replace('#','')
    
    # Check Transferred
    if case_assignment_counts.get(cid, 0) > 1:
        continue # Transferred
        
    # Check if history exists but count is 1 (Single owner).
    # If count is 0, also Single owner (Current only, no history logged).
    # So strictly > 1 is transferred.
    
    # Calculate Duration
    created_dt = pd.to_datetime(c['createddate'], utc=True)
    duration = (closed_dt - created_dt).total_seconds()
    
    oid = c['ownerid'].strip().replace('#','')
    if oid in valid_users:
        if oid not in handle_times: handle_times[oid] = []
        handle_times[oid].append(duration)

results = []
for agent in agents_gt_1:
    if agent in handle_times:
        times = handle_times[agent]
        if times:
            avg = sum(times)/len(times)
            results.append({'agent': agent, 'avg': avg})

results.sort(key=lambda x: x['avg'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2500583766527038450': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-8334225719153154105': 'file_storage/function-call-8334225719153154105.json', 'var_function-call-16673072815387886787': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-7458872839498508585': 'file_storage/function-call-7458872839498508585.json', 'var_function-call-18179623810098580225': [{'Id': '#005Wt000003MH26IAG'}, {'Id': '#005Wt000003MH27IAG'}, {'Id': '#005Wt000003MH29IAG'}, {'Id': '#005Wt000003MH2GIAW'}, {'Id': '#005Wt000003MH2JIAW'}, {'Id': '005Wt000003MH2OIAW'}, {'Id': '005Wt000003MH2WIAW'}, {'Id': '005Wt000003MNyjIAG'}, {'Id': '005Wt000003MOgHIAW'}, {'Id': '005Wt000003MOgIIAW'}, {'Id': '#005Wt000003MOgJIAW'}, {'Id': '005Wt000003NBcAIAW'}, {'Id': '005Wt000003NBcBIAW'}, {'Id': '005Wt000003NBp4IAG'}, {'Id': '005Wt000003NBp5IAG'}, {'Id': '005Wt000003NBsIIAW'}, {'Id': '005Wt000003NBykIAG'}, {'Id': '005Wt000003NBylIAG'}, {'Id': '005Wt000003NCRmIAO'}, {'Id': '#005Wt000003NCZqIAO'}, {'Id': '005Wt000003NCd5IAG'}, {'Id': '#005Wt000003NCegIAG'}, {'Id': '005Wt000003ND9KIAW'}, {'Id': '005Wt000003NDEBIA4'}, {'Id': '005Wt000003NDJ0IAO'}, {'Id': '005Wt000003NDJ1IAO'}, {'Id': '005Wt000003NDXZIA4'}, {'Id': '#005Wt000003NDXaIAO'}, {'Id': '005Wt000003NDqDIAW'}, {'Id': '005Wt000003NDqEIAW'}, {'Id': '#005Wt000003NDqFIAW'}, {'Id': '005Wt000003NDsUIAW'}, {'Id': '#005Wt000003NDu7IAG'}, {'Id': '005Wt000003NDu8IAG'}, {'Id': '#005Wt000003NEGhIAO'}, {'Id': '005Wt000003NEGiIAO'}, {'Id': '005Wt000003NEGjIAO'}, {'Id': '005Wt000003NETaIAO'}, {'Id': '#005Wt000003NETbIAO'}, {'Id': '#005Wt000003NEa3IAG'}, {'Id': '005Wt000003NEdJIAW'}, {'Id': '005Wt000003NEdKIAW'}, {'Id': '#005Wt000003NEoYIAW'}, {'Id': '#005Wt000003NErnIAG'}, {'Id': '005Wt000003NEtOIAW'}, {'Id': '005Wt000003NEtPIAW'}, {'Id': '005Wt000003NEzqIAG'}, {'Id': '005Wt000003NEzrIAG'}, {'Id': '#005Wt000003NF1SIAW'}, {'Id': '005Wt000003NF9WIAW'}, {'Id': '005Wt000003NF9XIAW'}, {'Id': '005Wt000003NF9YIAW'}, {'Id': '#005Wt000003NFB8IAO'}, {'Id': '005Wt000003NFKoIAO'}, {'Id': '#005Wt000003NFKpIAO'}, {'Id': '005Wt000003NFRKIA4'}, {'Id': '005Wt000003NFW6IAO'}, {'Id': '005Wt000003NFhOIAW'}, {'Id': '005Wt000003NFhPIAW'}, {'Id': '005Wt000003NFr4IAG'}, {'Id': '#005Wt000003NG2MIAW'}, {'Id': '005Wt000003NG2NIAW'}, {'Id': '#005Wt000003NGFGIA4'}, {'Id': '#005Wt000003NGFHIA4'}, {'Id': '#005Wt000003NGOxIAO'}, {'Id': '005Wt000003NGdSIAW'}, {'Id': '005Wt000003NGjuIAG'}, {'Id': '005Wt000003NGjvIAG'}, {'Id': '005Wt000003NGjwIAG'}, {'Id': '005Wt000003NGtbIAG'}, {'Id': '#005Wt000003NGtcIAG'}, {'Id': '005Wt000003NGwoIAG'}, {'Id': '005Wt000003NGwpIAG'}, {'Id': '005Wt000003NH3GIAW'}, {'Id': '005Wt000003NH86IAG'}, {'Id': '#005Wt000003NHGAIA4'}, {'Id': '#005Wt000003NHfFIAW'}, {'Id': '#005Wt000003NHfyIAG'}, {'Id': '005Wt000003NHfzIAG'}, {'Id': '#005Wt000003NHg0IAG'}, {'Id': '#005Wt000003NHpdIAG'}, {'Id': '#005Wt000003NHpeIAG'}, {'Id': '005Wt000003NHrFIAW'}, {'Id': '005Wt000003NHsrIAG'}, {'Id': '005Wt000003NHuTIAW'}, {'Id': '005Wt000003NHuUIAW'}, {'Id': '#005Wt000003NHw5IAG'}, {'Id': '#005Wt000003NHxhIAG'}, {'Id': '005Wt000003NHzJIAW'}, {'Id': '005Wt000003NI2XIAW'}, {'Id': '005Wt000003NI49IAG'}, {'Id': '005Wt000003NI4AIAW'}, {'Id': '#005Wt000003NI5lIAG'}, {'Id': '005Wt000003NI5mIAG'}, {'Id': '005Wt000003NI7NIAW'}, {'Id': '005Wt000003NI7OIAW'}, {'Id': '005Wt000003NI7PIAW'}, {'Id': '005Wt000003NI7QIAW'}, {'Id': '005Wt000003NI90IAG'}, {'Id': '005Wt000003NIAbIAO'}, {'Id': '005Wt000003NIAcIAO'}, {'Id': '005Wt000003NIAdIAO'}, {'Id': '#005Wt000003NICDIA4'}, {'Id': '#005Wt000003NIDpIAO'}, {'Id': '005Wt000003NIDqIAO'}, {'Id': '005Wt000003NIH3IAO'}, {'Id': '005Wt000003NIIfIAO'}, {'Id': '#005Wt000003NIKHIA4'}, {'Id': '005Wt000003NILtIAO'}, {'Id': '005Wt000003NINVIA4'}, {'Id': '005Wt000003NINWIA4'}, {'Id': '005Wt000003NIP7IAO'}, {'Id': '005Wt000003NIQjIAO'}, {'Id': '#005Wt000003NISLIA4'}, {'Id': '005Wt000003NISMIA4'}, {'Id': '005Wt000003NISNIA4'}, {'Id': '005Wt000003NITxIAO'}, {'Id': '005Wt000003NIVZIA4'}, {'Id': '005Wt000003NIXBIA4'}, {'Id': '005Wt000003NIXCIA4'}, {'Id': '005Wt000003NIXDIA4'}, {'Id': '005Wt000003NIYnIAO'}, {'Id': '005Wt000003NIYoIAO'}, {'Id': '005Wt000003NIaPIAW'}, {'Id': '005Wt000003NIaQIAW'}, {'Id': '005Wt000003NIaRIAW'}, {'Id': '005Wt000003NIc1IAG'}, {'Id': '005Wt000003NIc2IAG'}, {'Id': '#005Wt000003NIc3IAG'}, {'Id': '#005Wt000003NIddIAG'}, {'Id': '005Wt000003NIdeIAG'}, {'Id': '005Wt000003NIfFIAW'}, {'Id': '005Wt000003NIfGIAW'}, {'Id': '005Wt000003NIfHIAW'}, {'Id': '005Wt000003NIgrIAG'}, {'Id': '#005Wt000003NIiTIAW'}, {'Id': '005Wt000003NIiUIAW'}, {'Id': '005Wt000003NIiVIAW'}, {'Id': '005Wt000003NIk5IAG'}, {'Id': '005Wt000003NIk6IAG'}, {'Id': '005Wt000003NIk7IAG'}, {'Id': '005Wt000003NIlhIAG'}, {'Id': '005Wt000003NIliIAG'}, {'Id': '005Wt000003NIljIAG'}, {'Id': '005Wt000003NInJIAW'}, {'Id': '005Wt000003NInKIAW'}, {'Id': '#005Wt000003NInLIAW'}, {'Id': '#005Wt000003NIovIAG'}, {'Id': '005Wt000003NIowIAG'}, {'Id': '005Wt000003NIqXIAW'}, {'Id': '005Wt000003NIs9IAG'}, {'Id': '005Wt000003NItlIAG'}, {'Id': '005Wt000003NItmIAG'}, {'Id': '005Wt000003NIvNIAW'}, {'Id': '005Wt000003NIwzIAG'}, {'Id': '005Wt000003NIx0IAG'}, {'Id': '005Wt000003NIx1IAG'}, {'Id': '005Wt000003NIybIAG'}, {'Id': '005Wt000003NJ0DIAW'}, {'Id': '005Wt000003NJ0EIAW'}, {'Id': '005Wt000003NJ1pIAG'}, {'Id': '005Wt000003NJ3RIAW'}, {'Id': '#005Wt000003NJ53IAG'}, {'Id': '#005Wt000003NJ6fIAG'}, {'Id': '005Wt000003NJ6gIAG'}, {'Id': '005Wt000003NJ8HIAW'}, {'Id': '#005Wt000003NJ9tIAG'}, {'Id': '005Wt000003NJ9uIAG'}, {'Id': '005Wt000003NJBVIA4'}, {'Id': '005Wt000003NJD7IAO'}, {'Id': '#005Wt000003NJD8IAO'}, {'Id': '005Wt000003NJD9IAO'}, {'Id': '005Wt000003NJEjIAO'}, {'Id': '#005Wt000003NJEkIAO'}, {'Id': '#005Wt000003NJGLIA4'}, {'Id': '#005Wt000003NJHxIAO'}, {'Id': '005Wt000003NJJZIA4'}, {'Id': '005Wt000003NJJaIAO'}, {'Id': '#005Wt000003NJLBIA4'}, {'Id': '#005Wt000003NJMnIAO'}, {'Id': '005Wt000003NJOPIA4'}, {'Id': '005Wt000003NJQ1IAO'}, {'Id': '#005Wt000003NJRdIAO'}, {'Id': '005Wt000003NJReIAO'}, {'Id': '005Wt000003NJTFIA4'}, {'Id': '005Wt000003NJTGIA4'}, {'Id': '005Wt000003NJUrIAO'}, {'Id': '#005Wt000003NJWTIA4'}, {'Id': '005Wt000003NJY5IAO'}, {'Id': '#005Wt000003NJZhIAO'}, {'Id': '#005Wt000003NJbJIAW'}, {'Id': '005Wt000003NJcvIAG'}, {'Id': '#005Wt000003NJcwIAG'}, {'Id': '005Wt000003NJeXIAW'}, {'Id': '005Wt000003NJg9IAG'}, {'Id': '005Wt000003NJgAIAW'}, {'Id': '005Wt000003NJhlIAG'}, {'Id': '005Wt000003NJjNIAW'}, {'Id': '005Wt000003NJkzIAG'}, {'Id': '#005Wt000003NJmbIAG'}, {'Id': '005Wt000003NJmcIAG'}, {'Id': '005Wt000003NJmdIAG'}, {'Id': '#005Wt000003NJoDIAW'}, {'Id': '005Wt000003NJppIAG'}, {'Id': '#005Wt000003NJrRIAW'}, {'Id': '#005Wt000003NJt3IAG'}, {'Id': '#005Wt000003NJufIAG'}, {'Id': '005Wt000003NJwHIAW'}, {'Id': '#005Wt000003NJxtIAG'}, {'Id': '005Wt000003NJzVIAW'}, {'Id': '005Wt000003NK17IAG'}, {'Id': '005Wt000003PUpBIAW'}], 'var_function-call-5602833549364379378': [], 'var_function-call-12187547159997547975': {'cases_count': 7}, 'var_function-call-18046995617480584225': [{'id': '500Wt00000DDepmIAD', 'current_owner': '005Wt000003NJufIAG', 'history_count': 1, 'is_transferred': False, 'hist_owners': ['005Wt000003NJufIAG']}, {'id': '500Wt00000DDyzpIAD', 'current_owner': '005Wt000003NJGLIA4', 'history_count': 1, 'is_transferred': False, 'hist_owners': ['005Wt000003NJGLIA4']}, {'id': '500Wt00000DDzUPIA1', 'current_owner': '005Wt000003NDqDIAW', 'history_count': 1, 'is_transferred': False, 'hist_owners': ['005Wt000003NDqDIAW']}, {'id': '500Wt00000DDzsbIAD', 'current_owner': '005Wt000003NJD9IAO', 'history_count': 1, 'is_transferred': False, 'hist_owners': ['005Wt000003NJD9IAO']}, {'id': '500Wt00000DDzscIAD', 'current_owner': '005Wt000003NEtOIAW', 'history_count': 1, 'is_transferred': False, 'hist_owners': ['005Wt000003NEtOIAW']}, {'id': '500Wt00000DDzuEIAT', 'current_owner': '005Wt000003NJJaIAO', 'history_count': 1, 'is_transferred': False, 'hist_owners': ['005Wt000003NJJaIAO']}, {'id': '500Wt00000DE02HIAT', 'current_owner': '005Wt000003NIddIAG', 'history_count': 1, 'is_transferred': False, 'hist_owners': ['005Wt000003NIddIAG']}], 'var_function-call-759121239418434150': [], 'var_function-call-4435325883446164405': {'overlap_count': 2}}

exec(code, env_args)
