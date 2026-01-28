code = """import json
import re

paper_docs_file_path = locals()['var_function-call-2095457112703000306']

with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text'].lower()

    # Extract year: Find all 4-digit numbers and consider them potential years
    years_found = re.findall(r'\b(19|20)\d{2}\b', text)
    year = None
    if years_found:
        # Filter for plausible years and take the minimum as a heuristic for publication year
        plausible_years = [int(y) for y in years_found if 1990 <= int(y) <= 2024]
        if plausible_years:
            year = min(plausible_years)

    # Extract contribution: Check for 'empirical' (case-insensitive)
    contribution = 'empirical' if 'empirical' in text else None

    if year and contribution:
        extracted_papers.append({'title': title, 'year': year, 'contribution': contribution})

filtered_papers = [paper for paper in extracted_papers if paper['year'] > 2016]

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-9650743875939497897': ['paper_docs'], 'var_function-call-2095457112703000306': 'file_storage/function-call-2095457112703000306.json', 'var_function-call-620095213941471173': [], 'var_function-call-8585478421154321217': []}

exec(code, env_args)
