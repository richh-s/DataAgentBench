code = """import pandas as pd
import json

# Load data from previous tool results
cases = pd.DataFrame(var_call_ZBTu4WlbexoaLnX13lyjWjOq)
casehist = pd.DataFrame(var_call_UhJssDByIAEJ8mjAMaqcYEkG)

# normalize id-like fields by stripping leading # and whitespace
def norm_id(x):
    if pd.isna(x):
        return x
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

cases['id_norm'] = cases['id'].apply(norm_id)
cases['ownerid_norm'] = cases['ownerid'].apply(norm_id)

casehist['caseid__c_norm'] = casehist['caseid__c'].apply(norm_id)
casehist['newvalue__c_norm'] = casehist['newvalue__c'].apply(norm_id)
casehist['field__c'] = casehist['field__c'].astype(str)

# Consider only cases in our cases DataFrame
case_ids = set(cases['id_norm'].tolist())

# Build mapping of case -> list of owner assignments (normalized)
owner_assignments = {}
for cid in case_ids:
    rows = casehist[(casehist['caseid__c_norm'] == cid) & (casehist['field__c'] == 'Owner Assignment')]
    vals = rows['newvalue__c_norm'].dropna().tolist()
    # filter out 'None' strings
    vals = [v for v in vals if str(v).lower() != 'none']
    owner_assignments[cid] = vals

# Determine transferred status (more than one owner assignment)
transferred = {cid: (len(owner_assignments.get(cid, [])) > 1) for cid in case_ids}

# For handle time, we only include cases NOT transferred
# Compute handle time in seconds: closeddate - createddate
from datetime import datetime

def parse_dt(s):
    if pd.isna(s):
        return None
    # remove timezone offset for parsing simplicity
    try:
        return pd.to_datetime(s)
    except Exception:
        try:
            # fallback
            return datetime.fromisoformat(s)
        except Exception:
            return None

cases['created_dt'] = cases['createddate'].apply(parse_dt)
cases['closed_dt'] = cases['closeddate'].apply(parse_dt)

cases['handle_seconds'] = (cases['closed_dt'] - cases['created_dt']).dt.total_seconds()

# For each non-transferred case, determine the agent who handled it for handle time calculation
case_agent_for_handle = {}
for _, row in cases.iterrows():
    cid = row['id_norm']
    if transferred.get(cid, False):
        continue
    assigns = owner_assignments.get(cid, [])
    if len(assigns) == 1:
        agent = assigns[0]
    elif len(assigns) == 0:
        # fallback to case.ownerid
        agent = row['ownerid_norm']
    else:
        # should not happen since transferred filtered
        agent = assigns[-1]
    case_agent_for_handle[cid] = agent

# Build processed counts per agent (counts appearances in owner assignment OR fallback ownerid if no history)
from collections import defaultdict
processed_counts = defaultdict(int)

for cid in case_ids:
    assigns = owner_assignments.get(cid, [])
    if assigns:
        # each unique agent appearing in assignments for this case counts once
        uniq = set(assigns)
        for a in uniq:
            processed_counts[a] += 1
    else:
        # count the ownerid from cases
        owner = cases.loc[cases['id_norm'] == cid, 'ownerid_norm'].values
        if len(owner) > 0 and pd.notna(owner[0]):
            processed_counts[owner[0]] += 1

# Aggregate handle times per agent
agent_times = defaultdict(list)
for _, row in cases.iterrows():
    cid = row['id_norm']
    if cid in case_agent_for_handle:
        agent = case_agent_for_handle[cid]
        secs = row['handle_seconds']
        if pd.notna(secs):
            agent_times[agent].append(secs)

# Compute average handle time for agents with processed_counts > 1
avg_handle = {}
for agent, times in agent_times.items():
    if processed_counts.get(agent, 0) > 1 and len(times) > 0:
        avg_handle[agent] = sum(times) / len(times)

# Find agent with lowest average handle time
if len(avg_handle) == 0:
    final_answer = 'No agent processed more than one case in the past four months.'
else:
    best_agent = min(avg_handle.items(), key=lambda x: x[1])[0]
    final_answer = best_agent

print("__RESULT__:")
print(json.dumps(final_answer))"""

env_args = {'var_call_tBTxttUmSj0jM735usvSiPTE': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_OUOPHOd9dJR5HGQOhc0AwjTX': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_ZBTu4WlbexoaLnX13lyjWjOq': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_call_W2CdgCdmZDucVmbxAwWdlLDA': [{'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_call_UhJssDByIAEJ8mjAMaqcYEkG': [{'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-07-01T19:41:08.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-08-15T14:54:02.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-05-10T14:59:42.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-02T13:35:12.000+0000'}]}

exec(code, env_args)
