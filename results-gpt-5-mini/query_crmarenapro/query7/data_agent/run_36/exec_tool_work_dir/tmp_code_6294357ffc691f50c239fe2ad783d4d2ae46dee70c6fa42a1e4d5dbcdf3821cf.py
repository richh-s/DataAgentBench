code = """import json
from pathlib import Path

# Load knowledge articles from the JSON file path stored in var_call_fbAfNZ10WHKFEzaRx4mUDOu8
kp = Path(var_call_fbAfNZ10WHKFEzaRx4mUDOu8)
with kp.open('r', encoding='utf-8') as f:
    k_articles = json.load(f)

# Load emails and case
emails = var_call_Od21qY6ReJvA8rBFeZ3uRrdn
cases = var_call_kuO9EFzbBd9yJd9v3e7Cph3m

# Combine email bodies and case description/subject to form text to match
combined_texts = []
for e in emails:
    combined_texts.append((e.get('fromaddress'), e.get('textbody'), e.get('subject')))
for c in cases:
    combined_texts.append(('case', c.get('description',''), c.get('subject','')))

# Keywords to search for
keywords = ['Scalability Enhancement Package', 'Scalability Enhancement', 'scalability', 'QuantumPCB', '2-3 weeks', 'implementation takes about 2-3 weeks']

# Find knowledge articles containing any of the keywords in title or faq_answer__c or summary
matched = []
for art in k_articles:
    text = ' '.join([str(art.get('title','') or ''), str(art.get('faq_answer__c','') or ''), str(art.get('summary','') or '')]).lower()
    for kw in keywords:
        if kw.lower() in text:
            matched.append({'id': art.get('id'), 'title': art.get('title'), 'matched_keyword': kw})
            break

# Additionally check for high similarity between Chloe's email texts and article texts via simple substring matching
chloe_texts = [e['textbody'] for e in emails if e.get('fromaddress','').lower().startswith('chloe') or e.get('fromaddress','').lower().endswith('@techagents.com')]
for art in k_articles:
    art_text = (art.get('faq_answer__c','') or '').strip()
    for ct in chloe_texts:
        if len(art_text) > 50 and art_text[:50] in ct:
            matched.append({'id': art.get('id'), 'title': art.get('title'), 'matched_keyword': 'chloe_email_substring'})
            break

# Deduplicate
unique_matched = {m['id']: m for m in matched}.values()
result_ids = [m['id'] for m in unique_matched]

# If none matched, return None
out = result_ids if result_ids else None

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_haE969pABfd9lKu8byucZSTV': [], 'var_call_kuO9EFzbBd9yJd9v3e7Cph3m': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'ownerid': '005Wt000003NHsrIAG', 'accountid': '001Wt00000PGaZCIA1', 'issueid__c': 'a03Wt00000JqxtvIAB'}], 'var_call_Od21qY6ReJvA8rBFeZ3uRrdn': [{'id': '02sWt000001zpbJIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'relatedtoid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-23T09:12:38.000+0000'}, {'id': '02sWt000001zpY5IAI', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'relatedtoid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-22T19:28:30.000+0000'}, {'id': '#02sWt000001zpZhIAI', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'relatedtoid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-22T21:05:14.000+0000'}, {'id': '02sWt000001zpcvIAA', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'relatedtoid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-23T10:47:59.000+0000'}, {'id': '02sWt000001zpg9IAA', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'relatedtoid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-23T13:36:22.000+0000'}, {'id': '#02sWt000001zpeXIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'relatedtoid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-23T11:23:47.000+0000'}, {'id': '02sWt000001zphlIAA', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'relatedtoid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-23T14:02:51.000+0000'}, {'id': '02sWt000001zpjNIAQ', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'relatedtoid': '500Wt00000DDyznIAD', 'messagedate': '2022-09-23T15:18:39.000+0000'}], 'var_call_fbAfNZ10WHKFEzaRx4mUDOu8': 'file_storage/call_fbAfNZ10WHKFEzaRx4mUDOu8.json'}

exec(code, env_args)
