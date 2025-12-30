code = """import json
import re

paper_docs_path = locals()['var_function-call-17131210383825528866']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

filtered_papers = []

for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    # Check if 'physical activity' is in the text (case-insensitive)
    is_physical_activity_domain = bool(re.search(r'physical activity', text, re.IGNORECASE))

    if is_physical_activity_domain:
        # Try to extract the year, typically found early in the document
        year = None
        # Search for 2016, potentially preceded by 'CHI '' or similar conference format
        # and limit the search to the first 1000 characters to make it more likely to be the publication year
        year_match = re.search(r'\b(19|20)\d{2}\b', text[:1000])
        if year_match:
            year = int(year_match.group(0))

        if year == 2016:
            filtered_papers.append({'title': title})

print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-5022180096970479671': ['paper_docs'], 'var_function-call-17131210383825528866': 'file_storage/function-call-17131210383825528866.json', 'var_function-call-14138390069928318324': [], 'var_function-call-9495907471577820416': []}

exec(code, env_args)
