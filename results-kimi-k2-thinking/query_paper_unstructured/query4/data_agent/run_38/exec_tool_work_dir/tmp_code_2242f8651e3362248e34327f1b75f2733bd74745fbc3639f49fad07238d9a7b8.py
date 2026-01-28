code = """import json
import re
import pandas as pd

# Get file paths
paper_docs_file = locals()['var_functions.query_db:8']
citations_file = locals()['var_functions.query_db:5']

# Read paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

print("Processing papers...")

# Extract physical activity papers from 2016
papers_2016_pa = []
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
    
    # Check for 2016
    if year != 2016:
        continue
    
    text_lower = text.lower()
    # Check physical activity domain
    pa_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracker']
    if any(keyword in text_lower for keyword in pa_keywords):
        papers_2016_pa.append({'title': title})

print("Found papers:", len(papers_2016_pa))

# Read citations
with open(citations_file, 'r') as f:
    citations = json.load(f)

df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)
df_citation_sums = df_citations.groupby('title')['citation_count'].sum().reset_index()
df_citation_sums.columns = ['title', 'total_citations']

# Merge
if papers_2016_pa:
    df_papers = pd.DataFrame(papers_2016_pa)
    result = pd.merge(df_papers, df_citation_sums, on='title', how='left')
    result = result.fillna({'total_citations': 0})
    result['total_citations'] = result['total_citations'].astype(int)
    output = result.to_dict('records')
else:
    output = []

result_str = json.dumps(output)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:24': []}

exec(code, env_args)
