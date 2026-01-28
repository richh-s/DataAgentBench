code = """import json
import re

paper_docs_path = locals()['var_function-call-17131210383825528866']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    domain_match = re.search(r'domain: ([a-zA-Z0-9, ]+)', text, re.IGNORECASE)
    domain = domain_match.group(1).lower() if domain_match else ""

    if year == 2016 and 'physical activity' in domain:
        extracted_papers.append({'title': title, 'year': year, 'domain': domain})

print("__RESULT__:")
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-5022180096970479671': ['paper_docs'], 'var_function-call-17131210383825528866': 'file_storage/function-call-17131210383825528866.json'}

exec(code, env_args)
