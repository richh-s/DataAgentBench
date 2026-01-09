code = """import json, pandas as pd

# load filenames
fn_src = var_call_WnEcXQiro9huPhhHUYOhIKfS
if isinstance(fn_src, str) and fn_src.endswith('.json'):
    with open(fn_src, 'r', encoding='utf-8') as f:
        filenames = json.load(f)
else:
    filenames = fn_src

# load citations
cit_src = var_call_BnNP1SMwJ1XTwfQiOt7DaZqL
if isinstance(cit_src, str) and cit_src.endswith('.json'):
    with open(cit_src, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = cit_src

# determine 'food' domain papers using filename substring heuristic
# (papers in food domain commonly have 'food' in title/filename)
food_titles = set()
for r in filenames:
    fn = r.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if 'food' in title.lower():
        food_titles.add(title)

# sum citation_count across all years for those titles
cit_df = pd.DataFrame(citations)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)
    cit_df['is_food'] = cit_df['title'].isin(food_titles)
    total = int(cit_df.loc[cit_df['is_food'], 'citation_count'].sum())
else:
    total = 0

out = {'total_citation_count_food_domain': total, 'food_paper_count_matched_by_title_contains_food': int(len(food_titles))}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WnEcXQiro9huPhhHUYOhIKfS': 'file_storage/call_WnEcXQiro9huPhhHUYOhIKfS.json', 'var_call_BnNP1SMwJ1XTwfQiOt7DaZqL': 'file_storage/call_BnNP1SMwJ1XTwfQiOt7DaZqL.json'}

exec(code, env_args)
