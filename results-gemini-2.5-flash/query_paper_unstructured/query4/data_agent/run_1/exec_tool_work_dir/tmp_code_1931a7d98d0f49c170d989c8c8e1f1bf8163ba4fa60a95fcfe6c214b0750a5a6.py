code = """import json
import re

file_path = locals()['var_function-call-3921672676854055861']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'([A-Z]{3,}\s+\'\d{2}|\d{4})', text)
    year = None
    if year_match:
        year_str = year_match.group(1)
        if year_str.isdigit() and len(year_str) == 4:
            year = int(year_str)
        elif "'" in year_str:
            year_suffix = year_str.split("'')[1]
            if year_suffix.isdigit():
                full_year = int("20" + year_suffix) if int(year_suffix) < 50 else int("19" + year_suffix)
                year = full_year

    domain = []
    if 'physical activity' in text.lower():
        domain.append('physical activity')

    if year and domain:
        extracted_papers.append({
            'title': title,
            'year': year,
            'domain': domain
        })

filtered_papers = [
    paper for paper in extracted_papers
    if paper['year'] == 2016 and 'physical activity' in [d.lower() for d in paper['domain']]
]

print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-4911569923958279959': ['paper_docs'], 'var_function-call-3921672676854055861': 'file_storage/function-call-3921672676854055861.json'}

exec(code, env_args)
