code = """import pandas as pd
from datetime import datetime
import json

cases = locals()['var_function-call-15982897061041835184']
owner_assignments = pd.read_json(locals()['var_function-call-18137263129467487004'])

df_cases = pd.DataFrame(cases)
df_owner_assignments = pd.DataFrame(owner_assignments)

df_cases['id'] = df_cases['case_id'].astype(str).str.replace('#', '')
df_owner_assignments['caseid__c'] = df_owner_assignments['caseid__c'].astype(str).str.replace('#', '')

merged_df = pd.merge(df_cases, df_owner_assignments, left_on='id', right_on='caseid__c', how='inner')

filtered_cases = merged_df[merged_df['owner_assignment_count'] == '1'].copy()

if not filtered_cases.empty:
    filtered_cases['createddate'] = pd.to_datetime(filtered_cases['createddate'])
    filtered_cases['closeddate'] = pd.to_datetime(filtered_cases['closeddate'])

    filtered_cases['handle_time_seconds'] = (filtered_cases['closeddate'] - filtered_cases['createddate']).dt.total_seconds()

    agent_handle_time = filtered_cases.groupby('ownerid').agg(
        average_handle_time=('handle_time_seconds', 'mean'),
        case_count=('case_id', 'count')
    ).reset_index()

    qualified_agents = agent_handle_time[agent_handle_time['case_count'] > 1]

    if not qualified_agents.empty:
        lowest_avg_handle_time_agent = qualified_agents.sort_values(by='average_handle_time').iloc[0]
        print("__RESULT__:")
        print(json.dumps(lowest_avg_handle_time_agent['ownerid']))
    else:
        print("__RESULT__:")
        print(json.dumps("No agent processed more than one case with a single owner assignment in the specified period."))
else:
    print("__RESULT__:")
    print(json.dumps("No cases found matching the criteria for a single owner assignment."))"""

env_args = {'var_function-call-6907360190667713395': [], 'var_function-call-8869806185366925560': [{'ownerid': '005Wt000003NJufIAG', 'id': '500Wt00000DDepmIAD', 'closeddate': '2023-07-01T19:41:08.000+0000', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'ownerid': '005Wt000003NJGLIA4', 'id': '500Wt00000DDyzpIAD', 'closeddate': '2023-08-15T14:54:02.000+0000', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'ownerid': '005Wt000003NDqDIAW', 'id': '500Wt00000DDzUPIA1', 'closeddate': '2023-05-10T14:59:42.000+0000', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'ownerid': '005Wt000003NJD9IAO', 'id': '500Wt00000DDzsbIAD', 'closeddate': '2023-06-30T19:03:08.000+0000', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'ownerid': '005Wt000003NEtOIAW', 'id': '#500Wt00000DDzscIAD', 'closeddate': '2023-05-03T00:11:47.000+0000', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'ownerid': '005Wt000003NJJaIAO', 'id': '500Wt00000DDzuEIAT', 'closeddate': '2023-06-02T13:35:12.000+0000', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'ownerid': '005Wt000003NIddIAG', 'id': '#500Wt00000DE02HIAT', 'closeddate': '2023-06-03T15:21:34.000+0000', 'createddate': '2023-06-03T14:45:00.000+0000'}], 'var_function-call-1760885609500656868': [], 'var_function-call-15396199020605542410': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-3935448621276007475': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-17989773560654426803': [], 'var_function-call-8906516923666930874': [{'case_id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'case_id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'case_id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'case_id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'case_id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'case_id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'case_id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-3248724496295902820': 'file_storage/function-call-3248724496295902820.json', 'var_function-call-15982897061041835184': [{'case_id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'case_id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'case_id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'case_id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'case_id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'case_id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'case_id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-18137263129467487004': 'file_storage/function-call-18137263129467487004.json'}

exec(code, env_args)
