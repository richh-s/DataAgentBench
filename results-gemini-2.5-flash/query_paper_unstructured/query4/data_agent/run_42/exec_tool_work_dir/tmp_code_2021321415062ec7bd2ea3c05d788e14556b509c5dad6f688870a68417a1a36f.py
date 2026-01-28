code = """import json
import re

file_path = locals()['var_function-call-1020461737059661264']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_in_domain_and_year = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Extract year from the entire text
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Check if 'physical activity' is in the text (case-insensitive)
    is_physical_activity_domain = 'physical activity' in text.lower()

    if year == 2016 and is_physical_activity_domain:
        papers_in_domain_and_year.append({'title': title})

print('__RESULT__:')
print(json.dumps(papers_in_domain_and_year))"""

env_args = {'var_function-call-10668140555731164678': ['paper_docs'], 'var_function-call-1020461737059661264': 'file_storage/function-call-1020461737059661264.json', 'var_function-call-18293935031113841746': [], 'var_function-call-2347887543621677021': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
