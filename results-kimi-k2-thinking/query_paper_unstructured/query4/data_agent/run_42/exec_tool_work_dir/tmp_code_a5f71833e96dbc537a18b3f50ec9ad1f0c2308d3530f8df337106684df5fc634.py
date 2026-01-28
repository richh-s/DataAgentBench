code = """import json
import os

# Load MongoDB results
mongo_path = locals()['var_functions.query_db:2']
with open(mongo_path, 'r') as f:
    papers = json.load(f)

# Load citations data
citations_path = locals()['var_functions.query_db:5']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

print(f'Loaded {len(papers)} papers and {len(citations_data)} citations')

# Check if any papers mention 2016
papers_2016 = []
for i, paper in enumerate(papers):
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check for 2016 in the text
    if '2016' in text:
        # Check if physical activity is mentioned  
        if 'physical activity' in text.lower():
            papers_2016.append({
                'title': title,
                'index': i
            })
            print(f'Found 2016 paper: {title}')

print(f'\nFound {len(papers_2016)} papers from 2016 in physical activity domain')

# Process citations
import pandas as pd

citations_df = pd.DataFrame(citations_data)
citation_titles = set(citations_df['title'].tolist())

print(f'\nChecking for citation matches...')
results = []

for paper in papers_2016:
    paper_title = paper['title']
    
    # Check for exact match
    if paper_title in citation_titles:
        paper_cites = citations_df[citations_df['title'] == paper_title]
        total = paper_cites['citation_count'].astype(int).sum()
        results.append({
            'title': paper_title,
            'total_citation_count': int(total)
        })
        print(f'MATCH: {paper_title} -> {total} citations')
    else:
        print(f'NO MATCH: {paper_title}')

print(f'\nFinal results count: {len(results)}')
output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': []}

exec(code, env_args)
