code = """import json, pandas as pd
import os, textwrap

# knowledge articles file path
ka_path = var_call_AVM478CkCARyMsrPIgBZnueE
with open(ka_path, 'r') as f:
    ka = json.load(f)

df = pd.DataFrame(ka)

# Simple heuristic: look for articles mentioning scalability issues with QuantumPCB Modeler or Scalability Enhancement Package
text_cols = ['title', 'faq_answer__c', 'summary']
for col in text_cols:
    df[col] = df[col].fillna('')

mask = (
    df['faq_answer__c'].str.contains('Scalability Enhancement Package', case=False) |
    df['summary'].str.contains('Scalability Enhancement Package', case=False) |
    df['title'].str.contains('Scalability', case=False)
)

matches = df[mask]

if matches.empty:
    result = None
else:
    # assume the most relevant is the first match
    result = matches.iloc[0]['id']

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_iH9KUFF140TAt2376dWyRl7h': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'}], 'var_call_AVM478CkCARyMsrPIgBZnueE': 'file_storage/call_AVM478CkCARyMsrPIgBZnueE.json', 'var_call_17XJfh3wdRequIcuytiSK2zq': [{'id': '02sWt000001zpbJIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid'}, {'id': '02sWt000001zpY5IAI', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi"}, {'id': '#02sWt000001zpZhIAI', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval"}, {'id': '02sWt000001zpcvIAA', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe"}, {'id': '02sWt000001zpg9IAA', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe"}, {'id': '#02sWt000001zpeXIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid'}, {'id': '02sWt000001zphlIAA', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid'}, {'id': '02sWt000001zpjNIAQ', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe'}], 'var_call_R3uM06xpkSvDTVlxpgXAoxUc': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'field__c': 'Owner Assignment'}]}

exec(code, env_args)
