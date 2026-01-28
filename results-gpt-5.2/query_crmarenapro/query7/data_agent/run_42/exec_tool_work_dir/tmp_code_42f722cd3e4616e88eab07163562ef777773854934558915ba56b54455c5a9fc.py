code = """import json, pandas as pd

case = var_call_jqfkUgzv2qRQjbU0Xy24Mjpm[0]

# Load knowledge articles (may be file path)
ka_raw = var_call_QjzONP1LY86vdaFqI5hfe1Mt
if isinstance(ka_raw, str):
    with open(ka_raw, 'r', encoding='utf-8') as f:
        ka_list = json.load(f)
else:
    ka_list = ka_raw

emails = var_call_xjnWusNGXXsGHlAQgwpu5v33
issue = var_call_0A30HVld1q3r08XeBmq7Zre5

texts = []
for x in [case.get('subject'), case.get('description')]:
    if x and x != 'None':
        texts.append(str(x))
for em in emails:
    tb = em.get('textbody')
    if tb and tb != 'None':
        texts.append(str(tb))
for i in issue:
    d = i.get('description__c')
    if d and d != 'None':
        texts.append(str(d))

full = "\n".join(texts).lower()

# Heuristic: breach if agent recommended something that conflicts with a knowledge article.
# Only explicit policy-like article available: volume-based installation timeline policy.
# If agent promised 2-3 weeks or set schedule without referencing/aligning with that policy => potential breach.
# Identify article by title match.
violated_id = None
for ka in ka_list:
    title = (ka.get('title') or '').strip().lower()
    if 'installation timeline policy' in title:
        # Check if agent discussed timelines/scheduling
        if any(k in full for k in ['2-3 weeks','scheduled','september 27','timeline','implementation takes']):
            violated_id = ka.get('id')
            break

print('__RESULT__:')
print(json.dumps(violated_id))"""

env_args = {'var_call_jqfkUgzv2qRQjbU0Xy24Mjpm': [{'case_id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt000007928FIAQ', 'accountid': '001Wt00000PGaZCIA1', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer', 'priority': 'High'}], 'var_call_QjzONP1LY86vdaFqI5hfe1Mt': 'file_storage/call_QjzONP1LY86vdaFqI5hfe1Mt.json', 'var_call_xjnWusNGXXsGHlAQgwpu5v33': [{'id': '02sWt000001zpbJIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid', 'messagedate': '2022-09-23T09:12:38.000+0000'}, {'id': '02sWt000001zpY5IAI', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi", 'messagedate': '2022-09-22T19:28:30.000+0000'}, {'id': '#02sWt000001zpZhIAI', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval", 'messagedate': '2022-09-22T21:05:14.000+0000'}, {'id': '02sWt000001zpcvIAA', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe", 'messagedate': '2022-09-23T10:47:59.000+0000'}, {'id': '02sWt000001zpg9IAA', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe", 'messagedate': '2022-09-23T13:36:22.000+0000'}, {'id': '#02sWt000001zpeXIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid', 'messagedate': '2022-09-23T11:23:47.000+0000'}, {'id': '02sWt000001zphlIAA', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid', 'messagedate': '2022-09-23T14:02:51.000+0000'}, {'id': '02sWt000001zpjNIAQ', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe', 'messagedate': '2022-09-23T15:18:39.000+0000'}], 'var_call_A0uME2RCIwTQIRwMp22XMC6g': [], 'var_call_baD89vErfp50zlC1vBepJPIQ': [{'id': 'a04Wt00000535bOIAQ', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': 'a04Wt00000537V8IAI', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}], 'var_call_0A30HVld1q3r08XeBmq7Zre5': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}]}

exec(code, env_args)
