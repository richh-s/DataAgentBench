code = """import json
import re

paper_docs_file_path = locals()['var_function-call-6544619829393036365']

with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_titles_for_2016_physical_activity = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # --- Year Extraction ---
    # Simplified: Check for '2016' explicitly and early in the document.
    year = None
    if '2016' in text[:1000]: # Check in the first 1000 characters
        year = 2016
    elif '2016' in text: # Fallback to check in the entire text
        year = 2016

    # --- Domain Extraction ---
    # Check for 'physical activity' explicitly in the text
    is_physical_activity_domain = 'physical activity' in text.lower()

    if year == 2016 and is_physical_activity_domain:
        extracted_titles_for_2016_physical_activity.append(title)

print("__RESULT__:")
print(json.dumps(extracted_titles_for_2016_physical_activity))"""

env_args = {'var_function-call-17463833612075543362': ['paper_docs'], 'var_function-call-6544619829393036365': 'file_storage/function-call-6544619829393036365.json', 'var_function-call-15282443211329679729': [], 'var_function-call-3755615379006169032': ['Citations', 'sqlite_sequence'], 'var_function-call-8085450063270148717': []}

exec(code, env_args)
