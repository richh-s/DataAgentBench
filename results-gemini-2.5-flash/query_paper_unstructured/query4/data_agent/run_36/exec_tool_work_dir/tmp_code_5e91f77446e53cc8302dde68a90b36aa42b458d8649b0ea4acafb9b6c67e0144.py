code = """import pandas as pd
import re
import json

# Load citation data
with open(locals()['var_function-call-1105675117886834803'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load paper documents
with open(locals()['var_function-call-12491728221895612274'], 'r') as f:
    paper_docs = json.load(f)

# Process paper documents to extract title, year, and domain
papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Extract year (e.g., "UbiComp '16" or "publication year: 2016")
    year_match = re.search(r"(?:\'|UbiComp |publication year: )(\d{4})", text)
    year = int(year_match.group(1)) if year_match else None

    # Extract domain
    domain_match = re.search(r"domain: ([a-zA-Z0-9, ]+)", text)
    domain = domain_match.group(1).lower() if domain_match else ""

    papers_info.append({'title': title, 'year': year, 'domain': domain})

papers_df = pd.DataFrame(papers_info)

# Filter papers for 2016 and 'physical activity' domain
filtered_papers_df = papers_df[
    (papers_df['year'] == 2016) & 
    (papers_df['domain'].str.contains('physical activity'))
]

# Merge with citations data
merged_df = pd.merge(filtered_papers_df, citations_df, on='title', how='inner')

# Calculate total citation count for each paper
result = merged_df.groupby('title')['citation_count'].sum().reset_index()
result.rename(columns={'citation_count': 'total_citation_count'}, inplace=True)

print('__RESULT__:')
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-1105675117886834803': 'file_storage/function-call-1105675117886834803.json', 'var_function-call-12491728221895612274': 'file_storage/function-call-12491728221895612274.json'}

exec(code, env_args)
