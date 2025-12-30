code = """import json
import re

file_path = locals()['var_function-call-4281778254792506949']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Extract year: search for a 4-digit number that looks like a year
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Extract domain using keywords, as domains can be part of a list
    domain = None
    domain_keywords = ['physical activity'] # Focusing on the requested domain
    found_domains = [kw for kw in domain_keywords if kw in text.lower()]
    if found_domains:
        domain = ', '.join(found_domains)

    if year is not None and domain is not None:
        extracted_papers.append({
            'title': title,
            'year': year,
            'domain': domain
        })

filtered_papers = [
    p for p in extracted_papers
    if p['year'] == 2016 and 'physical activity' in p['domain'].lower()
]

result = json.dumps(filtered_papers)
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9075844566900917724': ['paper_docs'], 'var_function-call-4281778254792506949': 'file_storage/function-call-4281778254792506949.json'}

exec(code, env_args)
