code = """import json
import pandas as pd

# Load citation data
with open(locals()['var_function-call-17160475346575029016'], 'r') as f:
    citation_data = json.load(f)
df_citations = pd.DataFrame(citation_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Load paper documents
with open(locals()['var_function-call-2159275579680613019'], 'r') as f:
    paper_docs = json.load(f)

# Extract paper information
extracted_papers = []
for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    source = None

    # Simple regex for finding source. 'ACM' is often near 'Copyright' or 'Permission'
    if "ACM" in text:
        # Check for specific patterns that indicate ACM as the publisher
        if "ACM Copyright" in text or "Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org." in text:
            source = "ACM"

    extracted_papers.append({'title': title, 'source': source})

df_papers = pd.DataFrame(extracted_papers)

# Filter for ACM papers
df_acm_papers = df_papers[df_papers['source'] == 'ACM']

# Merge with citation data
df_merged = pd.merge(df_acm_papers, df_citations, on='title', how='inner')

# Calculate the average citation count
average_citation_count = df_merged['citation_count'].mean()

print('__RESULT__:')
print(json.dumps(average_citation_count))"""

env_args = {'var_function-call-17160475346575029016': 'file_storage/function-call-17160475346575029016.json', 'var_function-call-2159275579680613019': 'file_storage/function-call-2159275579680613019.json'}

exec(code, env_args)
