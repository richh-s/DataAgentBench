code = """import json
import re

def extract_paper_info(doc):
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None
    domain_match = re.search(r'Domain: (.+)', text)
    domain_match_inline = re.search(r'trackers of (.+), finances', text) # Alternative pattern
    domain = []
    if domain_match:
        domain = [d.strip() for d in domain_match.group(1).split(',')]
    elif domain_match_inline:
        domain = [d.strip() for d in domain_match_inline.group(1).split(',')]
    
    return {'title': title, 'year': year, 'domain': domain}

with open(locals()['var_function-call-1819138674056248880'], 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    extracted_papers.append(extract_paper_info(doc))

filtered_papers = [
    p for p in extracted_papers 
    if p['year'] == 2016 and any('physical activity' in d.lower() for d in p['domain'])
]

result = [
    {'title': p['title'], 'year': p['year'], 'domain': p['domain']} 
    for p in filtered_papers
]
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-14428271549656226849': ['paper_docs'], 'var_function-call-1819138674056248880': 'file_storage/function-call-1819138674056248880.json'}

exec(code, env_args)
