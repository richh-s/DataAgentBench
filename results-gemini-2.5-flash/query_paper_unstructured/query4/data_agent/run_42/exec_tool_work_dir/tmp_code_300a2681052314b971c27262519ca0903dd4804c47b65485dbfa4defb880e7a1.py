code = """import json
import re

file_path = locals()['var_function-call-1020461737059661264']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_paper_info = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Extract year: search for a 4-digit number that looks like a year (19xx or 20xx) in the entire text
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Check for 'physical activity' domain (case-insensitive)
    is_physical_activity_domain = 'physical activity' in text.lower()

    extracted_paper_info.append({
        'title': title,
        'year': year,
        'is_physical_activity_domain': is_physical_activity_domain
    })

print('__RESULT__:')
print(json.dumps(extracted_paper_info))"""

env_args = {'var_function-call-10668140555731164678': ['paper_docs'], 'var_function-call-1020461737059661264': 'file_storage/function-call-1020461737059661264.json', 'var_function-call-18293935031113841746': [], 'var_function-call-2347887543621677021': ['Citations', 'sqlite_sequence'], 'var_function-call-13651244775567562643': []}

exec(code, env_args)
