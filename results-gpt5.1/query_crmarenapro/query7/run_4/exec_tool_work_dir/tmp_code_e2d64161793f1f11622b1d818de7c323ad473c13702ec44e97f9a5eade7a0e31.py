code = """import json, re, pandas as pd

case = var_call_BSPs3DfPBblrxInKdTu98IKY[0]
case_text = (case.get('subject','') or '') + '\n' + (case.get('description','') or '')

path = var_call_NkPMYjTQPMvSZZtEmkZR91fn
with open(path, 'r') as f:
    articles = json.load(f)

best_id = None
best_score = 0

case_words = set(re.findall(r"[a-zA-Z0-9']+", case_text.lower()))

for art in articles:
    text = (art.get('title','') or '') + '\n' + (art.get('faq_answer__c','') or '') + '\n' + (art.get('summary','') or '')
    art_words = set(re.findall(r"[a-zA-Z0-9']+", text.lower()))
    overlap = len(case_words & art_words)
    if overlap > best_score:
        best_score = overlap
        best_id = art.get('id')

result = best_id if best_score > 0 else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BSPs3DfPBblrxInKdTu98IKY': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'}], 'var_call_NkPMYjTQPMvSZZtEmkZR91fn': 'file_storage/call_NkPMYjTQPMvSZZtEmkZR91fn.json'}

exec(code, env_args)
