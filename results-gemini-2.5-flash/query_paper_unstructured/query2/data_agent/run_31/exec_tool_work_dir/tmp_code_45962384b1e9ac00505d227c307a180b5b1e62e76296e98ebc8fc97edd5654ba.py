code = """import json
import pandas as pd
import numpy as np # Import numpy to properly handle NaN values

# Load citation data
with open(locals()['var_function-call-17160475346575029016'], 'r') as f:
    citation_data = json.load(f)
df_citations = pd.DataFrame(citation_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Load paper documents
with open(locals()['var_function-call-2159275579680613019'], 'r') as f:
    paper_docs = json.load(f)

# Extract paper information and identify ACM papers using a more robust pattern
extracted_papers = []
acm_copyright_string = "Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org."

for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    source = None

    # Check for the specific ACM copyright text, which is a strong indicator.
    # Replace problematic characters for a robust match if necessary, but for now, exact string matching.
    if acm_copyright_string in text:
        source = "ACM"

    extracted_papers.append({'title': title, 'source': source})

df_papers = pd.DataFrame(extracted_papers)

# Filter for ACM papers
df_acm_papers = df_papers[df_papers['source'] == 'ACM']

# Merge with citation data
df_merged = pd.merge(df_acm_papers, df_citations, on='title', how='inner')

# Calculate the average citation count
# Check if the dataframe is empty after merging or if the mean is NaN
if df_merged.empty or np.isnan(df_merged['citation_count'].mean()):
    result_message = "No ACM papers found with citations in 2018 or no citation data available for ACM papers."
else:
    average_citation_count = df_merged['citation_count'].mean()
    result_message = str(average_citation_count)

print('__RESULT__:')
print(json.dumps(result_message))"""

env_args = {'var_function-call-17160475346575029016': 'file_storage/function-call-17160475346575029016.json', 'var_function-call-2159275579680613019': 'file_storage/function-call-2159275579680613019.json', 'var_function-call-16183112740951873073': nan}

exec(code, env_args)
