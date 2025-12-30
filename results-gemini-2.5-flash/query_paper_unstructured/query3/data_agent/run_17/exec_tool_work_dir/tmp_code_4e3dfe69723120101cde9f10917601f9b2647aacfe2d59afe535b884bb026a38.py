code = """import json
import re

# Load the full result from the JSON file
with open(locals()['var_function-call-9538164357219464109'], 'r') as f:
    paper_docs = json.load(f)

filtered_papers = []

for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    # Extract year (looking for common patterns like "YEAR," "YEAR", "(YEAR)")
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Check for 'empirical' contribution (case-insensitive and as a whole word)
    contribution_empirical = re.search(r'\bempirical\b', text, re.IGNORECASE)

    if contribution_empirical and year and year > 2016:
        filtered_papers.append({'title': title, 'year': year})

print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-17116570147297263366': ['paper_docs'], 'var_function-call-9538164357219464109': 'file_storage/function-call-9538164357219464109.json'}

exec(code, env_args)
