code = """import json, re, pandas as pd
case = var_call_vwkHBonaEOzQLnmi8UmHwIXh[0]
case_text = (case.get('subject','') or '') + ' ' + (case.get('description','') or '')
path = var_call_j8zn0nlxwgeLJuJ6lZQN9pHp
with open(path,'r') as f:
    arts = json.load(f)
best_id = None
best_score = 0
for art in arts:
    text = ' '.join([(art.get('title') or ''), (art.get('summary') or ''), (art.get('faq_answer__c') or '')])
    score = 0
    for kw in ['scalability','scaling','performance','throughput']:
        if re.search(kw, text, re.I):
            score += 1
    if 'QuantumPCB' in text:
        score += 3
    if score > best_score:
        best_score = score
        best_id = art.get('id')
result = best_id if best_score>0 else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vwkHBonaEOzQLnmi8UmHwIXh': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'}], 'var_call_j8zn0nlxwgeLJuJ6lZQN9pHp': 'file_storage/call_j8zn0nlxwgeLJuJ6lZQN9pHp.json'}

exec(code, env_args)
