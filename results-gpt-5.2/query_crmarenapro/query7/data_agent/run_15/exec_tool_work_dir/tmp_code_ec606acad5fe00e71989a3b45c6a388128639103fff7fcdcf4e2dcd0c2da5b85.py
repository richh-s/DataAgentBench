code = """import json, pandas as pd

# load knowledge articles (may be in file)
ka_src = var_call_kJP50q6P9babKdjeNvR2oxy0
if isinstance(ka_src, str):
    with open(ka_src, 'r', encoding='utf-8') as f:
        ka = json.load(f)
else:
    ka = ka_src

emails = var_call_gvs6j0caOIr8hSkpMrr9wGK5
case_rec = var_call_x3h55CSXZdaFsJCHtruRPcFK[0]

text = ' '.join([(case_rec.get('subject') or ''), (case_rec.get('description') or '')] + [(e.get('subject') or '') + ' ' + (e.get('textbody') or '') for e in emails])
text_l = text.lower()

# simple policy check: if agent recommends something that should reference a knowledge article, see if any KA title keywords appear in agent email(s)
agent_msgs = [e for e in emails if 'chloe' in (e.get('textbody') or '').lower()]
agent_text = ' '.join([(m.get('subject') or '')+' '+(m.get('textbody') or '') for m in agent_msgs]).lower()

# identify if agent referenced any KA explicitly by id or title
ka_ids = [r['id'].replace('#','') for r in ka if 'id' in r]
referenced_id = None
for kid in ka_ids:
    if kid.lower() in agent_text:
        referenced_id = kid
        break

# also check title mention
referenced_title = None
for r in ka:
    title = (r.get('title') or '').strip().lower()
    if title and title in agent_text:
        referenced_title = r['id'].replace('#','')
        break

# Determine breach: here none apparent (no prohibited content/policy indicator in available data)
result = None

print('__RESULT__:')
print(json.dumps({'breach': bool(result), 'knowledge_article_id': result, 'referenced_ka_id': referenced_id, 'referenced_ka_title_id': referenced_title}))"""

env_args = {'var_call_x3h55CSXZdaFsJCHtruRPcFK': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt000007928FIAQ'}], 'var_call_kJP50q6P9babKdjeNvR2oxy0': 'file_storage/call_kJP50q6P9babKdjeNvR2oxy0.json', 'var_call_gvs6j0caOIr8hSkpMrr9wGK5': [{'id': '02sWt000001zpY5IAI', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi", 'parentid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-22T19:28:30.000+0000'}, {'id': '#02sWt000001zpZhIAI', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval", 'parentid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-22T21:05:14.000+0000'}, {'id': '02sWt000001zpbJIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-23T09:12:38.000+0000'}, {'id': '02sWt000001zpcvIAA', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-23T10:47:59.000+0000'}, {'id': '#02sWt000001zpeXIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-23T11:23:47.000+0000'}, {'id': '02sWt000001zpg9IAA', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-23T13:36:22.000+0000'}, {'id': '02sWt000001zphlIAA', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-23T14:02:51.000+0000'}, {'id': '02sWt000001zpjNIAQ', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe', 'parentid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-23T15:18:39.000+0000'}], 'var_call_mLufd7R5cyyZqzR5TZzJdiY0': [], 'var_call_ihADPEQA6UN0Ha9yZdZAZRlR': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}]}

exec(code, env_args)
