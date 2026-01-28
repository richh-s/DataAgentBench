code = """import json
import pandas as pd
from pathlib import Path

# Load the large casehistory JSON file from storage path
casehistory_path = Path(var_call_gXidmUcMSr2YWU7nS0kjCm1h)
with open(casehistory_path, 'r', encoding='utf-8') as f:
    ch_list = json.load(f)

# DataFrames
ch_df = pd.DataFrame(ch_list)
# Filter Owner Assignment
ch_df = ch_df[ch_df['field__c'] == 'Owner Assignment'].copy()
# Normalize ids: strip leading '#' and whitespace
for col in ['caseid__c', 'newvalue__c', 'oldvalue__c']:
    if col in ch_df.columns:
        ch_df[col] = ch_df[col].astype(str).str.strip().str.lstrip('#')

# Group owner assignments by case id, preserving order by createddate
if 'createddate' in ch_df.columns:
    ch_df['createddate'] = pd.to_datetime(ch_df['createddate'], utc=True, errors='coerce')
    ch_df = ch_df.sort_values(['caseid__c', 'createddate'])

owner_groups = ch_df.groupby('caseid__c')['newvalue__c'].apply(list).to_dict()
owner_counts = {k: len(v) for k, v in owner_groups.items()}

# Load cases from var_call_Qt1YkeB1aMeVbEvXnjPXXyCe
cases = var_call_Qt1YkeB1aMeVbEvXnjPXXyCe
cases_df = pd.DataFrame(cases)
# Normalize case ids and ownerid
if 'id' in cases_df.columns:
    cases_df['id'] = cases_df['id'].astype(str).str.strip().str.lstrip('#')
if 'ownerid' in cases_df.columns:
    cases_df['ownerid'] = cases_df['ownerid'].astype(str).str.strip().str.lstrip('#')

# Parse dates
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'], utc=True, errors='coerce')
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'], utc=True, errors='coerce')
# Compute handle time in seconds
cases_df['handle_seconds'] = (cases_df['closeddate'] - cases_df['createddate']).dt.total_seconds()

# Prepare per-agent processed cases (counting cases where agent appeared in owner assignments)
agent_case_sets = {}
# Prepare per-agent handle times for non-transferred cases (owner assignment count == 1)
agent_handle_times = {}

for _, row in cases_df.iterrows():
    case_id = str(row['id'])
    # get owner assignment list from casehistory; if missing, fallback to cases.ownerid
    owners = owner_groups.get(case_id, [])
    if not owners:
        # fallback
        ownerid = row.get('ownerid')
        if pd.notna(ownerid):
            owners = [str(ownerid).strip().lstrip('#')]
    # Count each case once per agent
    unique_owners = set([o for o in owners if o and o.lower() != 'none'])
    for agent in unique_owners:
        agent_case_sets.setdefault(agent, set()).add(case_id)
    # For handle time, only consider cases that were NOT transferred: i.e., total owner assignments == 1
    total_assignments = owner_counts.get(case_id, 0)
    # If owner_groups missing but we fell back to ownerid, treat as one assignment
    if total_assignments == 0 and owners:
        total_assignments = 1
    if total_assignments == 1:
        # single owner is the agent that handled the case
        owner_agent = None
        if owners:
            owner_agent = list(owners)[0]
        elif pd.notna(row.get('ownerid')):
            owner_agent = str(row.get('ownerid')).strip().lstrip('#')
        if owner_agent and owner_agent.lower() != 'none':
            if pd.notna(row['handle_seconds']):
                agent_handle_times.setdefault(owner_agent, []).append(float(row['handle_seconds']))

# Now compute agents who processed more than one case (in the period)
agents_with_counts = {agent: len(cases) for agent, cases in agent_case_sets.items()}
qualified_agents = [a for a, cnt in agents_with_counts.items() if cnt > 1]

# For these agents, compute average handle time from agent_handle_times
import math
agent_avg = {}
for agent in qualified_agents:
    times = agent_handle_times.get(agent, [])
    if times:
        agent_avg[agent] = float(sum(times) / len(times))

# Find agent with lowest average handle time
if agent_avg:
    min_agent = min(agent_avg.items(), key=lambda x: (x[1], x[0]))[0]
else:
    min_agent = None

# Output result as JSON serializable string
result = min_agent if min_agent is not None else ""

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1fi5aVOTplqAFOVoXFINT5VH': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_zSZ6ij3VmDZWk9ExXulApiRb': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_gXidmUcMSr2YWU7nS0kjCm1h': 'file_storage/call_gXidmUcMSr2YWU7nS0kjCm1h.json', 'var_call_Qt1YkeB1aMeVbEvXnjPXXyCe': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}]}

exec(code, env_args)
