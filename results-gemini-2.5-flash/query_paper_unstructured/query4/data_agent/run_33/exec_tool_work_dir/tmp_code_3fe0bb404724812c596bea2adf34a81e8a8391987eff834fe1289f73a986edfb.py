code = """import json
import re

file_path = locals()['var_function-call-481143422120978278']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

parsed_papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']

    title = filename.replace('.txt', '')

    year_match = re.search(r'([A-Z]{3,}\s'\d{2}|[A-Z][a-z]+\s\d{4}|\d{4})', text)
    year = None
    if year_match:
        year_str = year_match.group(1)
        if len(year_str) == 4 and year_str.isdigit():
            year = int(year_str)
        else:
            year_num_match = re.search(r'\d{4}', year_str)
            if year_num_match:
                year = int(year_num_match.group(0))

    domain = 'physical activity' if 'physical activity' in text.lower() else None

    if year and domain:
        parsed_papers.append({'title': title, 'year': year, 'domain': domain})

filtered_papers_2016_pa = [
    paper for paper in parsed_papers
    if paper['year'] == 2016 and paper['domain'] == 'physical activity'
]

print('__RESULT__:')
print(json.dumps(filtered_papers_2016_pa))"""

env_args = {'var_function-call-481143422120978278': 'file_storage/function-call-481143422120978278.json'}

exec(code, env_args)
