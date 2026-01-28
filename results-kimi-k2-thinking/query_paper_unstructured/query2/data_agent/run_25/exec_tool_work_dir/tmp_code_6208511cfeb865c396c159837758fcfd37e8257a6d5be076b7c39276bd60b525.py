code = """import json
import pandas as pd
import re

# Load the citations data for 2018
citations_var_name = 'var_functions.query_db:0'
citations_file = locals().get(citations_var_name)
citations_data = []

if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
elif isinstance(citations_file, list):
    citations_data = citations_file

# Create DataFrame from citations
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'], errors='coerce')

# Load the paper documents
papers_var_name = 'var_functions.query_db:1'
papers_file = locals().get(papers_var_name)
papers_data = []

if isinstance(papers_file, str) and papers_file.endswith('.json'):
    with open(papers_file, 'r') as f:
        papers_data = json.load(f)
elif isinstance(papers_file, list):
    papers_data = papers_file

# Extract filename without .txt extension and match with title
paper_info = []
for paper in papers_data:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    if not title or not text:
        continue
    
    # Extract source/publisher from text
    
    # Look for source info in the text (common patterns)
    # ACM copyright notice
    acm_patterns = [
        r'ACM [0-9]{4}',
        r'ACM Classification',
        r'Permission to make digital or hard copies.*ACM',
        r'Copyright [0-9]{4}.*ACM',
        r'Published by ACM',
        r'https://doi.org/10.1145'  # ACM DOI pattern
    ]
    
    ieee_patterns = [
        r'IEEE [0-9]{4}',
        r'IEEE  Transactions',
        r'IEEE  International',
        r'IEEE  Conference',
        r'Copyright.*IEEE',
        r'10.1109'  # IEEE DOI pattern
    ]
    
    # Check for ACM
    is_acm = False
    is_ieee = False
    
    for pattern in acm_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_acm = True
            break
    
    for pattern in ieee_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_ieee = True
            break
    
    if is_acm:
        source = 'ACM'
    elif is_ieee:
        source = 'IEEE'
    else:
        # Try to find other sources
        if re.search(r'PubMed', text, re.IGNORECASE):
            source = 'PubMed'
        elif re.search(r'Springer', text, re.IGNORECASE):
            source = 'Springer'
        elif re.search(r'Elsevier', text, re.IGNORECASE) or re.search(r'10.1016', text):
            source = 'Elsevier'
        elif re.search(r'MDPI', text, re.IGNORECASE):
            source = 'MDPI'
        else:
            source = 'Unknown'
    
    paper_info.append({'title': title.strip(), 'source': source})

# Create paper info DataFrame
paper_df = pd.DataFrame(paper_info)

# Merge citations with paper info on title
merged_df = citations_df.merge(paper_df, on='title', how='inner')

# Filter for ACM papers
acm_papers = merged_df[merged_df['source'] == 'ACM']

# Calculate average citation count
if not acm_papers.empty:
    avg_citations = acm_papers['citation_count'].mean()
    count = len(acm_papers)
    result = {
        'average_citation_count': round(float(avg_citations), 2),
        'number_of_acm_papers_cited_in_2018': count
    }
else:
    result = {
        'average_citation_count': 0, 
        'number_of_acm_papers_cited_in_2018': 0, 
        'message': 'No ACM papers found in citation data'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
