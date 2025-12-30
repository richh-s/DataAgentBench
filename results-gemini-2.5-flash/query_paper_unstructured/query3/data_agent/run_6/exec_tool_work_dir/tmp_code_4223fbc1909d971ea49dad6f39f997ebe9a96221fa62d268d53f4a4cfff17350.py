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

    year_match = re.search(r'\b(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)?\s*'?(\d{2,4})\b', text)
    year = int(year_match.group(1)) if year_match else None
    if year and len(str(year)) == 2:
        if year > 50:  # Assuming 1950-1999
            year += 1900
        else:  # Assuming 2000-2049
            year += 2000

    contribution_match = re.search(r'contribution(?:s)?:\s*([^\n]*)', text, re.IGNORECASE)
    contribution = contribution_match.group(1).lower() if contribution_match else ''

    extracted_papers.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

filtered_papers = [
    p for p in extracted_papers
    if p['year'] and p['year'] > 2016 and 'empirical' in p['contribution']
]

print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-15609089362044603763': ['paper_docs'], 'var_function-call-68838740435367397': 'file_storage/function-call-68838740435367397.json'}

exec(code, env_args)
