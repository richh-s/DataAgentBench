code = """import json
import re

# Load data from storage
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

# Convert from file paths if needed
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Find all papers with empirical contribution after 2016
empirical_papers = []

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
    
    # Check if paper has empirical contribution
    text_lower = text.lower()
    has_empirical = 'empirical' in text_lower or 'empirically' in text_lower
    
    # Include only papers after 2016 with empirical contribution
    if year and year > 2016 and has_empirical:
        empirical_papers.append({'title': title, 'year': year})

# Build citation map for efficient lookup
citation_map = {}
for cit in citations:
    lower_title = cit['title'].lower()
    total_citations = int(cit['total_citations'])
    citation_map[lower_title] = total_citations

# Join papers with citation data
results = []
for paper in empirical_papers:
    lower_title = paper['title'].lower()
    if lower_title in citation_map:
        results.append({
            'title': paper['title'],
            'total_citations': citation_map[lower_title]
        })

# Sort by total citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Return results
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': []}

exec(code, env_args)
