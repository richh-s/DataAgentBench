code = """import json
import re

file_path = locals()['var_function-call-3921672676854055861']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_titles = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    is_2016 = False
    # Check for '2016' as a publication year indicator, robustly.
    # Common patterns: YEAR, Year, 2016
    if re.search(r'\b2016\b', text):
        is_2016 = True

    is_physical_activity_domain = False
    if 'physical activity' in text.lower():
        is_physical_activity_domain = True
    
    if is_2016 and is_physical_activity_domain:
        extracted_titles.append(title)

print("__RESULT__:")
print(json.dumps(extracted_titles))"""

env_args = {'var_function-call-4911569923958279959': ['paper_docs'], 'var_function-call-3921672676854055861': 'file_storage/function-call-3921672676854055861.json', 'var_function-call-12899150304275043457': []}

exec(code, env_args)
