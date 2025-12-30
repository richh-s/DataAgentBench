code = """import pandas as pd
import json
import re

# Load the paper documents
with open(locals()['var_function-call-5086176610189847508'], 'r') as f:
    paper_docs_data = json.load(f)

# Extract information from paper documents
papers_info = []
for doc in paper_docs_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year = None
    # Attempt to find a 4-digit year in the text
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    if year_match:
        year = int(year_match.group(0))
    
    domain = None
    # Check for 'physical activity' in the text content, case-insensitive
    if "physical activity" in text.lower():
        domain = "physical activity"

    papers_info.append({'title': title, 'year': year, 'domain': domain})

papers_df = pd.DataFrame(papers_info)

# Filter papers for year 2016 and 'physical activity' domain
filtered_papers_df = papers_df[(papers_df['year'] == 2016) & (papers_df['domain'] == 'physical activity')]

# Load the citation data
with open(locals()['var_function-call-14899754217231563024'], 'r') as f:
    citation_data = json.load(f)
citations_df = pd.DataFrame(citation_data)
citations_df['total_citations'] = pd.to_numeric(citations_df['total_citations'])

# Merge with citation data
final_df = pd.merge(filtered_papers_df, citations_df, on='title', how='inner')

# Select and rename columns
result = final_df[['title', 'total_citations']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-14899754217231563024': 'file_storage/function-call-14899754217231563024.json', 'var_function-call-5086176610189847508': 'file_storage/function-call-5086176610189847508.json', 'var_function-call-11623832545968088349': [], 'var_function-call-8083494279687056325': [], 'var_function-call-17843394603732887599': []}

exec(code, env_args)
