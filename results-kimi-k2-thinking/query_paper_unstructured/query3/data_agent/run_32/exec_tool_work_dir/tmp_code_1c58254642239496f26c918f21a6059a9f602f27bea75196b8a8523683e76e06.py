code = """import json
import re

# Load MongoDB data from storage
mongo_key = 'var_functions.query_db:34'
if isinstance(locals()[mongo_key], str) and locals()[mongo_key].endswith('.json'):
    with open(locals()[mongo_key], 'r') as f:
        mongo_data = json.load(f)
else:
    mongo_data = locals()[mongo_key]

# Process papers
papers = {}
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract year
    year = None
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check if empirical
    is_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    if title and year and is_empirical and year > 2016:
        papers[title.lower()] = [title, year]

# Load citations
citation_key = 'var_functions.query_db:35'
if isinstance(locals()[citation_key], str) and locals()[citation_key].endswith('.json'):
    with open(locals()[citation_key], 'r') as f:
        citations = json.load(f)
else:
    citations = locals()[citation_key]

# Build citation map
citation_map = {}
for cit in citations:
    citation_map[cit['title'].lower()] = int(cit['total_citations'])

# Join data
results = []
for key, value in papers.items():
    if key in citation_map:
        results.append({
            'title': value[0],
            'year': value[1],
            'total_citations': citation_map[key]
        })

# Sort by citations
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}}

exec(code, env_args)
