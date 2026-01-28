code = """import json
import pandas as pd
import re

# Read the citations data from the file
citations_file_path = locals()['var_functions.query_db:0']
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

# Read the paper documents data from the file
docs_file_path = locals()['var_functions.query_db:2']
with open(docs_file_path, 'r') as f:
    docs_data = json.load(f)

# Create DataFrames
citations_df = pd.DataFrame(citations_data)
docs_df = pd.DataFrame(docs_data)

# Extract title from filename (remove .txt extension)
docs_df['title'] = docs_df['filename'].str.replace('.txt$', '', regex=True)

# More sophisticated function to check if paper is from ACM
def is_acm_paper(text):
    if not text:
        return False
    
    text_upper = text.upper()
    
    # Look for ACM copyright pattern (common in ACM papers)
    if re.search(r'COPYRIGHT.*\d{4}.*©.*ACM', text):
        return True
    
    # Look for ACM publication patterns
    if re.search(r'ACM.*\d{4}.*\$15\.00', text):
        return True
        
    # Look for specific ACM conference indicators
    acm_conferences = ['CHI', 'CSCW', 'DIS', 'UIST', 'UBICOMP', 'PERVASIVE', 'TEI', 'IUI', 'WWW']
    for conf in acm_conferences:
        # Check if it's an ACM conference by looking for both ACM and conference name
        if 'ACM' in text_upper and conf in text_upper:
            return True
    
    # Direct ACM mentions in copyright/permission blocks
    if 'ASSOCIATION FOR COMPUTING MACHINERY' in text_upper:
        return True
        
    return False

# Apply the function to identify ACM papers
docs_df['is_acm'] = docs_df['text'].apply(is_acm_paper)

# Count total ACM papers detected
total_acm_papers = docs_df['is_acm'].sum()

# Filter ACM papers
acm_docs_df = docs_df[docs_df['is_acm']][['title']].copy()

# Merge with citations data for 2018
merged_df = pd.merge(citations_df, acm_docs_df, on='title', how='inner')

# Calculate average citation count if we have data
if not merged_df.empty:
    # Convert citation_count to numeric
    merged_df['citation_count'] = pd.to_numeric(merged_df['citation_count'])
    avg_citations = merged_df['citation_count'].mean()
    count_papers = len(merged_df)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'number_of_acm_papers_cited_in_2018': count_papers,
        'total_acm_papers_in_database': int(total_acm_papers)
    }
else:
    result = {
        'average_citation_count': None,
        'number_of_acm_papers_cited_in_2018': 0,
        'total_acm_papers_in_database': int(total_acm_papers),
        'message': 'Found ACM papers in database but none have 2018 citations'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'average_citation_count': 68.5, 'number_of_acm_papers': 2}}

exec(code, env_args)
