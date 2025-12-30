code = """import re
import json

paper_docs = json.loads(open(locals()['var_function-call-6962359753067570097'], 'r').read())
parsed_papers = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    
    year_match = re.search(r'(?:19|20)\d{2}', text)
    year = int(year_match.group(0)) if year_match else None
    
    domain = 'physical activity' if 'physical activity' in text.lower() else None
    
    if year and domain:
        parsed_papers.append({'title': title, 'year': year, 'domain': domain})

filtered_papers_2016_pa = [p for p in parsed_papers if p['year'] == 2016 and p['domain'] == 'physical activity']

print('__RESULT__:')
print(json.dumps(filtered_papers_2016_pa))"""

env_args = {'var_function-call-6962359753067570097': 'file_storage/function-call-6962359753067570097.json'}

exec(code, env_args)
