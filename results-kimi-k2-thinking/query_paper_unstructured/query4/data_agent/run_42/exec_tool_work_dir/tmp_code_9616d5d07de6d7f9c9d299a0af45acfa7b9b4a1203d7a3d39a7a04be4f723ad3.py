code = """import json
import re

# Load the data
mongo_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:5']

with open(mongo_path, 'r') as f:
    papers = json.load(f)

with open(citations_path, 'r') as f:
    citations_data = json.load(f)

print('Step 1: Data loaded')
print('  Papers:', len(papers))
print('  Citations:', len(citations_data))

# Find 2016 papers in physical activity domain
papers_2016_pa = []
for idx, paper in enumerate(papers):
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check for 2016
    has_2016 = '2016' in text or 'Proceedings of the 2016' in text or re.search(r"CHI\s+'16", text) or re.search(r"Ubicomp\s+'16", text)
    
    # Check for physical activity
    has_pa = 'physical activity' in text.lower()
    
    if has_2016 and has_pa:
        papers_2016_pa.append(title)
        print('Found 2016 PA paper:', title[:60])

print('\nStep 2: Found', len(papers_2016_pa), 'papers from 2016 in physical activity domain')

# Process citations
import pandas as pd

df = pd.DataFrame(citations_data)
df['citation_count'] = df['citation_count'].astype(int)

# Create lookup
lookup = {}
for _, row in df.iterrows():
    title = str(row['title'])
    simplified = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
    if simplified not in lookup:
        lookup[simplified] = []
    lookup[simplified].append(row['citation_count'])

print('Step 3: Created citation lookup with', len(lookup), 'entries')

# Match papers with citations
final_results = []
for paper_title in papers_2016_pa:
    simplified_title = re.sub(r'[^a-zA-Z0-9]', '', paper_title.lower())
    
    if simplified_title in lookup:
        total = sum(lookup[simplified_title])
        final_results.append({'title': paper_title, 'total_citation_count': int(total)})
        print('MATCH:', paper_title[:50], '->', total, 'citations')
    else:
        print('NO MATCH:', paper_title[:50])

print('\nStep 4: Final results count =', len(final_results))
for r in final_results:
    print('  -', r['title'], ':', r['total_citation_count'])

output = json.dumps(final_results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': []}

exec(code, env_args)
