code = """import json
import re
import pandas as pd

# Get file paths
paper_docs_file = locals()['var_functions.query_db:8']

# Read paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information
all_papers_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Extract year
    year = None
    year_matches = re.findall(r"\b(20\d{2})\b", text[:5000])
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2010 <= int(y) <= 2025]
        if valid_years:
            year = min(valid_years)
    
    # Extract domain indicators
    text_lower = text.lower()
    domains_found = []
    
    if 'physical activity' in text_lower or 'fitness' in text_lower or 'exercise' in text_lower:
        domains_found.append('physical activity')
    if 'sleep' in text_lower:
        domains_found.append('sleep')
    if 'food' in text_lower or 'diet' in text_lower:
        domains_found.append('food')
    if 'mental' in text_lower or 'stress' in text_lower:
        domains_found.append('mental')
    if 'finance' in text_lower or 'money' in text_lower:
        domains_found.append('finances')
    
    all_papers_info.append({
        'title': title,
        'year': year,
        'domains': domains_found
    })

# Create DataFrame
df_all = pd.DataFrame(all_papers_info)

# Find 2016 papers with physical activity domain
papers_2016_pa = df_all[
    (df_all['year'] == 2016) & 
    (df_all['domains'].apply(lambda x: isinstance(x, list) and 'physical activity' in x))
]

# Get citation counts
citations_file = locals()['var_functions.query_db:5']
with open(citations_file, 'r') as f:
    citations = json.load(f)

df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)
df_citation_sums = df_citations.groupby('title')['citation_count'].sum().reset_index()
df_citation_sums.columns = ['title', 'total_citations']

# Merge paper titles with citations
if not papers_2016_pa.empty:
    result = pd.merge(papers_2016_pa, df_citation_sums, on='title', how='left')
    result = result.fillna({'total_citations': 0})
    result['total_citations'] = result['total_citations'].astype(int)
    output = result[['title', 'total_citations']].to_dict('records')
else:
    output = []

# Format output for printing
result_str = json.dumps(output)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': []}

exec(code, env_args)
