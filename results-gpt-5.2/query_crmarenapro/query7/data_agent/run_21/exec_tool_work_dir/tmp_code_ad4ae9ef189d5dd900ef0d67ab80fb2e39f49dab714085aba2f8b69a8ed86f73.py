code = """import json
from pathlib import Path

case = var_call_hSMAPQPYj6mXFkeMlpCTU6ce[0]
emails = var_call_6CULLoJDNWvn9fLSOipzp2WN

kn_raw = var_call_oaMKl287iRxTV4fwXuXYqRUW
if isinstance(kn_raw, str):
    kn = json.loads(Path(kn_raw).read_text())
else:
    kn = kn_raw

agent_text = "\n".join([e.get('textbody','') for e in emails if (e.get('fromaddress','') or '').endswith('@techagents.com')])

norm = lambda s: (s or '').strip().lower()

match_id = None
if 'scalability enhancement package' in norm(agent_text):
    for r in kn:
        if ('scalability enhancement package' in norm(r.get('title')) or
            'scalability enhancement package' in norm(r.get('summary')) or
            'scalability enhancement package' in norm(r.get('faq_answer__c'))):
            match_id = r.get('id')
            break

result = match_id if match_id else None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hSMAPQPYj6mXFkeMlpCTU6ce': [{'case_id': '#500Wt00000DDyznIAD', 'case_subject': 'Scalability Problems ', 'case_description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt000007928FIAQ', 'contactid': '003Wt00000JqoiZIAR', 'accountid': '001Wt00000PGaZCIA1', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer', 'issue_name': 'None', 'issue_description': 'None'}], 'var_call_6CULLoJDNWvn9fLSOipzp2WN': [{'id': '02sWt000001zpY5IAI', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi", 'messagedate': '2022-09-22T19:28:30.000+0000', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]'}, {'id': '#02sWt000001zpZhIAI', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval", 'messagedate': '2022-09-22T21:05:14.000+0000', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]'}, {'id': '02sWt000001zpbJIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid', 'messagedate': '2022-09-23T09:12:38.000+0000', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]'}, {'id': '02sWt000001zpcvIAA', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe", 'messagedate': '2022-09-23T10:47:59.000+0000', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]'}, {'id': '#02sWt000001zpeXIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid', 'messagedate': '2022-09-23T11:23:47.000+0000', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]'}, {'id': '02sWt000001zpg9IAA', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe", 'messagedate': '2022-09-23T13:36:22.000+0000', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]'}, {'id': '02sWt000001zphlIAA', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid', 'messagedate': '2022-09-23T14:02:51.000+0000', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]'}, {'id': '02sWt000001zpjNIAQ', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe', 'messagedate': '2022-09-23T15:18:39.000+0000', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]'}], 'var_call_qDSjmey7KHzLmUJEwsP7GeuS': [], 'var_call_oaMKl287iRxTV4fwXuXYqRUW': 'file_storage/call_oaMKl287iRxTV4fwXuXYqRUW.json'}

exec(code, env_args)
