code = """import json
import re

file_path = locals()['var_function-call-68838740435367397']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']

    title = filename.replace('.txt', '')

    # More flexible year extraction
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group(0)) if year_match else None

    # Check for 'empirical' directly in the text, case-insensitively
    is_empirical = 'empirical' in text.lower()

    if year and year > 2016 and is_empirical:
        extracted_papers.append({
            'title': title,
            'year': year
        })

print("__RESULT__:")
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-15609089362044603763': ['paper_docs'], 'var_function-call-68838740435367397': 'file_storage/function-call-68838740435367397.json', 'var_function-call-3064361672336217427': []}

exec(code, env_args)
