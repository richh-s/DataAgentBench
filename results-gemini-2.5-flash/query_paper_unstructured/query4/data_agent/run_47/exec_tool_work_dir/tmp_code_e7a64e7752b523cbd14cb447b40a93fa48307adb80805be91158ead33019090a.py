code = """import json
import re

def extract_year(text):
    match = re.search(r'\b(19|20)\d{2}\b', text)
    if match:
        return int(match.group(0))
    return None

def extract_domain(text):
    if 'physical activity' in text.lower():
        return 'physical activity'
    return None

paper_docs_raw = json.load(open(locals()['var_function-call-13040654951209415358'], 'r'))
papers = []
for doc in paper_docs_raw:
    title = doc['filename'].replace('.txt', '')
    year = extract_year(doc['text'])
    domain = extract_domain(doc['text'])
    if year and domain == 'physical activity':
        papers.append({'title': title, 'year': year, 'domain': domain})

filtered_papers = [p for p in papers if p['year'] == 2016]

print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-12305578897446280284': 'file_storage/function-call-12305578897446280284.json', 'var_function-call-2531435270866315542': ['paper_docs'], 'var_function-call-13040654951209415358': 'file_storage/function-call-13040654951209415358.json'}

exec(code, env_args)
