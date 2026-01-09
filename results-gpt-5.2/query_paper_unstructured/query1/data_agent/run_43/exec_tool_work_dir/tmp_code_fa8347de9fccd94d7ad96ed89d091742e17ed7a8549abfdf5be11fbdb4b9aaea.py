code = """import json, re
import pandas as pd

mongo_path = var_call_RMQKSsolBYjWeUf9ULlofJRZ
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Determine food-domain papers by presence of 'food' in title (common in this corpus)
# and also by occurrences of 'food journaling' / 'diet' in abstract/keywords.
food_titles = set()

def is_food_doc(title, text):
    t = (title or '').lower()
    if 'food' in t or 'diet' in t or 'nutrition' in t or 'eating' in t:
        return True
    # fallback: keyword/abstract cues
    tt = (text or '').lower()
    cues = ['food journaling','food journal','dietary','nutrition','eating behaviors','calorie','meal','diet']
    return any(c in tt for c in cues)

for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if is_food_doc(title, d.get('text','')):
        food_titles.add(title)

cit_path = var_call_GfI4WpofEDCfkESKbOgXpize
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df = pd.DataFrame(cit)
if df.empty:
    total = 0
else:
    df['total_citations'] = pd.to_numeric(df['total_citations'], errors='coerce').fillna(0).astype(int)
    total = int(df[df['title'].isin(food_titles)]['total_citations'].sum())

out = json.dumps({'total_citation_count_food_domain': total, 'num_food_papers_identified': len(food_titles)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_FjHglCZcpOpHFT0wAFuDYgzo': 'file_storage/call_FjHglCZcpOpHFT0wAFuDYgzo.json', 'var_call_GfI4WpofEDCfkESKbOgXpize': 'file_storage/call_GfI4WpofEDCfkESKbOgXpize.json', 'var_call_6vDRKonGaChoz1MZ6jZB7tWK': {'total_citation_count_food_domain': 0, 'num_food_domain_papers_matched': 0}, 'var_call_RMQKSsolBYjWeUf9ULlofJRZ': 'file_storage/call_RMQKSsolBYjWeUf9ULlofJRZ.json'}

exec(code, env_args)
