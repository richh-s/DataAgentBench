code = """import json
import pandas as pd
import re

# Load data from storage
citations_data_path = locals()['var_function-call-11138316338384426243']
paper_docs_data_path = locals()['var_function-call-10055513205149118217']

with open(citations_data_path, 'r') as f:
    citations_data = json.load(f)

with open(paper_docs_data_path, 'r') as f:
    paper_docs_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
# Convert citation_count to numeric, handling potential errors and missing values
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'], errors='coerce').fillna(0)

food_domain_papers = []
domain_pattern = re.compile(r"domain: ([^\n]*?)(?:\n|$)", re.DOTALL | re.IGNORECASE)

for doc in paper_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')

    match = domain_pattern.search(text)
    if match:
        domain_string = match.group(1).strip()
        if 'food' in domain_string.lower():
            food_domain_papers.append({'title': title})

food_papers_df = pd.DataFrame(food_domain_papers)

# Merge dataframes
merged_df = pd.merge(food_papers_df, citations_df, on='title', how='inner')

# Calculate total citation count
total_citations = merged_df['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(total_citations))"""

env_args = {'var_function-call-11138316338384426243': 'file_storage/function-call-11138316338384426243.json', 'var_function-call-10055513205149118217': 'file_storage/function-call-10055513205149118217.json'}

exec(code, env_args)
