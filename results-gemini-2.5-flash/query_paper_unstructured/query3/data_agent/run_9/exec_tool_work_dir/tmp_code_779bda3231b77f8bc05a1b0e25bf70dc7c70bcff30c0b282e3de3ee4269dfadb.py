code = """import json
import pandas as pd
import re

# Load the full results from the files
with open(locals()['var_function-call-10390657380476430485'], 'r') as f:
    citations_data = json.load(f)
with open(locals()['var_function-call-15312335423605836466'], 'r') as f:
    paper_docs_data = json.load(f)

# Process citations data
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])
total_citations_df = citations_df.groupby('title')['citation_count'].sum().reset_index()

# Process paper documents
papers_list = []
for doc in paper_docs_data:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')

    year = None
    year_match = re.search(r'\b(19|20)\d{2}\b', text[:500]) # Search for a 4-digit year in the first 500 characters
    if year_match:
        year = int(year_match.group(0))

    contribution = []
    if re.search(r'empirical', text, re.IGNORECASE):
        contribution.append('empirical')
    if re.search(r'artifact', text, re.IGNORECASE):
        contribution.append('artifact')
    if re.search(r'theoretical', text, re.IGNORECASE):
        contribution.append('theoretical')
    if re.search(r'survey', text, re.IGNORECASE):
        contribution.append('survey')
    if re.search(r'methodological', text, re.IGNORECASE):
        contribution.append('methodological')

    papers_list.append({'title': title, 'year': year, 'contribution': contribution})

papers_df = pd.DataFrame(papers_list)

# Filter papers for 'empirical' contribution and year > 2016
empirical_papers_after_2016 = papers_df[
    papers_df['contribution'].apply(lambda x: 'empirical' in x) &
    (papers_df['year'] > 2016)
]

# Merge with total citations
final_result = pd.merge(empirical_papers_after_2016, total_citations_df, on='title', how='inner')

# Select and rename columns as requested
final_result = final_result[['title', 'citation_count']]
final_result = final_result.rename(columns={'citation_count': 'total citation count'})

print('__RESULT__:')
print(final_result.to_json(orient='records'))"""

env_args = {'var_function-call-10390657380476430485': 'file_storage/function-call-10390657380476430485.json', 'var_function-call-15312335423605836466': 'file_storage/function-call-15312335423605836466.json'}

exec(code, env_args)
