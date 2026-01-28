code = """import json, pandas as pd

# load full knowledge if stored as file path
kb = var_call_JLIF3RQWq21QVoiLoq6MaVJy
if isinstance(kb, str):
    with open(kb, 'r', encoding='utf-8') as f:
        kb = json.load(f)

case = var_call_hF0iqG1Jl1IHlGcqKjmypjGH[0]
text = ' '.join([str(case.get('subject','') or ''), str(case.get('description','') or ''), str(case.get('issue_name','') or ''), str(case.get('issue_description','') or '')]).lower()

matches = []
for art in kb:
    blob = ' '.join([str(art.get('title','') or ''), str(art.get('summary','') or ''), str(art.get('faq_answer__c','') or ''), str(art.get('urlname','') or '')]).lower()
    # naive policy breach detection: if article content references same product/issue keywords
    if ('scalab' in blob) and ('scalab' in text) and ('quantumpcb' in text or 'quantumpcb' in blob):
        matches.append(art.get('id'))

result = None
if matches:
    # return first match
    result = matches[0]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hF0iqG1Jl1IHlGcqKjmypjGH': [{'case_id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'issueid__c': 'a03Wt00000JqxtvIAB', 'issue_name': 'None', 'issue_description': 'None'}], 'var_call_JLIF3RQWq21QVoiLoq6MaVJy': 'file_storage/call_JLIF3RQWq21QVoiLoq6MaVJy.json'}

exec(code, env_args)
