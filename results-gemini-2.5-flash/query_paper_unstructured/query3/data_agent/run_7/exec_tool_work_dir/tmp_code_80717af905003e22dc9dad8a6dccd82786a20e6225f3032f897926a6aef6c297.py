code = """import json
import re

file_path = locals()['var_function-call-6604890257152561261']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    year = None
    contribution = []

    # Extract year
    year_match = re.search(r'(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+\'(\d{2})', text, re.IGNORECASE)
    if year_match:
        year = int('20' + year_match.group(1)) # Assuming '15' means 2015

    # Extract contribution
    if re.search(r'empirical', text, re.IGNORECASE):
        contribution.append('empirical')
    if re.search(r'artifact', text, re.IGNORECASE):
        contribution.append('artifact')
    if re.search(r'theoretical', text, re.IGNORECASE):
        contribution.append('theoretical')
    if re.search(r'survey', text, re.IGNORECASE):
        contribution.append('survey')
    if re.search(r'methodological', text, re.IGNORECASE):
        contribution.append('methodological')

    extracted_papers.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

filtered_papers = [
    p for p in extracted_papers
    if p['year'] and p['year'] > 2016 and 'empirical' in p['contribution']
]

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-14474643791060089691': ['paper_docs'], 'var_function-call-6604890257152561261': 'file_storage/function-call-6604890257152561261.json'}

exec(code, env_args)
