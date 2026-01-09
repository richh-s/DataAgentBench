code = """import json, re
import pandas as pd

path_docs = var_call_BtEbLXyyZV0w9lnZVawtFTiH
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

path_cit = var_call_TkEXuHV3XWB3YIhoERtLV8EV
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

df_cit = pd.DataFrame(cits)
if 'total_citations' in df_cit.columns:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)


def extract_year(text: str):
    m = re.search(r'\b(19\d{2}|20\d{2})\b', text or '')
    if not m:
        return None
    y = int(m.group(1))
    return y if 1900 <= y <= 2099 else None


def is_empirical(text: str):
    return 'empirical' in (text or '').lower()

rows = []
for d in docs:
    fn = d.get('filename','') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    year = extract_year(d.get('text',''))
    if year is not None and year > 2016 and is_empirical(d.get('text','')):
        rows.append({'title': title, 'year': year})

df_papers = pd.DataFrame(rows).drop_duplicates(subset=['title'])

out = df_papers.merge(df_cit, on='title', how='left')
out['total_citations'] = out.get('total_citations', 0)
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_BtEbLXyyZV0w9lnZVawtFTiH': 'file_storage/call_BtEbLXyyZV0w9lnZVawtFTiH.json', 'var_call_TkEXuHV3XWB3YIhoERtLV8EV': 'file_storage/call_TkEXuHV3XWB3YIhoERtLV8EV.json'}

exec(code, env_args)
