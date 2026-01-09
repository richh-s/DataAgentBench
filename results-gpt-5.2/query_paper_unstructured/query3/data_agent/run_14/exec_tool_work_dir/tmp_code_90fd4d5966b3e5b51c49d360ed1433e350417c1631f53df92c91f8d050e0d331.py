code = """import json, re
import pandas as pd

# Load paper docs
path_docs = var_call_bMaYt66mb6roBxGLoQlh3BzP
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def extract_year(text):
    # Prefer explicit copyright year
    m = re.search(r'Copyright\s+\d{4}', text, flags=re.IGNORECASE)
    if m:
        return int(re.search(r'\d{4}', m.group(0)).group(0))
    # Look for venue pattern 'CHI '18' or UBICOMP '15 etc.
    m = re.search(r"\b(?:CHI|CSCW|UBICOMP|UbiComp|DIS|IUI|TEI|OzCHI|WWW|AH|PervasiveHealth)\s*['’](\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy
    # Fallback: first year 20xx in first 500 chars
    head = text[:800]
    m = re.search(r'\b(20\d{2})\b', head)
    if m:
        return int(m.group(1))
    return None

# contribution heuristic: contains word empirical (case-insensitive)
def is_empirical(text):
    return re.search(r'\bempirical\b', text, flags=re.IGNORECASE) is not None

records = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text') or ''
    year = extract_year(text)
    emp = is_empirical(text)
    records.append({'title': title, 'year': year, 'empirical': emp})

df_papers = pd.DataFrame(records)

# Load citations totals
cit = var_call_bDY43izLmNwP8bFReFDniPmI
# handle if stored in file
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

df_cit = pd.DataFrame(cit)
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

# Join
df = df_papers.merge(df_cit, on='title', how='inner')

df = df[(df['empirical'] == True) & (df['year'].notna()) & (df['year'] > 2016)]

df_out = df[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True]).reset_index(drop=True)

result = df_out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WH14wst887dJYk2ihkJs6ERm': 'file_storage/call_WH14wst887dJYk2ihkJs6ERm.json', 'var_call_bDY43izLmNwP8bFReFDniPmI': 'file_storage/call_bDY43izLmNwP8bFReFDniPmI.json', 'var_call_bMaYt66mb6roBxGLoQlh3BzP': 'file_storage/call_bMaYt66mb6roBxGLoQlh3BzP.json'}

exec(code, env_args)
