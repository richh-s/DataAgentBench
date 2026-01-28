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

    # Broader year extraction: look for any 4-digit number that could be a year
    years_found = re.findall(r'\b(19|20)\d{2}\b', text)
    year = None
    if years_found:
        # Assuming the first found year is the publication year
        year = int(years_found[0])

    domain = 'physical activity' if 'physical activity' in text.lower() else None

    if year and domain:
        parsed_papers.append({'title': title, 'year': year, 'domain': domain})

filtered_papers_2016_pa = [
    paper for paper in parsed_papers
    if paper['year'] == 2016 and paper['domain'] == 'physical activity'
]

print('__RESULT__:')
print(json.dumps(filtered_papers_2016_pa))"""

env_args = {'var_function-call-481143422120978278': 'file_storage/function-call-481143422120978278.json', 'var_function-call-3747855985844918712': []}

exec(code, env_args)
