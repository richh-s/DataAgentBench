code = """import json
import re
import pandas as pd

file_path = locals()['var_function-call-481143422120978278']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

relevant_papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']

    title = filename.replace('.txt', '')

    # Check if '2016' is present anywhere in the text as a strong indicator of publication year
    is_2016_paper = '2016' in text

    # Check if 'physical activity' (case-insensitive) is present in the text
    is_physical_activity_domain = 'physical activity' in text.lower()

    if is_2016_paper and is_physical_activity_domain:
        relevant_papers_info.append({'title': title})

print('__RESULT__:')
print(json.dumps(relevant_papers_info))"""

env_args = {'var_function-call-481143422120978278': 'file_storage/function-call-481143422120978278.json', 'var_function-call-3747855985844918712': [], 'var_function-call-15019300684085188001': [], 'var_function-call-13624425745219991834': [], 'var_function-call-11123221346862781213': []}

exec(code, env_args)
