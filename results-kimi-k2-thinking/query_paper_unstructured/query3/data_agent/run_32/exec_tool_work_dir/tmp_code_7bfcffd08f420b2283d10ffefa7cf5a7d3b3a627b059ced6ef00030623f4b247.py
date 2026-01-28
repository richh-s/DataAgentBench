code = """import json
import re

# Load MongoDB data from storage reference
mongo_path = 'var_functions.query_db:70'
with open(locals()[mongo_path], 'r') as f:
    mongo_data = json.load(f)

# Load citation data from storage reference
citation_path = 'var_functions.query_db:71'
with open(locals()[citation_path], 'r') as f:
    citations = json.load(f)

# Build citation map for lookup
citation_map = {}
for cit in citations:
    citation_map[cit['title']] = int(cit['total_citations'])

# Find papers meeting all criteria
results = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract year
    year = None
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    # Check citation data exists
    if title not in citation_map:
        continue
    
    # Apply all filters
    if year and year > 2016 and has_empirical:
        results.append({
            'title': title,
            'total_citations': citation_map[title]
        })

# Sort by total citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Print result
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': [], 'var_functions.execute_python:120': [], 'var_functions.execute_python:124': [], 'var_functions.execute_python:130': [], 'var_functions.execute_python:134': [], 'var_functions.execute_python:138': [], 'var_functions.execute_python:140': [], 'var_functions.execute_python:146': [], 'var_functions.execute_python:150': [], 'var_functions.execute_python:152': []}

exec(code, env_args)
