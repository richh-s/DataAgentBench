code = """import json, pandas as pd

# Load citations totals per title
cit_path = var_call_IBbYqorI2JWVGqgFc0ClSigv
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

# Load paper docs
docs_path = var_call_9QKvaQJOGXhlLo3iNYrBSvU5
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def extract_domain(text):
    # heuristic: look for a line like 'domain:' or 'domains:' (case-insensitive)
    import re
    m = re.search(r'(?im)^\s*domain\s*:\s*(.+?)\s*$', text)
    if m:
        return m.group(1).strip()
    m = re.search(r'(?im)^\s*domains\s*:\s*(.+?)\s*$', text)
    if m:
        return m.group(1).strip()
    return None

food_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    domain = extract_domain(d.get('text','') or '')
    if domain and ('food' in domain.lower()):
        food_titles.add(title)

# Join with citations totals
cit_df = pd.DataFrame(cit)
if not cit_df.empty:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

food_total = int(cit_df[cit_df['title'].isin(food_titles)]['total_citations'].sum())

print('__RESULT__:')
print(json.dumps({'total_citation_count_food_domain': food_total, 'num_food_papers_matched': len(food_titles)}))"""

env_args = {'var_call_IBbYqorI2JWVGqgFc0ClSigv': 'file_storage/call_IBbYqorI2JWVGqgFc0ClSigv.json', 'var_call_9QKvaQJOGXhlLo3iNYrBSvU5': 'file_storage/call_9QKvaQJOGXhlLo3iNYrBSvU5.json'}

exec(code, env_args)
