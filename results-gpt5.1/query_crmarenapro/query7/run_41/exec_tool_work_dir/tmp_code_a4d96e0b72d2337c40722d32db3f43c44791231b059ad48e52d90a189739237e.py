code = """import json, pandas as pd, os

# Load full knowledge__kav data from file path
file_path = var_call_kXIAtDJhSYSox5WqUmj2A8xE
if isinstance(file_path, str) and os.path.isfile(file_path):
    import json as _json
    with open(file_path, 'r') as f:
        knowledge_data = _json.load(f)
else:
    knowledge_data = var_call_kXIAtDJhSYSox5WqUmj2A8xE

emails = pd.DataFrame(var_call_1COBLG7WHicA6R2eDVcqgvI3)
case = pd.DataFrame(var_call_Iw52vPrsaQCb6PihFsQpvtoq)
knowledge = pd.DataFrame(knowledge_data)

text = '\n'.join(list(emails['textbody']) + list(case['description']))
text_lower = text.lower()

violating_id = None
for _, row in knowledge.iterrows():
    title = str(row.get('title','')).strip().lower()
    summary = str(row.get('summary','')).strip().lower()
    answer = str(row.get('faq_answer__c','')).strip().lower()
    if title and title in text_lower:
        violating_id = row['id']
        break
    if summary and summary[:80] in text_lower:
        violating_id = row['id']
        break
    if answer and answer[:80] in text_lower:
        violating_id = row['id']
        break

result = violating_id if violating_id is not None else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1COBLG7WHicA6R2eDVcqgvI3': [{'id': '02sWt000001zpbJIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid'}, {'id': '02sWt000001zpY5IAI', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi"}, {'id': '#02sWt000001zpZhIAI', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval"}, {'id': '02sWt000001zpcvIAA', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe"}, {'id': '02sWt000001zpg9IAA', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe"}, {'id': '#02sWt000001zpeXIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid'}, {'id': '02sWt000001zphlIAA', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid'}, {'id': '02sWt000001zpjNIAQ', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe'}], 'var_call_kXIAtDJhSYSox5WqUmj2A8xE': 'file_storage/call_kXIAtDJhSYSox5WqUmj2A8xE.json', 'var_call_ockYcArepvzDMstQwORdcpYK': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'field__c': 'Owner Assignment'}], 'var_call_Iw52vPrsaQCb6PihFsQpvtoq': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer'}]}

exec(code, env_args)
