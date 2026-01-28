code = """# Access full query result
import json
import pandas as pd

# Read the full query result from storage
result_key = 'var_functions.query_db:2'
cases_data = locals()[result_key]

# Convert to DataFrame for analysis
df_cases = pd.DataFrame(cases_data)

# Calculate handle time for closed cases
import dateutil.parser as dp

def calculate_handle_time(created, closed):
    if closed == 'None' or closed is None:
        return None
    try:
        created_dt = dp.parse(created)
        closed_dt = dp.parse(closed)
        return (closed_dt - created_dt).total_seconds() / 3600  # in hours
    except:
        return None

df_cases['handle_time_hours'] = df_cases.apply(
    lambda row: calculate_handle_time(row['createddate'], row['closeddate']), axis=1
)

# Count cases per owner
case_counts = df_cases.groupby('ownerid').size().reset_index(name='case_count')

# Filter owners with more than 1 case
owners_multiple_cases = case_counts[case_counts['case_count'] > 1]

# For closed cases, calculate average handle time per owner
closed_cases = df_cases[df_cases['handle_time_hours'].notna()]
avg_handle_times = closed_cases.groupby('ownerid')['handle_time_hours'].mean().reset_index(name='avg_handle_time_hours')

# Combine with owners who have multiple cases
owners_with_avg = pd.merge(
    owners_multiple_cases[['ownerid']], 
    avg_handle_times, 
    on='ownerid', 
    how='inner'
)

# Find owner with lowest average handle time
if not owners_with_avg.empty:
    lowest_avg_owner = owners_with_avg.loc[owners_with_avg['avg_handle_time_hours'].idxmin()]
    result = lowest_avg_owner['ownerid']
else:
    result = None

print('__RESULT__:')
print(json.dumps({'agent_id': result}))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': '#500Wt00000DDDfwIAH', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDTxbIAH', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NIfFIAW'}, {'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDflsIAD', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJppIAG'}, {'id': '#500Wt00000DDsG3IAL', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzXdIAL', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NJUrIAO'}, {'id': '500Wt00000DDzZHIA1', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '#500Wt00000DDzivIAD', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzkXIAT', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NINVIA4'}, {'id': '500Wt00000DDzr0IAD', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NJcvIAG'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_functions.query_db:5': []}

exec(code, env_args)
