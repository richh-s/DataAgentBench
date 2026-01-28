code = """import json
import re
import pandas as pd

# Access the stored file paths using locals()
paper_docs_file = locals()['var_functions.query_db:8']
citations_file = locals()['var_functions.query_db:5']

# Read paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Read citations
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Extract paper information for 2016 papers in physical activity domain
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Extract year - look for 4-digit years
    year = None
    year_matches = re.findall(r"\b(20\d{2})\b", text[:3000])
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2010 <= int(y) <= 2025]
        if valid_years:
            year = min(valid_years)
    
    if year != 2016:
        continue
    
    # Check for physical activity domain
    text_lower = text.lower()
    domain_indicators = [
        'physical activity',
        'fitness',
        'exercise',
        'activity tracking',
        'activity tracker',
        'workout'
    ]
    
    if any(indicator in text_lower for indicator in domain_indicators):
        paper_info.append({
            'title': title
        })

# Process citations
if citations:
    df_citations = pd.DataFrame(citations)
    df_citations['citation_count'] = df_citations['citation_count'].astype(int)
    df_citation_sums = df_citations.groupby('title')['citation_count'].sum().reset_index()
    df_citation_sums.columns = ['title', 'total_citations']
else:
    df_citation_sums = pd.DataFrame(columns=['title', 'total_citations'])

# Merge and get results
if paper_info:
    df_papers = pd.DataFrame(paper_info)
    result = pd.merge(df_papers, df_citation_sums, on='title', how='left')
    result = result.fillna({'total_citations': 0})
    result['total_citations'] = result['total_citations'].astype(int)
    final_result = result[['title', 'total_citations']].sort_values('total_citations', ascending=False)
    output = final_result.to_dict('records')
else:
    output = []

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
