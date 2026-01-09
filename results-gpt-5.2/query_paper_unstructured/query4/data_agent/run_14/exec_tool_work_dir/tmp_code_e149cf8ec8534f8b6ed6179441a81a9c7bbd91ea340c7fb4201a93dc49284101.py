code = """import json, re, pandas as pd

# Load mongo docs (may be file path)
docs_src = var_call_9n3ncxRx5cQLe9qa5CL6gClv
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

cits_src = var_call_XqJxNKJf5mT34w24YxGFCsMb
if isinstance(cits_src, str):
    with open(cits_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cits_src

# Heuristic: domain physical activity if text contains 'physical activity' (case-insensitive)
# Publication year: look for patterns around 2016 near venue lines, or copyright line.
# We'll require year==2016 anywhere in first ~2000 chars and also a venue marker with 2016? Too hard.
# Use regex for common citation string: 'CHI 2016' etc. If found, take that year.

venue_year_re = re.compile(r'\b(CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|WWW|PervasiveHealth|OzCHI|TEI|AH)\s+20(\d{2})\b', re.IGNORECASE)
year_re = re.compile(r'\b(19|20)\d{2}\b')

def infer_year(text):
    head = text[:4000]
    m = venue_year_re.search(head)
    if m:
        return int('20'+m.group(2))
    # fallback: find first year in head that looks like publication year, prefer 2016
    years = [int(x.group(0)) for x in year_re.finditer(head)]
    if 2016 in years:
        return 2016
    return years[0] if years else None

rows=[]
for d in docs:
    title = d.get('filename','')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = d.get('text','') or ''
    if 'physical activity' not in text.lower():
        continue
    yr = infer_year(text)
    if yr != 2016:
        continue
    rows.append({'title': title})

pa2016 = pd.DataFrame(rows).drop_duplicates()

cits_df = pd.DataFrame(cits)
if not cits_df.empty:
    cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'], errors='coerce').fillna(0).astype(int)

out = pa2016.merge(cits_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_9n3ncxRx5cQLe9qa5CL6gClv': 'file_storage/call_9n3ncxRx5cQLe9qa5CL6gClv.json', 'var_call_XqJxNKJf5mT34w24YxGFCsMb': 'file_storage/call_XqJxNKJf5mT34w24YxGFCsMb.json'}

exec(code, env_args)
