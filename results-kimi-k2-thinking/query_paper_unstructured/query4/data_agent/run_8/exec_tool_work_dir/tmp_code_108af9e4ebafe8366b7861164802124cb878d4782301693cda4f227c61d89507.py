code = """import json
import pandas as pd
import re

# Load paper documents from MongoDB
paper_docs_var = locals()['var_functions.query_db:14']
if isinstance(paper_docs_var, str):
    with open(paper_docs_var, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_var

# Load citations from SQLite
citations_var = locals()['var_functions.query_db:15']
if isinstance(citations_var, str):
    with open(citations_var, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_var

print('Loaded', len(paper_docs), 'paper documents')
print('Loaded', len(citations), 'citation records')

# Extract title, year, and domain from paper documents
paper_info = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Find publication year in text
    year = None
    year_patterns = [r'(20\d{2})', r'CHI\D*(\d{2})\b', r'Ubicomp\D*(\d{2})\b', r'CSCW\D*(\d{2})\b']
    
    for pattern in year_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            yr = match.group(1)
            if len(yr) == 4:
                year = int(yr)
                if 2010 <= year <= 2020:
                    break
            elif len(yr) == 2:
                year = int('20' + yr)
                if 2010 <= year <= 2020:
                    break
    
    # Check for physical activity domain
    lower_text = text.lower()
    has_physical_activity = any(keyword in lower_text for keyword in 
                               ['physical activity', 'fitness', 'exercise', 'steps', 'walking', 
                                'running', 'workout', 'activit', 'fitbit'])
    
    if title:
        paper_info.append({
            'title': title,
            'year': year,
            'is_physical_activity': has_physical_activity
        })

# Filter for 2016 papers in physical activity domain
papers_2016 = [p for p in paper_info if p['year'] == 2016 and p['is_physical_activity']]
print('\nFound', len(papers_2016), 'papers from 2016 in physical activity domain')

for p in papers_2016[:5]:
    print('-', p['title'])

# Create citations dataframe and sum by title
df_citations = pd.DataFrame(citations)
total_citations = df_citations.groupby('title')['total_citations'].sum().reset_index()

# Match papers with their total citations
results = []
for paper in papers_2016:
    paper_title = paper['title']
    
    # Direct match
    match = total_citations[total_citations['title'] == paper_title]
    if not match.empty:
        citations = int(match.iloc[0]['total_citations'])
        results.append({
            'title': paper_title,
            'total_citation_count': citations
        })
    else:
        # Try fuzzy match - check if paper title contains citation title or vice versa
        for _, row in total_citations.iterrows():
            cit_title = row['title']
            if (paper_title.lower() in cit_title.lower() or 
                cit_title.lower() in paper_title.lower()):
                results.append({
                    'title': paper_title,
                    'total_citation_count': int(row['total_citations'])
                })
                break

print('\nFound matches for', len(results), 'papers')
results_json = json.dumps(results)
print('__RESULT__:')
print(results_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)
