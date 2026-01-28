code = """import json
import pandas as pd

# Load the large query result from the file path stored in var_call_daYNAbhIkpKYaciAKjJ8IaR2
file_path = var_call_daYNAbhIkpKYaciAKjJ8IaR2
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Normalize id-like fields: strip whitespace, remove leading '#', treat 'None' as None
def normalize_id(x):
    if x is None:
        return None
    if isinstance(x, str):
        s = x.strip()
        if s == '' or s.lower() == 'none':
            return None
        # remove leading # characters
        while s.startswith('#'):
            s = s[1:]
        return s
    return x

for col in ['oldvalue__c','newvalue__c','caseid__c']:
    if col in df.columns:
        df[col] = df[col].apply(normalize_id)
    else:
        df[col] = None

# Parse dates
df['createddate'] = pd.to_datetime(df['createddate'], errors='coerce')

# Define date range: last 4 quarters relative to 2023-04-10 -> from 2022-04-10 to 2023-04-10 inclusive
start_date = pd.to_datetime('2022-04-10')
end_date = pd.to_datetime('2023-04-10')

# Filter Owner Assignment records within date range
mask = (df['field__c'] == 'Owner Assignment') & (df['createddate'] >= start_date) & (df['createddate'] <= end_date)
owner_df = df.loc[mask].copy()

# Compute transfer counts: when oldvalue is not None and newvalue is not None and old != new
owner_df['is_transfer'] = owner_df.apply(lambda r: (r['oldvalue__c'] is not None) and (r['newvalue__c'] is not None) and (r['oldvalue__c'] != r['newvalue__c']), axis=1)

transfer_counts = {}
handled_cases = {}  # agent -> set of case ids they were assigned to (newvalue)

for _, row in owner_df.iterrows():
    old = row['oldvalue__c']
    new = row['newvalue__c']
    caseid = row['caseid__c']

    # handled: new assignment to agent
    if new is not None:
        handled_cases.setdefault(new, set()).add(caseid)
    # transfer: count for old agent when it's a transfer
    if row['is_transfer'] and old is not None:
        transfer_counts[old] = transfer_counts.get(old, 0) + 1

# Consider agents who handled > 0 cases
agents_with_handled = [agent for agent, cases in handled_cases.items() if len(cases) > 0]

# For each such agent, get transfer count (default 0)
agent_transfer_list = []
for agent in agents_with_handled:
    tc = transfer_counts.get(agent, 0)
    agent_transfer_list.append((agent, tc))

if not agent_transfer_list:
    result = None
else:
    # find minimum transfer count
    min_tc = min(tc for _, tc in agent_transfer_list)
    # filter agents with min transfer count
    candidates = sorted([agent for agent, tc in agent_transfer_list if tc == min_tc])
    # pick the lexicographically smallest Id among ties
    result = candidates[0]

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_K4gLGCAEc7IZ1pfngVsfmrlv': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_daYNAbhIkpKYaciAKjJ8IaR2': 'file_storage/call_daYNAbhIkpKYaciAKjJ8IaR2.json'}

exec(code, env_args)
