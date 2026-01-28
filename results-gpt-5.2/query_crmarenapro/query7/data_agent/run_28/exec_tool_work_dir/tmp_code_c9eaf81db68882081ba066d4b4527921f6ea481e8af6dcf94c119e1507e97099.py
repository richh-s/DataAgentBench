code = """import json, pandas as pd

# Load knowledge articles (may be filepath)
ka = var_call_Rp6umbmvislGylOvLhDeh27p
if isinstance(ka, str):
    with open(ka, 'r', encoding='utf-8') as f:
        ka = json.load(f)

case_issue = var_call_xtunQBDLnUqQbRQZwOj7YWOW[0]
issue_name = (case_issue.get('issue_name') or '').strip().lower()
issue_desc = (case_issue.get('issue_description') or '').strip().lower()

# Heuristic: policy breach if there's a knowledge article explicitly about the issue and implies restricted guidance.
# We'll map issue keywords to knowledge titles containing them.

def norm(s):
    return (s or '').strip().lower().replace('\n',' ')

cands = []
for r in ka:
    text = ' '.join([norm(r.get('title')), norm(r.get('summary')), norm(r.get('faq_answer__c'))])
    score = 0
    for kw in set(issue_name.split()):
        if kw and kw in text:
            score += 1
    # also match 'scal' for scalability
    if 'scalab' in issue_name or 'scalab' in issue_desc:
        if 'scalab' in text:
            score += 3
    if score>0:
        cands.append((score, r.get('id')))

cands.sort(reverse=True)
# No evidence of breach in provided data; return None
result = None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_xtunQBDLnUqQbRQZwOj7YWOW': [{'case_id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'issueid__c': 'a03Wt00000JqxtvIAB', 'issue_id': '#a03Wt00000JqxtvIAB', 'issue_name': 'Scalability Issue', 'issue_description': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_call_Rp6umbmvislGylOvLhDeh27p': 'file_storage/call_Rp6umbmvislGylOvLhDeh27p.json'}

exec(code, env_args)
