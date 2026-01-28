code = """import json
import re

with open(locals()['var_function-call-7965215549551189536'], 'r') as f:
    paper_docs = json.load(f)

filtered_papers = []

for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    # Extract year
    year_match = re.search(r'\b(19|20)\d{2}\b', text[:500])  # Search in the first 500 characters
    year = int(year_match.group(0)) if year_match else None

    # Extract contribution
    contribution_match = re.search(r'contribution[s]?:.*?(\bempirical\b)', text, re.IGNORECASE)
    is_empirical = bool(contribution_match)
    
    if is_empirical and year and year > 2016:
        filtered_papers.append({'title': title, 'year': year})

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-7965215549551189536': 'file_storage/function-call-7965215549551189536.json'}

exec(code, env_args)
