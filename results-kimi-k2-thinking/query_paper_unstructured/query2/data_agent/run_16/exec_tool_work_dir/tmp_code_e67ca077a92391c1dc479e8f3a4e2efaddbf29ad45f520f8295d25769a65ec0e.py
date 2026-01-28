code = """import json
import pandas as pd

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

# Function to check if paper is from ACM based on text content
def is_acm_paper(text):
    if not text:
        return False
    text_upper = text.upper()
    # Look for ACM indicators
    acm_indicators = ['ACM', 'ASSOCIATION FOR COMPUTING MACHINERY']
    for indicator in acm_indicators:
        if indicator in text_upper:
            return True
    return False

# Apply the function to identify ACM papers
docs_df['is_acm'] = docs_df['text'].apply(is_acm_paper)

# Filter ACM papers
acm_docs_df = docs_df[docs_df['is_acm']][['title']].copy()

# Merge with citations data
merged_df = pd.merge(citations_df, acm_docs_df, on='title', how='inner')

# Calculate average citation count
if not merged_df.empty:
    # Convert citation_count to numeric
    merged_df['citation_count'] = pd.to_numeric(merged_df['citation_count'])
    avg_citations = merged_df['citation_count'].mean()
    count_papers = len(merged_df)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'number_of_acm_papers': count_papers
    }
else:
    result = {
        'average_citation_count': 0,
        'number_of_acm_papers': 0,
        'message': 'No ACM papers found in 2018 citations'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
