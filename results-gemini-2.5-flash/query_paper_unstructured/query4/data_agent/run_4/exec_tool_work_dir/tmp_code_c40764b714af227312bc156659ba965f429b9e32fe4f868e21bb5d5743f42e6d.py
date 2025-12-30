code = """import json
import re

with open(locals()['var_function-call-11852784549828080247'], 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    if year == 2016 and 'physical activity' in text.lower():
        extracted_papers.append({'title': title, 'year': year})

print('__RESULT__:')
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-8240804717267947776': ['paper_docs'], 'var_function-call-11852784549828080247': 'file_storage/function-call-11852784549828080247.json'}

exec(code, env_args)
