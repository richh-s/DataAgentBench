code = """import json, re
from pathlib import Path

case = var_call_FspAyHAzwjyr2mbxf8f0PMuk[0]
case_text = (case.get('subject','') or '') + '\n' + (case.get('description','') or '')

path = Path(var_call_eDalqibTL5jeR0DJzAmRaviG)
articles = json.loads(path.read_text())

violation_id = None

for art in articles:
    text = (art.get('faq_answer__c','') or '') + '\n' + (art.get('summary','') or '')
    if re.search(r"scalability", text, re.IGNORECASE):
        violation_id = art['id']
        break

result = json.dumps(violation_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_FspAyHAzwjyr2mbxf8f0PMuk': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'}], 'var_call_eDalqibTL5jeR0DJzAmRaviG': 'file_storage/call_eDalqibTL5jeR0DJzAmRaviG.json'}

exec(code, env_args)
