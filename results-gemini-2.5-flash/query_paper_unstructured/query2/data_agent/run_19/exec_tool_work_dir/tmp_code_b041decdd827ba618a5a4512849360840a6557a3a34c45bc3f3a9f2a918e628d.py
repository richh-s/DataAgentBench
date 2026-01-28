code = """import json
import pandas as pd
import re
import math

# Load citation data from call-1
with open(locals()['var_function-call-233801284919248895'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load paper documents from call-3 (all papers)
with open(locals()['var_function-call-5743369089668728071'], 'r') as f:
    paper_docs_data = json.load(f)

# Extract paper titles that contain 'ACM' in their text content
acm_titles = []
for doc in paper_docs_data:
    title = doc['filename'].replace('.txt', '')
    text_content = doc['text']
    # Search for 'ACM' anywhere in the text content (case-insensitive)
    if re.search(r'ACM', text_content, re.IGNORECASE):
        acm_titles.append(title)

# Filter citations dataframe to include only papers identified as ACM
filtered_citations_df = citations_df[citations_df['title'].isin(acm_titles)]

# Calculate the average citation count for these ACM papers
average_citation_count = filtered_citations_df['citation_count'].mean()

# Handle NaN case for JSON serialization
if math.isnan(average_citation_count):
    result = "No ACM papers found or no citation data for ACM papers."
else:
    result = str(average_citation_count)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-233801284919248895': 'file_storage/function-call-233801284919248895.json', 'var_function-call-1065165148221286602': [], 'var_function-call-5743369089668728071': 'file_storage/function-call-5743369089668728071.json', 'var_function-call-11544588049775542127': nan}

exec(code, env_args)
