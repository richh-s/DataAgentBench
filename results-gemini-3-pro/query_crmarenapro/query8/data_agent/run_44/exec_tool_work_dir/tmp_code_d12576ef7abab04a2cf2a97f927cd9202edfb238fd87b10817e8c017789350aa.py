code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-3927801684446189843'], 'r') as f:
    history_data = json.load(f)

df = pd.DataFrame(history_data)

# Clean IDs
def clean_id(val):
    if val is None:
        return None
    s = str(val).strip()
    if s.startswith('#'):
        s = s[1:]
    if s == 'None':
        return None
    return s

df['oldvalue'] = df['oldvalue__c'].apply(clean_id)
df['newvalue'] = df['newvalue__c'].apply(clean_id)
df['date'] = pd.to_datetime(df['createddate'])

# Filter by date range: 2022-04-10 to 2023-04-10
start_date = pd.Timestamp('2022-04-10', tz='UTC')
end_date = pd.Timestamp('2023-04-10', tz='UTC')

# Ensure date is timezone aware or handle it. The strings have offset.
# pd.to_datetime handles ISO8601 with offsets.

# Filter
mask = (df['date'] >= start_date) & (df['date'] <= end_date)
window_df = df[mask]

# Identify agents active in the window (Handled > 0)
# Handled means appearing in newvalue (assignment to them)
# Definition: "filter applies to both the first agent that the case was first assigned to and the agent that the case was transferred to."
# This corresponds to newvalue column in "Owner Assignment" history.

# Count handled cases per agent
handled_counts = window_df['newvalue'].value_counts()
agents_handled_gt_0 = handled_counts[handled_counts > 0].index.tolist()

# Calculate transfer counts per agent in the window
# Transfer means appearing in oldvalue (transfer from them)
transfer_counts = window_df['oldvalue'].value_counts()

# Prepare results for agents who handled > 0 cases
results = []
for agent_id in agents_handled_gt_0:
    if agent_id is None:
        continue
    t_count = transfer_counts.get(agent_id, 0)
    results.append({'AgentId': agent_id, 'TransferCount': t_count, 'HandledCount': handled_counts[agent_id]})

# Find agent with min transfer count
results_df = pd.DataFrame(results)

if not results_df.empty:
    min_transfers = results_df['TransferCount'].min()
    candidates = results_df[results_df['TransferCount'] == min_transfers]
else:
    candidates = pd.DataFrame()

print("__RESULT__:")
print(json.dumps(candidates.to_dict(orient='records')))"""

env_args = {'var_function-call-7815841651268430622': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-1911759767125460883': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-3927801684446189843': 'file_storage/function-call-3927801684446189843.json'}

exec(code, env_args)
