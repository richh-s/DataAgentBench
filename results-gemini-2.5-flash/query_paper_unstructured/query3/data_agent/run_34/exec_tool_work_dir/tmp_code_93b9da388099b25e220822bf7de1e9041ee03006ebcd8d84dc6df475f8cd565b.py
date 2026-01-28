code = """import json
import re

paper_docs_file_path = locals()['var_function-call-2095457112703000306']

with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'\b(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)?\s*(\d{4})\b', text)
    year = int(year_match.group(1)) if year_match else None

    contribution = 'empirical' if 'empirical' in text.lower() else None

    if year and contribution:
        extracted_papers.append({'title': title, 'year': year, 'contribution': contribution})

filtered_papers = [paper for paper in extracted_papers if paper['year'] > 2016]

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-9650743875939497897': ['paper_docs'], 'var_function-call-2095457112703000306': 'file_storage/function-call-2095457112703000306.json'}

exec(code, env_args)
