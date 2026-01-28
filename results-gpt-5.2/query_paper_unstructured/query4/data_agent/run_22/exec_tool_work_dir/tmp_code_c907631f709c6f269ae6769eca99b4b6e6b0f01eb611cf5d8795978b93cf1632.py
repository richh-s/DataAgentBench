code = """import json, re
import pandas as pd

def load_maybe_path(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

papers = load_maybe_path(var_call_duyvWhzI3mtUdFp11T6tEHdQ)
cits = load_maybe_path(var_call_vyT4FifmQXuoheX5UbyoZ23G)

def extract_year(text):
    if not text:
        return None
    # look for 4-digit years 2000-2026, pick earliest plausible publication year
    years = [int(y) for y in re.findall(r'\b(20\d{2})\b', text)]
    years = [y for y in years if 2000 <= y <= 2026]
    if not years:
        return None
    return min(years)

rows = []
for d in papers:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    year = extract_year(text)
    # domain: require explicit mention; we already filtered by regex, but keep robust
    if re.search(r'(?i)physical activity', text):
        rows.append({'title': title, 'year': year})

pdf = pd.DataFrame(rows).drop_duplicates(subset=['title'])
# keep only publication year 2016
pdf2016 = pdf[pdf['year'] == 2016].copy()

cիտ = pd.DataFrame(cits)
# total_citations came as strings sometimes
if not cит.empty:
    cит['total_citations'] = pd.to_numeric(cит['total_citations'], errors='coerce')

out = pdf2016.merge(cит, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_duyvWhzI3mtUdFp11T6tEHdQ': 'file_storage/call_duyvWhzI3mtUdFp11T6tEHdQ.json', 'var_call_vyT4FifmQXuoheX5UbyoZ23G': 'file_storage/call_vyT4FifmQXuoheX5UbyoZ23G.json'}

exec(code, env_args)
