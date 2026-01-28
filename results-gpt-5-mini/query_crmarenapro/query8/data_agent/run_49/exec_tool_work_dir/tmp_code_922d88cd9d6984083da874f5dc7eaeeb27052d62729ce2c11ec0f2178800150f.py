code = """import json
import pandas as pd

# Load the casehistory data from storage path
path = var_call_nqOpOVNnlAMDMIvHBq0rRjtS
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
df['createddate'] = pd.to_datetime(df['createddate'], errors='coerce')

# Define last 4 quarters window based on today's date 2023-04-10 (inclusive)
end_date = pd.to_datetime('2023-04-10')
start_date = end_date - pd.DateOffset(months=12)  # last 4 quarters = last 12 months

# Filter for Owner Assignment entries within window
df = df[df['field__c'].fillna('') == 'Owner Assignment']
df_window = df[(df['createddate'] >= start_date) & (df['createddate'] <= end_date)].copy()

# Clean agent id fields: strip whitespace and leading '#'
for col in ['oldvalue__c', 'newvalue__c']:
    df_window[col] = df_window[col].fillna('').astype(str).str.strip()
    df_window[col] = df_window[col].str.lstrip('#')

# Agents who handled >0 cases in window: appear as newvalue__c and not 'None' or empty
handled_mask = (~df_window['newvalue__c'].isin(['', 'None']))
handled_agents = set(df_window.loc[handled_mask, 'newvalue__c'].unique())

# Compute transfer counts in window: count of rows where oldvalue__c is an agent (not None/empty)
transfer_mask = (~df_window['oldvalue__c'].isin(['', 'None']))
transfers = df_window.loc[transfer_mask].copy()
# Clean again just in case
transfers['oldvalue__c'] = transfers['oldvalue__c'].astype(str).str.strip().str.lstrip('#')

transfer_counts = transfers.groupby('oldvalue__c').size().to_dict()

# For handled agents, get their transfer counts (0 if not present)
results = []
for agent in handled_agents:
    count = int(transfer_counts.get(agent, 0))
    results.append((agent, count))

# If no handled agents, return None
if not results:
    out = None
else:
    # Find agent(s) with minimum transfer count
    min_count = min(c for _, c in results)
    min_agents = sorted([a for a, c in results if c == min_count])
    # Tie-breaker: choose lexicographically smallest Id
    selected_agent = min_agents[0]
    out = selected_agent

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_rOzDP5H3RM7H6093kWdgb5jt': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_efsqYuKIamLsITilBvlMITox': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_nqOpOVNnlAMDMIvHBq0rRjtS': 'file_storage/call_nqOpOVNnlAMDMIvHBq0rRjtS.json'}

exec(code, env_args)
