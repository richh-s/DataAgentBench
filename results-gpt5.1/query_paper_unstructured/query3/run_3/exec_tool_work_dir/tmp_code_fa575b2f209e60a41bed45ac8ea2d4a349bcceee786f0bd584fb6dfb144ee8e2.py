code = """import re, json
import pandas as pd

path_docs = var_call_h3tkAL1VKwqoy8CYKnH7qe3y
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Extract title (filename without .txt) and approximate year from text
records = []
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','', fn)
    text = d.get('text','')
    m = re.search(r'CHI\s+(20\d{2})', text)
    if not m:
        m = re.search(r'(20\d{2})', text)
    year = int(m.group(1)) if m else None
    records.append({'title': title, 'year': year})

emp_df = pd.DataFrame(records)
emp_df = emp_df.dropna(subset=['year'])
emp_df = emp_df[emp_df['year'] > 2016]

# Load citations
path_cit = var_call_4is8vMF9H4w9fnHgcokztNTZ
with open(path_cit, 'r') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = pd.merge(emp_df, cit_df, on='title', how='inner')

result = merged[['title','total_citations']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_h3tkAL1VKwqoy8CYKnH7qe3y': 'file_storage/call_h3tkAL1VKwqoy8CYKnH7qe3y.json', 'var_call_4is8vMF9H4w9fnHgcokztNTZ': 'file_storage/call_4is8vMF9H4w9fnHgcokztNTZ.json'}

exec(code, env_args)
