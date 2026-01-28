code = """import json
import re
import pandas as pd

paper_docs_file = locals()['var_functions.query_db:8']
citations_file = locals()['var_functions.query_db:5']

with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

with open(citations_file, 'r') as f:
    citations = json.load(f)

# Extract paper information
papers = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Extract year
    year = None
    matches = re.findall(r'\b(20\d{2})\b', text[:3000])
    if matches:
        valid_years = [int(y) for y in matches if 2010 <= int(y) <= 2025]
        if valid_years:
            year = min(valid_years)
    
    # Extract domains
    text_lower = text.lower()
    domains = []
    
    domain_keywords = {
        'physical activity': ['physical activity', 'fitness', 'exercise', 'activity tracking'],
        'sleep': ['sleep'],
        'food': ['food', 'diet'],
        'mental': ['mental', 'stress'],
        'finances': ['finance', 'money']
    }
    
    for domain, keywords in domain_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            domains.append(domain)
    
    papers.append({'title': title, 'year': year, 'domains': domains})

df_papers = pd.DataFrame(papers)

# Filter for 2016 physical activity papers
physical_activity_2016 = []
for _, paper in df_papers.iterrows():
    if paper['year'] == 2016 and 'physical activity' in paper['domains']:
        physical_activity_2016.append({'title': paper['title']})

# Sum citations by title
df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)
df_citation_totals = df_citations.groupby('title')['citation_count'].sum().reset_index()
df_citation_totals.columns = ['title', 'total_citations']

# Merge with 2016 papers
if physical_activity_2016:
    df_2016 = pd.DataFrame(physical_activity_2016)
    result = pd.merge(df_2016, df_citation_totals, on='title', how='left')
    result = result.fillna({'total_citations': 0})
    result['total_citations'] = result['total_citations'].astype(int)
    result = result[['title', 'total_citations']].sort_values('total_citations', ascending=False)
    output = result.to_dict('records')
else:
    output = []

print('Found {} papers'.format(len(output)))
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:24': [], 'var_functions.execute_python:30': [], 'var_functions.execute_python:34': []}

exec(code, env_args)
