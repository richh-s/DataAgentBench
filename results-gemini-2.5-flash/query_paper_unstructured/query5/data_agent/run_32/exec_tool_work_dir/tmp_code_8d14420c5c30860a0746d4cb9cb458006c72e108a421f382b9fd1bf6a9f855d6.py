code = """import pandas as pd
import json
import re

# Load citation data
with open(locals()['var_function-call-7332512200166014028'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)

# Convert citation_count to numeric, handling potential non-numeric values
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'], errors='coerce').fillna(0).astype(int)

# Load paper documents
with open(locals()['var_function-call-17024158260398121326'], 'r') as f:
    paper_docs_data = json.load(f)

# Extract paper information (title, venue)
papers_info = []
for doc in paper_docs_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    venue_match = re.search(r'\b(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\b', text, re.IGNORECASE)
    venue = venue_match.group(0).upper() if venue_match else None
    papers_info.append({'title': title, 'venue': venue})

papers_df = pd.DataFrame(papers_info)

# Merge citations with paper information
merged_df = pd.merge(citations_df, papers_df, on='title', how='inner')

# Filter for papers presented at CHI
chi_papers_df = merged_df[merged_df['venue'] == 'CHI']

# Calculate total citation count for CHI papers
total_chi_citations = chi_papers_df['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(total_chi_citations))"""

env_args = {'var_function-call-7332512200166014028': 'file_storage/function-call-7332512200166014028.json', 'var_function-call-17024158260398121326': 'file_storage/function-call-17024158260398121326.json'}

exec(code, env_args)
