code = """import json
import pandas as pd
from datetime import datetime

# Load data
# Case data is in a file
with open(locals()['var_function-call-16144040936612064075'], 'r') as f:
    case_data = json.load(f)

# History data is in a file
with open(locals()['var_function-call-5796599664818877858'], 'r') as f:
    case_history_data = json.load(f)

def clean_id(i):
    if i and isinstance(i, str):
        if i.startswith('#'):
            return i[1:]
        return i
    return i

start_date = pd.Timestamp("2022-04-10", tz='UTC')
end_date = pd.Timestamp("2023-04-10", tz='UTC')

# 1. Check for transfers in period
transfer_events = []
transfer_counts = {}

for row in case_history_data:
    if row.get('field__c') == 'Owner Assignment':
        c_date_str = row.get('createddate')
        try:
            c_date = pd.to_datetime(c_date_str)
            if c_date.tzinfo is None:
                c_date = c_date.tz_localize('UTC')
            
            if start_date <= c_date <= end_date:
                old_val = clean_id(row.get('oldvalue__c'))
                if old_val and old_val != "None":
                    transfer_counts[old_val] = transfer_counts.get(old_val, 0) + 1
                    transfer_events.append(row)
        except:
            pass

# 2. Identify Population (Handled > 0 cases)
handlers_lifetime = set()

# From Case (current owners)
for row in case_data:
    oid = clean_id(row.get('ownerid'))
    if oid: handlers_lifetime.add(oid)

# From History (past owners)
for row in case_history_data:
    old_val = clean_id(row.get('oldvalue__c'))
    new_val = clean_id(row.get('newvalue__c'))
    if old_val and old_val != "None": handlers_lifetime.add(old_val)
    if new_val and new_val != "None": handlers_lifetime.add(new_val)

# 3. Find Min Count
min_count = float('inf')
min_agents = []

# All handlers have 0 count by default
final_counts = {}
for h in handlers_lifetime:
    c = transfer_counts.get(h, 0)
    final_counts[h] = c
    if c < min_count:
        min_count = c
        min_agents = [h]
    elif c == min_count:
        min_agents.append(h)

# 4. Filter ties by Activity in Period
active_handlers = set()

# From Case data (active during period)
for row in case_data:
    oid = clean_id(row.get('ownerid'))
    if not oid: continue
    
    # Check if case active in period
    created = row.get('createddate')
    closed = row.get('closeddate')
    
    is_active = False
    try:
        c_dt = pd.to_datetime(created)
        if c_dt.tzinfo is None: c_dt = c_dt.tz_localize('UTC')
        
        cl_dt = None
        if closed and closed != "None":
            cl_dt = pd.to_datetime(closed)
            if cl_dt.tzinfo is None: cl_dt = cl_dt.tz_localize('UTC')
        
        # Active if created <= end and (closed >= start or closed is None)
        if c_dt <= end_date:
            if cl_dt is None or cl_dt >= start_date:
                is_active = True
    except:
        pass
    
    if is_active:
        active_handlers.add(oid)

# From History (assignment in period)
for row in case_history_data:
    if row.get('field__c') == 'Owner Assignment':
        c_date_str = row.get('createddate')
        try:
            c_date = pd.to_datetime(c_date_str)
            if c_date.tzinfo is None: c_date = c_date.tz_localize('UTC')
            if start_date <= c_date <= end_date:
                old_val = clean_id(row.get('oldvalue__c'))
                new_val = clean_id(row.get('newvalue__c'))
                if old_val and old_val != "None": active_handlers.add(old_val)
                if new_val and new_val != "None": active_handlers.add(new_val)
        except:
            pass

# Filter min_agents by active_handlers
active_min_agents = [a for a in min_agents if a in active_handlers]

result = {
    "transfer_events_count": len(transfer_events),
    "min_count": min_count,
    "num_tied_lifetime": len(min_agents),
    "num_active_tied": len(active_min_agents),
    "active_tied_agents": active_min_agents
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2127136136054705201': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-13141099944045946825': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-4751015758984029337': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-6793032206411110950': [{'id': 'a04Wt00000534p0IAA', 'caseid__c': '500Wt00000DDzRCIA1', 'oldvalue__c': '005Wt000003NFhOIAW', 'newvalue__c': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:38:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000535UwIAI', 'caseid__c': '500Wt00000DDzW3IAL', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NIfHIAW', 'createddate': '2021-11-02T13:31:14.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537riIAA', 'caseid__c': '500Wt00000DDzSnIAL', 'oldvalue__c': '005Wt000003NHuUIAW', 'newvalue__c': '005Wt000003NJ9tIAG', 'createddate': '2021-10-15T13:58:32.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt0000053831IAA', 'caseid__c': '500Wt00000DDnt7IAD', 'oldvalue__c': '005Wt000003NHGAIA4', 'newvalue__c': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T15:47:56.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt000005389SIAQ', 'caseid__c': '500Wt00000DDfvXIAT', 'oldvalue__c': '005Wt000003NHg0IAG', 'newvalue__c': '005Wt000003NFW6IAO', 'createddate': '2021-03-24T20:27:15.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538NzIAI', 'caseid__c': '500Wt00000DDz6FIAT', 'oldvalue__c': '005Wt000003NDqFIAW', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T13:07:23.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538m9IAA', 'caseid__c': '500Wt00000DDYpGIAX', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NJLBIA4', 'createddate': '2021-03-31T13:52:45.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539QTIAY', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:30:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000539blIAA', 'caseid__c': '500Wt00000DDTERIA5', 'oldvalue__c': '005Wt000003NJ6fIAG', 'newvalue__c': '005Wt000003NIk5IAG', 'createddate': '2022-03-10T11:37:09.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-24565791696621762': [{'count': '165'}], 'var_function-call-2227011961242394449': [{'count': '153'}], 'var_function-call-17657878652496307354': [{'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '#005Wt000003NJWTIA4'}, {'ownerid': '005Wt000003NIc3IAG'}, {'ownerid': '#005Wt000003NEzqIAG'}, {'ownerid': '005Wt000003NISLIA4'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NJD9IAO'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '#005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NJcwIAG'}, {'ownerid': '005Wt000003NFhOIAW'}, {'ownerid': '005Wt000003NItlIAG'}, {'ownerid': '005Wt000003NFKpIAO'}, {'ownerid': '005Wt000003NJ9tIAG'}, {'ownerid': '005Wt000003NIk5IAG'}, {'ownerid': '#005Wt000003NJeXIAW'}, {'ownerid': '#005Wt000003NIfFIAW'}, {'ownerid': '#005Wt000003NDqEIAW'}, {'ownerid': '#005Wt000003NJ6gIAG'}, {'ownerid': '#005Wt000003NJbJIAW'}, {'ownerid': '005Wt000003NHuUIAW'}, {'ownerid': '005Wt000003NJLBIA4'}, {'ownerid': '005Wt000003NJLBIA4'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '#005Wt000003NEtOIAW'}, {'ownerid': '005Wt000003NJzVIAW'}, {'ownerid': '005Wt000003NHfyIAG'}, {'ownerid': '#005Wt000003NJoDIAW'}, {'ownerid': '#005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NGjuIAG'}, {'ownerid': '#005Wt000003NIYnIAO'}, {'ownerid': '005Wt000003NJufIAG'}, {'ownerid': '005Wt000003NH3GIAW'}, {'ownerid': '005Wt000003NFKpIAO'}, {'ownerid': '005Wt000003NIXBIA4'}, {'ownerid': '005Wt000003NIk5IAG'}, {'ownerid': '005Wt000003NJcvIAG'}, {'ownerid': '005Wt000003NJppIAG'}, {'ownerid': '005Wt000003NFW6IAO'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NJbJIAW'}, {'ownerid': '005Wt000003NJrRIAW'}, {'ownerid': '005Wt000003NIvNIAW'}, {'ownerid': '#005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NEGhIAO'}, {'ownerid': '#005Wt000003NHuUIAW'}, {'ownerid': '005Wt000003NDqFIAW'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NEdKIAW'}, {'ownerid': '#005Wt000003NI90IAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '#005Wt000003NJQ1IAO'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '#005Wt000003NDu7IAG'}, {'ownerid': '005Wt000003NJufIAG'}, {'ownerid': '005Wt000003NJTFIA4'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NIYnIAO'}, {'ownerid': '005Wt000003NDsUIAW'}, {'ownerid': '005Wt000003NDJ1IAO'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NHsrIAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NISLIA4'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '005Wt000003NIDqIAO'}, {'ownerid': '005Wt000003NJGLIA4'}, {'ownerid': '005Wt000003NHsrIAG'}, {'ownerid': '005Wt000003NBykIAG'}, {'ownerid': '005Wt000003NJGLIA4'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '#005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NInJIAW'}, {'ownerid': '#005Wt000003NInLIAW'}, {'ownerid': '005Wt000003NJzVIAW'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NDqEIAW'}, {'ownerid': '005Wt000003NI2XIAW'}, {'ownerid': '#005Wt000003NBcAIAW'}, {'ownerid': '005Wt000003NIc3IAG'}, {'ownerid': '005Wt000003NJ9tIAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '#005Wt000003NH3GIAW'}, {'ownerid': '005Wt000003NIk7IAG'}, {'ownerid': '#005Wt000003NIfHIAW'}, {'ownerid': '#005Wt000003NJUrIAO'}, {'ownerid': '005Wt000003NJhlIAG'}, {'ownerid': '005Wt000003NI5mIAG'}, {'ownerid': '005Wt000003NJ8HIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '005Wt000003NHGAIA4'}, {'ownerid': '005Wt000003NIwzIAG'}, {'ownerid': '005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NIfFIAW'}, {'ownerid': '005Wt000003NIaQIAW'}, {'ownerid': '005Wt000003NDqDIAW'}, {'ownerid': '#005Wt000003NINVIA4'}, {'ownerid': '005Wt000003NJ3RIAW'}, {'ownerid': '005Wt000003NJbJIAW'}, {'ownerid': '#005Wt000003NIDqIAO'}, {'ownerid': '005Wt000003NIXBIA4'}, {'ownerid': '005Wt000003NIwzIAG'}, {'ownerid': '005Wt000003NINVIA4'}, {'ownerid': '#005Wt000003NFr4IAG'}, {'ownerid': '#005Wt000003NJcvIAG'}, {'ownerid': '#005Wt000003NJEjIAO'}, {'ownerid': '005Wt000003NJD9IAO'}, {'ownerid': '005Wt000003NEtOIAW'}, {'ownerid': '005Wt000003NDu7IAG'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NIc2IAG'}, {'ownerid': '005Wt000003NIVZIA4'}, {'ownerid': '005Wt000003NFW6IAO'}, {'ownerid': '005Wt000003NIAcIAO'}, {'ownerid': '005Wt000003NJWTIA4'}, {'ownerid': '005Wt000003NBcAIAW'}, {'ownerid': '005Wt000003NIddIAG'}, {'ownerid': '005Wt000003NHfzIAG'}, {'ownerid': '005Wt000003NI2XIAW'}, {'ownerid': '#005Wt000003NFr4IAG'}, {'ownerid': '005Wt000003NJTFIA4'}, {'ownerid': '005Wt000003NJoDIAW'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJ6gIAG'}, {'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NJeXIAW'}, {'ownerid': '#005Wt000003NGwpIAG'}, {'ownerid': '005Wt000003NGjuIAG'}, {'ownerid': '#005Wt000003NIvNIAW'}, {'ownerid': '#005Wt000003NFKoIAO'}, {'ownerid': '005Wt000003NFKoIAO'}, {'ownerid': '#005Wt000003NF1SIAW'}, {'ownerid': '005Wt000003NIliIAG'}, {'ownerid': '#005Wt000003NJEjIAO'}, {'ownerid': '005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NDu7IAG'}, {'ownerid': '#005Wt000003NHpeIAG'}, {'ownerid': '005Wt000003NIYnIAO'}, {'ownerid': '#005Wt000003NEGhIAO'}, {'ownerid': '005Wt000003NIVZIA4'}, {'ownerid': '005Wt000003NJ0DIAW'}, {'ownerid': '005Wt000003NJJaIAO'}, {'ownerid': '005Wt000003NDXZIA4'}, {'ownerid': '005Wt000003NJ6fIAG'}, {'ownerid': '005Wt000003NHGAIA4'}], 'var_function-call-5796599664818877858': 'file_storage/function-call-5796599664818877858.json', 'var_function-call-1461980605472959862': {'min_count': 0, 'num_tied': 77, 'tied_agents': ['005Wt000003NFKpIAO', '005Wt000003NEtOIAW', '005Wt000003NIfHIAW', '005Wt000003NJJaIAO', '005Wt000003NIVZIA4', '005Wt000003NI90IAG', '005Wt000003NI5mIAG', '005Wt000003NJbJIAW', '005Wt000003NIaQIAW', '005Wt000003NIc2IAG'], 'all_counts_sample': {'005Wt000003NFKpIAO': 0, '005Wt000003NEtOIAW': 0, '005Wt000003NIfHIAW': 0, '005Wt000003NJJaIAO': 0, '005Wt000003NIVZIA4': 0}}, 'var_function-call-10896370900980317986': {'num_candidates_in_period': 0, 'top_candidates': []}, 'var_function-call-16144040936612064075': 'file_storage/function-call-16144040936612064075.json'}

exec(code, env_args)
