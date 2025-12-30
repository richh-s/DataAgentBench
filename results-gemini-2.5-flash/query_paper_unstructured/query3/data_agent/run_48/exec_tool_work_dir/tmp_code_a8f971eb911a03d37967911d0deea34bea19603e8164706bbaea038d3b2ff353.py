code = """import json
import re

paper_docs_data = json.load(open(locals()['var_function-call-558217748425387803'], 'r'))

extracted_papers = []

for doc in paper_docs_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search('\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Using a normal string literal for the regex pattern, escaping backslashes
    contribution_match = re.search('contribution(?:s)?:\\s*(.*?)(?:\\n|\\.|;)', text, re.IGNORECASE)
    contribution = contribution_match.group(1).strip() if contribution_match else ''

    extracted_papers.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

filtered_papers = [
    p for p in extracted_papers
    if p['year'] and p['year'] > 2016 and 'empirical' in p['contribution'].lower()
]

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-11120416126101380269': ['paper_docs'], 'var_function-call-558217748425387803': 'file_storage/function-call-558217748425387803.json'}

exec(code, env_args)
