code = """import json
import re
import pandas as pd

file_path = locals()['var_function-call-481143422120978278']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

relevant_paper_titles = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']

    title = filename.replace('.txt', '')

    is_physical_activity = 'physical activity' in text.lower()

    if is_physical_activity:
        # Find all 4-digit numbers that could be years
        years_in_text = re.findall(r'\b(19|20)\d{2}\b', text)
        publication_year = None

        # Heuristic: assume the first encountered year is the publication year
        # This is a simplification; a more robust solution would involve checking context (e.g., 'Copyright', 'Published')
        if years_in_text:
            publication_year = int(years_in_text[0])

        if publication_year == 2016:
            relevant_paper_titles.append(title)

print('__RESULT__:')
print(json.dumps(relevant_paper_titles))"""

env_args = {'var_function-call-481143422120978278': 'file_storage/function-call-481143422120978278.json', 'var_function-call-3747855985844918712': [], 'var_function-call-15019300684085188001': [], 'var_function-call-13624425745219991834': []}

exec(code, env_args)
