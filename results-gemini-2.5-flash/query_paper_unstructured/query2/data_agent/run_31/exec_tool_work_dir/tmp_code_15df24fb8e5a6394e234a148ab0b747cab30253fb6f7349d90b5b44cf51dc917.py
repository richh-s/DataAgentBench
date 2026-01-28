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

# Extract paper information and identify ACM papers
extracted_papers = []
for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    source = None

    # Check for strong indicators of ACM publisher in the paper text
    if ("ACM" in text and 
        ("Copyright" in text or 
         "permissions@acm.org" in text.lower() or 
         "ACM Digital Library" in text or 
         "Association for Computing Machinery" in text)):
        source = "ACM"

    extracted_papers.append({'title': title, 'source': source})

df_papers = pd.DataFrame(extracted_papers)

# Filter for ACM papers
df_acm_papers = df_papers[df_papers['source'] == 'ACM']

# Merge with citation data
df_merged = pd.merge(df_acm_papers, df_citations, on='title', how='inner')

# Calculate the average citation count
if df_merged.empty or df_merged['citation_count'].count() == 0:
    result_string = "No ACM papers found with citations in 2018 or no citation data available for ACM papers."
else:
    average_citation_count = df_merged['citation_count'].mean()
    result_string = str(average_citation_count) # Convert to string for consistent output

print('__RESULT__:')
print(json.dumps(result_string))"""

env_args = {'var_function-call-17160475346575029016': 'file_storage/function-call-17160475346575029016.json', 'var_function-call-2159275579680613019': 'file_storage/function-call-2159275579680613019.json', 'var_function-call-16183112740951873073': nan}

exec(code, env_args)
