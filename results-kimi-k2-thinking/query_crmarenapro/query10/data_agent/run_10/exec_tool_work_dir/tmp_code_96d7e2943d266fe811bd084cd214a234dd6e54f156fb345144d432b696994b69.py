code = """# Access full query result
import json
import pandas as pd

# Read the full query result -- the preview shows a list so the entry should be the data directly
full_result = var_functions.query_db:2

# Convert to DataFrame for analysis
df_cases = pd.DataFrame(full_result)

print('__RESULT__:')
print(json.dumps({
  'num_cases': len(df_cases),
  'sample_cases': df_cases.head(10).to_dict('records'),
  'columns': list(df_cases.columns)
}))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': '#500Wt00000DDDfwIAH', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDTxbIAH', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NIfFIAW'}, {'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDflsIAD', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJppIAG'}, {'id': '#500Wt00000DDsG3IAL', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzXdIAL', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NJUrIAO'}, {'id': '500Wt00000DDzZHIA1', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '#500Wt00000DDzivIAD', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzkXIAT', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NINVIA4'}, {'id': '500Wt00000DDzr0IAD', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NJcvIAG'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_functions.query_db:5': []}

exec(code, env_args)
