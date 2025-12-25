code = """import json, pandas as pd, os

# Load full knowledge articles from file path
path = var_call_p1TkD6925gBQAmP5yayJPkqO
with open(path, 'r') as f:
    knowledge = json.load(f)

# Case info
case = var_call_hzT7dOSoKf5kMLFtfxSIaGar[0]

# Very naive "policy breach" heuristic: look for knowledge articles explicitly about policy/violation/breach
violating_ids = []
for art in knowledge:
    text = ' '.join(str(art.get(k,'') or '') for k in ['title','summary','faq_answer__c']).lower()
    if 'policy' in text and ('breach' in text or 'violation' in text):
        violating_ids.append(art['id'])

# In reality we'd need explicit policy + interaction content, but dataset doesn't encode policy breaches.
result = None

print("__RESULT__:")
print(json.dumps(result) )"""

env_args = {'var_call_Rtt4nuCAGXMmZLKnr8KjKWfz': [], 'var_call_p1TkD6925gBQAmP5yayJPkqO': 'file_storage/call_p1TkD6925gBQAmP5yayJPkqO.json', 'var_call_UPenQfHw1xQUgay9NMUVRVlg': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_call_hzT7dOSoKf5kMLFtfxSIaGar': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer'}]}

exec(code, env_args)
