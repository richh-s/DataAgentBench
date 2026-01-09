code = """import json
import pandas as pd

path = var_call_dEvBFgBZgulgkPoXImZ1pn3R
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

rows=[]
for d in docs:
    txt = d.get('text','') or ''
    if '2016' in txt:
        rows.append({'title': d.get('filename','')[:-4]})

df = pd.DataFrame(rows).drop_duplicates('title')
print('__RESULT__:')
print(json.dumps({'n_with_2016_in_text': int(df.shape[0]), 'titles': df['title'].tolist()[:200]}))"""

env_args = {'var_call_COmGVncUODl5zdBzJJcc7YJx': 'file_storage/call_COmGVncUODl5zdBzJJcc7YJx.json', 'var_call_uVaBQiXCLJw7TGNKKOOfZnPM': 'file_storage/call_uVaBQiXCLJw7TGNKKOOfZnPM.json', 'var_call_s7h3GUFNR9s82nNZARtKmwcW': {'titles': [], 'n_titles': 0}, 'var_call_dEvBFgBZgulgkPoXImZ1pn3R': 'file_storage/call_dEvBFgBZgulgkPoXImZ1pn3R.json'}

exec(code, env_args)
