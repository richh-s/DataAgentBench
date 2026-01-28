code = """import json
import re

file_path = locals()['var_function-call-3921672676854055861']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

paper_titles_2016_physical_activity = []

for doc in paper_docs:
    text = doc['text'].lower()
    filename = doc['filename']
    title = filename.replace('.txt', '')

    # Check if '2016' is present in the text
    year_found = '2016' in text

    # Check if 'physical activity' is present in the text
    domain_found = 'physical activity' in text

    if year_found and domain_found:
        paper_titles_2016_physical_activity.append(title)

print("__RESULT__:")
print(json.dumps(paper_titles_2016_physical_activity))"""

env_args = {'var_function-call-4911569923958279959': ['paper_docs'], 'var_function-call-3921672676854055861': 'file_storage/function-call-3921672676854055861.json', 'var_function-call-12899150304275043457': [], 'var_function-call-12244209382016302219': []}

exec(code, env_args)
