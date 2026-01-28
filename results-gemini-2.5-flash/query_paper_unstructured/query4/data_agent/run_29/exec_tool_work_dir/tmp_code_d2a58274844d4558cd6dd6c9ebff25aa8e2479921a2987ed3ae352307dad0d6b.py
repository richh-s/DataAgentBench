code = """import json
import re

file_path = locals()['var_function-call-18134843053043221786']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']

    # Extract title from filename
    title = filename.replace('.txt', '')

    # Extract year (assuming year is a 4-digit number, usually near the beginning of the text or in the first few lines)
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Extract domain (looking for 'physical activity' explicitly)
    domain = 'physical activity' if 'physical activity' in text.lower() else None
    
    if year == 2016 and domain == 'physical activity':
        papers_info.append({'title': title, 'year': year, 'domain': domain})

print('__RESULT__:')
print(json.dumps(papers_info))"""

env_args = {'var_function-call-5535784601978589816': ['paper_docs'], 'var_function-call-18134843053043221786': 'file_storage/function-call-18134843053043221786.json'}

exec(code, env_args)
