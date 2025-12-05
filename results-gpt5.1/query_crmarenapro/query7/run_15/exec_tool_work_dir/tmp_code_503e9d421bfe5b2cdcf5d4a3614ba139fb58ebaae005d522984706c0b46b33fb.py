code = """import json, pandas as pd
from pathlib import Path

# Load full knowledge articles
path = Path(var_call_tE8UIhQePyVM5JyyHeS9jRNM)
records = json.loads(path.read_text())

case = var_call_tTD0ddR1fxCgfmvcRUr8XJlA[0]
text = (case['subject'] or '') + ' ' + (case['description'] or '')
text_lower = text.lower()

best_id = None

for r in records:
    combined = ' '.join([str(r.get('title') or ''), str(r.get('summary') or ''), str(r.get('faq_answer__c') or '')]).lower()
    if 'scalability' in combined and 'quantumpcb modeler' in combined:
        best_id = r['id']
        break

result = best_id

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tTD0ddR1fxCgfmvcRUr8XJlA': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'}], 'var_call_tE8UIhQePyVM5JyyHeS9jRNM': 'file_storage/call_tE8UIhQePyVM5JyyHeS9jRNM.json'}

exec(code, env_args)
