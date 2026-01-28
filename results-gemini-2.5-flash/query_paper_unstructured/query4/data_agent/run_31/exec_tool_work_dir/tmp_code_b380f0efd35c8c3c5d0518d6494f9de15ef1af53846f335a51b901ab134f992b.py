code = """import json
import re

paper_docs_data = json.load(open(locals()['var_function-call-4122217980798213330'], 'r'))

extracted_papers = []
for doc in paper_docs_data:
    filename = doc['filename']
    text = doc['text']

    title = filename.replace('.txt', '')

    year = None
    year_match = re.search(r'\b(19|20)\d{2}\b', text[:500]) # Search in the first 500 characters
    if year_match:
        year = int(year_match.group(0))

    domain = None
    domain_match = re.search(r'(?i)domain[s]?:\s*([\w\s,]+)', text[:2000]) # Search in the first 2000 characters for "domain:" or "domains:"
    if domain_match:
        domain = domain_match.group(1).lower()
    else: # Try to find 'physical activity' directly
        if 'physical activity' in text.lower():
            domain = 'physical activity'

    extracted_papers.append({
        'title': title,
        'year': year,
        'domain': domain
    })

filtered_papers = [
    p for p in extracted_papers
    if p['year'] == 2016 and p['domain'] and 'physical activity' in p['domain']
]

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-6790850927886125725': ['paper_docs'], 'var_function-call-4122217980798213330': 'file_storage/function-call-4122217980798213330.json'}

exec(code, env_args)
