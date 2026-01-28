code = """import json
import pandas as pd

# Load citation data from call-1
with open(locals()['var_function-call-233801284919248895'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load paper documents from call-3
with open(locals()['var_function-call-5743369089668728071'], 'r') as f:
    paper_docs_data = json.load(f)

# Extract ACM papers
acm_papers = []
for doc in paper_docs_data:
    if "source: ACM" in doc['text']:
        title = doc['filename'].replace('.txt', '')
        acm_papers.append({'title': title})

acm_df = pd.DataFrame(acm_papers)

# Merge dataframes
merged_df = pd.merge(citations_df, acm_df, on='title', how='inner')

# Calculate average citation count
average_citation_count = merged_df['citation_count'].mean()

print('__RESULT__:')
print(json.dumps(average_citation_count))"""

env_args = {'var_function-call-233801284919248895': 'file_storage/function-call-233801284919248895.json', 'var_function-call-1065165148221286602': [], 'var_function-call-5743369089668728071': 'file_storage/function-call-5743369089668728071.json'}

exec(code, env_args)
