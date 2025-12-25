code = """import json
import pandas as pd

cases_data = locals()['var_function-call-5445523109931077059']
history_path = locals()['var_function-call-17191194624287533228']
with open(history_path, 'r') as f:
    history_data = json.load(f)

def clean_id(i):
    if not i: return i
    return i.lstrip('#')

cases_df = pd.DataFrame(cases_data)
cases_df['id'] = cases_df['id'].apply(clean_id)
history_df = pd.DataFrame(history_data)
history_df['caseid__c'] = history_df['caseid__c'].apply(clean_id)
history_df['newvalue__c'] = history_df['newvalue__c'].apply(clean_id)

relevant_case_ids = set(cases_df['id'].unique())
history_filtered = history_df[history_df['caseid__c'].isin(relevant_case_ids)].copy()

assignment_counts = history_filtered.groupby('caseid__c').size().reset_index(name='assign_count')
print("Assignment Counts per Case:")
print(assignment_counts)

processed_counts = history_filtered.groupby('newvalue__c')['caseid__c'].nunique().reset_index(name='processed_count')
print("Processed Counts per Agent:")
print(processed_counts)

single_owner_cases = assignment_counts[assignment_counts['assign_count'] == 1]['caseid__c']
print("Single Owner Cases:")
print(single_owner_cases.tolist())

# Join to find agents of single owner cases
single_history = history_filtered[history_filtered['caseid__c'].isin(single_owner_cases)]
print("Single Owner Agents:")
print(single_history[['caseid__c', 'newvalue__c']])

print("__RESULT__:")
print(json.dumps("Debug info printed"))"""

env_args = {'var_function-call-18262003565180936915': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5445523109931077059': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-15917723063401705946': [], 'var_function-call-18379950216490017826': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-9205801986047596649': [{'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4'}, {'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4'}, {'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG'}, {'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW'}, {'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG'}, {'caseid__c': '500Wt00000DE0NGIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG'}, {'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'caseid__c': '500Wt00000DDfYxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG'}, {'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG'}], 'var_function-call-9805771422527820542': [{'count': '7'}], 'var_function-call-17615445584445883886': [{'count': '165'}], 'var_function-call-4850416943357918028': 'Need to fetch history', 'var_function-call-17191194624287533228': 'file_storage/function-call-17191194624287533228.json', 'var_function-call-440547325235926189': 'No agents met the criteria'}

exec(code, env_args)
