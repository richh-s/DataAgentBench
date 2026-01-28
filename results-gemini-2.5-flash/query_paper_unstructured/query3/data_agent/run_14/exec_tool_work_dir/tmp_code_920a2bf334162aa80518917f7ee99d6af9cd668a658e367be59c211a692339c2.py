code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-89421489897449482']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

parsed_papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')

    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    contribution_match = re.search(r'(?i)contribution[s]?:.*?(empirical|artifact|theoretical|survey|methodological)', text)
    contribution = contribution_match.group(1).lower() if contribution_match else None

    # Refine contribution extraction to check if 'empirical' is present
    if 'empirical' in text.lower():
        contribution = 'empirical'
    else:
        contribution = None

    if year and contribution:
        parsed_papers.append({'title': title, 'year': year, 'contribution': contribution})

df_papers = pd.DataFrame(parsed_papers)
filtered_papers = df_papers[(df_papers['year'] > 2016) & (df_papers['contribution'].str.contains('empirical', na=False))]

print('__RESULT__:')
print(filtered_papers.to_json(orient='records'))"""

env_args = {'var_function-call-3207410245806214601': ['paper_docs'], 'var_function-call-89421489897449482': 'file_storage/function-call-89421489897449482.json'}

exec(code, env_args)
