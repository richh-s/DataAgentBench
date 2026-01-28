code = """import json
import re

file_path = locals()['var_function-call-17780243348356271674']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')

    # Extract year: look for a 4-digit number starting with 19 or 20, usually near the beginning of the text
    year_match = re.search(r'(19|20)\\d{2}', text[:500])  # Search in the first 500 characters
    year = int(year_match.group(0)) if year_match else None

    # Extract contribution: look for 'contribution:' keyword
    contribution_match = re.search(r'contribution:\\s*([\\w\\s,]+)', text, re.IGNORECASE)
    contribution = contribution_match.group(1).strip() if contribution_match else None

    extracted_papers.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

filtered_papers = [
    p for p in extracted_papers
    if p['year'] and p['year'] > 2016 and p['contribution'] and 'empirical' in p['contribution'].lower()
]

__RESULT__:
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-8377088647731712428': ['paper_docs'], 'var_function-call-17780243348356271674': 'file_storage/function-call-17780243348356271674.json'}

exec(code, env_args)
