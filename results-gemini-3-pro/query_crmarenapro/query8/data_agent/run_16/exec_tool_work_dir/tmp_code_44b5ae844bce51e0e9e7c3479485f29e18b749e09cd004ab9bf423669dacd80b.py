code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-1371008771125079157'], 'r') as f:
    history_data = json.load(f)

df = pd.DataFrame(history_data)

# Clean IDs function
def clean_id(x):
    if pd.isna(x) or x == 'None':
        return None
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

# Clean columns
df['old_clean'] = df['oldvalue__c'].apply(clean_id)
df['new_clean'] = df['newvalue__c'].apply(clean_id)
df['created_dt'] = pd.to_datetime(df['createddate'])

# Current date reference
today = pd.Timestamp('2023-04-10').tz_localize('UTC')

# Filter out future data (relative to today)
df_past = df[df['created_dt'] <= today]

# Identify all agents who handled cases (ever, up to today)
# Handlers are anyone appearing in new_clean or old_clean
handlers = set()
handlers.update(df_past['new_clean'].dropna().unique())
handlers.update(df_past['old_clean'].dropna().unique())

# Define Last 4 Quarters Window
# Option A: Last 4 completed quarters: 2022-04-01 to 2023-03-31
# Option B: Last 12 months: 2022-04-10 to 2023-04-10
# Using Option A for "quarters" precision.
window_start = pd.Timestamp('2022-04-01').tz_localize('UTC')
window_end = pd.Timestamp('2023-03-31').tz_localize('UTC') + pd.Timedelta(days=1) - pd.Timedelta(seconds=1) # End of day

# Filter for transfers in window
# Transfer is when old_clean is not None
df_window = df_past[(df_past['created_dt'] >= window_start) & (df_past['created_dt'] <= window_end)]
transfers_window = df_window[df_window['old_clean'].notna()]

# Count transfers per agent
transfer_counts = transfers_window['old_clean'].value_counts()

# Prepare result for all handlers
results = []
for agent in handlers:
    count = transfer_counts.get(agent, 0)
    results.append({'agent_id': agent, 'transfer_count': count})

results_df = pd.DataFrame(results)

# Find minimum
min_count = results_df['transfer_count'].min()
min_agents = results_df[results_df['transfer_count'] == min_count]

print("__RESULT__:")
print(json.dumps({
    "min_count": int(min_count),
    "agents": min_agents['agent_id'].tolist(),
    "count_distribution": results_df['transfer_count'].value_counts().to_dict()
}))"""

env_args = {'var_function-call-7142644131368088045': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12006095904079322963': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-9019972992037204871': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt000005322SIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt000005322UIAQ', 'caseid__c': '500Wt00000DE0NGIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000532wsIAA', 'caseid__c': '500Wt00000DDfYxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2022-04-01T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000532wtIAA', 'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-05-15T14:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-1371008771125079157': 'file_storage/function-call-1371008771125079157.json'}

exec(code, env_args)
