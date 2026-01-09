code = """import json, re
import pandas as pd

# Load Mongo docs
path_docs = var_call_eoQ1S1UbzgggTVVDdIB4aTst
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load citation totals
path_cit = var_call_mpSwS0Ea3nANePfsuaRBhn1o
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
# ensure numeric
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)


def extract_year(text):
    if not text:
        return None
    # Look for common patterns with years 1990-2026
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
    if not years:
        return None
    years_int = [int(y) for y in years]
    # publication year likely earliest year >=1990
    y = min(years_int)
    return y


def is_empirical(text):
    if not text:
        return False
    t = text.lower()
    # simple heuristic: contains word empirical or user study/interviews/survey/field study/experiment
    return ('empirical' in t) or ('user study' in t) or ('we conducted' in t and ('study' in t or 'interview' in t or 'survey' in t or 'experiment' in t))

rows = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    year = extract_year(text)
    contrib_emp = is_empirical(text)
    if year is not None and year > 2016 and contrib_emp:
        rows.append({'title': title, 'year': year})

df_p = pd.DataFrame(rows).drop_duplicates(subset=['title'])

if df_p.empty:
    out = []
else:
    df = df_p.merge(df_cit, on='title', how='left')
    df['total_citations'] = df['total_citations'].fillna(0).astype(int)
    df = df.sort_values(['total_citations','title'], ascending=[False, True])
    out = df[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_eoQ1S1UbzgggTVVDdIB4aTst': 'file_storage/call_eoQ1S1UbzgggTVVDdIB4aTst.json', 'var_call_mpSwS0Ea3nANePfsuaRBhn1o': 'file_storage/call_mpSwS0Ea3nANePfsuaRBhn1o.json'}

exec(code, env_args)
