code = """import json
import re

file_path = locals()['var_function-call-4281778254792506949']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers_all_years = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    is_physical_activity_domain = 'physical activity' in text.lower()

    if is_physical_activity_domain:
        year = None
        # Attempt to extract year from the first 500 characters, which usually contain publication info
        year_matches = re.findall(r'\b(19|20)\d{2}\b', text[:500])
        if year_matches:
            year = int(year_matches[0]) # Take the first year found in the header

        extracted_papers_all_years.append({
            'title': title,
            'year': year,
            'domain': 'physical activity'
        })

filtered_papers_2016 = [
    p for p in extracted_papers_all_years
    if p['year'] == 2016
]

result = json.dumps(filtered_papers_2016)
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9075844566900917724': ['paper_docs'], 'var_function-call-4281778254792506949': 'file_storage/function-call-4281778254792506949.json', 'var_function-call-6950853866291229053': [], 'var_function-call-17897123819145337208': ['Citations', 'sqlite_sequence'], 'var_function-call-6166251359363205848': [], 'var_function-call-13090763116385204972': []}

exec(code, env_args)
