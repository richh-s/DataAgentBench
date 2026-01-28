code = """import json, pandas as pd

# load case
case = pd.DataFrame(var_call_Bovwev4JYkq4f4aDKSh33x62).iloc[0].to_dict()

# load knowledge articles
ka_src = var_call_YzHWlrqTVogK11lAfsqZKHPy
if isinstance(ka_src, str) and ka_src.endswith('.json'):
    with open(ka_src, 'r', encoding='utf-8') as f:
        kas = json.load(f)
else:
    kas = ka_src

df = pd.DataFrame(kas)

# normalize text
for col in ['title','summary','faq_answer__c','urlname','id']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace('\u00a0',' ', regex=False).str.strip()

def norm(s):
    if s is None:
        return ''
    return str(s).replace('\u00a0',' ').strip().lower()

case_text = ' '.join([norm(case.get('subject')), norm(case.get('description')), norm(case.get('issue_name')), norm(case.get('issue_description'))]).strip()

# simple keyword-based breach detection: if any KA references scalability issues that match case subject/description
keywords = []
if 'scalab' in case_text:
    keywords.append('scalab')
if 'scale' in case_text:
    keywords.append('scale')
if 'quantumpcb' in case_text:
    keywords.append('quantumpcb')
if 'modeler' in case_text:
    keywords.append('modeler')

breach_id = None
if keywords:
    texts = (df.get('title','').fillna('') + ' ' + df.get('summary','').fillna('') + ' ' + df.get('faq_answer__c','').fillna('')).str.lower()
    # score by keyword hits
    scores = []
    for i, t in enumerate(texts.tolist()):
        score = sum(1 for k in keywords if k in t)
        scores.append(score)
    df['__score__'] = scores
    best = df.sort_values(['__score__'], ascending=False).head(1)
    if int(best['__score__'].iloc[0]) > 0:
        breach_id = best['id'].iloc[0]

print('__RESULT__:')
print(json.dumps({'breach_id': breach_id}))"""

env_args = {'var_call_Bovwev4JYkq4f4aDKSh33x62': [{'case_id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'issueid__c': 'a03Wt00000JqxtvIAB', 'issue_name': 'None', 'issue_description': 'None'}], 'var_call_YzHWlrqTVogK11lAfsqZKHPy': 'file_storage/call_YzHWlrqTVogK11lAfsqZKHPy.json'}

exec(code, env_args)
