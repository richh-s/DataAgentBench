code = """import json
import re

with open(locals()['var_function-call-2718979747807548177'], 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    domain = None
    if 'physical activity' in text.lower():
        domain = 'physical activity'

    if year == 2016 and domain == 'physical activity':
        extracted_papers.append({'title': title, 'year': year, 'domain': domain})

print("__RESULT__:")
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-16357124078300000711': ['paper_docs'], 'var_function-call-2718979747807548177': 'file_storage/function-call-2718979747807548177.json'}

exec(code, env_args)
