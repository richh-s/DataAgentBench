code = """import pandas as pd
from datetime import datetime

cases_data = locals()['var_function-call-9398286675371511951']['results']
df_cases = pd.DataFrame(cases_data)

# Clean IDs by removing '#' and stripping whitespace
df_cases['id'] = df_cases['id'].str.replace('#', '', regex=False).str.strip()
df_cases['ownerid'] = df_cases['ownerid'].str.replace('#', '', regex=False).str.strip()

# Filter for closed cases and within the last four months
df_closed_cases = df_cases[(df_cases['closeddate'] != 'None') & (df_cases['closeddate'].notna())]

# Convert date strings to datetime objects for calculation
df_closed_cases['createddate'] = pd.to_datetime(df_closed_cases['createddate'])
df_closed_cases['closeddate'] = pd.to_datetime(df_closed_cases['closeddate'])

# Calculate handle time in seconds
df_closed_cases['handle_time_seconds'] = (df_closed_cases['closeddate'] - df_closed_cases['createddate']).dt.total_seconds()

# Group by ownerid and count cases, then calculate average handle time
agent_stats = df_closed_cases.groupby('ownerid').agg(
    case_count=('id', 'count'),
    avg_handle_time_seconds=('handle_time_seconds', 'mean')
).reset_index()

# Filter for agents who processed more than one case
agents_more_than_one_case = agent_stats[agent_stats['case_count'] > 1]

# Find the agent with the lowest average handle time
if not agents_more_than_one_case.empty:
    lowest_avg_handle_time_agent = agents_more_than_one_case.sort_values(by='avg_handle_time_seconds').iloc[0]
    result = lowest_avg_handle_time_agent['ownerid']
else:
    result = "No agent processed more than one case in the specified period."

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-13801400219804228205': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-9398286675371511951': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000'}, {'id': '#500Wt00000DDZ27IAH', 'ownerid': '005Wt000003NJzVIAW', 'createddate': '2023-10-02T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000'}, {'id': '#500Wt00000DDfYwIAL', 'ownerid': '005Wt000003NIk5IAG', 'createddate': '2024-05-02T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDgLKIA1', 'ownerid': '#005Wt000003NHuUIAW', 'createddate': '2023-11-03T11:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000'}, {'id': '#500Wt00000DDsG2IAL', 'ownerid': '#005Wt000003NI90IAG', 'createddate': '2023-10-03T14:34:22.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDxSdIAL', 'ownerid': '005Wt000003NJ6gIAG', 'createddate': '2024-05-15T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDyuwIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-10-16T09:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000'}, {'id': '500Wt00000DDzRBIA1', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-20T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzZGIA1', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2023-09-06T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDze6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-20T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDznlIAD', 'ownerid': '005Wt000003NIwzIAG', 'createddate': '2023-09-04T14:20:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '500Wt00000DDzz3IAD', 'ownerid': '005Wt000003NFW6IAO', 'createddate': '2024-05-02T09:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE00fIAD', 'ownerid': '005Wt000003NIAcIAO', 'createddate': '2023-09-05T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000'}, {'id': '500Wt00000DE0ByIAL', 'ownerid': '005Wt000003NGjuIAG', 'createddate': '2024-05-05T10:15:30.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000'}], 'var_function-call-2403642849139633364': []}

exec(code, env_args)
