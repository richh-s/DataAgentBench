code = """import json
import pandas as pd
import re

# Load citations data for 2018
citations_file = locals()['var_functions.query_db:5']
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

citations_df = pd.DataFrame(citations_2018)
print('Citations 2018 shape:', citations_df.shape)
print('Sample citations:')
print(citations_df.head())

# Load paper documents
papers_file = locals()['var_functions.query_db:16']
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

papers_df = pd.DataFrame(paper_docs)
print('\nPaper documents shape:', papers_df.shape)

# Extract title from filename
papers_df['title'] = papers_df['filename'].str.replace('\.txt$', '', regex=True)

# Function to extract source from text
def extract_source(text):
    if not isinstance(text, str):
        return None
    
    text_upper = text.upper()
    
    # Look for ACM indicators
    acm_patterns = [
        'ACM ',
        'ASSOCIATION FOR COMPUTING MACHINERY',
        'PERMISSION@ACM.ORG',
        'ACM CLASSIFICATION KEYWORDS'
    ]
    
    for pattern in acm_patterns:
        if pattern in text_upper:
            return 'ACM'
    
    return None

# Apply source extraction
papers_df['source'] = papers_df['text'].apply(extract_source)

# Count ACM papers
acm_papers = papers_df[papers_df['source'] == 'ACM']
print('\nTotal ACM papers:', len(acm_papers))
print('Sample ACM papers:')
print(acm_papers[['title', 'source']].head())

# Merge citations with papers on title
merged_df = pd.merge(citations_df, papers_df[['title', 'source']], 
                     left_on='title', right_on='title', how='inner')

print('\nMerged shape:', merged_df.shape)
print('Merged sample:')
print(merged_df.head())

# Filter for ACM papers cited in 2018
acm_citations_2018 = merged_df[merged_df['source'] == 'ACM']
print('\nACM papers cited in 2018:', len(acm_citations_2018))
print('Sample ACM citations in 2018:')
print(acm_citations_2018[['title', 'citation_count']].head())

# Calculate average citation count
if not acm_citations_2018.empty:
    avg_citations = acm_citations_2018['citation_count'].astype(float).mean()
    print('\nAverage citation count for ACM papers cited in 2018:', avg_citations)
    
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers_cited': len(acm_citations_2018),
        'total_citations': acm_citations_2018['citation_count'].astype(float).sum()
    }
else:
    print('No ACM papers found in 2018 citations')
    result = {'average_citation_count': 0, 'total_acm_papers_cited': 0, 'total_citations': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
