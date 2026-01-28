code = """import json
import re

file_path = locals()['var_function-call-1692856430574437230']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_2016_physical_activity = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Check for 'physical activity' domain and '2016' as publication year.
    # A simple keyword search for '2016' is often sufficient for publication year.
    # We'll assume if '2016' appears prominently in the document, it's likely the publication year.
    # Also ensuring 'physical activity' is in the text.
    if '2016' in text and re.search(r'physical activity', text, re.IGNORECASE):
        papers_2016_physical_activity.append({'title': title})

print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_function-call-1692856430574437230': 'file_storage/function-call-1692856430574437230.json', 'var_function-call-17662153190898920493': []}

exec(code, env_args)
