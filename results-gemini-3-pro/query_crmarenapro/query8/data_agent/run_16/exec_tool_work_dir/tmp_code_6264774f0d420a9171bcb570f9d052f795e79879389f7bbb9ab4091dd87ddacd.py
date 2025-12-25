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

# Rolling window
window_start = pd.Timestamp('2022-04-10').tz_localize('UTC')
window_end = pd.Timestamp('2023-04-10').tz_localize('UTC')

df_window = df[(df['created_dt'] >= window_start) & (df['created_dt'] <= window_end)]
transfers_window = df_window[df_window['old_clean'].notna()]

transfers_list = transfers_window[['old_clean', 'new_clean', 'createddate']].to_dict(orient='records')
all_transfers_counts = df[df['old_clean'].notna()]['old_clean'].value_counts().to_dict()

# Active handlers
active_handlers = set()
active_handlers.update(df_window['new_clean'].dropna().unique())
active_handlers.update(df_window['old_clean'].dropna().unique())

print("__RESULT__:")
print(json.dumps({
    "transfers_rolling": transfers_list,
    "all_time_counts": all_transfers_counts,
    "active_handlers_count": len(active_handlers)
}))"""

env_args = {'var_function-call-7142644131368088045': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12006095904079322963': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-9019972992037204871': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt000005322SIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt000005322UIAQ', 'caseid__c': '500Wt00000DE0NGIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000532wsIAA', 'caseid__c': '500Wt00000DDfYxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2022-04-01T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000532wtIAA', 'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-05-15T14:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-1371008771125079157': 'file_storage/function-call-1371008771125079157.json', 'var_function-call-11849969387961348424': {'min_count': 0, 'agents': ['005Wt000003NFW6IAO', '005Wt000003NJoDIAW', '005Wt000003NIfFIAW', '005Wt000003NJJaIAO', '005Wt000003NHGAIA4', '005Wt000003NINVIA4', '005Wt000003NHpeIAG', '005Wt000003NJ8HIAW', '005Wt000003NJ6fIAG', '005Wt000003NJQ1IAO', '005Wt000003NJcwIAG', '005Wt000003NHsrIAG', '005Wt000003NJTFIA4', '005Wt000003NDXZIA4', '005Wt000003NH3GIAW', '005Wt000003NJ0DIAW', '005Wt000003NJ9tIAG', '005Wt000003NFhOIAW', '005Wt000003NEdKIAW', '005Wt000003NDJ1IAO', '005Wt000003NIfHIAW', '005Wt000003NJD9IAO', '005Wt000003NEzqIAG', '005Wt000003NJeXIAW', '005Wt000003NJLBIA4', '005Wt000003NIc2IAG', '005Wt000003NIk7IAG', '005Wt000003NJrRIAW', '005Wt000003NISLIA4', '005Wt000003NJcvIAG', '005Wt000003NJWTIA4', '005Wt000003NJzVIAW', '005Wt000003NJ6gIAG', '005Wt000003NDu7IAG', '005Wt000003NIvNIAW', '005Wt000003NIVZIA4', '005Wt000003NJ3RIAW', '005Wt000003NFr4IAG', '005Wt000003NDqFIAW', '005Wt000003NIXBIA4', '005Wt000003NIYnIAO', '005Wt000003NIaQIAW', '005Wt000003NHg0IAG', '005Wt000003NHfyIAG', '005Wt000003NJbJIAW', '005Wt000003NJEjIAO', '005Wt000003NBcAIAW', '005Wt000003NInJIAW', '005Wt000003NIwzIAG', '005Wt000003NFKoIAO', '005Wt000003NFKpIAO', '005Wt000003NIDqIAO', '005Wt000003NJufIAG', '005Wt000003NEtOIAW', '005Wt000003NInLIAW', '005Wt000003NJhlIAG', '005Wt000003NI5mIAG', '005Wt000003NBykIAG', '005Wt000003NDsUIAW', '005Wt000003NHuUIAW', '005Wt000003NEGhIAO', '005Wt000003NGjuIAG', '005Wt000003NI2XIAW', '005Wt000003NItlIAG', '005Wt000003NIk5IAG'], 'count_distribution': {'0': 65, '1': 1}}, 'var_function-call-6385296065279354518': {'window_records': 39, 'active_handlers_count': 32, 'transfer_distribution': {'0': 31, '1': 1}, 'min_agents': ['005Wt000003NEGhIAO', '005Wt000003NJ6gIAG', '005Wt000003NI2XIAW', '005Wt000003NIvNIAW', '005Wt000003NJ8HIAW', '005Wt000003NHsrIAG', '005Wt000003NGjuIAG', '005Wt000003NHpeIAG', '005Wt000003NJrRIAW', '005Wt000003NJ0DIAW', '005Wt000003NBcAIAW', '005Wt000003NINVIA4', '005Wt000003NBykIAG', '005Wt000003NJcvIAG', '005Wt000003NIVZIA4', '005Wt000003NJhlIAG', '005Wt000003NDsUIAW', '005Wt000003NFKoIAO', '005Wt000003NJoDIAW', '005Wt000003NIwzIAG', '005Wt000003NJTFIA4', '005Wt000003NDqFIAW', '005Wt000003NFr4IAG', '005Wt000003NJEjIAO', '005Wt000003NEzqIAG', '005Wt000003NDJ1IAO', '005Wt000003NISLIA4', '005Wt000003NInLIAW', '005Wt000003NJD9IAO', '005Wt000003NIc2IAG', '005Wt000003NIaQIAW']}}

exec(code, env_args)
