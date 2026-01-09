code = """import json, re, pandas as pd

# Load mongo docs (filename + text)
path_docs = var_call_qdz2ETJjrX8lNSJa2BWsZizN
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Heuristic extraction: year from first page patterns like "CHI '16" or "UbiComp '15" or Copyright 2016
# domain: check for 'physical activity' phrase (case-insensitive) in title/keywords/abstract/body.

def extract_year(text):
    head = text[:3000]
    m = re.search(r"\b(19|20)\d{2}\b", head)
    # better: venue short year like '16
    m2 = re.search(r"\b(?:CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|WWW|TEI|OzCHI|AH|PervasiveHealth)\s*['’](\d{2})\b", head)
    if m2:
        yy = int(m2.group(1))
        return 2000+yy if yy<80 else 1900+yy
    m3 = re.search(r"Copyright\s*(?:\(c\))?\s*(19|20)(\d{2})", head, flags=re.IGNORECASE)
    if m3:
        return int(m3.group(1)+m3.group(2))
    if m:
        y = int(m.group(0))
        if 1990 <= y <= 2026:
            return y
    return None

def is_physical_activity_domain(title, text):
    blob = (title + "\n" + text[:8000]).lower()
    return ('physical activity' in blob) or ('activity tracker' in blob) or ('activity tracking' in blob)

records=[]
for d in docs:
    fn=d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text=d.get('text','') or ''
    year=extract_year(text)
    if year==2016 and is_physical_activity_domain(title, text):
        records.append({'title': title, 'year': year})

# Load citations and compute total citations per paper (sum across all citation_years)
path_cit = var_call_iyw2z8ScA3sNOnDGG5dxTwPG
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

df_c = pd.DataFrame(cits)
if not df_c.empty:
    df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce').fillna(0).astype(int)

df_titles = pd.DataFrame(records)
if df_titles.empty:
    out=[]
else:
    df_total = df_c.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
    out_df = df_titles.merge(df_total, on='title', how='left')
    out_df['total_citations'] = out_df['total_citations'].fillna(0).astype(int)
    out_df = out_df[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])
    out = out_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_62m4laWlK2yDUKH8sdK4EmsK': 'file_storage/call_62m4laWlK2yDUKH8sdK4EmsK.json', 'var_call_iyw2z8ScA3sNOnDGG5dxTwPG': 'file_storage/call_iyw2z8ScA3sNOnDGG5dxTwPG.json', 'var_call_qdz2ETJjrX8lNSJa2BWsZizN': 'file_storage/call_qdz2ETJjrX8lNSJa2BWsZizN.json'}

exec(code, env_args)
