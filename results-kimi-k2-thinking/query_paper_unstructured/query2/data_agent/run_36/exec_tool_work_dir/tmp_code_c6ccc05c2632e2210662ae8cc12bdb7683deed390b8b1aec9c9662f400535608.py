code = """import json
import pandas as pd

# Load the full citations data for 2018
citations_path = locals()['var_functions.query_db:2']
citations_data = []
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Load the full paper documents data  
papers_path = locals()['var_functions.query_db:14']
papers_data = []
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

# Convert to DataFrames
citations_df = pd.DataFrame(citations_data)
papers_df = pd.DataFrame(papers_data)

# Clean and prepare citations data
citations_df['citation_count'] = citations_df['citation_count'].astype(int)
citations_df['citation_year'] = citations_df['citation_year'].astype(int)

# Extract title from filename
papers_df['title'] = papers_df['filename'].str.replace('.txt', '')

# Extract source from text content
def extract_source(text):
    if pd.isna(text):
        return None
    
    text_lower = text.lower()
    
    # Check for ACM indicators
    if 'acm' in text_lower or 'permissions@acm.org' in text_lower or 'http://doi.acm.org' in text_lower:
        return 'ACM'
    
    # Check for IEEE indicators
    if 'ieee' in text_lower or 'ieeexplore' in text_lower:
        return 'IEEE'
    
    # Check for PubMed indicators
    if 'pubmed' in text_lower or 'nih' in text_lower or 'pmid' in text_lower:
        return 'PubMed'
    
    return None

# Apply source extraction
papers_df['source'] = papers_df['text'].apply(extract_source)

# Merge citations with paper info on title
merged_df = citations_df.merge(papers_df, on='title', how='inner')

# Filter for ACM papers cited in 2018
acm_papers_2018 = merged_df[merged_df['source'] == 'ACM']

# Calculate average citation count
if not acm_papers_2018.empty:
    avg_citations = acm_papers_2018['citation_count'].mean()
    count = len(acm_papers_2018)
    total_citations = acm_papers_2018['citation_count'].sum()
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers': count,
        'total_citations': int(total_citations)
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers': 0,
        'total_citations': 0,
        'note': 'No ACM papers found in 2018 citations'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
