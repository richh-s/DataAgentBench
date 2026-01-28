code = """import json
import pandas as pd
# Access previous query results
cases = pd.DataFrame(var_call_Eq6KR3GYICkjJOxbhCwOXGRg)
emails = pd.DataFrame(var_call_0lL7qh3dB4pDuyQ41LDUs1Gi)
casehist = pd.DataFrame(var_call_EuknWZInnWi4g2rk5rgNNjAT)
# Load knowledge articles result from file
with open(var_call_SB5yhWuJHgXKMR0dG8fMp3QL, 'r') as f:
    knowledge = pd.DataFrame(json.load(f))

# Normalize IDs (remove leading # and trailing whitespace)
def normalize_id(x):
    if pd.isna(x):
        return x
    return str(x).strip().lstrip('#')

for df in [cases, emails, casehist, knowledge]:
    if 'id' in df.columns:
        df['id_norm'] = df['id'].apply(normalize_id)

# Find which knowledge articles mention the Scalability Enhancement Package or similar in faq_answer__c/title
mask = knowledge['faq_answer__c'].str.contains('Scalability Enhancement', case=False, na=False) | knowledge['title'].str.contains('Scalability', case=False, na=False) | knowledge['faq_answer__c'].str.contains('scalab', case=False, na=False)
matched_ka = knowledge[mask]

# Prepare output: if any matched, return first id normalized, else None
if not matched_ka.empty:
    # choose the most relevant: look for exact phrase
    exact = matched_ka[matched_ka['faq_answer__c'].str.contains('Scalability Enhancement', case=False, na=False)]
    if not exact.empty:
        ka_id = normalize_id(exact.iloc[0]['id'])
    else:
        ka_id = normalize_id(matched_ka.iloc[0]['id'])
else:
    ka_id = None

result = json.dumps({'case_id': normalize_id('500Wt00000DDyznIAD'), 'breach_knowledge_article_id': ka_id})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_gDSS7FGRmvsdNPhBZJdZEvTw': [], 'var_call_Eq6KR3GYICkjJOxbhCwOXGRg': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'status': 'Waiting on Customer', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'ownerid': '005Wt000003NHsrIAG'}], 'var_call_0lL7qh3dB4pDuyQ41LDUs1Gi': [{'id': '02sWt000001zpbJIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'messagedate': '2022-09-23T09:12:38.000+0000'}, {'id': '02sWt000001zpY5IAI', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi", 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'messagedate': '2022-09-22T19:28:30.000+0000'}, {'id': '#02sWt000001zpZhIAI', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval", 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'messagedate': '2022-09-22T21:05:14.000+0000'}, {'id': '02sWt000001zpcvIAA', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'messagedate': '2022-09-23T10:47:59.000+0000'}, {'id': '02sWt000001zpg9IAA', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'messagedate': '2022-09-23T13:36:22.000+0000'}, {'id': '#02sWt000001zpeXIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'messagedate': '2022-09-23T11:23:47.000+0000'}, {'id': '02sWt000001zphlIAA', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'messagedate': '2022-09-23T14:02:51.000+0000'}, {'id': '02sWt000001zpjNIAQ', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe', 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'messagedate': '2022-09-23T15:18:39.000+0000'}], 'var_call_SB5yhWuJHgXKMR0dG8fMp3QL': 'file_storage/call_SB5yhWuJHgXKMR0dG8fMp3QL.json', 'var_call_EuknWZInnWi4g2rk5rgNNjAT': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'field__c': 'Case Creation', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'field__c': 'Owner Assignment', 'createddate': '2022-09-22T19:28:00.000+0000'}]}

exec(code, env_args)
