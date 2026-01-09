code = """import json, pandas as pd
# load knowledge articles
ka_path = var_call_LQjw5WkE0iAiPqrrfkBXuRxS
with open(ka_path,'r',encoding='utf-8') as f:
    ka = json.load(f)

def norm(s):
    return (s or '').strip().lower()

# agent messages from email thread (from techagents.com)
emails = var_call_Omjl3UH7VOddXj7nIXHqPOGH
agent_text = '\n'.join([e.get('textbody','') for e in emails if 'techagents.com' in (e.get('fromaddress') or '')])
agent_norm = norm(agent_text)

# simple keyword match over titles/summaries/answers to see if agent quoted an internal KA
hits = []
for art in ka:
    aid = art.get('id')
    title = norm(art.get('title'))
    summ = norm(art.get('summary'))
    ans = norm(art.get('faq_answer__c'))
    # check if title or distinctive phrases appear in agent response
    if title and title in agent_norm:
        hits.append(aid)
        continue
    # check for urlname present
    url = norm(art.get('urlname'))
    if url and url in agent_norm:
        hits.append(aid)
        continue

result = {'agent_email_count': len([e for e in emails if 'techagents.com' in (e.get('fromaddress') or '')]),
          'matched_article_ids': hits}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_AIzm40e47lxji4HYNGcibQ1Y': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_call_LQjw5WkE0iAiPqrrfkBXuRxS': 'file_storage/call_LQjw5WkE0iAiPqrrfkBXuRxS.json', 'var_call_Omjl3UH7VOddXj7nIXHqPOGH': [{'id': '02sWt000001zpbJIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-23T09:12:38.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpY5IAI', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-22T19:28:30.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '#02sWt000001zpZhIAI', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-22T21:05:14.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpcvIAA', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-23T10:47:59.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpg9IAA', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-23T13:36:22.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '#02sWt000001zpeXIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-23T11:23:47.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zphlIAA', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-23T14:02:51.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpjNIAQ', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-23T15:18:39.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}], 'var_call_URTRqR0lUYiLwbRHk6OsKe1e': [], 'var_call_C5S21hQSRm748fefGCLZ20hd': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_call_u9wCn5jUXmRLk1h23CHAl8nf': []}

exec(code, env_args)
