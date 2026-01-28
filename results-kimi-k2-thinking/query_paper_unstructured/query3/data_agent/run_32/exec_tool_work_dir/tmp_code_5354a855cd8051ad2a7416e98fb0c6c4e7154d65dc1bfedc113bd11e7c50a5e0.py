code = """import json
import re

# Get MongoDB data from storage
mongo_key = 'var_functions.query_db:34'
mongo_path = locals()[mongo_key]

# Load the JSON file
with open(mongo_path, 'r') as f:
    mongo_data = json.load(f)

# Get citation data from storage
citation_key = 'var_functions.query_db:35'
citation_path = locals()[citation_key]

# Load citations
with open(citation_path, 'r') as f:
    citations = json.load(f)

print('Loaded ' + str(len(mongo_data)) + ' papers and ' + str(len(citations)) + ' citation records')

# Process papers to find empirical, post-2016 papers
empirical_papers = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract year from text
    year = None
    # Try venue format: CHI '17, Ubicomp '15
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Try full year format: 2017, 2018
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check if paper has empirical contribution
    text_lower = text.lower()
    has_empirical = 'empirical' in text_lower or 'empirically' in text_lower
    
    # Include papers after 2016 with empirical contribution
    if year and year > 2016 and has_empirical:
        empirical_papers.append({'title': title, 'year': year})

print('Found ' + str(len(empirical_papers)) + ' empirical papers after 2016')

# Build citation map for fast lookup
citation_map = {}
for cit in citations:
    citation_map[cit['title'].lower()] = int(cit['total_citations'])

# Join with citations and create final results
results = []
for paper in empirical_papers:
    title_lower = paper['title'].lower()
    if title_lower in citation_map:
        results.append({
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': citation_map[title_lower]
        })

# Sort by total citation count (descending)
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('Found ' + str(len(results)) + ' papers with citation data')
print('\nTop papers:')
for i, paper in enumerate(results[:10]):
    print(str(i+1) + '. ' + paper['title'] + ' (' + str(paper['year']) + ') - ' + str(paper['total_citations']) + ' citations')

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': []}

exec(code, env_args)
