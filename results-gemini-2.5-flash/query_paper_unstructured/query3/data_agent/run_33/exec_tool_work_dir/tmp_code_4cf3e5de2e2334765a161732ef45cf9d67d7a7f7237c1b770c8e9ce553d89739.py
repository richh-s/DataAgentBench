code = """import json
import re

file_path = locals()['var_function-call-241197343086052657']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')

    year = None
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    if year_match:
        year = int(year_match.group(0))

    contribution_types = []
    if re.search(r'empirical', text, re.IGNORECASE):
        contribution_types.append('empirical')

    if 'empirical' in contribution_types and year and year > 2016:
        extracted_papers.append({
            'title': title,
            'year': year,
            'contribution': contribution_types
        })

print('__RESULT__:')
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-17176896421169560921': ['paper_docs'], 'var_function-call-241197343086052657': 'file_storage/function-call-241197343086052657.json'}

exec(code, env_args)
