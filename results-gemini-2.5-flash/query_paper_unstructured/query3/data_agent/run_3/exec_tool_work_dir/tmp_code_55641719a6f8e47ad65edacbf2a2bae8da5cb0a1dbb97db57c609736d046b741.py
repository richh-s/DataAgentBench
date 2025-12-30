code = """import json
import re

file_path = locals()['var_function-call-8451556604040005886']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_data = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'([A-Z]{3,}\\s\'\\d{2}|\\d{4})', text)
    year = None
    if year_match:
        year_str = year_match.group(1)
        if len(year_str) == 4 and year_str.isdigit():
            year = int(year_str)
        elif len(year_str) > 4:
            year_suffix = year_str[-2:]
            if year_suffix.isdigit():
                year = int('20' + year_suffix) if int(year_suffix) < 50 else int('19' + year_suffix)

    contribution_match = re.search(r'contribution:\s*\[?([^\]]+)\]?', text, re.IGNORECASE)
    contribution_types = []
    if contribution_match:
        contributions_str = contribution_match.group(1)
        contribution_types = [c.strip().lower() for c in contributions_str.split(',')]
        if 'empirical' in contribution_types:
            contribution_types = ['empirical'] # only keep empirical if it exists

    if year and 'empirical' in contribution_types:
        papers_data.append({'title': title, 'year': year, 'contribution': 'empirical'})

filtered_papers = [p for p in papers_data if p['year'] > 2016 and 'empirical' in p['contribution']]

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-1330267927777135001': ['paper_docs'], 'var_function-call-8451556604040005886': 'file_storage/function-call-8451556604040005886.json'}

exec(code, env_args)
