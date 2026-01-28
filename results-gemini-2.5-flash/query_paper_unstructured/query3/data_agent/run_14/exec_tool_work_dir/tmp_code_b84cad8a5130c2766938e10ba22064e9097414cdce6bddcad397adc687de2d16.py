code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-89421489897449482']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

parsed_papers_data = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')

    # Year extraction - look in the first 2000 characters for a year pattern
    year = None
    year_match = re.search(r'\b(19|20)\d{2}\b', text[:2000])
    if year_match:
        year = int(year_match.group(0))

    # Contribution extraction - check for 'empirical' keyword in the text
    contribution = None
    if re.search(r'\bempirical\b', text, re.IGNORECASE):
        contribution = 'empirical'

    parsed_papers_data.append({'title': title, 'year': year, 'contribution': contribution})

df_papers = pd.DataFrame(parsed_papers_data)

# Filter for papers published after 2016 with 'empirical' contribution
filtered_papers = df_papers[(df_papers['year'] > 2016) & (df_papers['contribution'] == 'empirical')]

empirical_titles = filtered_papers['title'].tolist()

print('__RESULT__:')
print(json.dumps(empirical_titles))"""

env_args = {'var_function-call-3207410245806214601': ['paper_docs'], 'var_function-call-89421489897449482': 'file_storage/function-call-89421489897449482.json'}

exec(code, env_args)
