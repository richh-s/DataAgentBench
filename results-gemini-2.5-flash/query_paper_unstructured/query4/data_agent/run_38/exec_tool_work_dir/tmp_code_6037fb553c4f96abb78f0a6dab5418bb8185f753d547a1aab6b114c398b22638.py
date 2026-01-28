code = """import json
import re

with open(locals()['var_function-call-7689240133367752773'], 'r') as f:
    paper_docs = json.load(f)

papers_data = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year = None
    year_match = re.search(r'(2016)', text)
    if year_match:
        year = int(year_match.group(0))

    domain = None
    if 'physical activity' in text.lower():
        domain = 'physical activity'
    
    papers_data.append({'title': title, 'year': year, 'domain': domain})

filtered_papers = [p for p in papers_data if p['year'] == 2016 and p['domain'] == 'physical activity']

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-7385341935782596137': ['paper_docs'], 'var_function-call-15754045851250025291': ['Citations', 'sqlite_sequence'], 'var_function-call-7689240133367752773': 'file_storage/function-call-7689240133367752773.json', 'var_function-call-7978600574837803930': []}

exec(code, env_args)
