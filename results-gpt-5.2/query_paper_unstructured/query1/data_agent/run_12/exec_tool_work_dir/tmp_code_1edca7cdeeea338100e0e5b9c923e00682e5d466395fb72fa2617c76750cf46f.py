code = """import json, re
import pandas as pd

# Load citations totals per title
cit_path = var_call_7CSMavulR5EYTbE2xp0EXyDs
if isinstance(cit_path, str) and cit_path.endswith('.json'):
    with open(cit_path, 'r', encoding='utf-8') as f:
        cit = json.load(f)
else:
    cit = cit_path

df_cit = pd.DataFrame(cit)
# total_citations may be str
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

# Load paper docs
docs_path = var_call_aWFXXbvt8ZG9DZdeo3pg48h1
if isinstance(docs_path, str) and docs_path.endswith('.json'):
    with open(docs_path, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_path

# Determine titles in food domain by parsing explicit 'domain:' lines containing 'food'
food_titles = []
pat = re.compile(r'^\s*domain\s*:\s*(.*)$', re.IGNORECASE)
for d in docs:
    text = d.get('text','') or ''
    # scan line by line for domain field
    is_food = False
    for line in text.splitlines():
        m = pat.match(line)
        if m and 'food' in m.group(1).lower():
            is_food = True
            break
    if is_food:
        fn = d.get('filename','') or ''
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        food_titles.append(title)

food_set = set(food_titles)

# Join with citations totals
if df_cit.empty:
    total = 0
else:
    total = int(df_cit[df_cit['title'].isin(food_set)]['total_citations'].sum())

out = {"total_citation_count_food_domain": total, "num_food_papers_matched": int(df_cit[df_cit['title'].isin(food_set)]['title'].nunique()), "num_food_papers_in_docs": len(food_set)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_7CSMavulR5EYTbE2xp0EXyDs': 'file_storage/call_7CSMavulR5EYTbE2xp0EXyDs.json', 'var_call_aWFXXbvt8ZG9DZdeo3pg48h1': 'file_storage/call_aWFXXbvt8ZG9DZdeo3pg48h1.json'}

exec(code, env_args)
