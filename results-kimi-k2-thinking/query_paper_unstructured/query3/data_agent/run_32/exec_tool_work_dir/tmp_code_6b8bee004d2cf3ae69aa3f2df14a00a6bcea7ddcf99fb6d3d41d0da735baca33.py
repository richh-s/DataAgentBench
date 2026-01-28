code = """import json
import re

# Load data from storage
mongo_path = locals()['var_functions.query_db:70']
citation_path = locals()['var_functions.query_db:71']

with open(mongo_path, 'r') as f:
    mongo_data = json.load(f)

with open(citation_path, 'r') as f:
    citations = json.load(f)

# Build citation map for exact matching
citation_title_map = {}
for item in citations:
    citation_title_map[item['title']] = int(item['total_citations'])

# Process papers and find matches
final_results = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract year using regex patterns
    year = None
    
    # Try venue format first
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Try full year format
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check for empirical contribution keyword
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    # Apply filters and check citation data exists
    if year and year > 2016 and has_empirical and title in citation_title_map:
        final_results.append({
            'title': title,
            'total_citations': citation_title_map[title]
        })

# Sort by total citations descending
final_results.sort(key=lambda x: x['total_citations'], reverse=True)

# Output results
print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': []}

exec(code, env_args)
