code = """import os
import json

data_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            data_files.append(os.path.join(root, file))

# Identify file types
citations_file = None
papers_file = None

for filepath in data_files:
    with open(filepath) as f:
        data = json.load(f)
    if data and isinstance(data, list):
        if len(data) > 0:
            first_item = data[0]
            if 'title' in first_item and 'total_citations' in first_item:
                citations_file = filepath
            elif 'filename' in first_item and 'text' in first_item:
                papers_file = filepath

with open(citations_file) as f:
    citations = json.load(f)
with open(papers_file) as f:
    papers = json.load(f)

food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
food_titles = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    for kw in food_keywords:
        if kw in text:
            food_titles.append(filename.replace('.txt', ''))
            break

citation_totals = {c['title']: int(c['total_citations']) for c in citations}

total_citations = 0
for title in food_titles:
    if title in citation_totals:
        total_citations += citation_totals[title]

result = {"total_citations": total_citations}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:52': {'total_citations': 0}}

exec(code, env_args)
