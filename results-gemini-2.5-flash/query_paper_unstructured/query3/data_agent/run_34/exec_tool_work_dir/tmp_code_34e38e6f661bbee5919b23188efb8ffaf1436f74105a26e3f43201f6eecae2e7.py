code = """import json
import re

paper_docs_file_path = locals()['var_function-call-2095457112703000306']

with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
empirical_keywords = [
    'empirical study',
    'user study',
    'experiment',
    'survey',
    'qualitative study',
    'quantitative study',
    'field study',
    'evaluation'
]

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text'].lower()

    # More robust year extraction - look for a 4-digit number that's likely a year
    years_found = re.findall(r'\b(19|20)\d{2}\b', text)
    year = None
    if years_found:
        # Try to find the first year that appears in the context of publication info
        # This is a heuristic, and might need further refinement based on actual data patterns
        # For now, let's just take the first plausible year found.
        # A more advanced approach would involve checking proximity to keywords like 'copyright', 'published', 'conference name with year'
        year_candidates = [int(y) for y in years_found if 1900 <= int(y) <= 2024] # Filter for reasonable year ranges
        if year_candidates:
            year = min(year_candidates) # Often the earliest year is the publication year

    contribution = None
    for keyword in empirical_keywords:
        if keyword in text:
            contribution = 'empirical'
            break

    if year and contribution:
        extracted_papers.append({'title': title, 'year': year, 'contribution': contribution})

filtered_papers = [paper for paper in extracted_papers if paper['year'] > 2016]

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-9650743875939497897': ['paper_docs'], 'var_function-call-2095457112703000306': 'file_storage/function-call-2095457112703000306.json', 'var_function-call-620095213941471173': []}

exec(code, env_args)
