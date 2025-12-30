code = """import json
import re
import pandas as pd

# Load citation data
with open(locals()['var_function-call-9866274534013825103'], 'r') as f:
    citation_data = json.load(f)
citation_df = pd.DataFrame(citation_data)
citation_df['citation_count'] = pd.to_numeric(citation_df['citation_count'])

# Load all paper documents
with open(locals()['var_function-call-7973633068397485439'], 'r') as f:
    paper_docs = json.load(f)

# Extract relevant information from paper documents
papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace(".txt", "")
    text = doc['text']

    # Check if 'CHI' is in the text to identify CHI papers
    is_chi_paper = 'CHI' in text.upper()

    papers_info.append({
        'title': title,
        'is_chi_paper': is_chi_paper
    })

papers_df = pd.DataFrame(papers_info)

# Filter for CHI papers
chi_papers_df = papers_df[papers_df['is_chi_paper'] == True]

# Join with citation data
merged_df = pd.merge(chi_papers_df, citation_df, on='title', how='inner')

# Calculate total citation count and convert to int for JSON serialization
total_citations = int(merged_df['citation_count'].sum())

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-9866274534013825103': 'file_storage/function-call-9866274534013825103.json', 'var_function-call-12458711442629031814': 'file_storage/function-call-12458711442629031814.json', 'var_function-call-16518493279907426009': 'file_storage/function-call-16518493279907426009.json', 'var_function-call-7973633068397485439': 'file_storage/function-call-7973633068397485439.json'}

exec(code, env_args)
