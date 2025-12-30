code = """import pandas as pd
import re
import json

# Load the full MongoDB result from the file
with open(locals()['var_function-call-16572885030136982066'], 'r') as f:
    mongo_docs = json.load(f)

papers_data = []
for doc in mongo_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Extract year (e.g., "UBICOMP '15, SEPTEMBER 7–11, 2015" or "Year: 2018")
    year_match = re.search(r"(?:[A-Z]+\s'[0-9]{2}|\bYear:\s*)(\d{4})", text)
    year = int(year_match.group(1)) if year_match else None

    # Extract contribution (e.g., "contribution: empirical")
    contribution_match = re.search(r'contribution:\s*([a-zA-Z,\s]+)', text, re.IGNORECASE)
    contribution = contribution_match.group(1).lower() if contribution_match else ''

    papers_data.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

df_papers = pd.DataFrame(papers_data)

# Filter papers for 'empirical' contribution and year > 2016
filtered_papers = df_papers[
    (df_papers['contribution'].str.contains('empirical', na=False)) &
    (df_papers['year'] > 2016)
]

print('__RESULT__:')
print(filtered_papers.to_json(orient='records'))"""

env_args = {'var_function-call-3744194182005610721': ['paper_docs'], 'var_function-call-16572885030136982066': 'file_storage/function-call-16572885030136982066.json'}

exec(code, env_args)
