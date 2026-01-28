code = """import json, re
import pandas as pd

# Load mongo docs
mongo_path = var_call_FjHglCZcpOpHFT0wAFuDYgzo
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

food_titles = set()

# Heuristic: look for lines containing 'domain' and 'food'
# Also accept patterns like 'Domains: ... food ...'
pat = re.compile(r'(?:^|\n)\s*(?:domain|domains)\s*[:\-]\s*([^\n]+)', re.IGNORECASE)

for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    m = pat.search(text)
    if not m:
        continue
    dom_line = m.group(1)
    if re.search(r'\bfood\b', dom_line, re.IGNORECASE):
        food_titles.add(title)

# Load citations totals
cit_path = var_call_GfI4WpofEDCfkESKbOgXpize
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

# Join
if df_cit.empty or not food_titles:
    total = 0
else:
    total = int(df_cit[df_cit['title'].isin(food_titles)]['total_citations'].sum())

out = json.dumps({'total_citation_count_food_domain': total, 'num_food_domain_papers_matched': len(food_titles)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_FjHglCZcpOpHFT0wAFuDYgzo': 'file_storage/call_FjHglCZcpOpHFT0wAFuDYgzo.json', 'var_call_GfI4WpofEDCfkESKbOgXpize': 'file_storage/call_GfI4WpofEDCfkESKbOgXpize.json'}

exec(code, env_args)
