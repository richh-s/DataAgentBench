code = """import json
import pandas as pd

# Load citations data  
citations_file = var_functions.query_db:7
with open(citations_file) as f:
    citations_2018 = json.load(f)

# Load paper documents data
papers_file = var_functions.query_db:3
with open(papers_file) as f:
    paper_docs = json.load(f)

# Create DataFrames
citations_df = pd.DataFrame(citations_2018)

# Extract ACM papers from text
paper_titles = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    if 'ACM' in text or 'acm.org' in text:
        title = filename.replace('.txt', '') if filename else ''
        paper_titles.append(title)

# Filter citations for ACM papers
acm_citations = citations_df[citations_df['title'].isin(paper_titles)]

# Calculate average
if not acm_citations.empty:
    avg = acm_citations['citation_count'].astype(float).mean()
    count = len(acm_citations)
    result = f"Average: {avg:.2f} citations from {count} ACM papers"
else:
    result = "No ACM papers found"

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
