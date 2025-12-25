code = """import json
import pandas as pd

# Load previous data
cases_list = locals()['var_function-call-12169961977782919954']
history_file = locals()['var_function-call-11956446384836222109']
with open(history_file, 'r') as f:
    history_list = json.load(f)

def clean_id(val):
    if isinstance(val, str):
        val = val.strip()
        if val.startswith('#'):
            return val[1:]
    return val

cases_df = pd.DataFrame(cases_list)
cases_df['id'] = cases_df['id'].apply(clean_id)
cases_df['ownerid'] = cases_df['ownerid'].apply(clean_id)
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'])
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'])

start_date = pd.Timestamp("2023-05-02", tz='UTC')
end_date = pd.Timestamp("2023-09-02", tz='UTC')
cases_df = cases_df[
    (cases_df['closeddate'] >= start_date) & 
    (cases_df['closeddate'] <= end_date)
]

history_df = pd.DataFrame(history_list)
history_df['caseid__c'] = history_df['caseid__c'].apply(clean_id)

relevant_ids = set(cases_df['id'].unique())
history_relevant = history_df[history_df['caseid__c'].isin(relevant_ids)]

print("__RESULT__:")
debug_info = {
    "num_cases": len(cases_df),
    "case_ids": cases_df['id'].tolist(),
    "history_counts": history_relevant.groupby('caseid__c').size().to_dict(),
    "history_sample": history_relevant.head(5).to_dict(orient='records')
}
print(json.dumps(debug_info))"""

env_args = {'var_function-call-17593237228977388210': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12169961977782919954': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}], 'var_function-call-10103375238797437899': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-11956446384836222109': 'file_storage/function-call-11956446384836222109.json', 'var_function-call-11766718509489547150': []}

exec(code, env_args)
