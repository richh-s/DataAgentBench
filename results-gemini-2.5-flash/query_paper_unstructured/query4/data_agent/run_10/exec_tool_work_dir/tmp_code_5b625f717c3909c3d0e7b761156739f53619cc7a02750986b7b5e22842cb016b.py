code = """import pandas as pd
import re
import json

papers_data = json.loads(open(locals()['var_function-call-14890926156089513429'], 'r').read())

extracted_papers = []
for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')

    year_match = re.search(r'year:\s*(\d{4})', text, re.IGNORECASE)
    year = int(year_match.group(1)) if year_match else None

    domain_match = re.search(r'domain:\s*(.*)', text, re.IGNORECASE)
    domain = domain_match.group(1).strip() if domain_match else None

    extracted_papers.append({
        'title': title,
        'year': year,
        'domain': domain
    })

df_papers = pd.DataFrame(extracted_papers)

df_filtered_papers = df_papers[
    (df_papers['year'] == 2016) &
    (df_papers['domain'].str.contains('physical activity', case=False, na=False))
]

print('__RESULT__:')
print(df_filtered_papers.to_json(orient='records'))"""

env_args = {'var_function-call-12243833719420803506': ['paper_docs'], 'var_function-call-12656719124189789220': [], 'var_function-call-14890926156089513429': 'file_storage/function-call-14890926156089513429.json'}

exec(code, env_args)
