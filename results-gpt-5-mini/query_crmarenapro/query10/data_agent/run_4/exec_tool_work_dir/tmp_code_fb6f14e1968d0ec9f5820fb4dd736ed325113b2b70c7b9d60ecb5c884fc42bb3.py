code = """import pandas as pd
import json

# var_call_hmiUXLPxxcSfSTg7ynCkT16e is available from previous query
rows = var_call_hmiUXLPxxcSfSTg7ynCkT16e

df = pd.DataFrame(rows)
# Normalize 'None' strings to None
for col in ['case_createddate','case_closeddate','total_owner_assignments']:
    if col in df.columns:
        df[col] = df[col].replace({'None': None})

# parse datetimes
df['case_createddate_dt'] = pd.to_datetime(df['case_createddate'])
# case_closeddate may be None
df['case_closeddate_dt'] = pd.to_datetime(df['case_closeddate'])

# compute assignment counts per agent within the dataset (this dataset already filtered by date)
assignment_counts = df.groupby('agentid').size().to_dict()

# find agents who processed more than one case (count > 1)
agents_gt1 = {aid: cnt for aid, cnt in assignment_counts.items() if cnt > 1}

# For handle time, only consider cases with total_owner_assignments == '1' (no transfers) and with closeddate
# Note: total_owner_assignments may be string; ensure numeric
df['total_owner_assignments_num'] = pd.to_numeric(df['total_owner_assignments'], errors='coerce')

# Filter rows eligible for handle time calculation
eligible = df[(df['total_owner_assignments_num'] == 1) & (df['case_closeddate_dt'].notnull())]

# Compute handle time in seconds
eligible = eligible.copy()
eligible['handle_seconds'] = (eligible['case_closeddate_dt'] - eligible['case_createddate_dt']).dt.total_seconds()

# Compute average handle time per agent among eligible rows
avg_handle = eligible.groupby('agentid')['handle_seconds'].mean().to_dict()

# Now restrict to agents who processed >1 case
candidates = {aid: avg_handle[aid] for aid in agents_gt1.keys() if aid in avg_handle}

result_agent = None
if candidates:
    # find agent with lowest average handle time
    result_agent = min(candidates.items(), key=lambda x: x[1])[0]

# Prepare output
output = result_agent if result_agent is not None else None
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_jSLhUNI7fFjhfyhBIo3J0NNf': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_VOIooZTUgKcOiWUDte0Z0Rtc': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_UTYr2x2SWw54vM6kerKpgYSL': [{'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'caseid__c': '500Wt00000DDzZHIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000'}, {'caseid__c': '500Wt00000DDzr0IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzXdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDsG3IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NH3GIAW', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDTxbIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzkXIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzivIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:30:02.000+0000'}], 'var_call_8AYAvQrgQPyPfR9yL6bf9jtf': [{'caseid__c': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'case_createddate': '2023-07-02T09:30:00.000+0000', 'case_closeddate': 'None', 'owner_assigned_date': '2023-07-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'case_createddate': '2023-07-01T10:30:00.000+0000', 'case_closeddate': '2023-07-01T19:41:08.000+0000', 'owner_assigned_date': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzr0IAD', 'ownerid': '005Wt000003NJcvIAG', 'case_createddate': '2023-08-01T10:00:00.000+0000', 'case_closeddate': 'None', 'owner_assigned_date': '2023-08-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'case_createddate': '2023-05-10T14:45:00.000+0000', 'case_closeddate': '2023-05-10T14:59:42.000+0000', 'owner_assigned_date': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzXdIAL', 'ownerid': '005Wt000003NJUrIAO', 'case_createddate': '2023-06-22T11:00:00.000+0000', 'case_closeddate': 'None', 'owner_assigned_date': '2023-06-22T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDTxbIAH', 'ownerid': '005Wt000003NIfFIAW', 'case_createddate': '2023-08-15T14:30:00.000+0000', 'case_closeddate': 'None', 'owner_assigned_date': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzkXIAT', 'ownerid': '005Wt000003NINVIA4', 'case_createddate': '2023-06-19T14:30:00.000+0000', 'case_closeddate': 'None', 'owner_assigned_date': '2023-06-19T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'case_createddate': '2023-06-02T09:30:00.000+0000', 'case_closeddate': '2023-06-02T13:35:12.000+0000', 'owner_assigned_date': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'case_createddate': '2023-08-15T14:30:00.000+0000', 'case_closeddate': '2023-08-15T14:54:02.000+0000', 'owner_assigned_date': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'case_createddate': '2023-06-30T13:03:00.000+0000', 'case_closeddate': '2023-06-30T19:03:08.000+0000', 'owner_assigned_date': '2023-06-30T13:03:00.000+0000'}], 'var_call_hmiUXLPxxcSfSTg7ynCkT16e': [{'agentid': '005Wt000003NDqDIAW', 'caseid': '500Wt00000DDzUPIA1', 'case_createddate': '2023-05-10T14:45:00.000+0000', 'case_closeddate': '2023-05-10T14:59:42.000+0000', 'total_owner_assignments': '1'}, {'agentid': '005Wt000003NDqDIAW', 'caseid': '500Wt00000DDzZHIA1', 'case_createddate': '2023-07-02T09:30:00.000+0000', 'case_closeddate': 'None', 'total_owner_assignments': '1'}, {'agentid': '005Wt000003NF1SIAW', 'caseid': '500Wt00000DDflsIAD', 'case_createddate': '2023-06-12T09:45:00.000+0000', 'case_closeddate': 'None', 'total_owner_assignments': '2'}, {'agentid': '005Wt000003NINVIA4', 'caseid': '500Wt00000DDzkXIAT', 'case_createddate': '2023-06-19T14:30:00.000+0000', 'case_closeddate': 'None', 'total_owner_assignments': '1'}, {'agentid': '005Wt000003NIfFIAW', 'caseid': '500Wt00000DDTxbIAH', 'case_createddate': '2023-08-15T14:30:00.000+0000', 'case_closeddate': 'None', 'total_owner_assignments': '1'}, {'agentid': '005Wt000003NJD9IAO', 'caseid': '500Wt00000DDzsbIAD', 'case_createddate': '2023-06-30T13:03:00.000+0000', 'case_closeddate': '2023-06-30T19:03:08.000+0000', 'total_owner_assignments': '1'}, {'agentid': '005Wt000003NJGLIA4', 'caseid': '500Wt00000DDyzpIAD', 'case_createddate': '2023-08-15T14:30:00.000+0000', 'case_closeddate': '2023-08-15T14:54:02.000+0000', 'total_owner_assignments': '1'}, {'agentid': '005Wt000003NJJaIAO', 'caseid': '500Wt00000DDzuEIAT', 'case_createddate': '2023-06-02T09:30:00.000+0000', 'case_closeddate': '2023-06-02T13:35:12.000+0000', 'total_owner_assignments': '1'}, {'agentid': '005Wt000003NJUrIAO', 'caseid': '500Wt00000DDzXdIAL', 'case_createddate': '2023-06-22T11:00:00.000+0000', 'case_closeddate': 'None', 'total_owner_assignments': '1'}, {'agentid': '005Wt000003NJcvIAG', 'caseid': '500Wt00000DDzr0IAD', 'case_createddate': '2023-08-01T10:00:00.000+0000', 'case_closeddate': 'None', 'total_owner_assignments': '1'}, {'agentid': '005Wt000003NJppIAG', 'caseid': '500Wt00000DDflsIAD', 'case_createddate': '2023-06-12T09:45:00.000+0000', 'case_closeddate': 'None', 'total_owner_assignments': '2'}, {'agentid': '005Wt000003NJufIAG', 'caseid': '500Wt00000DDepmIAD', 'case_createddate': '2023-07-01T10:30:00.000+0000', 'case_closeddate': '2023-07-01T19:41:08.000+0000', 'total_owner_assignments': '1'}]}

exec(code, env_args)
