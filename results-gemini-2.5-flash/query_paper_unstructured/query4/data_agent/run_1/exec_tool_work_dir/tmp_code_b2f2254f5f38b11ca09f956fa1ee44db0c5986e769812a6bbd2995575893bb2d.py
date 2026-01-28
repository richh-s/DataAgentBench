code = """import json
import re

file_path = locals()['var_function-call-3921672676854055861']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year = None
    # Directly look for '2016' in the text to simplify year extraction for the target year.
    if re.search(r'\b2016\b', text):
        year = 2016

    domain = []
    if 'physical activity' in text.lower():
        domain.append('physical activity')

    if year == 2016 and 'physical activity' in domain:
        extracted_papers.append({
            'title': title
        })

print("__RESULT__:")
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-4911569923958279959': ['paper_docs'], 'var_function-call-3921672676854055861': 'file_storage/function-call-3921672676854055861.json'}

exec(code, env_args)
