code = """import pandas as pd
import json
import re

# Load the paper documents data
with open(locals()['var_function-call-3565873005998525411'], 'r') as f:
    paper_docs_data = json.load(f)

# Load the citation data
with open(locals()['var_function-call-13776783906841665151'], 'r') as f:
    citations_data = json.load(f)

# Create DataFrame for paper documents
paper_docs_df = pd.DataFrame(paper_docs_data)

# Extract title from filename
paper_docs_df['title'] = paper_docs_df['filename'].apply(lambda x: x.replace('.txt', ''))

# Function to extract domain from text.
def extract_domain(text):
    domains = []
    if "food" in text.lower():
        domains.append("food")
    return list(set(domains)) # Return unique domains

paper_docs_df['extracted_domain'] = paper_docs_df['text'].apply(extract_domain)

# Filter for papers in 'food' domain
food_papers_df = paper_docs_df[paper_docs_df['extracted_domain'].apply(lambda x: 'food' in x)]

# Create DataFrame for citations
citations_df = pd.DataFrame(citations_data)

# Convert citation_count to numeric
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Merge food papers with citation data
merged_df = pd.merge(food_papers_df, citations_df, on='title', how='inner')

# Calculate total citation count for food domain and convert to int for JSON serialization
total_citation_count = int(merged_df['citation_count'].sum())

print("__RESULT__:")
print(json.dumps(total_citation_count))"""

env_args = {'var_function-call-10843417409462739428': ['Citations', 'sqlite_sequence'], 'var_function-call-13776783906841665151': 'file_storage/function-call-13776783906841665151.json', 'var_function-call-15248009430255834493': ['paper_docs'], 'var_function-call-3565873005998525411': 'file_storage/function-call-3565873005998525411.json'}

exec(code, env_args)
