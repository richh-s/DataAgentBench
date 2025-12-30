code = """import json
import re

file_path = locals()['var_function-call-8974985645401887369']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'\\b(19|20)\\d{2}\\b', text)
    year = int(year_match.group(0)) if year_match else None

    contribution_match = re.search(r'contribution:\\s*([^\\n]+)', text, re.IGNORECASE)
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

env_args = {'var_function-call-3627491098943866791': ['paper_docs'], 'var_function-call-8974985645401887369': 'file_storage/function-call-8974985645401887369.json'}

exec(code, env_args)
