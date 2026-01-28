code = """import json
import pandas as pd

# Load the 2018 citations data
citations_2018_file = var_functions.query_db:7
with open(citations_2018_file, 'r') as f:
    citations_2018 = json.load(f)

# Load the paper documents data
paper_docs_file_path = var_functions.query_db:3
with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

# Convert to DataFrames
citations_df = pd.DataFrame(citations_2018)

# Create a list to store paper information extracted from MongoDB
paper_info_list = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract source/publisher information
    # Look for ACM, IEEE, PubMed in the text
    source = []
    if 'ACM' in text or 'acm.org' in text:
        source.append('ACM')
    if 'IEEE' in text or 'ieee.org' in text:
        source.append('IEEE')
    if 'PubMed' in text:
        source.append('PubMed')
    
    # Store as comma-separated string if multiple sources
    source_str = ', '.join(source) if source else ''
    
    paper_info_list.append({
        'title': title,
        'source': source_str
    })

# Convert to DataFrame
papers_df = pd.DataFrame(paper_info_list)

# Join citations with paper info
citations_with_source = pd.merge(citations_df, papers_df, on='title', how='left')

# Filter for papers published by ACM (source contains ACM)
acm_papers = citations_with_source[citations_with_source['source'].str.contains('ACM', na=False)]

# Calculate average citation count
if not acm_papers.empty:
    acm_papers['citation_count'] = pd.to_numeric(acm_papers['citation_count'], errors='coerce')
    avg_citations = acm_papers['citation_count'].mean()
    count = len(acm_papers)
    result = f"Average citation count: {avg_citations:.2f} (based on {count} ACM papers cited in 2018)"
else:
    result = "No ACM papers found in 2018 citations"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
