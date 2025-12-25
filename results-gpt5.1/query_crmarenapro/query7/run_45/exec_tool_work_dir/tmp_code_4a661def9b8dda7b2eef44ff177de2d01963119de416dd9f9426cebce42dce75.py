code = """import json
import pandas as pd

# Load full knowledge articles from file
path = var_call_JjQqBIxhtUmY0wMDKlUwtqa5
with open(path, 'r') as f:
    knowledge = json.load(f)

# Convert to DataFrame for simple scanning
df = pd.DataFrame(knowledge)

case_subject = 'Scalability Problems'.strip().lower()
case_description = 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'.strip().lower()

# Look for likely relevant article based on keywords
keywords = ['scalability', 'scalable', 'scaling', 'performance', 'quantumpcb']

def score_article(row):
    text = ((row.get('title') or '') + ' ' + (row.get('summary') or '') + ' ' + (row.get('faq_answer__c') or '')).lower()
    score = 0
    for kw in keywords:
        if kw in text:
            score += 1
    return score

if not df.empty:
    df['score'] = df.apply(score_article, axis=1)
    top = df.sort_values('score', ascending=False).head(1)
    best = top.iloc[0]
    # Assume a breach only if there is an article clearly about scalability issues and proposed package
    if best['score'] >= 3 and 'scalability enhancement package' in (best.get('faq_answer__c') or '').lower():
        result = best['id']
    else:
        result = None
else:
    result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_qLS1JSv7X6p8mYe2jwpvJvFG': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_call_Lh12toDu5KT0iVT2Gi417fhD': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_call_yjIx53T5Lgm4GolGfyk3fbfV': [{'id': '02sWt000001zpbJIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for the quick response. The Scalability Enhancement Package sounds promising. Could you please let me know the expected duration for the implementation and any potential downtime this might cause?\\n\\nLooking forward to your feedback.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-23T09:12:38.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpY5IAI', 'subject': 'Issue with Scaling QuantumPCB Modeler   ', 'textbody': "Hi Chloe,\\n\\nI hope this message finds you well. I'm reaching out regarding some scalability issues we're experiencing with the QuantumPCB Modeler. As our needs at GreenStar Electronics continue to grow, we've found the current setup insufficient to handle our increasing workload efficiently. Could you please assist us in addressing this problem?\\n\\nBest,\\nDavid Nkosi", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-22T19:28:30.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '#02sWt000001zpZhIAI', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': "Hello David,\\n\\nThank you for reaching out to us. I understand how crucial it is to have a scalable solution in place. I recommend implementing the Scalability Enhancement Package, which is specifically designed to boost system scalability and ensure seamless performance. I'll begin the preliminary assessments to tailor this package to your needs at GreenStar Electronics.\\n\\nI will keep you updated on the progress.\\n\\nBest regards,\\nChloe Duval", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-22T21:05:14.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpcvIAA', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler  ', 'textbody': "Hello David,\\n\\nI am glad to hear you're interested in the Scalability Enhancement Package. Typically, implementation takes about 2-3 weeks, but I will collaborate with our team to expedite the process for you. As for downtime, we'll ensure that disruptions are minimized — possibly scheduling updates during off-peak times to avoid impact. I will keep you informed on the scheduled timelines after coordinating with the implementation team.\\n\\nBest,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-23T10:47:59.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpg9IAA', 'subject': 'Scheduled Implementation for Scalability Enhancement  ', 'textbody': "Hi David,\\n\\nI'm pleased to inform you that the implementation for the Scalability Enhancement Package is scheduled to start on September 27th. Our team will manage the integration process during the evening to mitigate any impact. Please let me know if this schedule works for you or if adjustments are needed.\\n\\nBest regards,\\nChloe", 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-23T13:36:22.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '#02sWt000001zpeXIAQ', 'subject': 'Re: Issue with Scaling QuantumPCB Modeler', 'textbody': 'Hi Chloe,\\n\\nThank you for outlining the timeline and approach. Coordinating updates during off-peak hours would be ideal for minimizing business disruptions. I appreciate your assistance and will await further updates on the schedule.\\n\\nRegards,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-23T11:23:47.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zphlIAA', 'subject': 'Re: Scheduled Implementation for Scalability Enhancement   ', 'textbody': 'Hi Chloe,\\n\\nThe proposed schedule seems great. Thank you for organizing this promptly. Please proceed as planned and keep me updated on any developments.\\n\\nBest,\\nDavid', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'david.nkosi@greenstarelectronics.com', 'toids': '["005Wt000003NHsrIAG"]', 'messagedate': '2022-09-23T14:02:51.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}, {'id': '02sWt000001zpjNIAQ', 'subject': 'Final Confirmation and Next Steps', 'textbody': 'Hello David,\\n\\nJust confirming the final arrangements for the Scalability Enhancement implementation. We will initiate the process on September 27th and aim to complete it swiftly with minimal interruption. Our support team will be available throughout to assist with any queries.\\n\\nFeel free to reach out if you have any concerns.\\n\\nWarm regards,\\nChloe', 'parentid': '500Wt00000DDyznIAD', 'fromaddress': 'chloe.duval@techagents.com', 'toids': '["003Wt00000JqoiZIAR"]', 'messagedate': '2022-09-23T15:18:39.000+0000', 'relatedtoid': '500Wt00000DDyznIAD'}], 'var_call_RT41jDNyowfCW5qzoA9Uiaf2': [], 'var_call_8kmVlt6QThSLuU0hQgvNougX': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_call_JjQqBIxhtUmY0wMDKlUwtqa5': 'file_storage/call_JjQqBIxhtUmY0wMDKlUwtqa5.json'}

exec(code, env_args)
