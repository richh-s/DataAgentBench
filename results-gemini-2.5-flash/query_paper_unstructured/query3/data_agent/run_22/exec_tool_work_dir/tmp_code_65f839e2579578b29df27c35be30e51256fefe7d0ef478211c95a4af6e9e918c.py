code = """import json
import re

file_path = locals()['var_function-call-612713539004311745']

with open(file_path, 'r') as f:
    papers_data = json.load(f)

extracted_info = []

for i, paper in enumerate(papers_data):
    if i >= 10:  # Check only the first 10 papers for debugging
        break

    filename = paper['filename']
    text = paper['text']

    title = filename.replace('.txt', '')

    year = None
    # Broader year search in the first 2000 characters
    year_match = re.search(r'\b(19|20)\d{2}\b', text[:2000])
    if year_match:
        year = int(year_match.group(0))

    contribution = ''
    if 'empirical' in text.lower():
        contribution = 'empirical'
    elif re.search(r'(user study|experiment|interview|survey|field study)', text.lower()):
        contribution = 'empirical' # Broader definition of empirical

    extracted_info.append({'title': title, 'year': year, 'contribution': contribution, 'text_snippet': text[:500]})

print('__RESULT__:')
print(json.dumps(extracted_info))"""

env_args = {'var_function-call-3501279468467910328': ['paper_docs'], 'var_function-call-612713539004311745': 'file_storage/function-call-612713539004311745.json', 'var_function-call-14790136326172502952': []}

exec(code, env_args)
