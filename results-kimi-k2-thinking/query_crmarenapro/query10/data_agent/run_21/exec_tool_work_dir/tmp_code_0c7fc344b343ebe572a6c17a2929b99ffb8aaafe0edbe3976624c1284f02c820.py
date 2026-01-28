code = """import json
import pandas as pd
from datetime import datetime

# Load the data
cases = locals()['var_functions.query_db:10']  # Closed cases
history = locals()['var_functions.query_db:8']  # Case history

# Convert to DataFrames
df_cases = pd.DataFrame(cases)
df_history = pd.DataFrame(history)

# Clean up ID fields (handle leading #)
def clean_id(id_value):
  if isinstance(id_value, str) and id_value.startswith('#'):
    return id_value[1:]
  return id_value

if 'id' in df_cases.columns:
  df_cases['id'] = df_cases['id'].apply(clean_id)
if 'ownerid' in df_cases.columns:
  df_cases['ownerid'] = df_cases['ownerid'].apply(clean_id)

if 'caseid__c' in df_history.columns:
  df_history['caseid__c'] = df_history['caseid__c'].apply(clean_id)
if 'oldvalue__c' in df_history.columns:
  df_history['oldvalue__c'] = df_history['oldvalue__c'].apply(clean_id)
if 'newvalue__c' in df_history.columns:
  df_history['newvalue__c'] = df_history['newvalue__c'].apply(clean_id)

# Convert date strings to datetime
def parse_date(date_str):
  if pd.isna(date_str) or date_str == 'None' or date_str is None:
    return None
  # Remove the # prefix if present
  if isinstance(date_str, str) and date_str.startswith('#'):
    date_str = date_str[1:]
  try:
    # Handle the format like '2023-07-01T10:30:00.000+0000'
    return pd.to_datetime(date_str, utc=True)
  except:
    return None

df_cases['createddate'] = df_cases['createddate'].apply(parse_date)
df_cases['closeddate'] = df_cases['closeddate'].apply(parse_date)
df_history['createddate'] = df_history['createddate'].apply(parse_date)

# Analyze the history to identify transferred cases
# Cases that have multiple owner assignments where oldvalue is not 'None' (indicating a transfer)
transfer_data = df_history[df_history['field__c'] == 'Owner Assignment'].copy()
transferred_cases = set()

for case_id in transfer_data['caseid__c'].unique():
  case_transfers = transfer_data[transfer_data['caseid__c'] == case_id]
  # If there's at least one transfer (where oldvalue != 'None') and total assignments > 1
  has_transfer = (case_transfers['oldvalue__c'] != 'None').any()
  if has_transfer or len(case_transfers) > 1:
    transferred_cases.add(case_id)

# For transferred cases, use the FIRST owner (the one who started with the case)
# For non-transferred cases, use the owner from the cases table
agent_case_times = []

for idx, case_row in df_cases.iterrows():
  case_id = case_row['id']
  closed_date = case_row['closeddate']
  
  if case_id in transferred_cases:
    # Find the first owner
    case_transfers = transfer_data[transfer_data['caseid__c'] == case_id]
    if len(case_transfers) > 0:
      # Sort by createddate to get the first assignment
      first_transfer = case_transfers.sort_values('createddate').iloc[0]
      owner_id = first_transfer['newvalue__c']
      # The created date should come from the first assignment, but we use case created date
      # because the handle time is from case creation to case closure
      handle_time_hours = None
      if case_row['createddate'] is not None and closed_date is not None:
        handle_time_hours = (closed_date - case_row['createddate']).total_seconds() / 3600.0
      agent_case_times.append({
        'agent_id': owner_id,
        'case_id': case_id,
        'handle_time_hours': handle_time_hours
      })
  else:
    # Not transferred - use the owner from cases table
    handle_time_hours = None
    if case_row['createddate'] is not None and closed_date is not None:
      handle_time_hours = (closed_date - case_row['createddate']).total_seconds() / 3600.0
    agent_case_times.append({
      'agent_id': case_row['ownerid'],
      'case_id': case_id,
      'handle_time_hours': handle_time_hours
    })

# Create DataFrame of agent case times
df_times = pd.DataFrame(agent_case_times)

# Remove rows with None handle times and filter for agents with more than 1 case
valid_times = df_times[df_times['handle_time_hours'].notna()]
agent_stats = valid_times.groupby('agent_id').agg({
  'case_id': 'count',
  'handle_time_hours': 'mean'
}).reset_index()

agent_stats.columns = ['agent_id', 'case_count', 'avg_handle_time']
agents_with_multiple_cases = agent_stats[agent_stats['case_count'] > 1]

# Find the agent with lowest average handle time
if not agents_with_multiple_cases.empty:
  lowest_agent = agents_with_multiple_cases.loc[agents_with_multiple_cases['avg_handle_time'].idxmin()]
  result = lowest_agent['agent_id']
else:
  result = 'No agent found with multiple cases'

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}], 'var_functions.query_db:2': [], 'var_functions.list_db:5': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:6': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_functions.query_db:8': [{'caseid__c': '500Wt00000DDTxbIAH', 'field__c': 'Owner Assignment', 'createddate': '2023-08-15T14:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW'}, {'caseid__c': '500Wt00000DDTxbIAH', 'field__c': 'Case Creation', 'createddate': '2023-08-15T14:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Owner Assignment', 'createddate': '2023-07-01T10:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Creation', 'createddate': '2023-07-01T10:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Closed', 'createddate': '2023-07-01T19:41:08.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDflsIAD', 'field__c': 'Owner Assignment', 'createddate': '2023-06-12T09:45:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW'}, {'caseid__c': '500Wt00000DDflsIAD', 'field__c': 'Case Creation', 'createddate': '2023-06-12T09:45:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDflsIAD', 'field__c': 'Owner Assignment', 'createddate': '2023-06-12T10:00:06.000+0000', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Creation', 'createddate': '2023-08-15T14:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Owner Assignment', 'createddate': '2023-08-15T14:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Closed', 'createddate': '2023-08-15T14:54:02.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Owner Assignment', 'createddate': '2023-05-10T14:45:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Creation', 'createddate': '2023-05-10T14:45:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Closed', 'createddate': '2023-05-10T14:59:42.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzXdIAL', 'field__c': 'Owner Assignment', 'createddate': '2023-06-22T11:00:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO'}, {'caseid__c': '500Wt00000DDzXdIAL', 'field__c': 'Case Creation', 'createddate': '2023-06-22T11:00:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzZHIA1', 'field__c': 'Case Creation', 'createddate': '2023-07-02T09:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzZHIA1', 'field__c': 'Owner Assignment', 'createddate': '2023-07-02T09:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW'}, {'caseid__c': '500Wt00000DDzkXIAT', 'field__c': 'Case Creation', 'createddate': '2023-06-19T14:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzkXIAT', 'field__c': 'Owner Assignment', 'createddate': '2023-06-19T14:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4'}, {'caseid__c': '500Wt00000DDzr0IAD', 'field__c': 'Case Creation', 'createddate': '2023-08-01T10:00:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzr0IAD', 'field__c': 'Owner Assignment', 'createddate': '2023-08-01T10:00:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Owner Assignment', 'createddate': '2023-06-30T13:03:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Creation', 'createddate': '2023-06-30T13:03:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Closed', 'createddate': '2023-06-30T19:03:08.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Owner Assignment', 'createddate': '2023-06-02T09:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Creation', 'createddate': '2023-06-02T09:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Closed', 'createddate': '2023-06-02T13:35:12.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}], 'var_functions.query_db:10': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}]}

exec(code, env_args)
