code = """import pandas as pd
import json

# Load citation data
with open(locals()['var_function-call-18218505575936351644'], 'r') as f:
    citation_data = json.load(f)
citations_df = pd.DataFrame(citation_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load paper document data
with open(locals()['var_function-call-15512037662651593729'], 'r') as f:
    paper_docs_data = json.load(f)
paper_docs_df = pd.DataFrame(paper_docs_data)

# Extract title and source from paper_docs_df
paper_docs_df['title'] = paper_docs_df['filename'].apply(lambda x: x.replace('.txt', ''))

def extract_source(text):
    if "ACM" in text:
        return "ACM"
    return None

paper_docs_df['source'] = paper_docs_df['text'].apply(extract_source)

# Filter for ACM papers
acm_papers_df = paper_docs_df[paper_docs_df['source'] == 'ACM']

# Merge with citations data
merged_df = pd.merge(citations_df, acm_papers_df, on='title', how='inner')

# Calculate average citation count
average_citation_count = merged_df['citation_count'].mean()

print("__RESULT__:")
print(json.dumps(average_citation_count))"""

env_args = {'var_function-call-18218505575936351644': 'file_storage/function-call-18218505575936351644.json', 'var_function-call-15512037662651593729': 'file_storage/function-call-15512037662651593729.json'}

exec(code, env_args)
