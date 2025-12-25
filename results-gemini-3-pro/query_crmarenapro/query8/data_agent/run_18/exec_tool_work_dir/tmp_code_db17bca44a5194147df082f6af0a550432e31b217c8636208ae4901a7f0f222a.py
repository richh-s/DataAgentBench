code = """import pandas as pd
import json

file_path = 'var_function-call-13217811307273762437'  # Using the storage key directly if it's a file path? 
# Wait, the tool output says "The file path is stored under key: var_...". 
# The actual key content is the path? Or I need to read the variable?
# The instruction says: "To access the full result, your execute_python code must open and read that .json file."
# And "variables" are available in `locals()`.
# So `locals()['var_function-call-13217811307273762437']` contains the file path string.

try:
    file_path_var = locals()['var_function-call-13217811307273762437']
    with open(file_path_var, 'r') as f:
        data = json.load(f)
except KeyError:
    # If it wasn't a file, it might be the data directly.
    # But the message said "stored in a file".
    # Just in case, I'll check.
    # Actually, the instructions say: "The next message will include ... and the storage entry will be the .json file path (a string)".
    # So the variable IS the path.
    pass

df = pd.DataFrame(data)

# Clean IDs (strip leading # and potential whitespace)
def clean_id(x):
    if isinstance(x, str):
        x = x.strip()
        if x.startswith('#'):
            return x[1:]
    return x

df['oldvalue__c'] = df['oldvalue__c'].apply(clean_id)
df['newvalue__c'] = df['newvalue__c'].apply(clean_id)

# Parse dates
# Format: "2023-09-07T16:30:00.000+0000"
df['createddate'] = pd.to_datetime(df['createddate'])

# Define range
start_date = pd.Timestamp("2022-04-10", tz='UTC')
end_date = pd.Timestamp("2023-04-10", tz='UTC')

# Filter for relevant period
df_period = df[(df['createddate'] >= start_date) & (df['createddate'] <= end_date)]

# Identify Agents (User IDs start with '005')
def is_agent(x):
    return isinstance(x, str) and x.startswith('005')

# Population: Agents involved in assignment (in or out) during the period
agents_in = set(df_period[df_period['newvalue__c'].apply(is_agent)]['newvalue__c'])
agents_out = set(df_period[df_period['oldvalue__c'].apply(is_agent)]['oldvalue__c'])
population = agents_in.union(agents_out)

# Calculate Transfer Counts (only outgoing transfers count)
# A transfer is when an agent is in oldvalue.
transfer_df = df_period[df_period['oldvalue__c'].apply(is_agent)]
transfer_counts = transfer_df['oldvalue__c'].value_counts()

# Combine
results = []
for agent in population:
    count = transfer_counts.get(agent, 0)
    results.append({'AgentId': agent, 'TransferCount': count})

results_df = pd.DataFrame(results)
results_df = results_df.sort_values(by=['TransferCount', 'AgentId'])

print("__RESULT__:")
print(results_df.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-3617434593521771938': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-11996573601860322231': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-11996573601860322286': [], 'var_function-call-15416341987766006294': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-15416341987766007543': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'id': '500Wt00000DDDtTIAX', 'ownerid': '#005Wt000003NJWTIA4', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000'}, {'id': '500Wt00000DDPIsIAP', 'ownerid': '#005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'ownerid': '005Wt000003NISLIA4', 'createddate': '2020-09-01T10:30:00.000+0000'}], 'var_function-call-5902995038254626216': [{'Id': '#005Wt000003MH26IAG'}, {'Id': '#005Wt000003MH27IAG'}, {'Id': '#005Wt000003MH29IAG'}, {'Id': '#005Wt000003MH2GIAW'}, {'Id': '#005Wt000003MH2JIAW'}], 'var_function-call-13217811307273762437': 'file_storage/function-call-13217811307273762437.json'}

exec(code, env_args)
