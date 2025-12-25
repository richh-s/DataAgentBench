code = """import pandas as pd
import json

file_path_var = locals()['var_function-call-13217811307273762437']
with open(file_path_var, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def clean_id(x):
    if isinstance(x, str):
        x = x.strip()
        if x.startswith('#'):
            return x[1:]
    return x

df['oldvalue__c'] = df['oldvalue__c'].apply(clean_id)
df['newvalue__c'] = df['newvalue__c'].apply(clean_id)
df['createddate'] = pd.to_datetime(df['createddate'])

# Time range: Last 4 quarters (Assuming 2022-04-01 to 2023-03-31 based on typical quarters relative to Apr 2023)
# Or 2022-04-10 to 2023-04-10?
# Let's use 2022-04-01 to 2023-03-31 as "last 4 full quarters".
start_date = pd.Timestamp("2022-04-01", tz='UTC')
end_date = pd.Timestamp("2023-03-31", tz='UTC')

df_period = df[(df['createddate'] >= start_date) & (df['createddate'] <= end_date)]

def is_user(x):
    return isinstance(x, str) and x.startswith('005')

# Handled Cases Population:
# Agents who were 'newvalue' (assigned) or 'oldvalue' (transferred from) in the period.
# Note: If 'oldvalue' is None, it's a creation assignment to 'newvalue'.
# If 'oldvalue' is Agent, it's a transfer from Agent to 'newvalue'.
# In both cases, 'newvalue' handles the case.
# 'oldvalue' handled the case *before* the transfer.
# We need to count how many *cases* they handled.
# But for the *population filter*, we just need "handled > 0".
# So any agent appearing in 'newvalue' or 'oldvalue' in the period is in the population?
# Wait. If I held a case from 2021 and transferred it in May 2022. I am in 'oldvalue'. I handled > 0 cases (this one).
# If I received a case in May 2022. I am in 'newvalue'. I handled > 0 cases.
# So yes, set of all users in newvalue/oldvalue in the period.

users_in = set(df_period[df_period['newvalue__c'].apply(is_user)]['newvalue__c'])
users_out = set(df_period[df_period['oldvalue__c'].apply(is_user)]['oldvalue__c'])
population = users_in.union(users_out)

# Calculate Transfer Counts for this population
# Count occurrences in 'oldvalue' where 'newvalue' is ALSO a User?
# "Transfer from agent A to agent B".
# If I transfer to a Queue, is it a transfer count?
# I'll check both with and without "dest is user" filter.
# If I strictly follow "from agent A to agent B", I should require newvalue to be a User.

# Option 1: Any transfer out
transfers_all = df_period[df_period['oldvalue__c'].isin(population)]
counts_all = transfers_all['oldvalue__c'].value_counts()

# Option 2: Transfer to User
transfers_user = df_period[
    (df_period['oldvalue__c'].isin(population)) & 
    (df_period['newvalue__c'].apply(is_user))
]
counts_user = transfers_user['oldvalue__c'].value_counts()

# Let's use Option 1 (Any transfer out) as "transfer count" usually implies "gave up ownership".
# The "to agent B" might be descriptive. But if B is a Queue, it's still a transfer.
# However, "Agent B" strongly implies a person.
# If I use Option 2, counts might be lower.

# Handled Case Count (for tie breaking / verification)
# We need to count unique cases handled.
# But we don't have CaseId in the simplified dataframe? 
# Wait, I didn't select CaseId in the SQL query!
# I selected: oldvalue__c, newvalue__c, createddate.
# I need CaseId to count unique cases handled if I want to use it as a tiebreaker.
# I'll re-run SQL if needed. But let's see the counts first.
# Using Option 1 counts.

results = []
for agent in population:
    c_all = counts_all.get(agent, 0)
    c_user = counts_user.get(agent, 0)
    results.append({
        'AgentId': agent,
        'TransferCount_All': c_all,
        'TransferCount_User': c_user
    })

res_df = pd.DataFrame(results)
res_df = res_df.sort_values(by=['TransferCount_All', 'AgentId'])

print("__RESULT__:")
print(res_df.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-3617434593521771938': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-11996573601860322231': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-11996573601860322286': [], 'var_function-call-15416341987766006294': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-15416341987766007543': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'id': '500Wt00000DDDtTIAX', 'ownerid': '#005Wt000003NJWTIA4', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000'}, {'id': '500Wt00000DDPIsIAP', 'ownerid': '#005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'ownerid': '005Wt000003NISLIA4', 'createddate': '2020-09-01T10:30:00.000+0000'}], 'var_function-call-5902995038254626216': [{'Id': '#005Wt000003MH26IAG'}, {'Id': '#005Wt000003MH27IAG'}, {'Id': '#005Wt000003MH29IAG'}, {'Id': '#005Wt000003MH2GIAW'}, {'Id': '#005Wt000003MH2JIAW'}], 'var_function-call-13217811307273762437': 'file_storage/function-call-13217811307273762437.json', 'var_function-call-11766681463817807529': [{'AgentId': '005Wt000003NBcAIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NBykIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NDJ1IAO', 'TransferCount': 0}, {'AgentId': '005Wt000003NDqFIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NDsUIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NEGhIAO', 'TransferCount': 0}, {'AgentId': '005Wt000003NEzqIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NFKoIAO', 'TransferCount': 0}, {'AgentId': '005Wt000003NFr4IAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NGjuIAG', 'TransferCount': 0}], 'var_function-call-4848430679224115050': 'file_storage/function-call-4848430679224115050.json'}

exec(code, env_args)
