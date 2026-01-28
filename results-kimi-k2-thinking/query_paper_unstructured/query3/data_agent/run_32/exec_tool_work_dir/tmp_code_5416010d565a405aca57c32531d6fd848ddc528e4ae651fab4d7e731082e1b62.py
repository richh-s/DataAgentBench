code = """import json
import re

# Load data
mongo_key = 'var_functions.query_db:70'
citation_key = 'var_functions.query_db:71'

mongo_data = locals()[mongo_key]
citations = locals()[citation_key]

if isinstance(mongo_data, str):
    mongo_data = json.load(open(mongo_data))
if isinstance(citations, str):
    citations = json.load(open(citations))

# Count empirical papers after 2016
empirical_2017plus = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
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
    if year and year > 2016 and ('empirical' in text.lower() or 'empirically' in text.lower()):
        empirical_2017plus.append({'title': title, 'year': year})

# Build citation map
citation_map = {}
for cit in citations:
    citation_map[cit['title'].lower()] = int(cit['total_citations'])

# Join with citations
results = []
for paper in empirical_2017plus:
    if paper['title'].lower() in citation_map:
        results.append({
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': citation_map[paper['title'].lower()]
        })

# Sort
def get_citations(item):
    return item['total_citations']
results.sort(key=get_citations, reverse=True)

# Debug output
print('Total papers:', len(mongo_data))
print('Empirical papers after 2016:', len(empirical_2017plus))
print('Papers with citations:', len(results))

# Show sample matches
if results:
    print('Top 10:')
    for i in range(min(10, len(results))):
        p = results[i]
        print(str(i+1) + '. ' + p['title'] + ' (' + str(p['year']) + ') - ' + str(p['total_citations']))
else:
    # Show what empirical papers were found
    print('Empirical papers found:')
    for i in range(min(10, len(empirical_2017plus))):
        p = empirical_2017plus[i]
        print(str(i+1) + '. ' + p['title'] + ' (' + str(p['year']) + ')')
    
    # Show sample citation titles  
    print('\nSample citation titles:')
    for i in range(min(10, len(citations))):
        print(citations[i]['title'])

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': []}

exec(code, env_args)
