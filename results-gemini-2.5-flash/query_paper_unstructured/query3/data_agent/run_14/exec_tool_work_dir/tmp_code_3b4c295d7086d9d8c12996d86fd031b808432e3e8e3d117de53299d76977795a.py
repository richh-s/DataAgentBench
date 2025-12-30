code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-89421489897449482']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

parsed_papers_debug = []
for doc in paper_docs[:20]: # Only process first 20 docs for debugging
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')

    year = None
    # Search for a 4-digit year in the first 5000 characters of the text
    year_match = re.search(r'\b(19|20)\d{2}\b', text[:5000])
    if year_match:
        year = int(year_match.group(0))

    # Check for 'empirical' (case-insensitive) in the entire text
    has_empirical = bool(re.search(r'\bempirical\b', text, re.IGNORECASE))

    parsed_papers_debug.append({'title': title, 'year': year, 'has_empirical': has_empirical})

df_debug = pd.DataFrame(parsed_papers_debug)

print('__RESULT__:')
print(df_debug.to_json(orient='records'))"""

env_args = {'var_function-call-3207410245806214601': ['paper_docs'], 'var_function-call-89421489897449482': 'file_storage/function-call-89421489897449482.json', 'var_function-call-2589591416908310925': [], 'var_function-call-13239531528128313526': []}

exec(code, env_args)
