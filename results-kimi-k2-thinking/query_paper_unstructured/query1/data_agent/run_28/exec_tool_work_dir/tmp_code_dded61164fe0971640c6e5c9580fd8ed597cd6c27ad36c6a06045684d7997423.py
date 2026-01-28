code = """import json
import pandas as pd
import re

# Load paper documents
paper_docs = locals()['var_functions.query_db:22']
if isinstance(paper_docs, str):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

# Extract paper domains
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text = doc.get('text', '').lower()
    
    domain = ''
    if 'food' in text:
        domain = 'food'
    elif 'physical activity' in text or 'exercise' in text:
        domain = 'physical activity'
    elif 'sleep' in text:
        domain = 'sleep'
    elif 'mental' in text or 'stress' in text:
        domain = 'mental'
    elif 'finances' in text:
        domain = 'finances'
    
    paper_info.append({'title': title, 'domain': domain})

papers_df = pd.DataFrame(paper_info)
food_papers = papers_df[papers_df['domain'] == 'food']
print('Food papers count:', len(food_papers))

# Load citations
citations = locals()['var_functions.query_db:2']
if isinstance(citations, str):
    with open(citations, 'r') as f:
        citations = json.load(f)

citations_df = pd.DataFrame(citations)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)

# Find matching titles
food_titles = set(food_papers['title'].tolist())
citation_titles = set(citations_df['title'].tolist())

# Use exact matching
total_citations = 0
for title in food_titles:
    if title in citation_titles:
        paper_cits = citations_df[citations_df['title'] == title]
        total_citations += paper_cits['citation_count'].sum()

print('Total citations for exact matches:', total_citations)

# Use fuzzy matching as backup
from difflib import get_close_matches
fuzzy_total = 0
matched = 0

for _, paper in food_papers.iterrows():
    matches = get_close_matches(paper['title'], list(citation_titles), n=1, cutoff=0.8)
    if matches:
        paper_cits = citations_df[citations_df['title'] == matches[0]]
        fuzzy_total += paper_cits['citation_count'].sum()
        matched += 1

print('Total citations for fuzzy matches:', fuzzy_total)
print('Papers matched:', matched)

result = {'total_citation_count': int(fuzzy_total)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_citation_count': 0, 'matched_papers': 0}}

exec(code, env_args)
