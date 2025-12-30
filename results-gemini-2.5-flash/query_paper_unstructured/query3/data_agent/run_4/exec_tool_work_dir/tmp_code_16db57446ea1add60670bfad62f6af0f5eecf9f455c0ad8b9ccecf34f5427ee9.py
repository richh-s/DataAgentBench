code = """import json
import re

paper_docs_path = locals()['var_function-call-7196525365521970479']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    contribution_match = re.search(r'contribution:\s*([^\n]+)', text, re.IGNORECASE)
    contribution_types = []
    if contribution_match:
        contribution_text = contribution_match.group(1)
        if 'empirical' in contribution_text.lower():
            contribution_types.append('empirical')
        if 'artifact' in contribution_text.lower():
            contribution_types.append('artifact')
        if 'theoretical' in contribution_text.lower():
            contribution_types.append('theoretical')
        if 'survey' in contribution_text.lower():
            contribution_types.append('survey')
        if 'methodological' in contribution_text.lower():
            contribution_types.append('methodological')

    if year and 'empirical' in contribution_types:
        extracted_papers.append({
            'title': title,
            'year': year,
            'contribution': contribution_types
        })

filtered_papers = [paper for paper in extracted_papers if paper['year'] > 2016]

print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-11680401091389409545': 'file_storage/function-call-11680401091389409545.json', 'var_function-call-7196525365521970479': 'file_storage/function-call-7196525365521970479.json'}

exec(code, env_args)
