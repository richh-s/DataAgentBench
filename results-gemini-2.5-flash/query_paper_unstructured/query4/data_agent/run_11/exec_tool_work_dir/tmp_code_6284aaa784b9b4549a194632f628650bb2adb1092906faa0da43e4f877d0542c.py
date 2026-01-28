code = """import json
import re

paper_docs_path = locals()['var_function-call-17131210383825528866']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

papers_in_physical_activity_domain = []

for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    # Check if 'physical activity' is in the text (case-insensitive) for domain
    if re.search(r'physical activity', text, re.IGNORECASE):
        # Attempt to extract year 2016. Look for '2016' or a common conference year format like "'16" at the beginning of the paper.
        # The publication year is typically found early in the document. Let's check the first 2000 characters.
        year_match = re.search(r'(2016|\'16)\b', text[:2000], re.IGNORECASE)
        if year_match:
            # If '16 is found, assume it refers to 2016 in the context of academic papers.
            papers_in_physical_activity_domain.append({'title': title, 'year': 2016})

print("__RESULT__:")
print(json.dumps(papers_in_physical_activity_domain))"""

env_args = {'var_function-call-5022180096970479671': ['paper_docs'], 'var_function-call-17131210383825528866': 'file_storage/function-call-17131210383825528866.json', 'var_function-call-14138390069928318324': [], 'var_function-call-9495907471577820416': [], 'var_function-call-6090686903900208578': []}

exec(code, env_args)
