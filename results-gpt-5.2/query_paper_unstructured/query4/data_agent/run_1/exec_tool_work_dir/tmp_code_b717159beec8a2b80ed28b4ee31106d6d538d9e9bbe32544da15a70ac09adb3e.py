code = """import json, re
import pandas as pd

path = var_call_dEvBFgBZgulgkPoXImZ1pn3R
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def pub_year(text):
    # prefer explicit venue year patterns
    m = re.search(r"\b(CHI|UbiComp|UBICOMP|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\b[^\n\r]{0,40}\b(20\d{2})\b", text)
    if m:
        return int(m.group(2))
    m = re.search(r"\b(20\d{2})\b[^\n\r]{0,20}\b(ACM|IEEE)\b", text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r"\bCopyright\s+(20\d{2})\b", text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r"\b©\s*(20\d{2})\b", text)
    if m:
        return int(m.group(1))
    return None

rows=[]
for d in docs:
    year = pub_year(d.get('text','') or '')
    if year==2016:
        rows.append({'title': re.sub(r'\.txt$','', d.get('filename','')), 'year': year})

df = pd.DataFrame(rows).drop_duplicates('title')
print('__RESULT__:')
print(json.dumps({'n_2016_physical_activity': int(df.shape[0]), 'titles': df['title'].tolist()}))"""

env_args = {'var_call_COmGVncUODl5zdBzJJcc7YJx': 'file_storage/call_COmGVncUODl5zdBzJJcc7YJx.json', 'var_call_uVaBQiXCLJw7TGNKKOOfZnPM': 'file_storage/call_uVaBQiXCLJw7TGNKKOOfZnPM.json', 'var_call_s7h3GUFNR9s82nNZARtKmwcW': {'titles': [], 'n_titles': 0}, 'var_call_dEvBFgBZgulgkPoXImZ1pn3R': 'file_storage/call_dEvBFgBZgulgkPoXImZ1pn3R.json'}

exec(code, env_args)
