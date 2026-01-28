code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-11985281394751560404']

with open(file_path, 'r') as f:
    papers_data = json.load(f)

extracted_papers = []

for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')

    year_match = re.search(r'(?:(?:19|20)\\d{2})', text)
    year = int(year_match.group(0)) if year_match else None

    contribution_match = re.search(r'contribution: (.*?)(?:\\n|\\.|,)', text, re.IGNORECASE)
    contribution = contribution_match.group(1).strip() if contribution_match else None

    extracted_papers.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

df_papers = pd.DataFrame(extracted_papers)

filtered_papers = df_papers[
    (df_papers['year'] > 2016) &
    (df_papers['contribution'].str.contains('empirical', case=False, na=False))
]

print('__RESULT__:')
print(filtered_papers.to_json(orient='records'))"""

env_args = {'var_function-call-2783535409203713964': ['paper_docs'], 'var_function-call-11985281394751560404': 'file_storage/function-call-11985281394751560404.json'}

exec(code, env_args)
