code = """import json, re, pandas as pd

path_docs = var_call_bcXU1gAR7JWAJROBDk0vKr2G
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

venue_year_re = re.compile(r"\b(?:CHI|UbiComp|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['’](\d{2})\b", re.IGNORECASE)
year_re = re.compile(r"\b(19\d{2}|20\d{2})\b")

def extract_year(text):
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

rows=[]
for d in docs:
    title = d['filename'].rsplit('.txt',1)[0]
    year = extract_year(d.get('text','') or '')
    if year == 2016 and has_domain_physical_activity(d.get('text','')):
        rows.append({'title': title, 'year': year})

papers_df = pd.DataFrame(rows).drop_duplicates(subset=['title'])

path_cit = var_call_lQPvr4jLWcuGx4GMacVkBaZm
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
if not cit_df.empty:
    # normalize columns
    if 'Title' in cit_df.columns and 'title' not in cit_df.columns:
        cit_df = cit_df.rename(columns={'Title':'title'})
    if 'citationCount' in cit_df.columns and 'citation_count' not in cit_df.columns:
        cit_df = cit_df.rename(columns={'citationCount':'citation_count'})

if (not cit_df.empty) and ('title' in cit_df.columns):
    cit_df['citation_count'] = pd.to_numeric(cit_df.get('citation_count'), errors='coerce').fillna(0).astype(int)
    cit_tot = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
else:
    cit_tot = pd.DataFrame(columns=['title','total_citations'])

out = papers_df.merge(cit_tot, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TfX9M9enUCk4BvRhLnewUTBq': 'file_storage/call_TfX9M9enUCk4BvRhLnewUTBq.json', 'var_call_lQPvr4jLWcuGx4GMacVkBaZm': 'file_storage/call_lQPvr4jLWcuGx4GMacVkBaZm.json', 'var_call_bcXU1gAR7JWAJROBDk0vKr2G': 'file_storage/call_bcXU1gAR7JWAJROBDk0vKr2G.json'}

exec(code, env_args)
