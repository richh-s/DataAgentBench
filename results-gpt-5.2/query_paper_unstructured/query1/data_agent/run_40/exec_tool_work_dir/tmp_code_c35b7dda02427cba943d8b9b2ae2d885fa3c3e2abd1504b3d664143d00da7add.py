code = """import json, re
import pandas as pd

mongo = var_call_EW6ZkLyOUitYdQnVW7iJrdm4
if isinstance(mongo, str):
    with open(mongo, 'r', encoding='utf-8') as f:
        mongo = json.load(f)

# any paper whose text contains the token 'food'
food_titles_set = set()
for d in mongo:
    t = (d.get('text') or '').lower()
    if re.search(r'\bfood\b', t):
        fn = d.get('filename','') or ''
        title = re.sub(r'\.txt$', '', fn)
        food_titles_set.add(title)

cits = var_call_tyrnpDAzagc0QSKLMCufz677
if isinstance(cits, str):
    with open(cits, 'r', encoding='utf-8') as f:
        cits = json.load(f)

df = pd.DataFrame(cits)
if df.empty:
    total = 0
else:
    df['citation_count'] = pd.to_numeric(df['citation_count'], errors='coerce').fillna(0).astype(int)
    total = int(df[df['title'].isin(food_titles_set)]['citation_count'].sum())

out = {"total_citation_count_food_domain": total, "num_food_papers": int(len(food_titles_set))}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_EW6ZkLyOUitYdQnVW7iJrdm4': 'file_storage/call_EW6ZkLyOUitYdQnVW7iJrdm4.json', 'var_call_tyrnpDAzagc0QSKLMCufz677': 'file_storage/call_tyrnpDAzagc0QSKLMCufz677.json'}

exec(code, env_args)
