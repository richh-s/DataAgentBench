code = """import json
import re

file_path = locals()['var_function-call-4281778254792506949']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers_all = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Check for 'physical activity' (case-insensitive) anywhere in the text
    is_physical_activity_domain = 'physical activity' in text.lower()

    if is_physical_activity_domain:
        year = None
        # Search for a 4-digit number that could be a year, anywhere in the text
        year_matches = re.findall(r'\b(19|20)\d{2}\b', text)
        if year_matches:
            # Take the first year found as a heuristic for publication year
            year = int(year_matches[0])

        extracted_papers_all.append({
            'title': title,
            'year': year,
            'domain': 'physical activity'
        })

# Now filter for year 2016
filtered_papers_2016 = [
    p for p in extracted_papers_all
    if p['year'] == 2016
]

result = json.dumps(filtered_papers_2016)
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9075844566900917724': ['paper_docs'], 'var_function-call-4281778254792506949': 'file_storage/function-call-4281778254792506949.json', 'var_function-call-6950853866291229053': [], 'var_function-call-17897123819145337208': ['Citations', 'sqlite_sequence'], 'var_function-call-6166251359363205848': [], 'var_function-call-13090763116385204972': [], 'var_function-call-588974641254065992': []}

exec(code, env_args)
