code = """import json
import re

paper_docs_file_path = locals()['var_function-call-6544619829393036365']

with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    domain_match = re.search(r'Domains?:\s*([\w\s,]+)', text, re.IGNORECASE)
    domain = domain_match.group(1).strip() if domain_match else None

    # Try to find domain within the first 500 characters if not found earlier
    if not domain:
        snippet = text[:500]
        if 'physical activity' in snippet.lower():
            domain = 'physical activity'

    if year == 2016 and domain and 'physical activity' in domain.lower():
        extracted_papers.append({'title': title, 'year': year, 'domain': domain})

print("__RESULT__:")
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-17463833612075543362': ['paper_docs'], 'var_function-call-6544619829393036365': 'file_storage/function-call-6544619829393036365.json'}

exec(code, env_args)
