code = """import json
import re
import pandas as pd

# Load files
paper_docs_file = locals()['var_functions.query_db:8']
citations_file = locals()['var_functions.query_db:5']

with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

with open(citations_file, 'r') as f:
    citations = json.load(f)

print("Analyzing {} papers...".format(len(paper_docs)))

# Create a dictionary to store paper info
paper_dict = {}
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Extract year from text
    year = None
    matches = re.findall(r'\b(20\d{2})\b', text[:5000])
    if matches:
        valid_years = [int(y) for y in matches if 2010 <= int(y) <= 2025]
        if valid_years:
            year = min(valid_years)
    
    paper_dict[title] = {
        'year': year,
        'text': text
    }

# Look for physical activity papers from 2016
pa_2016_papers = []
for title, info in paper_dict.items():
    if info['year'] == 2016:
        text_lower = info['text'].lower()
        if any(keyword in text_lower for keyword in ['physical activity', 'fitness', 'exercise', 'activity tracker', 'walking', 'running']):
            pa_2016_papers.append(title)

print("Found {} physical activity papers from 2016".format(len(pa_2016_papers)))

# Process citations
df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)
df_citation_totals = df_citations.groupby('title')['citation_count'].sum().reset_index()
df_citation_totals.columns = ['title', 'total_citations']

# Get results
results = []
for title in pa_2016_papers:
    citation_count = df_citation_totals[df_citation_totals['title'] == title]['total_citations']
    if not citation_count.empty:
        total_citations = int(citation_count.iloc[0])
    else:
        total_citations = 0
    results.append({'title': title, 'total_citations': total_citations})

results = sorted(results, key=lambda x: x['total_citations'], reverse=True)

output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:24': [], 'var_functions.execute_python:30': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
