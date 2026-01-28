code = """import json
import re

# Load MongoDB data from storage
mongo_path = 'var_functions.query_db:70'
with open(locals()[mongo_path], 'r') as f:
    mongo_data = json.load(f)

# Load citation data from storage  
citation_path = 'var_functions.query_db:71'
with open(locals()[citation_path], 'r') as f:
    citations = json.load(f)

# Build citation map
citation_map = {}
for item in citations:
    citation_map[item['title']] = int(item['total_citations'])

# Find empirical papers after 2016
results = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract year
    year = None
    
    # Try venue format: CHI '17, UbiComp '15
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Try full year format: 2017, 2018
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    # Filter and collect
    if year and year > 2016 and has_empirical and title in citation_map:
        results.append({
            'title': title,
            'total_citations': citation_map[title]
        })

# Sort by total citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Return results
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': []}

exec(code, env_args)
