code = """import json
import pandas as pd
from pathlib import Path

casehistory_path = Path(var_call_gXidmUcMSr2YWU7nS0kjCm1h)
with open(casehistory_path, 'r', encoding='utf-8') as f:
    ch_list = json.load(f)

ch_df = pd.DataFrame(ch_list)
ch_df = ch_df[ch_df['field__c'] == 'Owner Assignment'].copy()
for col in ['caseid__c', 'newvalue__c', 'oldvalue__c']:
    if col in ch_df.columns:
        ch_df[col] = ch_df[col].astype(str).str.strip().str.lstrip('#')
ch_df['createddate'] = pd.to_datetime(ch_df['createddate'], utc=True, errors='coerce')
ch_df = ch_df.sort_values(['caseid__c', 'createddate'])
owner_groups = ch_df.groupby('caseid__c')['newvalue__c'].apply(list).to_dict()
owner_counts = {k: len(v) for k, v in owner_groups.items()}

cases = var_call_Qt1YkeB1aMeVbEvXnjPXXyCe
cases_df = pd.DataFrame(cases)
if 'id' in cases_df.columns:
    cases_df['id'] = cases_df['id'].astype(str).str.strip().str.lstrip('#')
if 'ownerid' in cases_df.columns:
    cases_df['ownerid'] = cases_df['ownerid'].astype(str).str.strip().str.lstrip('#')
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'], utc=True, errors='coerce')
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'], utc=True, errors='coerce')
cases_df['handle_seconds'] = (cases_df['closeddate'] - cases_df['createddate']).dt.total_seconds()

agent_case_sets = {}
agent_handle_times = {}

for _, row in cases_df.iterrows():
    case_id = str(row['id'])
    owners = owner_groups.get(case_id, [])
    if not owners:
        ownerid = row.get('ownerid')
        if pd.notna(ownerid):
            owners = [str(ownerid).strip().lstrip('#')]
    unique_owners = set([o for o in owners if o and o.lower() != 'none'])
    for agent in unique_owners:
        agent_case_sets.setdefault(agent, set()).add(case_id)
    total_assignments = owner_counts.get(case_id, 0)
    if total_assignments == 0 and owners:
        total_assignments = 1
    if total_assignments == 1:
        owner_agent = None
        if owners:
            owner_agent = list(owners)[0]
        elif pd.notna(row.get('ownerid')):
            owner_agent = str(row.get('ownerid')).strip().lstrip('#')
        if owner_agent and owner_agent.lower() != 'none':
            if pd.notna(row['handle_seconds']):
                agent_handle_times.setdefault(owner_agent, []).append(float(row['handle_seconds']))

agents_with_counts = {agent: len(cases) for agent, cases in agent_case_sets.items()}
qualified_agents = [a for a, cnt in agents_with_counts.items() if cnt > 1]

agent_avg = {}
for agent in qualified_agents:
    times = agent_handle_times.get(agent, [])
    if times:
        agent_avg[agent] = float(sum(times) / len(times))

out = {
    'num_cases_in_period': len(cases_df),
    'agents_with_counts_sample': dict(list(agents_with_counts.items())[:20]),
    'num_agents_with_counts': len(agents_with_counts),
    'qualified_agents_sample': qualified_agents[:20],
    'agent_handle_times_sample_keys': list(agent_handle_times.keys())[:20],
    'agent_avg_sample': agent_avg,
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1fi5aVOTplqAFOVoXFINT5VH': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_zSZ6ij3VmDZWk9ExXulApiRb': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_gXidmUcMSr2YWU7nS0kjCm1h': 'file_storage/call_gXidmUcMSr2YWU7nS0kjCm1h.json', 'var_call_Qt1YkeB1aMeVbEvXnjPXXyCe': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_call_7Lznj704ckLojl7wDHr26fME': ''}

exec(code, env_args)
