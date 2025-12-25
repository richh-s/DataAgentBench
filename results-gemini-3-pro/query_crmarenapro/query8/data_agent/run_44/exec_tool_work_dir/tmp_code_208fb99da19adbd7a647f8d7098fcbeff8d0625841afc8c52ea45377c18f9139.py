code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-3927801684446189843'], 'r') as f:
    history_data = json.load(f)
with open(locals()['var_function-call-13624463416273525932'], 'r') as f:
    case_data = json.load(f)

# Convert to DF
history_df = pd.DataFrame(history_data)
case_df = pd.DataFrame(case_data)

# Helper for cleaning IDs
def clean_id(val):
    if val is None:
        return None
    s = str(val).strip()
    if s.startswith('#'):
        s = s[1:]
    if s == 'None':
        return None
    return s

# Clean History
history_df['oldvalue'] = history_df['oldvalue__c'].apply(clean_id)
history_df['newvalue'] = history_df['newvalue__c'].apply(clean_id)
history_df['caseid'] = history_df['caseid__c'].apply(clean_id)
history_df['date'] = pd.to_datetime(history_df['createddate'])

# Clean Case
case_df['id'] = case_df['id'].apply(clean_id)
case_df['ownerid'] = case_df['ownerid'].apply(clean_id)
# Handle None string in dates
def parse_date(d):
    if d == 'None' or d is None:
        return pd.NaT
    return pd.to_datetime(d)

case_df['createddate'] = case_df['createddate'].apply(parse_date)
case_df['closeddate'] = case_df['closeddate'].apply(parse_date)

# Define Window
start_date = pd.Timestamp('2022-04-10', tz='UTC')
end_date = pd.Timestamp('2023-04-10', tz='UTC')

# 1. Transfer Counts (in window)
mask_hist = (history_df['date'] >= start_date) & (history_df['date'] <= end_date)
window_hist = history_df[mask_hist]

transfer_counts = window_hist[window_hist['oldvalue'].notnull()]['oldvalue'].value_counts()

# 2. Handled Sets
handled_sets = {} # AgentId -> Set of CaseIds

# A. From History (Assignments in window)
# Both newvalue (recipient) counts as handling.
for _, row in window_hist.iterrows():
    agent = row['newvalue']
    if agent:
        if agent not in handled_sets: handled_sets[agent] = set()
        handled_sets[agent].add(row['caseid'])

# B. From Case Table (Held active from before window)
# Criteria: Created < start_date AND (Closed >= start_date OR Open) AND Owner = Agent
# Note: Case table ownerid is the CURRENT owner. 
# If they are current owner and case was open in window, they handled it.
# (If they transferred it away before window, they aren't owner. If they transferred in window, casehistory covers it?
# Wait. If they transferred it away in window, they WERE owner. 
# If they transferred it away, `casehistory` (oldvalue) tracks them?
# Yes. But does `casehistory` count as "handled"?
# If I transfer a case, I must have handled it.
# So agents in `oldvalue` also handled the case.
# Let's add `oldvalue` agents to Handled set too.
for _, row in window_hist.iterrows():
    agent = row['oldvalue']
    if agent:
        if agent not in handled_sets: handled_sets[agent] = set()
        handled_sets[agent].add(row['caseid'])

# Now add from Case table for "Passive Holding" (Assigned before, held through/part of window)
# Filter Cases: Created < StartDate
# And Active in Window: (ClosedDate is NaT OR ClosedDate >= StartDate)
# And Owner = Agent
mask_case = (case_df['createddate'] < start_date) & \
            ((case_df['closeddate'].isna()) | (case_df['closeddate'] >= start_date))

passive_cases = case_df[mask_case]

for _, row in passive_cases.iterrows():
    agent = row['ownerid']
    if agent:
        if agent not in handled_sets: handled_sets[agent] = set()
        handled_sets[agent].add(row['id'])

# Compile Results
results = []
all_agents = set(handled_sets.keys()) | set(transfer_counts.index)

for agent in all_agents:
    if not agent: continue
    t_count = transfer_counts.get(agent, 0)
    h_set = handled_sets.get(agent, set())
    h_count = len(h_set)
    
    if h_count > 0: # Filter handled > 0
        results.append({
            'AgentId': agent,
            'TransferCount': t_count,
            'HandledCount': h_count
        })

results_df = pd.DataFrame(results)
if not results_df.empty:
    results_df = results_df.sort_values(by=['TransferCount', 'HandledCount'], ascending=[True, False])

print("__RESULT__:")
print(json.dumps(results_df.head(10).to_dict(orient='records')))"""

env_args = {'var_function-call-7815841651268430622': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-1911759767125460883': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-3927801684446189843': 'file_storage/function-call-3927801684446189843.json', 'var_function-call-3544899369714927464': [{'AgentId': '005Wt000003NJ8HIAW', 'TransferCount': 0, 'HandledCount': 3}, {'AgentId': '005Wt000003NFKoIAO', 'TransferCount': 0, 'HandledCount': 3}, {'AgentId': '005Wt000003NJhlIAG', 'TransferCount': 0, 'HandledCount': 2}, {'AgentId': '005Wt000003NHsrIAG', 'TransferCount': 0, 'HandledCount': 2}, {'AgentId': '005Wt000003NINVIA4', 'TransferCount': 0, 'HandledCount': 2}, {'AgentId': '005Wt000003NEGhIAO', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NBcAIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NIVZIA4', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJ6gIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NFr4IAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NHpeIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NI2XIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NDqFIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NEzqIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJoDIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJTFIA4', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NIc2IAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NBykIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJrRIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJD9IAO', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NIwzIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NDsUIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NIaQIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NDJ1IAO', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NIvNIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NISLIA4', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJEjIAO', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NGjuIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJ0DIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NInLIAW', 'TransferCount': 0, 'HandledCount': 1}], 'var_function-call-15158139698347831638': [{'count': '153'}], 'var_function-call-4959567348419484179': [{'AgentId': '005Wt000003NJ8HIAW', 'TransferCount': 0, 'HandledCount': 3}, {'AgentId': '005Wt000003NFKoIAO', 'TransferCount': 0, 'HandledCount': 3}, {'AgentId': '005Wt000003NJhlIAG', 'TransferCount': 0, 'HandledCount': 2}, {'AgentId': '005Wt000003NHsrIAG', 'TransferCount': 0, 'HandledCount': 2}, {'AgentId': '005Wt000003NINVIA4', 'TransferCount': 0, 'HandledCount': 2}, {'AgentId': '005Wt000003NEGhIAO', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NBcAIAW', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NIVZIA4', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NJ6gIAG', 'TransferCount': 0, 'HandledCount': 1}, {'AgentId': '005Wt000003NFr4IAG', 'TransferCount': 0, 'HandledCount': 1}], 'var_function-call-7212576070251012142': [{'Id': '005Wt000003NFKoIAO', 'FirstName': 'Akari', 'LastName': 'Fujiwara', 'Username': '1745179504.lam3c.akari.fujiwara@techagents.com'}, {'Id': '005Wt000003NJ8HIAW', 'FirstName': 'Sun', 'LastName': 'Park', 'Username': '1745179504.4ll4g.sun.park@techagents.com'}], 'var_function-call-16236003141207340885': {'max_transfers': 1, 'total_transfers': 1, 'agents_with_transfers': ['005Wt000003NIliIAG']}, 'var_function-call-13624463416273525932': 'file_storage/function-call-13624463416273525932.json'}

exec(code, env_args)
