code = """import json
import pandas as pd
from dateutil import parser

# Load cases
cases_list = locals()['var_function-call-6685924510354294491']
cases_df = pd.DataFrame(cases_list)

# Load history
history_file = locals()['var_function-call-17573147314422126302']
with open(history_file, 'r') as f:
    history_list = json.load(f)
history_df = pd.DataFrame(history_list)

# Clean IDs
def clean_id(x):
    if not isinstance(x, str):
        return str(x)
    return x.strip().lstrip('#')

cases_df['clean_id'] = cases_df['id'].apply(clean_id)
cases_df['clean_owner'] = cases_df['ownerid'].apply(clean_id)
history_df['clean_caseid'] = history_df['caseid__c'].apply(clean_id)
history_df['clean_new'] = history_df['newvalue__c'].apply(lambda x: clean_id(x) if x != 'None' else None)
history_df['clean_old'] = history_df['oldvalue__c'].apply(lambda x: clean_id(x) if x != 'None' else None)

# Filter history for relevant cases and Owner Assignment
relevant_case_ids = set(cases_df['clean_id'])
history_df = history_df[history_df['clean_caseid'].isin(relevant_case_ids)]
owner_history = history_df[history_df['field__c'] == 'Owner Assignment']

# Parse dates and calculate handle time
cases_df['created_dt'] = cases_df['createddate'].apply(parser.parse)
cases_df['closed_dt'] = cases_df['closeddate'].apply(parser.parse)
cases_df['handle_time_sec'] = (cases_df['closed_dt'] - cases_df['created_dt']).dt.total_seconds()

# Map Case -> Set of Agents
case_agents = {}
for cid in relevant_case_ids:
    case_agents[cid] = set()

# Add final owners
for _, row in cases_df.iterrows():
    cid = row['clean_id']
    owner = row['clean_owner']
    case_agents[cid].add(owner)

# Add history owners
for _, row in owner_history.iterrows():
    cid = row['clean_caseid']
    if row['clean_new']:
        case_agents[cid].add(row['clean_new'])
    if row['clean_old']:
        case_agents[cid].add(row['clean_old'])

# Count managed cases per agent
agent_counts = {}
for cid, agents in case_agents.items():
    for agent in agents:
        agent_counts[agent] = agent_counts.get(agent, 0) + 1

# Calculate Average Handle Time for eligible agents
# Handle time is only credited to the Final Owner (Case.OwnerId)
# AND only if they qualify (>1 managed case)
# AND only for the cases they closed.

agent_handle_times = {} # Agent -> [list of times]

for _, row in cases_df.iterrows():
    final_owner = row['clean_owner']
    time = row['handle_time_sec']
    if final_owner not in agent_handle_times:
        agent_handle_times[final_owner] = []
    agent_handle_times[final_owner].append(time)

results = []
for agent, count in agent_counts.items():
    if count > 1:
        if agent in agent_handle_times:
            times = agent_handle_times[agent]
            avg_time = sum(times) / len(times)
            results.append({'agent': agent, 'avg_time': avg_time, 'count': count})
        else:
            # Agent managed > 1 cases but closed 0 cases (so handle time is undefined or 0? Usually ignored)
            pass

# Find min
if results:
    min_agent = min(results, key=lambda x: x['avg_time'])
    final_res = min_agent['agent']
else:
    final_res = "No eligible agents"

print("__RESULT__:")
print(json.dumps(final_res))"""

env_args = {'var_function-call-5368791863856089937': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}], 'var_function-call-11270569426259875892': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-9673334345705858900': [{'count': '165'}], 'var_function-call-16300619007678097437': [{'count': '7'}], 'var_function-call-805110141175851061': [{'count': '153'}], 'var_function-call-6685924510354294491': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}], 'var_function-call-17573147314422126302': 'file_storage/function-call-17573147314422126302.json'}

exec(code, env_args)
