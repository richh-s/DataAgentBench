code = """import json
import pandas as pd

# Access the storage variables properly
citations_file_path = locals()['var_functions.query_db:7']
papers_file_path = locals()['var_functions.query_db:3']

# Read the JSON files
citations_2018 = []
with open(citations_file_path, 'r') as f:
    citations_2018 = json.load(f)

paper_docs = []
with open(papers_file_path, 'r') as f:
    paper_docs = json.load(f)

# Create DataFrame for citations
citations_df = pd.DataFrame(citations_2018)

# Extract ACM paper titles by checking text content
acm_titles = []
for doc in paper_docs:
    text = doc.get('text', '')
    if 'ACM' in text:
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '') if filename else ''
        acm_titles.append(title)

# Filter citations to ACM papers only
acm_citations = citations_df[citations_df['title'].isin(acm_titles)]

# Calculate average citation count
if not acm_citations.empty:
    avg_citations = acm_citations['citation_count'].astype(float).mean()
    paper_count = len(acm_citations)
    result = 'Average citation count for ACM papers cited in 2018: {:.2f} (based on {} ACM papers)'.format(avg_citations, paper_count)
else:
    result = 'No ACM papers found in 2018 citations data'

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
