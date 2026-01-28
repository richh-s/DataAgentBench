code = """import json
import re

# Load data from storage
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

# Load from file paths if needed
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Build citation map for exact matching
citation_map = {cit['title']: int(cit['total_citations']) for cit in citations}

# Simple extraction
titles_and_citations = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    
    # Only include papers with citation data
    if title not in citation_map:
        continue
    
    text = doc.get('text', '')
    
    # Extract year
    year = None
    match = re.search(r"\b(20\d{2})\b", text)
    if match:
        year = int(match.group(1))
    
    # Check empirical
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    # Apply filters
    if year and year > 2016 and has_empirical:
        titles_and_citations.append({
            'title': title,
            'total_citations': citation_map[title]
        })

# Sort
if titles_and_citations:
    titles_and_citations.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(titles_and_citations))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': [], 'var_functions.execute_python:120': [], 'var_functions.execute_python:124': [], 'var_functions.execute_python:130': [], 'var_functions.execute_python:134': [], 'var_functions.execute_python:138': [], 'var_functions.execute_python:140': []}

exec(code, env_args)
