code = """import json
import pandas as pd
from datetime import datetime

# Load results from previous queries
cases = locals().get('var_functions.query_db:2', [])
history = locals().get('var_functions.query_db:8', [])

# Clean case data to remove leading #
cleaned_cases = []
for case in cases:
    clean_case = {
        'id': case['id'].lstrip('#'),
        'ownerid': case['ownerid'].lstrip('#'),
        'createddate': case['createddate'],
        'closeddate': case['closeddate']
    }
    cleaned_cases.append(clean_case)

# Clean history data
cleaned_history = []
for hist in history:
    clean_hist = {
        'id': hist['id'].lstrip('#'),
        'caseid__c': hist['caseid__c'].lstrip('#'),
        'oldvalue__c': hist['oldvalue__c'].lstrip('#'),
        'newvalue__c': hist['newvalue__c'].lstrip('#'),
        'field__c': hist['field__c'],
        'createddate': hist['createddate']
    }
    cleaned_history.append(clean_hist)

# Create DataFrames
cases_df = pd.DataFrame(cleaned_cases)
history_df = pd.DataFrame(cleaned_history)

# Parse dates
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'])
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'])

history_df['createddate'] = pd.to_datetime(history_df['createddate'])

# Find cases with multiple Owner Assignments (indicating transfers)
summary = history_df.groupby('caseid__c').size().reset_index(name='owner_assignment_count')
transferred_cases = summary[summary['owner_assignment_count'] > 1]['caseid__c'].tolist()

# Create initial assignment data
initial_assignments = history_df.sort_values('createddate').groupby('caseid__c').first().reset_index()

# Identify cases that should be included:
# 1. Cases with only ONE Owner Assignment (not transferred)
# 2. Cases processed in the last 4 months (already filtered)
cases_not_transferred = summary[summary['owner_assignment_count'] == 1]['caseid__c'].tolist()

# Filter cases to only include non-transferred cases
filtered_cases = cases_df[cases_df['id'].isin(cases_not_transferred)].copy()

# Calculate handle time in hours
filtered_cases['handle_time_hours'] = (filtered_cases['closeddate'] - filtered_cases['createddate']).dt.total_seconds() / 3600

# Join with initial assignments to get the original agent
final_data = filtered_cases.merge(initial_assignments[['caseid__c', 'newvalue__c']], left_on='id', right_on='caseid__c', how='left')
final_data = final_data.rename(columns={'newvalue__c': 'original_agent'})
final_data['original_agent'] = final_data['original_agent'].fillna(final_data['ownerid'])

# Count cases per agent
case_counts = final_data.groupby('original_agent').size().reset_index(name='case_count')

# Filter agents with more than 1 case
agents_with_multiple_cases = case_counts[case_counts['case_count'] > 1]['original_agent'].tolist()
multiple_case_data = final_data[final_data['original_agent'].isin(agents_with_multiple_cases)]

# Calculate average handle time per agent
avg_handle_time = multiple_case_data.groupby('original_agent').agg({
    'handle_time_hours': 'mean',
    'id': 'count'
}).reset_index()
avg_handle_time = avg_handle_time.rename(columns={'id': 'case_count'})
avg_handle_time = avg_handle_time.sort_values('handle_time_hours')

# Find agent with lowest average handle time
if not avg_handle_time.empty:
    lowest_agent = avg_handle_time.iloc[0]['original_agent']
    lowest_hours = avg_handle_time.iloc[0]['handle_time_hours']
    print("__RESULT__:")
    print(json.dumps(lowest_agent))
else:
    print("__RESULT__:")
    print(json.dumps(None))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_functions.query_db:8': [{'id': 'a04Wt00000538O1IAI', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NH3GIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'id': 'a04Wt00000539QTIAY', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-07-02T11:30:02.000+0000'}, {'id': 'a04Wt00000538O3IAI', 'caseid__c': '500Wt00000DDTxbIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'id': '#a04Wt00000537LUIAY', 'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'id': 'a04Wt00000538mAIAQ', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-06-12T10:00:06.000+0000'}, {'id': 'a04Wt00000538FtIAI', 'caseid__c': '500Wt00000DDsG3IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI5mIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'id': '#a04Wt00000538r0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'field__c': 'Owner Assignment', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'id': 'a04Wt00000537baIAA', 'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'id': '#a04Wt00000537zlIAA', 'caseid__c': '500Wt00000DDzXdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO', 'field__c': 'Owner Assignment', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'id': 'a04Wt00000536Z5IAI', 'caseid__c': '500Wt00000DDzZHIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'id': 'a04Wt00000538pNIAQ', 'caseid__c': '500Wt00000DDzivIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'id': 'a04Wt00000538hKIAQ', 'caseid__c': '500Wt00000DDzkXIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'field__c': 'Owner Assignment', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'id': 'a04Wt00000537ZzIAI', 'caseid__c': '500Wt00000DDzr0IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'id': 'a04Wt00000538scIAA', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'field__c': 'Owner Assignment', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'id': 'a04Wt00000538hMIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'field__c': 'Owner Assignment', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-06-03T14:45:00.000+0000'}]}

exec(code, env_args)
