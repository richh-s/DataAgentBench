code = """import json
import re

paper_docs_path = locals()['var_function-call-17131210383825528866']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

papers_of_interest = []

for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    # Check if 'physical activity' is in the text for domain matching
    if re.search(r'physical activity', text, re.IGNORECASE):
        # Search for publication year 2016 within the first 1000 characters of the text
        # This helps in identifying the actual publication year and not a citation year
        year_match = re.search(r'\b(2016|\'16)\b', text[:1000])
        if year_match:
            papers_of_interest.append({'title': title})

print("__RESULT__:")
print(json.dumps(papers_of_interest))"""

env_args = {'var_function-call-5022180096970479671': ['paper_docs'], 'var_function-call-17131210383825528866': 'file_storage/function-call-17131210383825528866.json', 'var_function-call-14138390069928318324': [], 'var_function-call-9495907471577820416': [], 'var_function-call-6090686903900208578': []}

exec(code, env_args)
