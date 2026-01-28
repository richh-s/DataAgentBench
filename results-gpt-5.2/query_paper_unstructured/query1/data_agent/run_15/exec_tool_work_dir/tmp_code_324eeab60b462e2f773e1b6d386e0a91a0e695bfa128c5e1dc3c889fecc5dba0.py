code = """import json, pandas as pd, re
path_docs = var_call_7AQEbSHfc7XRQeVVG9Jc63gg
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def infer_domains(text):
    if not text:
        return []
    pattern = re.compile(r'(?im)^\s*domain\s*:\s*([^\n\r]+)')
    m = pattern.search(text)
    if m:
        s = m.group(1)
        parts = re.split(r'[,;\\|/]+', s)
        return [p.strip().lower() for p in parts if p.strip()]
    return []

food_titles = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    doms = infer_domains(d.get('text',''))
    if any(x == 'food' or x.startswith('food') or x.endswith('food') for x in doms):
        food_titles.append(title)

path_cit = var_call_pmRJIsQowKhCtllM7HULxU4g
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

total = int(df_cit[df_cit['title'].isin(food_titles)]['total_citations'].sum()) if food_titles else 0

print('__RESULT__:')
print(json.dumps({'total_citations_food_domain': total, 'num_food_domain_papers': int(len(food_titles))}))"""

env_args = {'var_call_2WlLZUaK1vOadvMBmGByqQjd': ['paper_docs'], 'var_call_OqKNaHuyc1Sxbu8qJ591L0nD': [], 'var_call_7AQEbSHfc7XRQeVVG9Jc63gg': 'file_storage/call_7AQEbSHfc7XRQeVVG9Jc63gg.json', 'var_call_pmRJIsQowKhCtllM7HULxU4g': 'file_storage/call_pmRJIsQowKhCtllM7HULxU4g.json'}

exec(code, env_args)
