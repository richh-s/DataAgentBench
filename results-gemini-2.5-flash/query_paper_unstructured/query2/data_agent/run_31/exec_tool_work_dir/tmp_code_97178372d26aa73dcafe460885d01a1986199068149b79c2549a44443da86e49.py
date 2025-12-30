code = """import json
import pandas as pd
import numpy as np

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
acm_copyright_pattern = "Permission to make digital or hard copies of all or part of this work for\npersonal or classroom use is granted without fee provided that copies are \nnot made or distributed for profit or commercial advantage and that copies\nbear  this  notice  and  the  full  citation  on  the  first  page.  Copyrights  for\ncomponents  of  this  work  owned  by  others  than  ACM  must  be  honored.\nAbstracting  with  credit  is  permitted.  To  copy  otherwise,  or  republish,  to\npost on servers or to redistribute to lists, requires prior specific permission\nand/or a fee. Request permissions from permissions@acm.org."

for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    source = None

    if acm_copyright_pattern in text:
        source = "ACM"

    extracted_papers.append({'title': title, 'source': source})

df_papers = pd.DataFrame(extracted_papers)

# Filter for ACM papers
df_acm_papers = df_papers[df_papers['source'] == 'ACM']

# Merge with citation data
df_merged = pd.merge(df_acm_papers, df_citations, on='title', how='inner')

# Calculate the average citation count
if not df_merged.empty:
    average_citation_count = df_merged['citation_count'].mean()
    result_message = str(average_citation_count)
else:
    result_message = "No ACM papers found with citations in 2018 or no citation data available for ACM papers."

print('__RESULT__:')
print(json.dumps(result_message))"""

env_args = {'var_function-call-17160475346575029016': 'file_storage/function-call-17160475346575029016.json', 'var_function-call-2159275579680613019': 'file_storage/function-call-2159275579680613019.json', 'var_function-call-16183112740951873073': nan}

exec(code, env_args)
