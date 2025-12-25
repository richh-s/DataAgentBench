code = """import json
import re
from pathlib import Path

path = var_call_meORUjSBwzFzsLEF6HdYpFxU
with open(path, 'r') as f:
    articles = json.load(f)

keywords = ['scalability', 'scalable', 'scaling', 'QuantumPCB Modeler']
pattern = re.compile('|'.join(re.escape(k) for k in keywords), re.IGNORECASE)

matched_ids = []
for art in articles:
    text = ' '.join(str(art.get(k, '')) for k in ['title', 'faq_answer__c', 'summary'])
    if pattern.search(text):
        matched_ids.append(art['id'])

result = matched_ids[:10]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MsKSuyQbL0hHZn65UQXwi35W': [{'id': '02sWt000001zpY5IAI', 'parentid': '500Wt00000DDyznIAD', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi"}, {'id': '#02sWt000001zpZhIAI', 'parentid': '500Wt00000DDyznIAD', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval"}, {'id': '02sWt000001zpbJIAQ', 'parentid': '500Wt00000DDyznIAD', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid'}, {'id': '02sWt000001zpcvIAA', 'parentid': '500Wt00000DDyznIAD', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe"}, {'id': '#02sWt000001zpeXIAQ', 'parentid': '500Wt00000DDyznIAD', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid'}, {'id': '02sWt000001zpg9IAA', 'parentid': '500Wt00000DDyznIAD', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe"}, {'id': '02sWt000001zphlIAA', 'parentid': '500Wt00000DDyznIAD', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid'}, {'id': '02sWt000001zpjNIAQ', 'parentid': '500Wt00000DDyznIAD', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe'}], 'var_call_p1ONEwoOuPNDVJbonkWo3cNX': [], 'var_call_9XuO4haeCXEtAEMeDBHm82zG': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer'}], 'var_call_meORUjSBwzFzsLEF6HdYpFxU': 'file_storage/call_meORUjSBwzFzsLEF6HdYpFxU.json'}

exec(code, env_args)
