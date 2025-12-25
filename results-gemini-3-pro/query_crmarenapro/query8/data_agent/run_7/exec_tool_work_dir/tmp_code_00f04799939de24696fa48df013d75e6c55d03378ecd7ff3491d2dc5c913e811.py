code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-10702498914549235007'], 'r') as f:
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
df['caseid__c'] = df['caseid__c'].apply(clean_id)

# Convert date
df['createddate'] = pd.to_datetime(df['createddate'])

# Define range
start_date = pd.Timestamp("2022-04-10", tz='UTC')
end_date = pd.Timestamp("2023-04-10", tz='UTC')

# Filter by date
mask = (df['createddate'] >= start_date) & (df['createddate'] <= end_date)
df_period = df[mask]

# Calculate transfer counts (oldvalue occurences)
# Filter oldvalue not None
transfer_counts = df_period[df_period['oldvalue__c'].notna()]['oldvalue__c'].value_counts().reset_index()
transfer_counts.columns = ['AgentId', 'TransferCount']

# Calculate handled counts (unique cases for each agent)
agent_cases = []
for index, row in df_period.iterrows():
    cid = row['caseid__c']
    nv = row['newvalue__c']
    ov = row['oldvalue__c']
    
    if nv:
        agent_cases.append((nv, cid))
    if ov:
        agent_cases.append((ov, cid))

ac_df = pd.DataFrame(agent_cases, columns=['AgentId', 'CaseId'])
handled_counts_df = ac_df.groupby('AgentId')['CaseId'].nunique().reset_index(name='HandledCount')

# Merge
final_df = pd.merge(handled_counts_df, transfer_counts, on='AgentId', how='left')
final_df['TransferCount'] = final_df['TransferCount'].fillna(0)

# Sort by TransferCount ASC, HandledCount DESC
final_sorted = final_df.sort_values(by=['TransferCount', 'HandledCount'], ascending=[True, False])

print("__RESULT__:")
print(final_sorted.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-10626013757060285086': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-11785374727513229811': [{'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000'}, {'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000'}, {'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000'}, {'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000'}, {'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000'}], 'var_function-call-14958781564526342327': [{'id': 'a04Wt00000534p0IAA', 'caseid__c': '500Wt00000DDzRCIA1', 'oldvalue__c': '005Wt000003NFhOIAW', 'newvalue__c': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:38:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000535UwIAI', 'caseid__c': '500Wt00000DDzW3IAL', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NIfHIAW', 'createddate': '2021-11-02T13:31:14.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537riIAA', 'caseid__c': '500Wt00000DDzSnIAL', 'oldvalue__c': '005Wt000003NHuUIAW', 'newvalue__c': '005Wt000003NJ9tIAG', 'createddate': '2021-10-15T13:58:32.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt0000053831IAA', 'caseid__c': '500Wt00000DDnt7IAD', 'oldvalue__c': '005Wt000003NHGAIA4', 'newvalue__c': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T15:47:56.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-10511443330656022317': 'file_storage/function-call-10511443330656022317.json', 'var_function-call-18210778300925714813': [{'AgentId': '005Wt000003NEzqIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NFr4IAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NIvNIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NJTFIA4', 'TransferCount': 0}, {'AgentId': '005Wt000003NINVIA4', 'TransferCount': 0}, {'AgentId': '005Wt000003NIVZIA4', 'TransferCount': 0}, {'AgentId': '005Wt000003NJ8HIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NJD9IAO', 'TransferCount': 0}, {'AgentId': '005Wt000003NIwzIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NJ6gIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NFKoIAO', 'TransferCount': 0}, {'AgentId': '005Wt000003NISLIA4', 'TransferCount': 0}, {'AgentId': '005Wt000003NJrRIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NJhlIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NDsUIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NJEjIAO', 'TransferCount': 0}, {'AgentId': '005Wt000003NIaQIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NInLIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NJ0DIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NHsrIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NJoDIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NIc2IAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NEGhIAO', 'TransferCount': 0}, {'AgentId': '005Wt000003NDqFIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NGjuIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NBykIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NHpeIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NBcAIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NI2XIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NDJ1IAO', 'TransferCount': 0}], 'var_function-call-10702498914549235007': 'file_storage/function-call-10702498914549235007.json'}

exec(code, env_args)
