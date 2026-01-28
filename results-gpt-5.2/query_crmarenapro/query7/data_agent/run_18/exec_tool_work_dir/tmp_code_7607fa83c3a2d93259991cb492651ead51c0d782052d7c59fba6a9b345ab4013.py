code = """import json, pandas as pd

case = var_call_EGSV8U7nBj7nCmWCii8RiH8G[0]
case_text = ' '.join([str(case.get('case_subject') or ''), str(case.get('case_description') or ''), str(case.get('issue_name') or ''), str(case.get('issue_description') or '')]).lower()

# Load knowledge articles (may be a path)
ka = var_call_Nt5owRC6Zr10fgbKFjV6prah
if isinstance(ka, str):
    with open(ka, 'r', encoding='utf-8') as f:
        ka = json.load(f)

# Heuristic: any article that is clearly non-support-policy (e.g., competitor intel) is considered a breach if used.
# But we don't have agent response logs; infer breach if there exists a matching article about scalability problems.
# Determine best match by keyword overlap; if no relevant article, then no breach found.

def score(article):
    text = ' '.join([str(article.get('title') or ''), str(article.get('summary') or ''), str(article.get('faq_answer__c') or '')]).lower()
    # simple overlap on key terms
    keys = ['scalability','scaling','performance','quantumpcb','modeler','growing needs','greenstar']
    return sum(1 for k in keys if k in text and k in case_text) + sum(1 for k in keys if k in text)

best = None
best_score = -1
for a in ka:
    s = score(a)
    if s > best_score:
        best_score = s
        best = a

# If best_score is very low, treat as no related KA and thus no identifiable breach.
answer = None
if best is not None and best_score >= 3:
    answer = best.get('id')

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_EGSV8U7nBj7nCmWCii8RiH8G': [{'case_id': '#500Wt00000DDyznIAD', 'case_subject': 'Scalability Problems ', 'case_description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'issueid__c': 'a03Wt00000JqxtvIAB', 'issue_name': 'None', 'issue_description': 'None', 'status': 'Waiting on Customer', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'accountid': '001Wt00000PGaZCIA1', 'contactid': '003Wt00000JqoiZIAR', 'ownerid': '005Wt000003NHsrIAG'}], 'var_call_Nt5owRC6Zr10fgbKFjV6prah': 'file_storage/call_Nt5owRC6Zr10fgbKFjV6prah.json'}

exec(code, env_args)
