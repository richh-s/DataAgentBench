code = """import json, re
import pandas as pd

path_docs = var_call_qLY4kovmeVVWQw7Djd9fp8jg
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def extract_year(text):
    m = re.search(r"\b(20\d{2})\b", text)
    return int(m.group(1)) if m else None

def extract_contribution(text):
    m = re.search(r"\bcontribution\s*[:\-]\s*([^\n\r]+)", text, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip().lower()
    empirical_pat = r"\b(we (conducted|ran|performed) (a |an )?(study|experiment|field trial|survey)|participants?\b|interviews?\b|questionnaire\b|randomized trial|user study|evaluat)"
    if re.search(empirical_pat, text, flags=re.IGNORECASE):
        return 'empirical'
    return None

rows=[]
for d in docs:
    fn=d.get('filename','')
    title=fn[:-4] if fn.lower().endswith('.txt') else fn
    text=d.get('text','') or ''
    year=extract_year(text)
    contrib=extract_contribution(text)
    rows.append({'title':title,'year':year,'contribution':contrib})

df_papers=pd.DataFrame(rows)
emp = df_papers[(df_papers['year'].notna()) & (df_papers['year']>2016) & (df_papers['contribution'].fillna('').str.contains('empirical', case=False, na=False))]

path_cit = var_call_XQb1EiywazFEasQRobCxYvZX
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

df_cit=pd.DataFrame(cits)
df_cit['citation_count']=pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

cit_tot=df_cit.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})

out = emp.merge(cit_tot, on='title', how='left')
out['total_citations']=out['total_citations'].fillna(0).astype(int)

out = out[['title','total_citations']].drop_duplicates().sort_values(['total_citations','title'], ascending=[False, True])

print('__RESULT__:')
print(json.dumps(out.to_dict(orient='records')))"""

env_args = {'var_call_JBeCxfLzyReF2go1FrqeJmC6': 'file_storage/call_JBeCxfLzyReF2go1FrqeJmC6.json', 'var_call_XQb1EiywazFEasQRobCxYvZX': 'file_storage/call_XQb1EiywazFEasQRobCxYvZX.json', 'var_call_qLY4kovmeVVWQw7Djd9fp8jg': 'file_storage/call_qLY4kovmeVVWQw7Djd9fp8jg.json'}

exec(code, env_args)
