code = """import json, pandas as pd

# load knowledge articles
path = var_call_xZKxB5pbBaPsgAWkZJbIULMK
with open(path,'r',encoding='utf-8') as f:
    kav = json.load(f)

def norm(s):
    if s is None:
        return ''
    return str(s).strip().lower()

case = var_call_dxJRkD8xioTfo6Ecv5VkJkKs[0]
subj = norm(case.get('subject'))
desc = norm(case.get('description'))

hits = []
for a in kav:
    tid = a.get('id')
    title = norm(a.get('title'))
    summ = norm(a.get('summary'))
    ans = norm(a.get('faq_answer__c'))
    # simple relevance: title words in case or vice versa
    score = 0
    for field in (title, summ, ans):
        if subj and subj in field:
            score += 3
        if field and field in desc:
            score += 2
    if score>0:
        hits.append((score, tid, a.get('title')))

hits_sorted = sorted(hits, reverse=True)[:20]
print('__RESULT__:')
print(json.dumps({'case': {'id': case.get('id'), 'subject': case.get('subject'), 'description': case.get('description')}, 'top_hits': hits_sorted}))"""

env_args = {'var_call_dxJRkD8xioTfo6Ecv5VkJkKs': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt000007928FIAQ'}], 'var_call_xZKxB5pbBaPsgAWkZJbIULMK': 'file_storage/call_xZKxB5pbBaPsgAWkZJbIULMK.json'}

exec(code, env_args)
