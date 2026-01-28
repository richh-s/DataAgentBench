code = """import json, pandas as pd

# Load knowledge articles (may be in file)
ka = var_call_CgptobLyyLQEYpAjgIw9Ezdn
if isinstance(ka, str):
    with open(ka, 'r', encoding='utf-8') as f:
        ka = json.load(f)

emails = var_call_BgsefeCmWTKY3oWgDpwiN73K
case_rec = var_call_LDD65579doRF8POQynfYXPn8[0]
issue = var_call_FSxQxQNYkFWUkXgsXh2Mbd4h[0] if var_call_FSxQxQNYkFWUkXgsXh2Mbd4h else None

# Heuristic: policy breach if agent recommended something matching a KB article that is about competitors or disallowed guidance.
# We'll search for keyword overlaps between agent messages (from techagents.com) and KB titles/answers.
agent_msgs = [e for e in emails if (e.get('fromaddress') or '').endswith('@techagents.com')]
agent_text = '\n'.join([(m.get('subject') or '') + '\n' + (m.get('textbody') or '') for m in agent_msgs]).lower()

# Find KB article most related to what agent said, focusing on any explicit package / implementation promises.
# We'll compute simple score for each article.
terms = ['scalability enhancement package','enhancement package','implementation','downtime','scheduled']

def score_article(a):
    text = ((a.get('title') or '') + ' ' + (a.get('summary') or '') + ' ' + (a.get('faq_answer__c') or '')).lower()
    sc = 0
    for t in terms:
        if t in agent_text and t in text:
            sc += 5
    # general word overlap
    for w in set([w for w in agent_text.replace('\n',' ').split(' ') if len(w)>4]):
        if w in text:
            sc += 0.01
    return sc

scores = [(a.get('id'), score_article(a), a.get('title','')) for a in ka]
# pick max score
best = max(scores, key=lambda x: x[1]) if scores else (None,0,'')

# Determine violation: agent recommended a "Scalability Enhancement Package"; check if such KB exists. If none, assume no breach.
# Also consider any KB about competitor; agent didn't mention competitor. So no breach.
violation = None

# If there is a KB explicitly about "Scalability Enhancement Package" and agent deviated from it, we'd flag. Not present in KB list.
# We'll additionally search KB for 'scalability enhancement package'
matched = [a for a in ka if 'scalability enhancement package' in ((a.get('title','')+' '+a.get('summary','')+' '+a.get('faq_answer__c','')).lower())]
if matched:
    # If exists, treat as breached for recommending without proper steps; return that id.
    violation = matched[0].get('id')

out = violation if violation is not None else None
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_LDD65579doRF8POQynfYXPn8': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_call_CgptobLyyLQEYpAjgIw9Ezdn': 'file_storage/call_CgptobLyyLQEYpAjgIw9Ezdn.json', 'var_call_BgsefeCmWTKY3oWgDpwiN73K': [{'id': '02sWt000001zpbJIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-23T09:12:38.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpY5IAI', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-22T19:28:30.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '#02sWt000001zpZhIAI', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-22T21:05:14.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpcvIAA', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-23T10:47:59.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpg9IAA', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-23T13:36:22.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '#02sWt000001zpeXIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-23T11:23:47.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zphlIAA', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-23T14:02:51.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpjNIAQ', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-23T15:18:39.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}], 'var_call_bVKmkKEAhPFkerF65kVe9I4J': [], 'var_call_QmZUb50v4XhoCRRI217n9PBS': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}], 'var_call_FSxQxQNYkFWUkXgsXh2Mbd4h': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}]}

exec(code, env_args)
