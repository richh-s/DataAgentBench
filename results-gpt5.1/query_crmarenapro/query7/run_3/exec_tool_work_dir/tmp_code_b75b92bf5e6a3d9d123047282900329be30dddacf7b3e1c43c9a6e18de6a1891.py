code = """import json, pandas as pd
from pathlib import Path

articles_path = var_call_36NuXYniS6b4h3HmNsSnUom4
with open(articles_path, 'r') as f:
    articles = json.load(f)

case = var_call_y8OifKJ3hSIr06UAGq8JGwFG[0]
text = (case.get('subject','') or '') + ' ' + (case.get('description','') or '')
text_lower = text.lower()

breach_id = None
for art in articles:
    title = (art.get('title','') or '').lower()
    if 'scalability' in title:
        if 'quantumpcb modeler' in text_lower or 'scaling the quantumpcb modeler' in text_lower:
            breach_id = art.get('id')
            break

result = json.dumps(breach_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_y8OifKJ3hSIr06UAGq8JGwFG': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'}], 'var_call_36NuXYniS6b4h3HmNsSnUom4': 'file_storage/call_36NuXYniS6b4h3HmNsSnUom4.json'}

exec(code, env_args)
