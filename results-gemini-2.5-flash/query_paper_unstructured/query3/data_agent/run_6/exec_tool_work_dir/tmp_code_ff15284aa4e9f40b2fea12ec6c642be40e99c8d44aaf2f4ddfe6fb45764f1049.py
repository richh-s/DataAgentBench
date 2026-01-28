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

    # Robust year extraction: look for 4 digits that look like a year
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Contribution type extraction: check for keywords in text
    contribution = []
    contribution_keywords = ["empirical", "artifact", "theoretical", "survey", "methodological"]
    for keyword in contribution_keywords:
        if re.search(r'\b' + keyword + r'\b', text, re.IGNORECASE):
            contribution.append(keyword)
    contribution_str = ', '.join(contribution)

    extracted_papers.append({
        'title': title,
        'year': year,
        'contribution': contribution_str
    })

filtered_papers = [
    p for p in extracted_papers
    if p['year'] and p['year'] > 2016 and 'empirical' in p['contribution']
]

print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-15609089362044603763': ['paper_docs'], 'var_function-call-68838740435367397': 'file_storage/function-call-68838740435367397.json'}

exec(code, env_args)
