code = """import json
import re

file_path = locals()['var_function-call-7674742000925231744']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text = doc.get('text', '')

    year = None
    # Look for year in the first 2000 characters
    year_match = re.search(r'\b(19|20)\d{2}\b', text[:2000])
    if year_match:
        year = int(year_match.group(0))

    contribution_empirical = False
    # Look for 'empirical' in the text
    if re.search(r'empirical', text, re.IGNORECASE):
        contribution_empirical = True
    
    extracted_papers.append({
        'title': title,
        'year': year,
        'contribution_empirical': contribution_empirical
    })

filtered_papers = [
    paper for paper in extracted_papers 
    if paper['year'] is not None and paper['year'] > 2016 and paper['contribution_empirical']
]

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-7674742000925231744': 'file_storage/function-call-7674742000925231744.json'}

exec(code, env_args)
