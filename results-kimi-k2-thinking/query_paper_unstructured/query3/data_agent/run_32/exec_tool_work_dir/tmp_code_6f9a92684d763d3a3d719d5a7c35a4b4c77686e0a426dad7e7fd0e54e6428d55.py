code = """import json
import re

# Load data from storage
mongo_key = 'var_functions.query_db:70'
citation_key = 'var_functions.query_db:71'

mongo_data = locals()[mongo_key]
citations = locals()[citation_key]

# If they're file paths, read them
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as file:
        mongo_data = json.load(file)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as file:
        citations = json.load(file)

# Check data sizes
mongo_size = len(mongo_data)
citation_size = len(citations)

# Find empirical papers after 2016
empirical_papers_filtered = []

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
    has_empirical = 'empirical' in text_lower
    
    # Filter
    if year and year > 2016 and has_empirical:
        empirical_papers_filtered.append({'title': title, 'year': year})

# Build citation map
citation_map = {}
for cit in citations:
    citation_map[cit['title'].lower()] = int(cit['total_citations'])

# Join and create final results
final_results = []
for paper in empirical_papers_filtered:
    title_lower = paper['title'].lower()
    if title_lower in citation_map:
        final_results.append({
            'title': paper['title'],
            'total_citations': citation_map[title_lower]
        })

# Sort by citations descending
def citation_key(item):
    return item['total_citations']
final_results.sort(key=citation_key, reverse=True)

# Return the final formatted answer
print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': []}

exec(code, env_args)
