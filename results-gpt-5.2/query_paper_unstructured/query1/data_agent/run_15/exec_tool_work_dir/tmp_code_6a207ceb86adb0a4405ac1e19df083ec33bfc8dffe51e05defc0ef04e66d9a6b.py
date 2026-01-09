code = """import json, pandas as pd
path_docs = var_call_7AQEbSHfc7XRQeVVG9Jc63gg
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

food_titles = []
for d in docs:
    txt = (d.get('text') or '').lower()
    if 'domain:' in txt:
        idx = txt.find('domain:')
        line = txt[idx: idx+200].splitlines()[0]
        if 'food' in line:
            fn = d.get('filename','')
            title = fn[:-4] if fn.lower().endswith('.txt') else fn
            food_titles.append(title)

path_cit = var_call_pmRJIsQowKhCtllM7HULxU4g
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df = pd.DataFrame(cit)
df['total_citations'] = pd.to_numeric(df['total_citations'], errors='coerce').fillna(0).astype(int)

total = int(df[df['title'].isin(food_titles)]['total_citations'].sum()) if food_titles else 0

print('__RESULT__:')
print(json.dumps({'total_citations_food_domain': total, 'num_food_domain_papers': int(len(food_titles))}))"""

env_args = {'var_call_2WlLZUaK1vOadvMBmGByqQjd': ['paper_docs'], 'var_call_OqKNaHuyc1Sxbu8qJ591L0nD': [], 'var_call_7AQEbSHfc7XRQeVVG9Jc63gg': 'file_storage/call_7AQEbSHfc7XRQeVVG9Jc63gg.json', 'var_call_pmRJIsQowKhCtllM7HULxU4g': 'file_storage/call_pmRJIsQowKhCtllM7HULxU4g.json'}

exec(code, env_args)
