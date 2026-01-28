code = """import json
import re

# Load data from storage
mongo_file = var_functions.query_db:34
with open(mongo_file, 'r') as f:
    mongo_data = json.load(f)

citation_file = var_functions.query_db:35
with open(citation_file, 'r') as f:
    citations = json.load(f)

print('MongoDB papers: ' + str(len(mongo_data)))
print('Citation records: ' + str(len(citations)))

# Process papers
empirical_papers = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract year
    year = None
    m = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if m:
        year = 2000 + int(m.group(1))
    else:
        m = re.search(r"\b(20\d{2})\b", text)
        if m:
            year = int(m.group(1))
    
    # Check empirical
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    if year and year > 2016 and has_empirical:
        empirical_papers.append({'title': title, 'year': year})

print('Post-2016 empirical papers: ' + str(len(empirical_papers)))

# Build citation map
citation_map = {}
for c in citations:
    citation_map[c['title'].lower()] = int(c['total_citations'])

# Join and get citation counts
results = []
for paper in empirical_papers:
    title_lower = paper['title'].lower()
    if title_lower in citation_map:
        results.append({
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': citation_map[title_lower]
        })

# Sort by citations
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Show summary
print('Papers with citations: ' + str(len(results)))
for i in range(min(10, len(results))):
    p = results[i]
    print(str(i+1) + '. ' + p['title'] + ' (' + str(p['year']) + ') - ' + str(p['total_citations']) + ' citations')

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': []}

exec(code, env_args)
