code = """import json, re, pandas as pd

# docs
path_docs = var_call_bcXU1gAR7JWAJROBDk0vKr2G
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

venue_year_re = re.compile(r"\b(?:CHI|UbiComp|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['’](\d{2})\b", re.IGNORECASE)
year_re = re.compile(r"\b(19\d{2}|20\d{2})\b")

def extract_year(text):
    text = text or ''
    m = venue_year_re.search(text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy <= 30 else 1900 + yy
    m2 = re.search(r"Copyright\s+(\d{4})", text, re.IGNORECASE)
    if m2:
        return int(m2.group(1))
    head = text[:800]
    years = [int(y) for y in year_re.findall(head) if 1990 <= int(y) <= 2026]
    return min(years) if years else None

def has_domain_physical_activity(text):
    t = (text or '').lower()
    return ('physical activity' in t) or ('activity tracker' in t) or ('activity tracking' in t)

papers=[]
for d in docs:
    title = d.get('filename','').rsplit('.txt',1)[0]
    year = extract_year(d.get('text',''))
    if year == 2016 and has_domain_physical_activity(d.get('text','')):
        papers.append({'title': title})

papers_df = pd.DataFrame(papers)
if not papers_df.empty:
    papers_df = papers_df.drop_duplicates(subset=['title'])

# citations
path_cit = var_call_lQPvr4jLWcuGx4GMacVkBaZm
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)

cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)
cit_tot = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})

if papers_df.empty:
    result = []
else:
    out = papers_df.merge(cit_tot, on='title', how='left')
    out['total_citations'] = out['total_citations'].fillna(0).astype(int)
    out = out.sort_values(['total_citations','title'], ascending=[False, True])
    result = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps({'count': len(result), 'records': result[:50]}))"""

env_args = {'var_call_TfX9M9enUCk4BvRhLnewUTBq': 'file_storage/call_TfX9M9enUCk4BvRhLnewUTBq.json', 'var_call_lQPvr4jLWcuGx4GMacVkBaZm': 'file_storage/call_lQPvr4jLWcuGx4GMacVkBaZm.json', 'var_call_bcXU1gAR7JWAJROBDk0vKr2G': 'file_storage/call_bcXU1gAR7JWAJROBDk0vKr2G.json', 'var_call_scRgKCZJVRGv0wCiP5y7Zsiq': {'columns': ['title', 'citation_count', 'citation_year'], 'head': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}]}, 'var_call_WptAeGbbAZsjoJGDAUYlgUeH': {'columns': ['title'], 'head': [{'title': 'A Lived Informatics Model of Personal Informatics'}, {'title': 'A Stage-based Model of Personal Informatics Systems'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection'}]}}

exec(code, env_args)
