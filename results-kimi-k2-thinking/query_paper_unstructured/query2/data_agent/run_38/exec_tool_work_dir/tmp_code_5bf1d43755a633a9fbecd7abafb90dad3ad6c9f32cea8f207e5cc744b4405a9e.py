code = """import json
import pandas as pd
import re

# Load the citations data from 2018
citations_2018_json = locals()['var_functions.query_db:5']
with open(citations_2018_json, 'r') as f:
    citations_2018 = json.load(f)

citations_df = pd.DataFrame(citations_2018)
print('Citations 2018 shape:', citations_df.shape)

# Load the paper documents data
papers_json = locals()['var_functions.query_db:16']
with open(papers_json, 'r') as f:
    paper_docs = json.load(f)

papers_df = pd.DataFrame(paper_docs)
print('Paper documents shape:', papers_df.shape)

# Extract title from filename
papers_df['title'] = papers_df['filename'].str.replace(r'\.txt$', '', regex=True)

# Function to extract source publisher from text
def extract_source(text):
    if not isinstance(text, str):
        return None
    
    text_upper = text.upper()
    
    # Check for ACM
    acm_indicators = ['ACM ', 'ASSOCIATION FOR COMPUTING MACHINERY', 'PERMISSION@ACM.ORG']
    for indicator in acm_indicators:
        if indicator in text_upper:
            return 'ACM'
    
    return None

# Extract source for each paper
papers_df['source'] = papers_df['text'].apply(extract_source)
print('Total ACM papers found:', (papers_df['source'] == 'ACM').sum())

# Merge citations with papers
merged_df = pd.merge(citations_df, papers_df[['title', 'source']], on='title', how='inner')
print('Merged shape:', merged_df.shape)

# Filter for ACM papers cited in 2018
acm_citations = merged_df[merged_df['source'] == 'ACM']
print('ACM citations in 2018:', len(acm_citations))

# Calculate average citation count
if not acm_citations.empty:
    avg_citations = acm_citations['citation_count'].astype(float).mean()
    total_papers = len(acm_citations)
    total_citations = acm_citations['citation_count'].astype(float).sum()
    
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers_cited': total_papers,
        'total_citations': int(total_citations)
    }
    print('Average citation count:', avg_citations)
else:
    result = {'average_citation_count': 0, 'total_acm_papers_cited': 0, 'total_citations': 0}
    print('No ACM papers found')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
