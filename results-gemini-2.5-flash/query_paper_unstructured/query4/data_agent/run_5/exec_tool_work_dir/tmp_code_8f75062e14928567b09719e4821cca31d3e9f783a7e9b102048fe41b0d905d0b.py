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

    year_match = re.search(r'(?:[A-Z]+ ')?(\d{2}), (\d{4})', text)
    year = int(year_match.group(2)) if year_match else None

    domain_match = re.search(r'Domain: (.*?)\n', text, re.IGNORECASE)
    domain_match_2 = re.search(r'domains, first by surveying.*?trackers of (.*?),', text, re.IGNORECASE | re.DOTALL)
    domain_match_3 = re.search(r'domains: \"(.+?)\"', text)

    domain = None
    if domain_match:
        domain = domain_match.group(1)
    elif domain_match_2:
        domain = domain_match_2.group(1)
    elif domain_match_3:
        domain = domain_match_3.group(1)
    else:
        domain_keywords = ['food', 'physical activity', 'sleep', 'mental', 'finances', 'productivity', 'screen time', 'social interactions', 'location', 'chronic', 'diabetes', 'health_behavior']
        found_domains = [kw for kw in domain_keywords if kw in text.lower()]
        if found_domains:
            domain = ', '.join(found_domains)

    extracted_papers.append({
        'title': title,
        'year': year,
        'domain': domain
    })

filtered_papers = [
    p for p in extracted_papers
    if p['year'] == 2016 and p['domain'] and 'physical activity' in p['domain'].lower()
]

result = json.dumps(filtered_papers)
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9075844566900917724': ['paper_docs'], 'var_function-call-4281778254792506949': 'file_storage/function-call-4281778254792506949.json'}

exec(code, env_args)
