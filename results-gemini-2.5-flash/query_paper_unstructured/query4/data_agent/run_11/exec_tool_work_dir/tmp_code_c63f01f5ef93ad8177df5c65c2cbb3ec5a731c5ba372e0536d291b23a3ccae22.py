code = """import json
import re

paper_docs_path = locals()['var_function-call-17131210383825528866']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers_info = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Check for 'physical activity' in the text (case-insensitive)
    if re.search(r'physical activity', text, re.IGNORECASE):
        # Try to extract the year from the first 500 characters, as publication year is usually early
        year = None
        year_match = re.search(r'\b(19|20)\d{2}\b', text[:500])
        if year_match:
            year = int(year_match.group(0))

        if year == 2016:
            extracted_papers_info.append({'title': title, 'year': year})

print("__RESULT__:")
print(json.dumps(extracted_papers_info))"""

env_args = {'var_function-call-5022180096970479671': ['paper_docs'], 'var_function-call-17131210383825528866': 'file_storage/function-call-17131210383825528866.json', 'var_function-call-14138390069928318324': []}

exec(code, env_args)
