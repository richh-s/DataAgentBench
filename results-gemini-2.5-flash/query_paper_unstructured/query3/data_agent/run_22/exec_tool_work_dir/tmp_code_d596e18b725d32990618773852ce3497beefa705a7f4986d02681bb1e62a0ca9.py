code = """import json
import re

file_path = locals()['var_function-call-612713539004311745']

with open(file_path, 'r') as f:
    papers_data = json.load(f)

filtered_papers = []

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']

    title = filename.replace('.txt', '')

    year_match = re.search(r'([A-Z]{3,}\s?\'?\d{2})?,\s?(\d{4})', text)
    year = None
    if year_match:
        year = int(year_match.group(2))
    else:
        # Fallback to look for a year in the first 2000 characters
        year_match_fallback = re.search(r'\b(19|20)\d{2}\b', text[:2000])
        if year_match_fallback:
            year = int(year_match_fallback.group(0))

    contribution = ''
    if 'empirical' in text.lower():
        contribution = 'empirical'

    if year and year > 2016 and 'empirical' in contribution:
        filtered_papers.append({'title': title, 'year': year, 'contribution': contribution})

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-3501279468467910328': ['paper_docs'], 'var_function-call-612713539004311745': 'file_storage/function-call-612713539004311745.json'}

exec(code, env_args)
