code = """import json, pandas as pd, os
from pathlib import Path

path = var_call_vx7zVBiejTxQJnclrTEsHpjL
with open(path, 'r') as f:
    articles = json.load(f)

case = var_call_F6yTxm9uCQDzLPsxvkQo6gVj[0]
text = (case['subject'] or '') + ' ' + (case['description'] or '')
text_lower = text.lower()

violated_id = None
for art in articles:
    content = ' '.join([(art.get('title') or ''), (art.get('faq_answer__c') or ''), (art.get('summary') or '')]).lower()
    if 'scalability' in content and 'quantumpcb modeler' in content:
        violated_id = art['id']
        break

result = json.dumps(violated_id)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_F6yTxm9uCQDzLPsxvkQo6gVj': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'}], 'var_call_vx7zVBiejTxQJnclrTEsHpjL': 'file_storage/call_vx7zVBiejTxQJnclrTEsHpjL.json'}

exec(code, env_args)
