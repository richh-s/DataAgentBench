code = """import json
import re

file_path = locals()['var_function-call-3929304832823599734']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

parsed_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    domain = None
    if 'physical activity' in text.lower() and year == 2016:
        parsed_papers.append({'title': title, 'publication_year': year})

print('__RESULT__:')
print(json.dumps(parsed_papers))"""

env_args = {'var_function-call-15559630327221788903': ['paper_docs'], 'var_function-call-3929304832823599734': 'file_storage/function-call-3929304832823599734.json'}

exec(code, env_args)
