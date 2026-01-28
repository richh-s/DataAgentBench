code = """import json
import pandas as pd

# Get the data from storage
citations_data = locals()['var_functions.query_db:7']
papers_data = locals()['var_functions.query_db:3']

# Process citations
citations_df = pd.DataFrame(citations_data)

# Extract ACM papers
acm_titles = []
for doc in papers_data:
    if 'ACM' in doc.get('text', ''):
        title = doc.get('filename', '').replace('.txt', '')
        acm_titles.append(title)

# Filter and calculate average
acm_citations = citations_df[citations_df['title'].isin(acm_titles)]

if not acm_citations.empty:
    avg = acm_citations['citation_count'].astype(float).mean()
    result = f'Average citations for ACM papers in 2018: {avg:.2f}'
else:
    result = 'No ACM papers found'

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
