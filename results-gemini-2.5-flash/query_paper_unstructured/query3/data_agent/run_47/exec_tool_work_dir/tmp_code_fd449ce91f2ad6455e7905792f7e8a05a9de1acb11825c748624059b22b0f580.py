code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-6403520784644624662']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year = None
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    if year_match:
        year = int(year_match.group(0))

    contribution = 'unknown'
    if re.search(r'empirical', text, re.IGNORECASE):
        contribution = 'empirical'

    extracted_papers.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

df_papers = pd.DataFrame(extracted_papers)
filtered_papers = df_papers[
    (df_papers['contribution'].str.contains('empirical', case=False, na=False)) &
    (df_papers['year'] > 2016)
]

print('__RESULT__:')
print(filtered_papers.to_json(orient='records'))"""

env_args = {'var_function-call-16596318350231445115': ['paper_docs'], 'var_function-call-6403520784644624662': 'file_storage/function-call-6403520784644624662.json'}

exec(code, env_args)
