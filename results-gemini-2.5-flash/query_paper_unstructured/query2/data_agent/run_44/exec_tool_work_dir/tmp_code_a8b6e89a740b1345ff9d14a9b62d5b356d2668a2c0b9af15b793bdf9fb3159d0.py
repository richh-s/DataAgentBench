code = """import json
import pandas as pd
import re

# Load citation data
with open(locals()['var_function-call-6778768740193289220'], 'r') as f:
    citation_data = json.load(f)
citation_df = pd.DataFrame(citation_data)
citation_df['citation_count'] = pd.to_numeric(citation_df['citation_count'])

# Load paper documents data
with open(locals()['var_function-call-15127015561078301414'], 'r') as f:
    paper_docs_data = json.load(f)
paper_docs_df = pd.DataFrame(paper_docs_data)

# Extract title from filename for joining
paper_docs_df['title'] = paper_docs_df['filename'].apply(lambda x: x.replace('.txt', ''))

# Function to extract source from paper text
def extract_source(text):
    match = re.search(r'Copyright \d{4} \u00a9 (ACM|IEEE|PubMed)', text)
    if match:
        return match.group(1)
    return None

paper_docs_df['source'] = paper_docs_df['text'].apply(extract_source)

# Filter for ACM papers
acm_papers_df = paper_docs_df[paper_docs_df['source'] == 'ACM']

# Merge with citation data
merged_df = pd.merge(acm_papers_df, citation_df, on='title', how='inner')

# Calculate average citation count
average_citation_count = merged_df['citation_count'].mean()

print("__RESULT__:")
print(json.dumps(average_citation_count))"""

env_args = {'var_function-call-6778768740193289220': 'file_storage/function-call-6778768740193289220.json', 'var_function-call-15127015561078301414': 'file_storage/function-call-15127015561078301414.json'}

exec(code, env_args)
