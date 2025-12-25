code = """import pandas as pd
import json

with open(locals()['var_function-call-1371008771125079157'], 'r') as f:
    history_data = json.load(f)

df = pd.DataFrame(history_data)

def clean_id(x):
    if pd.isna(x) or x == 'None':
        return None
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

df['old_clean'] = df['oldvalue__c'].apply(clean_id)
df['new_clean'] = df['newvalue__c'].apply(clean_id)
df['created_dt'] = pd.to_datetime(df['createddate'])

# Rolling window (Last 12 months)
window_start = pd.Timestamp('2022-04-10').tz_localize('UTC')
window_end = pd.Timestamp('2023-04-10').tz_localize('UTC')

df_window = df[(df['created_dt'] >= window_start) & (df['created_dt'] <= window_end)]

# Handlers in window
# Calculate "Handle Count" = Number of times appearing in new_clean in the window?
# Or maybe lifetime? "among those who handled more than 0 cases" (lifetime check)
# But maybe we want to see activity in the window?
# Let's count occurrences in new_clean (Received cases) in the window.
handle_counts = df_window['new_clean'].value_counts().to_dict()

# Transfer counts in window
transfers_window = df_window[df_window['old_clean'].notna()]
transfer_counts = transfers_window['old_clean'].value_counts().to_dict()

# Combine
results = []
all_agents = set(handle_counts.keys())
# Also include agents who transferred but maybe didn't receive in window (unlikely)
all_agents.update(transfer_counts.keys())

for agent in all_agents:
    h_count = handle_counts.get(agent, 0)
    t_count = transfer_counts.get(agent, 0)
    results.append({'agent_id': agent, 'handle_count': h_count, 'transfer_count': t_count})

results_df = pd.DataFrame(results)

# Filter: handled > 0
# The question says "among those who handled more than 0 cases". 
# If they are in `all_agents` (based on window), they handled > 0 in window.
# If we need lifetime, we should check lifetime. 
# But let's look at window stats first.

print("__RESULT__:")
print(json.dumps({
    "data": results_df.sort_values(by=['transfer_count', 'handle_count']).to_dict(orient='records')
}))"""

env_args = {'var_function-call-7142644131368088045': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12006095904079322963': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-9019972992037204871': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt000005322SIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt000005322UIAQ', 'caseid__c': '500Wt00000DE0NGIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000532wsIAA', 'caseid__c': '500Wt00000DDfYxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2022-04-01T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000532wtIAA', 'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-05-15T14:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-1371008771125079157': 'file_storage/function-call-1371008771125079157.json', 'var_function-call-11849969387961348424': {'min_count': 0, 'agents': ['005Wt000003NFW6IAO', '005Wt000003NJoDIAW', '005Wt000003NIfFIAW', '005Wt000003NJJaIAO', '005Wt000003NHGAIA4', '005Wt000003NINVIA4', '005Wt000003NHpeIAG', '005Wt000003NJ8HIAW', '005Wt000003NJ6fIAG', '005Wt000003NJQ1IAO', '005Wt000003NJcwIAG', '005Wt000003NHsrIAG', '005Wt000003NJTFIA4', '005Wt000003NDXZIA4', '005Wt000003NH3GIAW', '005Wt000003NJ0DIAW', '005Wt000003NJ9tIAG', '005Wt000003NFhOIAW', '005Wt000003NEdKIAW', '005Wt000003NDJ1IAO', '005Wt000003NIfHIAW', '005Wt000003NJD9IAO', '005Wt000003NEzqIAG', '005Wt000003NJeXIAW', '005Wt000003NJLBIA4', '005Wt000003NIc2IAG', '005Wt000003NIk7IAG', '005Wt000003NJrRIAW', '005Wt000003NISLIA4', '005Wt000003NJcvIAG', '005Wt000003NJWTIA4', '005Wt000003NJzVIAW', '005Wt000003NJ6gIAG', '005Wt000003NDu7IAG', '005Wt000003NIvNIAW', '005Wt000003NIVZIA4', '005Wt000003NJ3RIAW', '005Wt000003NFr4IAG', '005Wt000003NDqFIAW', '005Wt000003NIXBIA4', '005Wt000003NIYnIAO', '005Wt000003NIaQIAW', '005Wt000003NHg0IAG', '005Wt000003NHfyIAG', '005Wt000003NJbJIAW', '005Wt000003NJEjIAO', '005Wt000003NBcAIAW', '005Wt000003NInJIAW', '005Wt000003NIwzIAG', '005Wt000003NFKoIAO', '005Wt000003NFKpIAO', '005Wt000003NIDqIAO', '005Wt000003NJufIAG', '005Wt000003NEtOIAW', '005Wt000003NInLIAW', '005Wt000003NJhlIAG', '005Wt000003NI5mIAG', '005Wt000003NBykIAG', '005Wt000003NDsUIAW', '005Wt000003NHuUIAW', '005Wt000003NEGhIAO', '005Wt000003NGjuIAG', '005Wt000003NI2XIAW', '005Wt000003NItlIAG', '005Wt000003NIk5IAG'], 'count_distribution': {'0': 65, '1': 1}}, 'var_function-call-6385296065279354518': {'window_records': 39, 'active_handlers_count': 32, 'transfer_distribution': {'0': 31, '1': 1}, 'min_agents': ['005Wt000003NEGhIAO', '005Wt000003NJ6gIAG', '005Wt000003NI2XIAW', '005Wt000003NIvNIAW', '005Wt000003NJ8HIAW', '005Wt000003NHsrIAG', '005Wt000003NGjuIAG', '005Wt000003NHpeIAG', '005Wt000003NJrRIAW', '005Wt000003NJ0DIAW', '005Wt000003NBcAIAW', '005Wt000003NINVIA4', '005Wt000003NBykIAG', '005Wt000003NJcvIAG', '005Wt000003NIVZIA4', '005Wt000003NJhlIAG', '005Wt000003NDsUIAW', '005Wt000003NFKoIAO', '005Wt000003NJoDIAW', '005Wt000003NIwzIAG', '005Wt000003NJTFIA4', '005Wt000003NDqFIAW', '005Wt000003NFr4IAG', '005Wt000003NJEjIAO', '005Wt000003NEzqIAG', '005Wt000003NDJ1IAO', '005Wt000003NISLIA4', '005Wt000003NInLIAW', '005Wt000003NJD9IAO', '005Wt000003NIc2IAG', '005Wt000003NIaQIAW']}, 'var_function-call-7464679391815737905': {'transfers_rolling': [{'old_clean': '005Wt000003NIliIAG', 'new_clean': '005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:12:42.000+0000'}], 'all_time_counts': {'005Wt000003NJ6gIAG': 2, '005Wt000003NFhOIAW': 1, '005Wt000003NF1SIAW': 1, '005Wt000003NHuUIAW': 1, '005Wt000003NHGAIA4': 1, '005Wt000003NHg0IAG': 1, '005Wt000003NDqFIAW': 1, '005Wt000003NH3GIAW': 1, '005Wt000003NJ6fIAG': 1, '005Wt000003NIliIAG': 1, '005Wt000003NIc2IAG': 1}, 'active_handlers_count': 31}, 'var_function-call-5281047989285782295': [{'Id': '#005Wt000003MH26IAG', 'FirstName': 'Integration', 'LastName': 'User'}, {'Id': '#005Wt000003MH27IAG', 'FirstName': 'Automated', 'LastName': 'Process'}, {'Id': '#005Wt000003MH29IAG', 'FirstName': 'None', 'LastName': 'Platform Integration User '}, {'Id': '#005Wt000003MH2GIAW', 'FirstName': 'None', 'LastName': 'Chatter Expert'}, {'Id': '#005Wt000003MH2JIAW', 'FirstName': 'None', 'LastName': 'Data.com Clean'}, {'Id': '005Wt000003MH2OIAW', 'FirstName': 'None', 'LastName': 'Commerce'}, {'Id': '005Wt000003MH2WIAW', 'FirstName': 'Security', 'LastName': 'User'}, {'Id': '005Wt000003MNyjIAG', 'FirstName': 'Steeve', 'LastName': 'Huang'}, {'Id': '005Wt000003MOgHIAW', 'FirstName': 'Insights', 'LastName': 'Integration'}, {'Id': '005Wt000003MOgIIAW', 'FirstName': 'B2BMA', 'LastName': 'Integration'}, {'Id': '#005Wt000003MOgJIAW', 'FirstName': 'SalesforceIQ', 'LastName': 'Integration'}, {'Id': '005Wt000003NBcAIAW', 'FirstName': 'Sanjay', 'LastName': 'Thakur'}, {'Id': '005Wt000003NBcBIAW', 'FirstName': 'Ayumi', 'LastName': 'Shimizu'}, {'Id': '005Wt000003NBp4IAG', 'FirstName': 'Jasper', 'LastName': 'Dijk'}, {'Id': '005Wt000003NBp5IAG', 'FirstName': 'Enzo', 'LastName': 'Rossi'}, {'Id': '005Wt000003NBsIIAW', 'FirstName': 'Mohamed', 'LastName': 'Ahmed  '}, {'Id': '005Wt000003NBykIAG', 'FirstName': 'Ivan', 'LastName': 'Ivanov'}, {'Id': '005Wt000003NBylIAG', 'FirstName': 'Mei', 'LastName': 'Chen'}, {'Id': '005Wt000003NCRmIAO', 'FirstName': 'Liam', 'LastName': "O'Sullivan"}, {'Id': '#005Wt000003NCZqIAO', 'FirstName': 'Daisuke', 'LastName': 'Yamamoto'}, {'Id': '005Wt000003NCd5IAG', 'FirstName': 'Mei', 'LastName': 'Lin'}, {'Id': '#005Wt000003NCegIAG', 'FirstName': 'Maria', 'LastName': 'Papadopoulos'}, {'Id': '005Wt000003ND9KIAW', 'FirstName': 'Hassan', 'LastName': 'Zain'}, {'Id': '005Wt000003NDEBIA4', 'FirstName': 'Nadia', 'LastName': 'Al-Balushi'}, {'Id': '005Wt000003NDJ0IAO', 'FirstName': 'Rashmi   ', 'LastName': 'Dey'}, {'Id': '005Wt000003NDJ1IAO', 'FirstName': 'Majed', 'LastName': 'Hussein'}, {'Id': '005Wt000003NDXZIA4', 'FirstName': 'Ayumi  ', 'LastName': 'Nakamura'}, {'Id': '#005Wt000003NDXaIAO', 'FirstName': 'Santiago', 'LastName': 'Fernandez  '}, {'Id': '005Wt000003NDqDIAW', 'FirstName': 'Amara', 'LastName': 'Okafor'}, {'Id': '005Wt000003NDqEIAW', 'FirstName': 'Lerato  ', 'LastName': 'Dlamini'}, {'Id': '#005Wt000003NDqFIAW', 'FirstName': 'Svetlana', 'LastName': 'Novikova'}, {'Id': '005Wt000003NDsUIAW', 'FirstName': 'Nadia', 'LastName': 'Al-Rashid'}, {'Id': '#005Wt000003NDu7IAG', 'FirstName': 'Elisabeth', 'LastName': 'Fischer'}, {'Id': '005Wt000003NDu8IAG', 'FirstName': 'Lucia', 'LastName': 'Bianchi   '}, {'Id': '#005Wt000003NEGhIAO', 'FirstName': 'Yara', 'LastName': 'Awad'}, {'Id': '005Wt000003NEGiIAO', 'FirstName': 'Rashid', 'LastName': 'Hadi'}, {'Id': '005Wt000003NEGjIAO', 'FirstName': 'Chen', 'LastName': 'Lixin'}, {'Id': '005Wt000003NETaIAO', 'FirstName': 'Junaid', 'LastName': 'Khan'}, {'Id': '#005Wt000003NETbIAO', 'FirstName': 'Carmen', 'LastName': 'Silva   '}, {'Id': '#005Wt000003NEa3IAG', 'FirstName': 'Linh', 'LastName': 'Tran'}, {'Id': '005Wt000003NEdJIAW', 'FirstName': 'Pierre', 'LastName': 'Fontaine'}, {'Id': '005Wt000003NEdKIAW', 'FirstName': 'Thandi', 'LastName': 'Ngcobo'}, {'Id': '#005Wt000003NEoYIAW', 'FirstName': 'Fatoumata', 'LastName': 'Traoré'}, {'Id': '#005Wt000003NErnIAG', 'FirstName': 'Thato', 'LastName': 'Mokoena'}, {'Id': '005Wt000003NEtOIAW', 'FirstName': 'Sorcha', 'LastName': "O'Neill"}, {'Id': '005Wt000003NEtPIAW', 'FirstName': 'Isabella', 'LastName': 'Rossi '}, {'Id': '005Wt000003NEzqIAG', 'FirstName': 'Lucas', 'LastName': 'Martinez'}, {'Id': '005Wt000003NEzrIAG', 'FirstName': 'Pedro', 'LastName': 'Alvarez'}, {'Id': '#005Wt000003NF1SIAW', 'FirstName': 'Svetlana', 'LastName': 'Ivanov'}, {'Id': '005Wt000003NF9WIAW', 'FirstName': 'Aarav', 'LastName': 'Sharma'}], 'var_function-call-13660607439614749410': 'file_storage/function-call-13660607439614749410.json'}

exec(code, env_args)
