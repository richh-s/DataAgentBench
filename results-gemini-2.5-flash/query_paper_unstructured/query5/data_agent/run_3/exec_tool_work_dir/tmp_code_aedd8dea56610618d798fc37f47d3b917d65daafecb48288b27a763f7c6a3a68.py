code = """import json
import pandas as pd
import re

# Load citations data for 2020
with open(locals()['var_function-call-688809817332979845'], 'r') as f:
    citations_2020_data = json.load(f)
citations_2020_df = pd.DataFrame(citations_2020_data)
citations_2020_df['citation_count'] = pd.to_numeric(citations_2020_df['citation_count'])

# Load paper documents data
with open(locals()['var_function-call-5811567055081790187'], 'r') as f:
    paper_docs_data = json.load(f)
paper_docs_df = pd.DataFrame(paper_docs_data)

# Extract title from filename
paper_docs_df['title'] = paper_docs_df['filename'].apply(lambda x: x.replace('.txt', ''))

# Function to extract venue, focusing on 'CHI'
def extract_venue(text):
    # Look for common venue patterns in the first few lines
    match = re.search(r'(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)(\s\'?\d{2}|\s\d{4})?', text, re.IGNORECASE)
    if match:
        return match.group(1).upper()
    # If not found in the initial search, look for 'CHI' anywhere in the text as a general check
    if 'CHI' in text.upper():
        return 'CHI'
    return None

# Apply venue extraction
paper_docs_df['venue'] = paper_docs_df['text'].apply(extract_venue)

# Filter for papers presented at CHI
chi_papers_df = paper_docs_df[paper_docs_df['venue'] == 'CHI']

# Merge with citations data
merged_df = pd.merge(chi_papers_df, citations_2020_df, on='title', how='inner')

# Calculate total citation count
total_citations = merged_df['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-688809817332979845': 'file_storage/function-call-688809817332979845.json', 'var_function-call-13029841251129633830': 'file_storage/function-call-13029841251129633830.json', 'var_function-call-8141991743298175387': {'status': 'ready for next step'}, 'var_function-call-5811567055081790187': 'file_storage/function-call-5811567055081790187.json'}

exec(code, env_args)
