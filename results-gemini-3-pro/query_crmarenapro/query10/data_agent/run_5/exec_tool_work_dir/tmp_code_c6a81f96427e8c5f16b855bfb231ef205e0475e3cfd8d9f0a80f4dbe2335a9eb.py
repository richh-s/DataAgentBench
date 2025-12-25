code = """import pandas as pd
from datetime import datetime

# Case Data
cases = [
    {"id": "500Wt00000DDepmIAD", "ownerid": "005Wt000003NJufIAG", "created": "2023-07-01T10:30:00.000+0000", "closed": "2023-07-01T19:41:08.000+0000"},
    {"id": "500Wt00000DDyzpIAD", "ownerid": "005Wt000003NJGLIA4", "created": "2023-08-15T14:30:00.000+0000", "closed": "2023-08-15T14:54:02.000+0000"},
    {"id": "500Wt00000DDzUPIA1", "ownerid": "005Wt000003NDqDIAW", "created": "2023-05-10T14:45:00.000+0000", "closed": "2023-05-10T14:59:42.000+0000"},
    {"id": "500Wt00000DDzsbIAD", "ownerid": "005Wt000003NJD9IAO", "created": "2023-06-30T13:03:00.000+0000", "closed": "2023-06-30T19:03:08.000+0000"},
    {"id": "500Wt00000DDzscIAD", "ownerid": "005Wt000003NEtOIAW", "created": "2023-05-02T23:55:00.000+0000", "closed": "2023-05-03T00:11:47.000+0000"},
    {"id": "500Wt00000DDzuEIAT", "ownerid": "005Wt000003NJJaIAO", "created": "2023-06-02T09:30:00.000+0000", "closed": "2023-06-02T13:35:12.000+0000"},
    {"id": "500Wt00000DE02HIAT", "ownerid": "005Wt000003NIddIAG", "created": "2023-06-03T14:45:00.000+0000", "closed": "2023-06-03T15:21:34.000+0000"}
]

# Calculate Handle Time (in seconds, or minutes?) 
# Question asks for "lowest average handle time". Unit doesn't matter for comparison.
# Let's use seconds.
results = []
for c in cases:
    fmt = "%Y-%m-%dT%H:%M:%S.%f%z"
    # Python 3.11+ supports %z with : but older might not. 
    # The string has +0000. It should parse.
    # Note: 3.12 environment.
    start = datetime.strptime(c["created"], fmt)
    end = datetime.strptime(c["closed"], fmt)
    duration = (end - start).total_seconds()
    results.append({"ownerid": c["ownerid"], "handle_time": duration})

df = pd.DataFrame(results)
# Since each agent has only 1 case in this set, average = value.
# But we need to filter by count > 1 later.
# Group by owner to be safe
avg_times = df.groupby("ownerid")["handle_time"].mean().reset_index()

agent_ids = df["ownerid"].unique().tolist()
agent_ids_str = ", ".join([f"'{x}'" for x in agent_ids])

print("__RESULT__:")
print(f'{{"avg_times": {avg_times.to_json(orient="records")}, "agent_ids_query": "{agent_ids_str}"}}')"""

env_args = {'var_function-call-10331671326788110190': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-1540628053348756103': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-4717624422894752826': [{'count': '7'}], 'var_function-call-8200405563081420475': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-12749052827483353767': [{'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}], 'var_function-call-6138125289454668363': [{'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG'}]}

exec(code, env_args)
