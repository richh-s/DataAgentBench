code = """import pandas as pd
import json
import datetime

# Load data
with open(locals()['var_function-call-8334225719153154105'], 'r') as f:
    cases_data = json.load(f)
with open(locals()['var_function-call-7458872839498508585'], 'r') as f:
    history_data = json.load(f)
users_data = locals()['var_function-call-18179623810098580225']

# Clean User IDs
valid_users = set()
for u in users_data:
    uid = u['Id'].strip()
    if uid.startswith('#'):
        uid = uid[1:]
    valid_users.add(uid)

# Process Cases
cases = []
for c in cases_data:
    cid = c['id'].strip()
    if cid.startswith('#'):
        cid = cid[1:]
    
    oid = c['ownerid'].strip()
    if oid.startswith('#'):
        oid = oid[1:]
        
    created = c['createddate']
    closed = c['closeddate']
    
    if not closed:
        continue
        
    cases.append({
        'id': cid,
        'ownerid': oid,
        'created': created,
        'closed': closed
    })

df_cases = pd.DataFrame(cases)
df_cases['closed_dt'] = pd.to_datetime(df_cases['closed'], utc=True)
df_cases['created_dt'] = pd.to_datetime(df_cases['created'], utc=True)

# Filter by date (Past 4 months from 2023-09-02)
# 2023-05-02 to 2023-09-02
start_date = pd.Timestamp('2023-05-02', tz='UTC')
end_date = pd.Timestamp('2023-09-02', tz='UTC')
# Adjust end_date to end of day? "In the past four months" usually includes the end date.
# Given time components in data, I should compare carefully.
# "Today's date: 2023-09-02".
# Let's assume inclusive.
df_cases = df_cases[(df_cases['closed_dt'] >= start_date) & (df_cases['closed_dt'] <= end_date + pd.Timedelta(days=1))] 
# Adding 1 day to include cases on 2023-09-02 regardless of time, or strictly less than 2023-09-03.

# Process History
history = []
for h in history_data:
    cid = h['caseid__c'].strip()
    if cid.startswith('#'):
        cid = cid[1:]
    
    oldv = h['oldvalue__c']
    newv = h['newvalue__c']
    
    if oldv and oldv.strip().startswith('#'): oldv = oldv.strip()[1:]
    if newv and newv.strip().startswith('#'): newv = newv.strip()[1:]
    
    history.append({
        'caseid': cid,
        'oldvalue': oldv,
        'newvalue': newv
    })

df_history = pd.DataFrame(history)

# Identify Transferred Cases and Processed Counts
processed_map = {} # Agent -> Set(CaseIds)
case_transfer_status = {} # CaseId -> Bool

# Get all relevant case IDs
relevant_case_ids = set(df_cases['id'].unique())

# Filter history for relevant cases
df_hist_rel = df_history[df_history['caseid'].isin(relevant_case_ids)]

# Group history by case
hist_groups = df_hist_rel.groupby('caseid')

for cid in relevant_case_ids:
    is_transferred = False
    owners = set()
    
    # Get current owner from Case table
    current_owner = df_cases[df_cases['id'] == cid]['ownerid'].iloc[0]
    if current_owner in valid_users:
        owners.add(current_owner)
    
    if cid in hist_groups.groups:
        group = hist_groups.get_group(cid)
        # Check transfer status
        # If any entry has oldvalue != None/None string, it's a transfer
        # Or if there are > 1 entries?
        # Let's look at the data pattern. "None" -> "User" is creation/first assignment.
        # "User" -> "User" is transfer.
        # So check if any oldvalue is not None.
        for _, row in group.iterrows():
            ov = row['oldvalue']
            nv = row['newvalue']
            
            # Update owners set
            if ov and ov != 'None' and ov in valid_users:
                owners.add(ov)
            if nv and nv in valid_users:
                owners.add(nv)
            
            if ov and ov != 'None':
                is_transferred = True
                
        # Also, if there are multiple entries where oldvalue is None? Unlikely.
        # If there is only 1 entry and oldvalue is None, is_transferred = False.
    
    case_transfer_status[cid] = is_transferred
    
    # Update processed map
    for agent in owners:
        if agent not in processed_map:
            processed_map[agent] = set()
        processed_map[agent].add(cid)

# Calculate Handle Time
agent_handle_times = {} # Agent -> List[duration_seconds]

for _, row in df_cases.iterrows():
    cid = row['id']
    if case_transfer_status.get(cid, False):
        continue # Skip transferred
    
    # Calculate duration
    duration = (row['closed_dt'] - row['created_dt']).total_seconds()
    
    agent = row['ownerid']
    if agent in valid_users:
        if agent not in agent_handle_times:
            agent_handle_times[agent] = []
        agent_handle_times[agent].append(duration)

# Compute Results
results = []
for agent in processed_map:
    # Filter: processed > 1 case
    if len(processed_map[agent]) > 1:
        # Get handle times
        times = agent_handle_times.get(agent, [])
        if times:
            avg_time = sum(times) / len(times)
            results.append({
                'agent': agent,
                'avg_time': avg_time,
                'processed_count': len(processed_map[agent]),
                'measured_count': len(times)
            })

# Sort by avg_time
results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2500583766527038450': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-8334225719153154105': 'file_storage/function-call-8334225719153154105.json', 'var_function-call-16673072815387886787': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-7458872839498508585': 'file_storage/function-call-7458872839498508585.json', 'var_function-call-18179623810098580225': [{'Id': '#005Wt000003MH26IAG'}, {'Id': '#005Wt000003MH27IAG'}, {'Id': '#005Wt000003MH29IAG'}, {'Id': '#005Wt000003MH2GIAW'}, {'Id': '#005Wt000003MH2JIAW'}, {'Id': '005Wt000003MH2OIAW'}, {'Id': '005Wt000003MH2WIAW'}, {'Id': '005Wt000003MNyjIAG'}, {'Id': '005Wt000003MOgHIAW'}, {'Id': '005Wt000003MOgIIAW'}, {'Id': '#005Wt000003MOgJIAW'}, {'Id': '005Wt000003NBcAIAW'}, {'Id': '005Wt000003NBcBIAW'}, {'Id': '005Wt000003NBp4IAG'}, {'Id': '005Wt000003NBp5IAG'}, {'Id': '005Wt000003NBsIIAW'}, {'Id': '005Wt000003NBykIAG'}, {'Id': '005Wt000003NBylIAG'}, {'Id': '005Wt000003NCRmIAO'}, {'Id': '#005Wt000003NCZqIAO'}, {'Id': '005Wt000003NCd5IAG'}, {'Id': '#005Wt000003NCegIAG'}, {'Id': '005Wt000003ND9KIAW'}, {'Id': '005Wt000003NDEBIA4'}, {'Id': '005Wt000003NDJ0IAO'}, {'Id': '005Wt000003NDJ1IAO'}, {'Id': '005Wt000003NDXZIA4'}, {'Id': '#005Wt000003NDXaIAO'}, {'Id': '005Wt000003NDqDIAW'}, {'Id': '005Wt000003NDqEIAW'}, {'Id': '#005Wt000003NDqFIAW'}, {'Id': '005Wt000003NDsUIAW'}, {'Id': '#005Wt000003NDu7IAG'}, {'Id': '005Wt000003NDu8IAG'}, {'Id': '#005Wt000003NEGhIAO'}, {'Id': '005Wt000003NEGiIAO'}, {'Id': '005Wt000003NEGjIAO'}, {'Id': '005Wt000003NETaIAO'}, {'Id': '#005Wt000003NETbIAO'}, {'Id': '#005Wt000003NEa3IAG'}, {'Id': '005Wt000003NEdJIAW'}, {'Id': '005Wt000003NEdKIAW'}, {'Id': '#005Wt000003NEoYIAW'}, {'Id': '#005Wt000003NErnIAG'}, {'Id': '005Wt000003NEtOIAW'}, {'Id': '005Wt000003NEtPIAW'}, {'Id': '005Wt000003NEzqIAG'}, {'Id': '005Wt000003NEzrIAG'}, {'Id': '#005Wt000003NF1SIAW'}, {'Id': '005Wt000003NF9WIAW'}, {'Id': '005Wt000003NF9XIAW'}, {'Id': '005Wt000003NF9YIAW'}, {'Id': '#005Wt000003NFB8IAO'}, {'Id': '005Wt000003NFKoIAO'}, {'Id': '#005Wt000003NFKpIAO'}, {'Id': '005Wt000003NFRKIA4'}, {'Id': '005Wt000003NFW6IAO'}, {'Id': '005Wt000003NFhOIAW'}, {'Id': '005Wt000003NFhPIAW'}, {'Id': '005Wt000003NFr4IAG'}, {'Id': '#005Wt000003NG2MIAW'}, {'Id': '005Wt000003NG2NIAW'}, {'Id': '#005Wt000003NGFGIA4'}, {'Id': '#005Wt000003NGFHIA4'}, {'Id': '#005Wt000003NGOxIAO'}, {'Id': '005Wt000003NGdSIAW'}, {'Id': '005Wt000003NGjuIAG'}, {'Id': '005Wt000003NGjvIAG'}, {'Id': '005Wt000003NGjwIAG'}, {'Id': '005Wt000003NGtbIAG'}, {'Id': '#005Wt000003NGtcIAG'}, {'Id': '005Wt000003NGwoIAG'}, {'Id': '005Wt000003NGwpIAG'}, {'Id': '005Wt000003NH3GIAW'}, {'Id': '005Wt000003NH86IAG'}, {'Id': '#005Wt000003NHGAIA4'}, {'Id': '#005Wt000003NHfFIAW'}, {'Id': '#005Wt000003NHfyIAG'}, {'Id': '005Wt000003NHfzIAG'}, {'Id': '#005Wt000003NHg0IAG'}, {'Id': '#005Wt000003NHpdIAG'}, {'Id': '#005Wt000003NHpeIAG'}, {'Id': '005Wt000003NHrFIAW'}, {'Id': '005Wt000003NHsrIAG'}, {'Id': '005Wt000003NHuTIAW'}, {'Id': '005Wt000003NHuUIAW'}, {'Id': '#005Wt000003NHw5IAG'}, {'Id': '#005Wt000003NHxhIAG'}, {'Id': '005Wt000003NHzJIAW'}, {'Id': '005Wt000003NI2XIAW'}, {'Id': '005Wt000003NI49IAG'}, {'Id': '005Wt000003NI4AIAW'}, {'Id': '#005Wt000003NI5lIAG'}, {'Id': '005Wt000003NI5mIAG'}, {'Id': '005Wt000003NI7NIAW'}, {'Id': '005Wt000003NI7OIAW'}, {'Id': '005Wt000003NI7PIAW'}, {'Id': '005Wt000003NI7QIAW'}, {'Id': '005Wt000003NI90IAG'}, {'Id': '005Wt000003NIAbIAO'}, {'Id': '005Wt000003NIAcIAO'}, {'Id': '005Wt000003NIAdIAO'}, {'Id': '#005Wt000003NICDIA4'}, {'Id': '#005Wt000003NIDpIAO'}, {'Id': '005Wt000003NIDqIAO'}, {'Id': '005Wt000003NIH3IAO'}, {'Id': '005Wt000003NIIfIAO'}, {'Id': '#005Wt000003NIKHIA4'}, {'Id': '005Wt000003NILtIAO'}, {'Id': '005Wt000003NINVIA4'}, {'Id': '005Wt000003NINWIA4'}, {'Id': '005Wt000003NIP7IAO'}, {'Id': '005Wt000003NIQjIAO'}, {'Id': '#005Wt000003NISLIA4'}, {'Id': '005Wt000003NISMIA4'}, {'Id': '005Wt000003NISNIA4'}, {'Id': '005Wt000003NITxIAO'}, {'Id': '005Wt000003NIVZIA4'}, {'Id': '005Wt000003NIXBIA4'}, {'Id': '005Wt000003NIXCIA4'}, {'Id': '005Wt000003NIXDIA4'}, {'Id': '005Wt000003NIYnIAO'}, {'Id': '005Wt000003NIYoIAO'}, {'Id': '005Wt000003NIaPIAW'}, {'Id': '005Wt000003NIaQIAW'}, {'Id': '005Wt000003NIaRIAW'}, {'Id': '005Wt000003NIc1IAG'}, {'Id': '005Wt000003NIc2IAG'}, {'Id': '#005Wt000003NIc3IAG'}, {'Id': '#005Wt000003NIddIAG'}, {'Id': '005Wt000003NIdeIAG'}, {'Id': '005Wt000003NIfFIAW'}, {'Id': '005Wt000003NIfGIAW'}, {'Id': '005Wt000003NIfHIAW'}, {'Id': '005Wt000003NIgrIAG'}, {'Id': '#005Wt000003NIiTIAW'}, {'Id': '005Wt000003NIiUIAW'}, {'Id': '005Wt000003NIiVIAW'}, {'Id': '005Wt000003NIk5IAG'}, {'Id': '005Wt000003NIk6IAG'}, {'Id': '005Wt000003NIk7IAG'}, {'Id': '005Wt000003NIlhIAG'}, {'Id': '005Wt000003NIliIAG'}, {'Id': '005Wt000003NIljIAG'}, {'Id': '005Wt000003NInJIAW'}, {'Id': '005Wt000003NInKIAW'}, {'Id': '#005Wt000003NInLIAW'}, {'Id': '#005Wt000003NIovIAG'}, {'Id': '005Wt000003NIowIAG'}, {'Id': '005Wt000003NIqXIAW'}, {'Id': '005Wt000003NIs9IAG'}, {'Id': '005Wt000003NItlIAG'}, {'Id': '005Wt000003NItmIAG'}, {'Id': '005Wt000003NIvNIAW'}, {'Id': '005Wt000003NIwzIAG'}, {'Id': '005Wt000003NIx0IAG'}, {'Id': '005Wt000003NIx1IAG'}, {'Id': '005Wt000003NIybIAG'}, {'Id': '005Wt000003NJ0DIAW'}, {'Id': '005Wt000003NJ0EIAW'}, {'Id': '005Wt000003NJ1pIAG'}, {'Id': '005Wt000003NJ3RIAW'}, {'Id': '#005Wt000003NJ53IAG'}, {'Id': '#005Wt000003NJ6fIAG'}, {'Id': '005Wt000003NJ6gIAG'}, {'Id': '005Wt000003NJ8HIAW'}, {'Id': '#005Wt000003NJ9tIAG'}, {'Id': '005Wt000003NJ9uIAG'}, {'Id': '005Wt000003NJBVIA4'}, {'Id': '005Wt000003NJD7IAO'}, {'Id': '#005Wt000003NJD8IAO'}, {'Id': '005Wt000003NJD9IAO'}, {'Id': '005Wt000003NJEjIAO'}, {'Id': '#005Wt000003NJEkIAO'}, {'Id': '#005Wt000003NJGLIA4'}, {'Id': '#005Wt000003NJHxIAO'}, {'Id': '005Wt000003NJJZIA4'}, {'Id': '005Wt000003NJJaIAO'}, {'Id': '#005Wt000003NJLBIA4'}, {'Id': '#005Wt000003NJMnIAO'}, {'Id': '005Wt000003NJOPIA4'}, {'Id': '005Wt000003NJQ1IAO'}, {'Id': '#005Wt000003NJRdIAO'}, {'Id': '005Wt000003NJReIAO'}, {'Id': '005Wt000003NJTFIA4'}, {'Id': '005Wt000003NJTGIA4'}, {'Id': '005Wt000003NJUrIAO'}, {'Id': '#005Wt000003NJWTIA4'}, {'Id': '005Wt000003NJY5IAO'}, {'Id': '#005Wt000003NJZhIAO'}, {'Id': '#005Wt000003NJbJIAW'}, {'Id': '005Wt000003NJcvIAG'}, {'Id': '#005Wt000003NJcwIAG'}, {'Id': '005Wt000003NJeXIAW'}, {'Id': '005Wt000003NJg9IAG'}, {'Id': '005Wt000003NJgAIAW'}, {'Id': '005Wt000003NJhlIAG'}, {'Id': '005Wt000003NJjNIAW'}, {'Id': '005Wt000003NJkzIAG'}, {'Id': '#005Wt000003NJmbIAG'}, {'Id': '005Wt000003NJmcIAG'}, {'Id': '005Wt000003NJmdIAG'}, {'Id': '#005Wt000003NJoDIAW'}, {'Id': '005Wt000003NJppIAG'}, {'Id': '#005Wt000003NJrRIAW'}, {'Id': '#005Wt000003NJt3IAG'}, {'Id': '#005Wt000003NJufIAG'}, {'Id': '005Wt000003NJwHIAW'}, {'Id': '#005Wt000003NJxtIAG'}, {'Id': '005Wt000003NJzVIAW'}, {'Id': '005Wt000003NK17IAG'}, {'Id': '005Wt000003PUpBIAW'}]}

exec(code, env_args)
