code = """import json, re, pandas as pd

def load_maybe_file(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

papers = load_maybe_file(var_call_CdnT7hLvpQ5OX71dQJ2VwPil)
cits = load_maybe_file(var_call_kLK4Fvc4jPN4vyEpRhI7i9Io)

def infer_year(text):
    if not text:
        return None
    m = re.search(r'\b(20\d{2}|19\d{2})\b', text)
    if not m:
        return None
    y = int(m.group(1))
    if 1980 <= y <= 2026:
        return y
    return None

def has_empirical(doc_text):
    if not doc_text:
        return False
    t = doc_text.lower()
    return ('empirical' in t) or ('user study' in t) or ('we conducted' in t and 'study' in t) or ('participants' in t)

rows = []
for d in papers:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    year = infer_year(d.get('text',''))
    if year is None or year <= 2016:
        continue
    if not has_empirical(d.get('text','')):
        continue
    rows.append({'title': title, 'year': year})

df_p = pd.DataFrame(rows).drop_duplicates(subset=['title'])
df_c = pd.DataFrame(cits)
if not df_c.empty:
    df_c['total_citations'] = pd.to_numeric(df_c['total_citations'], errors='coerce').fillna(0).astype(int)

out = df_p.merge(df_c, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_CdnT7hLvpQ5OX71dQJ2VwPil': 'file_storage/call_CdnT7hLvpQ5OX71dQJ2VwPil.json', 'var_call_kLK4Fvc4jPN4vyEpRhI7i9Io': 'file_storage/call_kLK4Fvc4jPN4vyEpRhI7i9Io.json'}

exec(code, env_args)
