code = """import json
import re

file_path = locals()['var_function-call-481143422120978278']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

relevant_paper_titles = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']

    title = filename.replace('.txt', '')

    # Check for '2016' in the first 1000 characters (header/metadata area)
    is_2016 = '2016' in text[:1000]

    # Check for 'physical activity' (case-insensitive) in the entire text
    is_physical_activity = 'physical activity' in text.lower()

    if is_2016 and is_physical_activity:
        relevant_paper_titles.append(title)

print('__RESULT__:')
print(json.dumps(relevant_paper_titles))"""

env_args = {'var_function-call-481143422120978278': 'file_storage/function-call-481143422120978278.json', 'var_function-call-3747855985844918712': [], 'var_function-call-15019300684085188001': []}

exec(code, env_args)
