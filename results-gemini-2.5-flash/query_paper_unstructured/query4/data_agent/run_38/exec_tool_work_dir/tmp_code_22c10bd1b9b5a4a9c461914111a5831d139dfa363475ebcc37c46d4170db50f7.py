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
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    if year_match:
        year = int(year_match.group(0))
    
    domain = None
    domains = ["food", "physical activity", "sleep", "mental", "finances", "productivity", "screen time", "social interactions", "location", "chronic", "diabetes", "health_behavior"]
    for d in domains:
        if d in text.lower(): # Case-insensitive check
            domain = d
            break
    
    papers_data.append({'title': title, 'year': year, 'domain': domain})

filtered_papers = [p for p in papers_data if p['year'] == 2016 and p['domain'] == 'physical activity']

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-7385341935782596137': ['paper_docs'], 'var_function-call-15754045851250025291': ['Citations', 'sqlite_sequence'], 'var_function-call-7689240133367752773': 'file_storage/function-call-7689240133367752773.json'}

exec(code, env_args)
