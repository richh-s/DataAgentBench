code = """import json
import re

# Load data
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Build citation lookup
citation_counts = {}
for cit in citations:
    citation_counts[cit['title']] = int(cit['total_citations'])

# Find matching papers
results = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    
    # Must have citation
    if title not in citation_counts:
        continue
    
    text = doc.get('text', '')
    
    # Check empirical
    if 'empirical' not in text.lower() and 'empirically' not in text.lower():
        continue
    
    # Extract year
    year = None
    match = re.search(r"\b(20\d{2})\b", text)
    if match:
        year = int(match.group(1))
    
    # Must be post-2016
    if not year or year <= 2016:
        continue
    
    # Add to results
    results.append({
        'title': title,
        'total_citations': citation_counts[title]
    })

# Sort
def sort_func(x):
    return x['total_citations']
results.sort(key=sort_func, reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': [], 'var_functions.execute_python:120': [], 'var_functions.execute_python:124': [], 'var_functions.execute_python:130': [], 'var_functions.execute_python:134': [], 'var_functions.execute_python:138': [], 'var_functions.execute_python:140': [], 'var_functions.execute_python:146': []}

exec(code, env_args)
