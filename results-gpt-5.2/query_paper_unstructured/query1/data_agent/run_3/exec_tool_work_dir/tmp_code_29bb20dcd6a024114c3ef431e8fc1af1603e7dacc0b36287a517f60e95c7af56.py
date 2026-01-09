code = """import json, pandas as pd, re

# Load paper docs (large) from json file path
paper_docs_path = var_call_KAnmESU0XUUkCNK5Odf3El9C
with open(paper_docs_path, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Build set of titles in food domain using substring match in text
food_titles = set()
for d in paper_docs:
    fn = d.get('filename','') or ''
    title = re.sub(r'\.txt$', '', fn)
    text = (d.get('text','') or '')
    if 'food' in text.lower():
        food_titles.add(title)

# Load citations (large) from json file
cit_path = var_call_Hae7i2gLTfDKLwDmUXxD8QHp
with open(cit_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

df = pd.DataFrame(citations)
# ensure int
if not df.empty:
    df['citation_count'] = pd.to_numeric(df['citation_count'], errors='coerce').fillna(0).astype(int)

# sum citation counts for titles in food_titles
if df.empty or not food_titles:
    total = 0
else:
    total = int(df[df['title'].isin(food_titles)]['citation_count'].sum())

out = json.dumps({'total_citation_count_food_domain': total, 'food_paper_count': len(food_titles)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_KAnmESU0XUUkCNK5Odf3El9C': 'file_storage/call_KAnmESU0XUUkCNK5Odf3El9C.json', 'var_call_Hae7i2gLTfDKLwDmUXxD8QHp': 'file_storage/call_Hae7i2gLTfDKLwDmUXxD8QHp.json'}

exec(code, env_args)
