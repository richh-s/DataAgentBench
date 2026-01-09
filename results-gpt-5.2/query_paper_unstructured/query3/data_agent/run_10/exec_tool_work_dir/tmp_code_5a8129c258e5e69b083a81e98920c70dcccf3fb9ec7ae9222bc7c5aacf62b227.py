code = """import json, re
import pandas as pd

# Load mongo docs
path_docs = var_call_T1Z9JWTl7NTQxeVyxkMGq8YF
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load citations totals
path_cit = var_call_L39N8tTimavNqKl7kyLBSb20
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

df_cit = pd.DataFrame(cits)
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

# helpers
venue_pat = re.compile(r"\b(chi|ubicomp|cscw|dis|pervasivehealth|www|iui|ozchi|tei|ah)\b", re.I)
source_pat = re.compile(r"\b(acm|ieee|pubmed)\b", re.I)
domain_pat = re.compile(r"\b(food|physical activity|sleep|mental|finances|productivity|screen time|social interactions|location|chronic|diabetes|health_behavior)\b", re.I)

def extract_year(text):
    # look for patterns like CHI '19 or UbiComp '15, or copyright year
    m = re.search(r"\b(19\d{2}|20\d{2})\b", text)
    # not great; try copyright specifically first
    m2 = re.search(r"Copyright\s*(?:\(c\))?\s*(19\d{2}|20\d{2})", text, re.I)
    if m2:
        return int(m2.group(1))
    # try venue short year e.g., '19
    m3 = re.search(r"\b(?:CHI|UbiComp|CSCW|DIS|IUI|TEI|OzCHI|AH|WWW)\s*['’](\d{2})\b", text, re.I)
    if m3:
        yy = int(m3.group(1))
        return 2000+yy if yy < 50 else 1900+yy
    if m:
        return int(m.group(1))
    return None


def has_empirical(text):
    # contribution likely tagged somewhere; use substring match
    return bool(re.search(r"\bempirical\b", text, re.I))

rows=[]
for d in docs:
    title = d.get('filename','')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = d.get('text','') or ''
    year = extract_year(text)
    empirical = has_empirical(text)
    if year is None:
        continue
    if empirical and year > 2016:
        rows.append({'title': title, 'year': year})

# Deduplicate by title keeping max year (in case)
df = pd.DataFrame(rows)
if df.empty:
    out = []
else:
    df = df.sort_values(['title','year']).drop_duplicates('title', keep='last')
    df = df.merge(df_cit, on='title', how='left')
    df['total_citations'] = df['total_citations'].fillna(0).astype(int)
    df = df.sort_values('total_citations', ascending=False)
    out = df[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_T1Z9JWTl7NTQxeVyxkMGq8YF': 'file_storage/call_T1Z9JWTl7NTQxeVyxkMGq8YF.json', 'var_call_L39N8tTimavNqKl7kyLBSb20': 'file_storage/call_L39N8tTimavNqKl7kyLBSb20.json'}

exec(code, env_args)
