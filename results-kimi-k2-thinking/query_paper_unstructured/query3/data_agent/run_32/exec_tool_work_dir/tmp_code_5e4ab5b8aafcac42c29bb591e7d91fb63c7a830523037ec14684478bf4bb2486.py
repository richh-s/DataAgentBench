code = """import json
import re

# Access storage keys directly
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

# If they're file paths, read them
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    mongo_data = json.load(open(mongo_data))
if isinstance(citations, str) and citations.endswith('.json'):
    citations = json.load(open(citations))

# Extract empirical papers after 2016
empirical_2017plus = []
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
    
    # Check empirical contribution
    text_lower = text.lower()
    has_empirical = 'empirical' in text_lower or 'empirically' in text_lower
    
    if year and year > 2016 and has_empirical:
        empirical_2017plus.append({'title': title, 'year': year})

# Build citation map
citation_map = {}
for cit in citations:
    citation_map[cit['title'].lower()] = int(cit['total_citations'])

# Join with citations
results = []
for paper in empirical_2017plus:
    title_lower = paper['title'].lower()
    if title_lower in citation_map:
        results.append({
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': citation_map[title_lower]
        })

# Sort by citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Create output
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json'}

exec(code, env_args)
