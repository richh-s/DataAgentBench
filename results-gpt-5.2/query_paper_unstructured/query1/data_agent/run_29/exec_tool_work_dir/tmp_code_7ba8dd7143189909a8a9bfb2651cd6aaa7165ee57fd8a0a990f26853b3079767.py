code = """import json, re
import pandas as pd

# Load citations
path_cit = var_call_FjtUP6HLKuliixLttcWxHLpR
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# Load docs that mention 'food'
path_docs = var_call_9SQaVeiXrZR9d3DE8OzkYTTw
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def is_food_domain(text: str) -> bool:
    if not isinstance(text, str):
        return False
    t = text.lower()
    # Look for explicit metadata patterns
    patterns = [
        r'domain\s*:\s*[^\n\r]*\bfood\b',
        r'domains\s*:\s*[^\n\r]*\bfood\b',
        r'\bdomains?\b[^\n\r]{0,40}\bfood\b',
    ]
    return any(re.search(p, t) for p in patterns)

food_titles = []
for d in docs:
    if is_food_domain(d.get('text','')):
        fn = d.get('filename','')
        if fn.endswith('.txt'):
            title = fn[:-4]
        else:
            title = fn
        food_titles.append(title)

food_set = set(food_titles)

# Sum citations for those titles
if len(food_set)==0:
    total = 0
else:
    total = int(df_cit[df_cit['title'].isin(food_set)]['citation_count'].sum())

out = json.dumps({"total_citation_count": total, "food_paper_count": len(food_set)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_FjtUP6HLKuliixLttcWxHLpR': 'file_storage/call_FjtUP6HLKuliixLttcWxHLpR.json', 'var_call_9SQaVeiXrZR9d3DE8OzkYTTw': 'file_storage/call_9SQaVeiXrZR9d3DE8OzkYTTw.json'}

exec(code, env_args)
