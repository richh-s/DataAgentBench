code = """import json, re
import pandas as pd

# Load mongo docs
path_docs = var_call_BtEbLXyyZV0w9lnZVawtFTiH
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load citations totals
path_cit = var_call_TkEXuHV3XWB3YIhoERtLV8EV
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

df_cit = pd.DataFrame(cits)
# Ensure numeric
if 'total_citations' in df_cit.columns:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)


def extract_year(text: str):
    # Look for common patterns like 2017, 2018 etc near header
    m = re.search(r'\b(19\d{2}|20\d{2})\b', text)
    if not m:
        return None
    y = int(m.group(1))
    if 1900 <= y <= 2099:
        return y
    return None


def is_empirical(text: str):
    # heuristic: look for contribution labels or keywords
    t = text.lower()
    # direct contribution tag
    if re.search(r'\bcontribution\b[^\n]{0,80}\bempirical\b', t):
        return True
    # common in metadata lines
    if re.search(r'\bempirical\b\s+(study|evaluation|investigation|analysis|research)', t):
        return True
    if re.search(r'\b(empirical study|empirical evaluation|empirical investigation)\b', t):
        return True
    # fallback: if 'empirical' appears anywhere, treat as empirical contribution per hint (substring match)
    return '\ncontribution' in t and 'empirical' in t or 'empirical' in t

rows = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','') or ''
    year = extract_year(text)
    emp = is_empirical(text)
    if year is not None and year > 2016 and emp:
        rows.append({'title': title, 'year': year})

df_papers = pd.DataFrame(rows).drop_duplicates(subset=['title'])

# Join citations totals
out = df_papers.merge(df_cit, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

# Sort by citations desc then title
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_BtEbLXyyZV0w9lnZVawtFTiH': 'file_storage/call_BtEbLXyyZV0w9lnZVawtFTiH.json', 'var_call_TkEXuHV3XWB3YIhoERtLV8EV': 'file_storage/call_TkEXuHV3XWB3YIhoERtLV8EV.json'}

exec(code, env_args)
