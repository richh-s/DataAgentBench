code = """import json
import collections

# Get file path
file_path = locals()['var_function-call-1870393683371189775']

# Load the file
with open(file_path, 'r') as f:
    history_data = json.load(f)

# Date range
start_date = "2022-04-01"
end_date = "2023-03-31"

# Containers
transfer_counts = collections.defaultdict(int)
handled_agents = set()

for record in history_data:
    created_date = record['createddate']
    date_str = created_date[:10]
    
    if start_date <= date_str <= end_date:
        old_val = record['oldvalue__c']
        new_val = record['newvalue__c']
        
        # Clean IDs
        if old_val and old_val != "None":
            old_val = old_val.lstrip('#')
            handled_agents.add(old_val)
            transfer_counts[old_val] += 1
            
        if new_val and new_val != "None":
            new_val = new_val.lstrip('#')
            handled_agents.add(new_val)

results = []
for agent in handled_agents:
    t_count = transfer_counts[agent]
    results.append({'id': agent, 'transfers': t_count})

# Sort by transfers (asc)
results.sort(key=lambda x: x['transfers'])

print("__RESULT__:")
print(json.dumps(results[:10]))"""

env_args = {'var_function-call-8025874654563589838': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-855199082558291909': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'id': '500Wt00000DDDtTIAX', 'ownerid': '#005Wt000003NJWTIA4', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000'}, {'id': '500Wt00000DDPIsIAP', 'ownerid': '#005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'ownerid': '005Wt000003NISLIA4', 'createddate': '2020-09-01T10:30:00.000+0000'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000'}, {'id': '500Wt00000DDPZ0IAP', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'id': '500Wt00000DDPsOIAX', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2021-07-06T14:30:00.000+0000'}, {'id': '500Wt00000DDPsPIAX', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2023-04-05T17:51:00.000+0000'}, {'id': '500Wt00000DDQRsIAP', 'ownerid': '#005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000'}], 'var_function-call-6931683400699587292': [{'caseid__c': '500Wt00000DDTEQIA5', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000'}, {'caseid__c': '500Wt00000DDzhJIAT', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzpNIAT', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000'}, {'caseid__c': '500Wt00000DDfHCIA1', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDZ0VIAX', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000'}, {'caseid__c': '500Wt00000DDQoUIAX', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzm9IAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDPsPIAX', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000'}, {'caseid__c': '500Wt00000DE00fIAD', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000'}], 'var_function-call-1870393683371189775': 'file_storage/function-call-1870393683371189775.json'}

exec(code, env_args)
