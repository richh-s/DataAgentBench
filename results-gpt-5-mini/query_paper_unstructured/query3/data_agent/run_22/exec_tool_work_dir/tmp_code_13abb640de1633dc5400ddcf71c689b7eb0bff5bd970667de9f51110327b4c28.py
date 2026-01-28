code = """import json
import pandas as pd
import re

# Load the MongoDB query result (paper documents)
path_papers = var_call_ASIUZwxdVKhBb0x0D1r1ArEE
with open(path_papers, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Process papers: extract title (from filename), year (first 4-digit year), and check for 'empirical'
processed = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','') or ''
    # find first year occurrence
    m = re.search(r"\b(19|20)\d{2}\b", text)
    year = int(m.group(0)) if m else None
    is_empirical = 'empirical' in text.lower()
    processed.append({'title': title, 'year': year, 'is_empirical': is_empirical})

df_papers = pd.DataFrame(processed)

# Filter papers published after 2016 and empirical
df_filtered = df_papers[(df_papers['year'].notnull()) & (df_papers['year'] > 2016) & (df_papers['is_empirical'])]

# Load citations aggregated totals
path_citations = var_call_ks33GFIQt1Ru5uWUyaBQNf6y
with open(path_citations, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Normalize citation titles (strip surrounding quotes and whitespace)
for c in citations:
    t = c.get('title','')
    t_clean = t.strip().strip('"').strip("'").strip()
    # remove common unicode smart quotes
    t_clean = t_clean.strip('\u201c').strip('\u201d').strip('\u2018').strip('\u2019')
    c['title_clean'] = t_clean
    # convert citation count to int if possible
    try:
        c['total_citations'] = int(c.get('total_citations',0))
    except:
        c['total_citations'] = 0

df_cite = pd.DataFrame(citations)

# Merge filtered papers with citation totals on title matching
result = pd.merge(df_filtered, df_cite, left_on='title', right_on='title_clean', how='inner')

# Prepare output list
output = []
for _, row in result.iterrows():
    output.append({'title': row['title'], 'total_citations': int(row['total_citations'])})

# Print result in required format
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_ASIUZwxdVKhBb0x0D1r1ArEE': 'file_storage/call_ASIUZwxdVKhBb0x0D1r1ArEE.json', 'var_call_ks33GFIQt1Ru5uWUyaBQNf6y': 'file_storage/call_ks33GFIQt1Ru5uWUyaBQNf6y.json'}

exec(code, env_args)
