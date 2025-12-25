code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-10511443330656022317'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Helper to clean ID
def clean_id(val):
    if not val or val == 'None':
        return None
    if val.startswith('#'):
        return val[1:]
    return val

# Clean columns
df['oldvalue__c'] = df['oldvalue__c'].apply(clean_id)
df['newvalue__c'] = df['newvalue__c'].apply(clean_id)

# Convert date
df['createddate'] = pd.to_datetime(df['createddate'])

# Define range
start_date = pd.Timestamp("2022-04-10", tz='UTC')
end_date = pd.Timestamp("2023-04-10", tz='UTC')

# Filter by date
mask = (df['createddate'] >= start_date) & (df['createddate'] <= end_date)
df_period = df[mask]

# Identify agents who handled cases in period
# Handled = appeared in newvalue (received/assigned) OR oldvalue (transferred from)
handled_agents = set()
handled_agents.update(df_period['newvalue__c'].dropna().unique())
handled_agents.update(df_period['oldvalue__c'].dropna().unique())

# Calculate transfer counts in period
# Transfer count = number of times agent is in oldvalue__c
transfer_counts = df_period['oldvalue__c'].dropna().value_counts()

# We need to consider ALL handled_agents. If an agent is in handled_agents but not in transfer_counts, their count is 0.
results = []
for agent in handled_agents:
    count = transfer_counts.get(agent, 0)
    results.append({'AgentId': agent, 'TransferCount': count})

results_df = pd.DataFrame(results)

# Find min
if not results_df.empty:
    min_transfers = results_df['TransferCount'].min()
    candidates = results_df[results_df['TransferCount'] == min_transfers]
    print("__RESULT__:")
    print(candidates.to_json(orient='records'))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-10626013757060285086': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-11785374727513229811': [{'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000'}, {'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000'}, {'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000'}, {'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000'}, {'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000'}], 'var_function-call-14958781564526342327': [{'id': 'a04Wt00000534p0IAA', 'caseid__c': '500Wt00000DDzRCIA1', 'oldvalue__c': '005Wt000003NFhOIAW', 'newvalue__c': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:38:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000535UwIAI', 'caseid__c': '500Wt00000DDzW3IAL', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NIfHIAW', 'createddate': '2021-11-02T13:31:14.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537riIAA', 'caseid__c': '500Wt00000DDzSnIAL', 'oldvalue__c': '005Wt000003NHuUIAW', 'newvalue__c': '005Wt000003NJ9tIAG', 'createddate': '2021-10-15T13:58:32.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt0000053831IAA', 'caseid__c': '500Wt00000DDnt7IAD', 'oldvalue__c': '005Wt000003NHGAIA4', 'newvalue__c': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T15:47:56.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-10511443330656022317': 'file_storage/function-call-10511443330656022317.json'}

exec(code, env_args)
