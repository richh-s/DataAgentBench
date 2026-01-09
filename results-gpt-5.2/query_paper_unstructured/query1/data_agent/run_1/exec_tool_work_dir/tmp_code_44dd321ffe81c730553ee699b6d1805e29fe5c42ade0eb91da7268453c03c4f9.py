code = """import json, pandas as pd, re

# load all docs
path_docs = var_call_iiR13FFomOxkyrHNLLhndaf6
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# food-domain heuristic: look for explicit domain metadata if present; else fallback to keyword-based is unsafe.
# We'll try to detect a metadata section containing 'domain' or 'domains' lines.
food_titles = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    head = text[:4000]
    m = re.search(r'(?im)^\s*domain\s*:\s*(.+)$', head)
    if not m:
        m = re.search(r'(?im)^\s*domains\s*:\s*(.+)$', head)
    if m:
        dom = m.group(1).strip().lower()
        if 'food' in dom:
            food_titles.append(title)

# If none found via metadata, assume domain is encoded elsewhere; use conservative keyword in title as proxy
if len(food_titles)==0:
    for d in docs:
        fn = d.get('filename','')
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        if re.search(r'\bfood\b', title, re.I) or re.search(r'\bnutrition\b', title, re.I) or re.search(r'\bdiet\b', title, re.I):
            food_titles.append(title)

food_titles = sorted(set(food_titles))

# load citations aggregated
path_cit = var_call_YUV2LW3WLUK3uO84M00LRg3n
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

# sum citations for food titles
s = int(df_cit[df_cit['title'].isin(food_titles)]['total_citations'].sum())

out = {'total_citation_count_food_domain': s, 'food_paper_count': len(food_titles)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YUV2LW3WLUK3uO84M00LRg3n': 'file_storage/call_YUV2LW3WLUK3uO84M00LRg3n.json', 'var_call_D4EDiQmMZPjXOaSjl0wlvwD2': [], 'var_call_Y9GVsLxZtGNwIT0I1DqhejHX': 'file_storage/call_Y9GVsLxZtGNwIT0I1DqhejHX.json', 'var_call_UOPHwXQptgR0ro0rbl1Z6nfc': {'status': 'need_all_docs'}, 'var_call_iiR13FFomOxkyrHNLLhndaf6': 'file_storage/call_iiR13FFomOxkyrHNLLhndaf6.json'}

exec(code, env_args)
