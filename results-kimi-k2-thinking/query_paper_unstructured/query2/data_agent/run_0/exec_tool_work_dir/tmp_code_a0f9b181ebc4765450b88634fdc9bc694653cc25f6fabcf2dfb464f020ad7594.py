code = """import json
import pandas as pd

# Load citations data from 2018
citations_file = 'var_functions.query_db:7'
with open(citations_file) as f:
    citations_2018 = json.load(f)

# Load paper documents data
papers_file = 'var_functions.query_db:3'  
with open(papers_file) as f:
    paper_docs = json.load(f)

# Create DataFrame for citations
citations_df = pd.DataFrame(citations_2018)

# Find ACM papers by checking text content
acm_titles = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    if 'ACM' in text or 'acm.org' in text:
        title = filename.replace('.txt', '') if filename else ''
        acm_titles.append(title)

# Filter citations to only ACM papers
acm_citations = citations_df[citations_df['title'].isin(acm_titles)]

# Calculate average citation count
if not acm_citations.empty:
    avg_citations = acm_citations['citation_count'].astype(float).mean()
    paper_count = len(acm_citations)
    result = 'Average citation count for ACM papers in 2018: {:.2f} (based on {} papers)'.format(avg_citations, paper_count)
else:
    result = 'No ACM papers found in 2018 citations data'

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
