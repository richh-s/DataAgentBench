code = """import json
import re

mongo_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:5']

with open(mongo_path, 'r') as f:
    papers = json.load(f)

with open(citations_path, 'r') as f:
    citations_data = json.load(f)

print('Loaded %d papers and %d citations' % (len(papers), len(citations_data)))

# Find papers from 2016 in physical activity domain
papers_2016_pa = []
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if published in 2016
    is_2016 = '2016' in text[:3000]
    # Check if about physical activity
    is_pa = 'physical activity' in text.lower()
    
    if is_2016 and is_pa:
        papers_2016_pa.append(title)
        print('Found 2016 paper: ' + title[:60])

print('\nTotal 2016 papers in PA domain: %d' % len(papers_2016_pa))

# Process citations
import pandas as pd

df = pd.DataFrame(citations_data)
df['citation_count'] = df['citation_count'].astype(int)

# Create simplified title lookup
citation_lookup = {}
for _, row in df.iterrows():
    simp = re.sub(r'[^a-zA-Z0-9]', '', str(row['title']).lower())
    if simp:
        if simp not in citation_lookup:
            citation_lookup[simp] = []
        citation_lookup[simp].append(row['citation_count'])

print('Created citation lookup')

# Match and compute total citations
results = []
for paper_title in papers_2016_pa:
    simp_title = re.sub(r'[^a-zA-Z0-9]', '', paper_title.lower())
    
    if simp_title in citation_lookup:
        total = sum(citation_lookup[simp_title])
        results.append({'title': paper_title, 'total_citation_count': int(total)})

print('Matched %d papers with citations' % len(results))

for r in results:
    print(r['title'] + ': ' + str(r['total_citation_count']))

output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': []}

exec(code, env_args)
