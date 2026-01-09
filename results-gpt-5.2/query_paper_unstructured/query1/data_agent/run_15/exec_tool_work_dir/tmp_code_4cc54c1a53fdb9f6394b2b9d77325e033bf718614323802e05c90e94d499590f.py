code = """import json, pandas as pd, re

# Load mongo docs
path_docs = var_call_7AQEbSHfc7XRQeVVG9Jc63gg
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def infer_domains(text):
    if not text:
        return []
    # try to find explicit domain line
    m = re.search(r'(?im)^\s*domain\s*:\s*([^\n\r]+)', text)
    if m:
        s = m.group(1)
        parts = re.split(r'[,;\|/]+', s)
        doms = [p.strip().lower() for p in parts if p.strip()]
        return doms
    return []

food_titles = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    doms = infer_domains(text)
    if any('food' == x or x.startswith('food') or x.endswith('food') for x in doms):
        food_titles.append(title)

# Load citations totals per title
path_cit = var_call_pmRJIsQowKhCtllM7HULxU4g
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'])

if food_titles:
    total = int(df_cit[df_cit['title'].isin(food_titles)]['total_citations'].sum())
else:
    total = 0

print('__RESULT__:')
print(json.dumps({'total_citations_food_domain': total, 'num_food_domain_papers': len(food_titles)}))"""

env_args = {'var_call_2WlLZUaK1vOadvMBmGByqQjd': ['paper_docs'], 'var_call_OqKNaHuyc1Sxbu8qJ591L0nD': [], 'var_call_7AQEbSHfc7XRQeVVG9Jc63gg': 'file_storage/call_7AQEbSHfc7XRQeVVG9Jc63gg.json', 'var_call_pmRJIsQowKhCtllM7HULxU4g': 'file_storage/call_pmRJIsQowKhCtllM7HULxU4g.json'}

exec(code, env_args)
