code = """import json
import re

file_path = locals()['var_function-call-1020461737059661264']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_in_domain = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Extract year: looking for a 4-digit number that could be a year in the first 500 characters of the text.
    # Often publication year is near the beginning.
    year_match = re.search(r'\b(19|20)\d{2}\b', text[:500])
    year = int(year_match.group(0)) if year_match else None

    # Check if 'physical activity' is in the text (case-insensitive)
    if 'physical activity' in text.lower() and year is not None and year == 2016:
        papers_in_domain.append({'title': title, 'year': year})

print('__RESULT__:')
print(json.dumps(papers_in_domain))"""

env_args = {'var_function-call-10668140555731164678': ['paper_docs'], 'var_function-call-1020461737059661264': 'file_storage/function-call-1020461737059661264.json'}

exec(code, env_args)
