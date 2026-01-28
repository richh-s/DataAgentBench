code = """import json
# access the stored results
cases = var_call_EzxueTftZv9hX9hCkd0UFrSN
emails = var_call_BVUG9V4OEoTvaBiRKaWrGDuz
issue = var_call_44kSecgdySzUlcH94zUmSsxd
# knowledge list is large and stored in file path var_call_XQeuOXh6QCPVdK7IqBH1Xgt9 for first call and var_call_c5EpeG3KRCGzRHkjhYZhhPvY for later call
# We'll read the full knowledge results from those json files
import pathlib
ka1_path = var_call_XQeuOXh6QCPVdK7IqBH1Xgt9
ka2_path = var_call_c5EpeG3KRCGzRHkjhYZhhPvY
with open(ka1_path, 'r') as f:
    ka1 = json.load(f)
with open(ka2_path, 'r') as f:
    ka2 = json.load(f)
# combine knowledge articles
knowledge = ka1 + ka2
# Normalize IDs by stripping leading # and whitespace for comparison
def normalize_id(i):
    if i is None:
        return None
    return i.strip().lstrip('#')
case = cases[0] if cases else None
case_id = normalize_id(case['id']) if case else None
issue_id = normalize_id(issue[0]['id']) if issue else None
# Determine if agent breached policy: look for any knowledge article text that matches content in emails from agent (chloe.duval@techagents.com)
# Collect messages from Chloe
chloe_msgs = [e for e in emails if e.get('fromaddress','').lower()=='chloe.duval@techagents.com']
# Check if any Chloe message contains content that appears verbatim in any knowledge article faq_answer__c or title
breach_ka_id = None
for msg in chloe_msgs:
    body = msg.get('textbody','').strip()
    for ka in knowledge:
        # compare normalized texts
        faq = (ka.get('faq_answer__c') or '').strip()
        title = (ka.get('title') or '').strip()
        summary = (ka.get('summary') or '').strip()
        if body in faq or body in title or body in summary:
            breach_ka_id = normalize_id(ka.get('id'))
            break
    if breach_ka_id:
        break
# If no exact match, check for mention of 'Scalability Enhancement Package' which appears in emails and might map to KA with Scalability in content
if not breach_ka_id:
    for ka in knowledge:
        text = ' '.join([str(ka.get('faq_answer__c') or ''), str(ka.get('title') or ''), str(ka.get('summary') or '')]).lower()
        for msg in chloe_msgs:
            if 'scalability enhancement package' in msg.get('textbody','') or 'scalability enhancement package' in msg.get('textbody',''):
                if 'scalability' in text:
                    breach_ka_id = normalize_id(ka.get('id'))
                    break
        if breach_ka_id:
            break
# Output result: if breach_ka_id found, return that id else None
result = breach_ka_id if breach_ka_id else None
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NgvBOiu9DAtalZV0nagkaBoC': [], 'var_call_EzxueTftZv9hX9hCkd0UFrSN': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'issueid__c': 'a03Wt00000JqxtvIAB'}], 'var_call_XQeuOXh6QCPVdK7IqBH1Xgt9': 'file_storage/call_XQeuOXh6QCPVdK7IqBH1Xgt9.json', 'var_call_VMGBctOsZ1cVzw4TWp8Hc2Bi': [], 'var_call_44kSecgdySzUlcH94zUmSsxd': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_call_BVUG9V4OEoTvaBiRKaWrGDuz': [{'id': '02sWt000001zpbJIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'messagedate': '2022-09-23T09:12:38.000+0000'}, {'id': '02sWt000001zpY5IAI', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi", 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'messagedate': '2022-09-22T19:28:30.000+0000'}, {'id': '#02sWt000001zpZhIAI', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval", 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'messagedate': '2022-09-22T21:05:14.000+0000'}, {'id': '02sWt000001zpcvIAA', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'messagedate': '2022-09-23T10:47:59.000+0000'}, {'id': '02sWt000001zpg9IAA', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'messagedate': '2022-09-23T13:36:22.000+0000'}, {'id': '#02sWt000001zpeXIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'messagedate': '2022-09-23T11:23:47.000+0000'}, {'id': '02sWt000001zphlIAA', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'messagedate': '2022-09-23T14:02:51.000+0000'}, {'id': '02sWt000001zpjNIAQ', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe', 'parentid': '500Wt00000DDyznIAD', 'relatedtoid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'messagedate': '2022-09-23T15:18:39.000+0000'}], 'var_call_c5EpeG3KRCGzRHkjhYZhhPvY': 'file_storage/call_c5EpeG3KRCGzRHkjhYZhhPvY.json'}

exec(code, env_args)
