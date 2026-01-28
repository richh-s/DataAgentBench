code = """import pandas as pd
import json

citations_data = pd.read_json(locals()['var_function-call-8518687322063148061'])
papers_data = pd.read_json(locals()['var_function-call-13645814686647943809'])

# Extract title from filename
papers_data['title'] = papers_data['filename'].apply(lambda x: x.replace('.txt', ''))

# Function to extract source from paper text
def extract_source(text):
    if "ACM" in text:
        return "ACM"
    elif "IEEE" in text:
        return "IEEE"
    else:
        return None

papers_data['source'] = papers_data['text'].apply(extract_source)

# Merge citations with paper information
merged_data = pd.merge(citations_data, papers_data, on='title')

# Filter for ACM papers
acm_papers = merged_data[merged_data['source'] == 'ACM']

# Calculate the average citation count for ACM papers
# Convert citation_count to numeric first
acm_papers['citation_count'] = pd.to_numeric(acm_papers['citation_count'])
average_citation_count = acm_papers['citation_count'].mean()

print("__RESULT__:")
print(json.dumps(average_citation_count))"""

env_args = {'var_function-call-8518687322063148061': 'file_storage/function-call-8518687322063148061.json', 'var_function-call-13645814686647943809': 'file_storage/function-call-13645814686647943809.json'}

exec(code, env_args)
