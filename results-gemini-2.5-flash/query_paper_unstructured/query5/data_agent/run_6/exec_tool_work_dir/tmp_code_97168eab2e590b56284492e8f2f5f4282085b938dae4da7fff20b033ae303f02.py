code = """import json
import pandas as pd

citations_df = pd.DataFrame(json.load(open(locals()['var_function-call-3484020798541970759'])))
paper_docs_df = pd.DataFrame(json.load(open(locals()['var_function-call-11265473742429461253'])))

# Extract title from filename
paper_docs_df['title'] = paper_docs_df['filename'].apply(lambda x: x.replace('.txt', ''))

# Function to extract venue from text
def extract_venue(text):
    if 'CHI' in text:
        return 'CHI'
    return None

paper_docs_df['venue'] = paper_docs_df['text'].apply(extract_venue)

# Filter for CHI papers
chi_papers_df = paper_docs_df[paper_docs_df['venue'] == 'CHI']

# Merge with citations data
merged_df = pd.merge(chi_papers_df, citations_df, on='title', how='inner')

# Convert 'citation_count' to numeric, handling potential errors and non-numeric values
merged_df['citation_count'] = pd.to_numeric(merged_df['citation_count'], errors='coerce')

# Calculate total citation count
total_citations = merged_df['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(total_citations))"""

env_args = {'var_function-call-3484020798541970759': 'file_storage/function-call-3484020798541970759.json', 'var_function-call-11265473742429461253': 'file_storage/function-call-11265473742429461253.json'}

exec(code, env_args)
