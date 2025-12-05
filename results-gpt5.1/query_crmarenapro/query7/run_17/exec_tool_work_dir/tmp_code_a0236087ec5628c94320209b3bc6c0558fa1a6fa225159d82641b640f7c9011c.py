code = """import json, pandas as pd, os
path = var_call_WRMaWlLZ6cgQADp9wAb13aX5
with open(path, 'r') as f:
    articles = json.load(f)
case = var_call_7R9NUjqTcrDJweHjgwn9CL3V[0]
text = (case.get('subject','') or '') + ' ' + (case.get('description','') or '')
text_lower = text.lower()
violated_id = None
for art in articles:
    body = ' '.join([str(art.get('title','')), str(art.get('faq_answer__c','')), str(art.get('summary',''))]).lower()
    if 'scalability' in body and 'quantumpcb modeler' in body:
        violated_id = art.get('id')
        break
result = json.dumps(violated_id)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_7R9NUjqTcrDJweHjgwn9CL3V': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'}], 'var_call_WRMaWlLZ6cgQADp9wAb13aX5': 'file_storage/call_WRMaWlLZ6cgQADp9wAb13aX5.json'}

exec(code, env_args)
