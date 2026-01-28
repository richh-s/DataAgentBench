code = """import json
import re

# Load data from storage
mongo_path = var_functions.query_db:34
citation_path = var_functions.query_db:35

with open(mongo_path, 'r') as f:
    mongo_data = json.load(f)

with open(citation_path, 'r') as f:
    citations = json.load(f)

print('MongoDB papers: ' + str(len(mongo_data)))
print('Citation records: ' + str(len(citations)))

# Extract title from filename
def get_title(filename):
    if filename:
        return filename.replace('.txt', '')
    return ''

# Extract year from text  
def extract_year(text):
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        return 2000 + int(match.group(1))
    match = re.search(r"\b(20\d{2})\b", text)
    if match:
        return int(match.group(1))
    return None

# Check if paper mentions empirical contribution
def has_empirical(text):
    return 'empirical' in text.lower() or 'empirically' in text.lower()

# Process papers
empirical_2017plus = []
for doc in mongo_data:
    title = get_title(doc.get('filename', ''))
    text = doc.get('text', '')
    
    if not title or not text:
        continue
    
    year = extract_year(text)
    if year and year > 2016 and has_empirical(text):
        empirical_2017plus.append({'title': title, 'year': year})

print('Empirical papers after 2016: ' + str(len(empirical_2017plus)))

# Build citation lookup
citation_lookup = {}
for cit in citations:
    citation_lookup[cit['title'].lower()] = int(cit['total_citations'])

# Join with citations
results = []
for paper in empirical_2017plus:
    title_lower = paper['title'].lower()
    if title_lower in citation_lookup:
        results.append({
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': citation_lookup[title_lower]
        })

# Sort by citations
def cit_sort(p):
    return p['total_citations']
results.sort(key=cit_sort, reverse=True)

print('Final matched papers: ' + str(len(results)))
if results:
    print('\nTop 5:')
    for i in range(min(5, len(results))):
        p = results[i]
        print(str(i+1) + '. "' + p['title'] + '" (' + str(p['year']) + ') - ' + str(p['total_citations'] + ' citations'))
else:
    print('No matches found')

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json'}

exec(code, env_args)
