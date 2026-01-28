code = """import json
import re
import pandas as pd

# Load paper documents
paper_docs_file = locals()['var_functions.query_db:8']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Load citations
citations_file = locals()['var_functions.query_db:5']
with open(citations_file, 'r') as f:
    citations = json.load(f)

print("Analyzing papers...")

# Extract papers data
papers_data = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Extract year
    year = None
    year_matches = re.findall(r'\b(20\d{2})\b', text[:5000])
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2010 <= int(y) <= 2025]
        if valid_years:
            year = min(valid_years)
    
    # Check for physical activity domain
    text_lower = text.lower()
    has_pa = any(keyword in text_lower for keyword in 
                 ['physical activity', 'fitness', 'exercise', 'activity tracking'])
    
    papers_data.append({
        'title': title,
        'year': year,
        'has_physical_activity': has_pa
    })

df_papers = pd.DataFrame(papers_data)

# Filter for 2016 physical activity papers
pa_2016 = df_papers[(df_papers['year'] == 2016) & (df_papers['has_physical_activity'] == True)]

# Process citations
df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)
df_citation_sums = df_citations.groupby('title')['citation_count'].sum().reset_index()
df_citation_sums.columns = ['title', 'total_citations']

# Merge and get results
if not pa_2016.empty:
    result = pd.merge(pa_2016, df_citation_sums, on='title', how='left')
    result = result.fillna({'total_citations': 0})
    result['total_citations'] = result['total_citations'].astype(int)
    output = result[['title', 'total_citations']].to_dict('records')
else:
    output = []

print("Found {} papers".format(len(output)))
result_json = json.dumps(output, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:24': [], 'var_functions.execute_python:30': []}

exec(code, env_args)
