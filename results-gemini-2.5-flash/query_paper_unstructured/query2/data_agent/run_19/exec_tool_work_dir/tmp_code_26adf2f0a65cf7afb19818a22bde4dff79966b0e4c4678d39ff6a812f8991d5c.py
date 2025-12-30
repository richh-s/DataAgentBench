code = """import json
import pandas as pd
import re

# Load citation data
with open(locals()['var_function-call-233801284919248895'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load paper documents
with open(locals()['var_function-call-5743369089668728071'], 'r') as f:
    paper_docs_data = json.load(f)

# Extract ACM paper titles by parsing the 'text' field
acm_titles = []
for doc in paper_docs_data:
    title = doc['filename'].replace('.txt', '')
    text_content = doc['text']
    # Search for 'ACM' in the text, usually preceded by 'source' or 'publisher' in a case-insensitive way
    if re.search(r'(source|publisher):\s*ACM', text_content, re.IGNORECASE):
        acm_titles.append(title)

# Filter citations dataframe to include only ACM papers
filtered_citations_df = citations_df[citations_df['title'].isin(acm_titles)]

# Calculate the average citation count for ACM papers
average_citation_count = filtered_citations_df['citation_count'].mean()

print('__RESULT__:')
print(json.dumps(average_citation_count))"""

env_args = {'var_function-call-233801284919248895': 'file_storage/function-call-233801284919248895.json', 'var_function-call-1065165148221286602': [], 'var_function-call-5743369089668728071': 'file_storage/function-call-5743369089668728071.json'}

exec(code, env_args)
