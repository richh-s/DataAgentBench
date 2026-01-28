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
    if domain == 'physical activity': # Removed year filter for debugging
        papers.append({'title': title, 'year': year, 'domain': domain})

print("__RESULT__:")
print(json.dumps(papers))"""

env_args = {'var_function-call-12305578897446280284': 'file_storage/function-call-12305578897446280284.json', 'var_function-call-2531435270866315542': ['paper_docs'], 'var_function-call-13040654951209415358': 'file_storage/function-call-13040654951209415358.json', 'var_function-call-13697098365809760818': []}

exec(code, env_args)
