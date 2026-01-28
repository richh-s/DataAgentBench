code = """import json, pandas as pd

# load filenames from mongo result (stored as json file path)
path_files = var_call_uUiSw4kgves6F4DN8WeRXDJO
with open(path_files, 'r', encoding='utf-8') as f:
    files = json.load(f)

cit_path = var_call_p4IPW4D4QcLPSwzSU0Sjdab1
with open(cit_path, 'r', encoding='utf-8') as f:
    cits = json.load(f)

def title_from_filename(fn):
    return fn[:-4] if fn.lower().endswith('.txt') else fn

# identify food-domain papers via filename containing 'food'
food_titles = [title_from_filename(r['filename']) for r in files if 'food' in r.get('filename','').lower()]
food_set = set(food_titles)

df_c = pd.DataFrame(cits)
if not df_c.empty:
    df_c['total_citations'] = pd.to_numeric(df_c['total_citations'], errors='coerce').fillna(0).astype(int)

# join by exact title match
food_total = int(df_c[df_c['title'].isin(food_set)]['total_citations'].sum()) if not df_c.empty else 0

print('__RESULT__:')
print(json.dumps({'total_citations_food_domain': food_total, 'food_paper_count_matched': int(df_c['title'].isin(food_set).sum()), 'food_paper_count_by_filename': len(food_set)}))"""

env_args = {'var_call_uUiSw4kgves6F4DN8WeRXDJO': 'file_storage/call_uUiSw4kgves6F4DN8WeRXDJO.json', 'var_call_p4IPW4D4QcLPSwzSU0Sjdab1': 'file_storage/call_p4IPW4D4QcLPSwzSU0Sjdab1.json'}

exec(code, env_args)
