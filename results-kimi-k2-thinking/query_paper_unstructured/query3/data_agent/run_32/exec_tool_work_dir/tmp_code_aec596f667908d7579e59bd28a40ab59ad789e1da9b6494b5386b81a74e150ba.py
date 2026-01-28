code = """import json
import re

# Read the MongoDB data file
mongo_file = var_functions.query_db:34
with open(mongo_file, 'r') as f:
    mongo_data = json.load(f)

# Process papers to extract metadata
papers = {}
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract publication year
    year = None
    # Pattern for venue format: CHI '17, UbiComp '15
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Pattern for full year: 2017, 2018
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check for empirical contribution
    is_empirical = False
    if 'empirical' in text.lower() or 'empirically' in text.lower():
        is_empirical = True
    
    papers[title.lower()] = {
        'title': title,
        'year': year,
        'empirical': is_empirical
    }

# Read the citation data file
citation_file = var_functions.query_db:35
with open(citation_file, 'r') as f:
    citations = json.load(f)

# Create citation map
citation_map = {}
for cit in citations:
    citation_map[cit['title'].lower()] = int(cit['total_citations'])

# Find matching papers: empirical, post-2016, with citations
results = []
for key, paper in papers.items():
    if paper['year'] and paper['year'] > 2016 and paper['empirical']:
        if key in citation_map:
            results.append([
                paper['title'],
                paper['year'],
                citation_map[key]
            ])

# Sort by citation count descending
results.sort(key=lambda x: x[2], reverse=True)

# Format output
output = []
for title, year, citations in results:
    output.append({
        'title': title,
        'year': year,
        'total_citations': citations
    })

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}}

exec(code, env_args)
