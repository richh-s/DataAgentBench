code = """import json
import re

mongo_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:5']

with open(mongo_path, 'r') as f:
    papers = json.load(f)

with open(citations_path, 'r') as f:
    citations_data = json.load(f)

print('Loaded', len(papers), 'papers and', len(citations_data), 'citations')

papers_2016 = []
count = 0
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    has_2016 = '2016' in text[0:2000]
    has_pa = 'physical activity' in text.lower()
    
    if has_2016 and has_pa:
        papers_2016.append(title)
        count += 1

print('Found', count, '2016 papers in physical activity domain')

import pandas as pd
df = pd.DataFrame(citations_data)
df['citation_count'] = df['citation_count'].astype(int)

lookup = {}
for i, row in df.iterrows():
    s = re.sub(r'[^a-zA-Z0-9]', '', str(row['title']).lower())
    if s:
        if s not in lookup:
            lookup[s] = []
        lookup[s].append(row['citation_count'])

results = []
for title in papers_2016:
    s_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
    if s_title in lookup:
        total = sum(lookup[s_title])
        results.append({'title': title, 'total_citation_count': int(total)})

print('Matched', len(results), 'papers')
output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': []}

exec(code, env_args)
