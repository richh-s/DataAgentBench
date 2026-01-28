code = """import json
# Load the knowledge articles result file and email messages from storage variables
kb_file = var_call_A7NlrLqBkP6FGLJ8h0pRcXWo
with open(kb_file, 'r', encoding='utf-8') as f:
    kb = json.load(f)
emails = var_call_qWAahbFJbAwWZNFw9mOvbK6u

# Normalize texts
def norm(s):
    if s is None:
        return ''
    return ' '.join(s.split()).lower()

emails_texts = [norm(e.get('textbody','') + ' ' + e.get('subject','')) for e in emails]

# Search KB for articles mentioning scalability or the phrase 'Scalability Enhancement Package'
candidates = []
for a in kb:
    faq = norm(a.get('faq_answer__c',''))
    title = norm(a.get('title',''))
    summary = norm(a.get('summary',''))
    combined = faq + ' ' + title + ' ' + summary
    if 'scalab' in combined or 'scalability' in combined or 'scalability enhancement' in combined or 'scalability enhancement package' in combined:
        candidates.append(a)

# Check if any candidate's text is substantially present in agent emails (fromaddress contains chloe.duval)
breached_ids = []
for c in candidates:
    c_text = norm(c.get('faq_answer__c','') + ' ' + c.get('summary','') + ' ' + c.get('title',''))
    for e in emails:
        fromaddr = (e.get('fromaddress') or '').lower()
        if 'chloe.duval' in fromaddr:  # agent messages
            e_text = norm(e.get('textbody','') + ' ' + e.get('subject',''))
            # if the email mentions Scalability Enhancement Package and KB mentions scalability, consider breach
            if 'scalability enhancement package' in e_text and 'scalability' in c_text:
                breached_ids.append(c.get('id'))
            else:
                # fallback: check if a significant substring from KB appears in email
                # take first 60 chars of kb faq
                snippet = c_text[:120]
                if snippet and snippet in e_text:
                    breached_ids.append(c.get('id'))

# Deduplicate
breached_ids = list(dict.fromkeys(breached_ids))

# If none found, return None
out = breached_ids[0] if breached_ids else None
import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_5S8yJxACJV0mUn1ecpqhCezA': [], 'var_call_uIXaTv4CCC6PJHPZuKahAMF1': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'ownerid': '005Wt000003NHsrIAG'}], 'var_call_V55kM0hQM9ybBXEWv2zpG8o5': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_call_A7NlrLqBkP6FGLJ8h0pRcXWo': 'file_storage/call_A7NlrLqBkP6FGLJ8h0pRcXWo.json', 'var_call_XWTAy6FbZfA0xkPEX4IwXdJa': [], 'var_call_qWAahbFJbAwWZNFw9mOvbK6u': [{'id': '02sWt000001zpbJIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-23T09:12:38.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpY5IAI', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-22T19:28:30.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '#02sWt000001zpZhIAI', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-22T21:05:14.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpcvIAA', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-23T10:47:59.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpg9IAA', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-23T13:36:22.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '#02sWt000001zpeXIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-23T11:23:47.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zphlIAA', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-23T14:02:51.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpjNIAQ', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-23T15:18:39.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}]}

exec(code, env_args)
