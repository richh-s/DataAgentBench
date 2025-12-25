code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-14150000516763647607'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Date filtering
# Parse dates. Format example: 2023-09-07T16:30:00.000+0000
# We can use pd.to_datetime with utc=True
df['createddate'] = pd.to_datetime(df['createddate'])

# Define range
start_date = pd.Timestamp("2022-04-10", tz="UTC")
end_date = pd.Timestamp("2023-04-10", tz="UTC")

# Filter
mask = (df['createddate'] >= start_date) & (df['createddate'] <= end_date)
df_period = df[mask].copy()

# Clean IDs
def clean_id(val):
    if val is None:
        return None
    val = str(val).strip()
    if val.startswith('#'):
        return val[1:]
    if val == 'None':
        return None
    return val

df_period['newvalue__c'] = df_period['newvalue__c'].apply(clean_id)
df_period['oldvalue__c'] = df_period['oldvalue__c'].apply(clean_id)

# 1. Identify agents who handled > 0 cases
# Handled = assigned to (newvalue__c)
handled_agents = df_period['newvalue__c'].dropna().unique()

# 2. Calculate Transfer Counts for these agents
# Transfer Count = number of times agent appears as oldvalue__c (sender)
transfer_counts = df_period['oldvalue__c'].value_counts()

# 3. Find agent with fewest transfer counts among handled_agents
results = []
for agent in handled_agents:
    # Default is 0 if not found in transfer_counts
    count = transfer_counts.get(agent, 0)
    results.append({'agent_id': agent, 'transfer_count': count})

results_df = pd.DataFrame(results)

if not results_df.empty:
    min_count = results_df['transfer_count'].min()
    candidates = results_df[results_df['transfer_count'] == min_count]
    
    # Check candidates
    final_list = candidates['agent_id'].tolist()
    
    # If tie, let's see handled count to maybe break tie?
    # Or just print the list
    print("__RESULT__:")
    print(json.dumps(final_list))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-11088062025914686682': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-6082533964182735930': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-3320703554039932973': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-14150000516763647607': 'file_storage/function-call-14150000516763647607.json'}

exec(code, env_args)
