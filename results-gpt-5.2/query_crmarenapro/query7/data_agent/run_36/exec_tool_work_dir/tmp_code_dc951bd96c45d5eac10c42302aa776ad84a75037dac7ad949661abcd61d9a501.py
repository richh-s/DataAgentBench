code = """import json, pandas as pd
from pathlib import Path

case = pd.DataFrame(var_call_cFCmHeQ8wTKzduwJhiyefCTB)
issue_name = (case.loc[0,'issue_name'] if not case.empty else '')
issue_desc = (case.loc[0,'issue_description'] if not case.empty else '')
case_text = ' '.join([str(case.loc[0,'subject']), str(case.loc[0,'description']), str(issue_name), str(issue_desc)]).lower()

# load knowledge articles
p = Path(var_call_ra0VN0CHM56c2AtVANHmIfzP)
arts = json.loads(p.read_text())
df = pd.DataFrame(arts)

# heuristic: look for policy/breach/violation language and match to relevant issue keywords
text_cols = ['title','summary','faq_answer__c']
for col in text_cols:
    if col not in df.columns:
        df[col] = ''

def score_row(r):
    blob = (' '.join([str(r.get('title','')), str(r.get('summary','')), str(r.get('faq_answer__c',''))])).lower()
    # base relevance to case: overlap on key tokens
    tokens = set([t for t in ['scalability','scale','enterprise','performance','growing','demands'] if t in case_text])
    rel = sum(1 for t in tokens if t in blob)
    # policy indicator
    pol = int(any(k in blob for k in ['policy','violation','breach','compliance','acceptable use','terms']))
    return rel + 2*pol

df['score'] = df.apply(score_row, axis=1)

# if there is no clear policy article, return None
best = df.sort_values(['score'], ascending=False).head(1)
answer = None
if not best.empty and int(best.iloc[0]['score'])>=2 and any(k in (' '.join([str(best.iloc[0][c]) for c in text_cols])).lower() for k in ['policy','violation','breach']):
    answer = best.iloc[0]['id']

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_cFCmHeQ8wTKzduwJhiyefCTB': [{'case_id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt000007928FIAQ', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer', 'issue_id': '#a03Wt00000JqxtvIAB', 'issue_name': 'Scalability Issue', 'issue_description': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_call_ra0VN0CHM56c2AtVANHmIfzP': 'file_storage/call_ra0VN0CHM56c2AtVANHmIfzP.json'}

exec(code, env_args)
