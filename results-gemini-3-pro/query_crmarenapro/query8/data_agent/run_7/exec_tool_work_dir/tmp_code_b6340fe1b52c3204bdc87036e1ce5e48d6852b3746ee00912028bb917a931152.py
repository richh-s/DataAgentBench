code = """# Try calendar quarters range
start_date_q = pd.Timestamp("2022-04-01", tz='UTC')
end_date_q = pd.Timestamp("2023-03-31 23:59:59", tz='UTC')

mask_q = (df['createddate'] >= start_date_q) & (df['createddate'] <= end_date_q)
df_period_q = df[mask_q]

# Transfer counts
transfer_counts_q = df_period_q[df_period_q['oldvalue__c'].notna()]['oldvalue__c'].value_counts().reset_index()
transfer_counts_q.columns = ['AgentId', 'TransferCount']

# Handled counts
agent_cases_q = []
for index, row in df_period_q.iterrows():
    cid = row['caseid__c']
    nv = row['newvalue__c']
    ov = row['oldvalue__c']
    
    if nv:
        agent_cases_q.append((nv, cid))
    if ov:
        agent_cases_q.append((ov, cid))

ac_df_q = pd.DataFrame(agent_cases_q, columns=['AgentId', 'CaseId'])
handled_counts_df_q = ac_df_q.groupby('AgentId')['CaseId'].nunique().reset_index(name='HandledCount')

# Merge
final_df_q = pd.merge(handled_counts_df_q, transfer_counts_q, on='AgentId', how='left')
final_df_q['TransferCount'] = final_df_q['TransferCount'].fillna(0)

# Sort
final_sorted_q = final_df_q.sort_values(by=['TransferCount', 'HandledCount'], ascending=[True, False])

print("__RESULT__:")
print(final_sorted_q.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-10626013757060285086': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-11785374727513229811': [{'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000'}, {'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000'}, {'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000'}, {'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000'}, {'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000'}], 'var_function-call-14958781564526342327': [{'id': 'a04Wt00000534p0IAA', 'caseid__c': '500Wt00000DDzRCIA1', 'oldvalue__c': '005Wt000003NFhOIAW', 'newvalue__c': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:38:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000535UwIAI', 'caseid__c': '500Wt00000DDzW3IAL', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NIfHIAW', 'createddate': '2021-11-02T13:31:14.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537riIAA', 'caseid__c': '500Wt00000DDzSnIAL', 'oldvalue__c': '005Wt000003NHuUIAW', 'newvalue__c': '005Wt000003NJ9tIAG', 'createddate': '2021-10-15T13:58:32.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt0000053831IAA', 'caseid__c': '500Wt00000DDnt7IAD', 'oldvalue__c': '005Wt000003NHGAIA4', 'newvalue__c': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T15:47:56.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-10511443330656022317': 'file_storage/function-call-10511443330656022317.json', 'var_function-call-18210778300925714813': [{'AgentId': '005Wt000003NEzqIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NFr4IAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NIvNIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NJTFIA4', 'TransferCount': 0}, {'AgentId': '005Wt000003NINVIA4', 'TransferCount': 0}, {'AgentId': '005Wt000003NIVZIA4', 'TransferCount': 0}, {'AgentId': '005Wt000003NJ8HIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NJD9IAO', 'TransferCount': 0}, {'AgentId': '005Wt000003NIwzIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NJ6gIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NFKoIAO', 'TransferCount': 0}, {'AgentId': '005Wt000003NISLIA4', 'TransferCount': 0}, {'AgentId': '005Wt000003NJrRIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NJhlIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NDsUIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NJEjIAO', 'TransferCount': 0}, {'AgentId': '005Wt000003NIaQIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NInLIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NJ0DIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NHsrIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NJoDIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NIc2IAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NEGhIAO', 'TransferCount': 0}, {'AgentId': '005Wt000003NDqFIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NGjuIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NBykIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NHpeIAG', 'TransferCount': 0}, {'AgentId': '005Wt000003NBcAIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NI2XIAW', 'TransferCount': 0}, {'AgentId': '005Wt000003NDJ1IAO', 'TransferCount': 0}], 'var_function-call-10702498914549235007': 'file_storage/function-call-10702498914549235007.json', 'var_function-call-4617240739277715832': [{'AgentId': '005Wt000003NFKoIAO', 'HandledCount': 3, 'TransferCount': 0.0}, {'AgentId': '005Wt000003NJ8HIAW', 'HandledCount': 3, 'TransferCount': 0.0}, {'AgentId': '005Wt000003NHsrIAG', 'HandledCount': 2, 'TransferCount': 0.0}, {'AgentId': '005Wt000003NINVIA4', 'HandledCount': 2, 'TransferCount': 0.0}, {'AgentId': '005Wt000003NJhlIAG', 'HandledCount': 2, 'TransferCount': 0.0}]}

exec(code, env_args)
