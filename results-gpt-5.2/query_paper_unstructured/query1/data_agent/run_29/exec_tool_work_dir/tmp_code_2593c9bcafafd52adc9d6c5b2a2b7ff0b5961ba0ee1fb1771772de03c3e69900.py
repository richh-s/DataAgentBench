code = """import json, re
import pandas as pd

path_cit = var_call_FjtUP6HLKuliixLttcWxHLpR
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

path_docs = var_call_9SQaVeiXrZR9d3DE8OzkYTTw
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def is_food_domain(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    patterns = [
        r'domain\s*:\s*.*\bfood\b',
        r'domains\s*:\s*.*\bfood\b'
    ]
    for p in patterns:
        if re.search(p, t):
            return True
    return False

food_set = set()
for d in docs:
    if is_food_domain(d.get('text','')):
        fn = d.get('filename','')
        title = fn[:-4] if fn.endswith('.txt') else fn
        if title:
            food_set.add(title)

total = int(df_cit[df_cit['title'].isin(food_set)]['citation_count'].sum()) if food_set else 0

out = json.dumps({'total_citation_count': total, 'food_paper_count': len(food_set)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_FjtUP6HLKuliixLttcWxHLpR': 'file_storage/call_FjtUP6HLKuliixLttcWxHLpR.json', 'var_call_9SQaVeiXrZR9d3DE8OzkYTTw': 'file_storage/call_9SQaVeiXrZR9d3DE8OzkYTTw.json'}

exec(code, env_args)
