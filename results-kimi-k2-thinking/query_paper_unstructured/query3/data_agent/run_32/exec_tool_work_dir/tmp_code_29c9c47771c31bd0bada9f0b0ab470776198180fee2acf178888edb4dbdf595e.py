code = """import json
import re

# Load MongoDB data
storage_key = 'var_functions.query_db:24'
mongo_result = locals()[storage_key]

if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        all_papers = json.load(f)
else:
    all_papers = mongo_result

print('MongoDB papers: ' + str(len(all_papers)))

# Process papers
papers_data = {}

for paper in all_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year
    year = None
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check for empirical
    text_lower = text.lower()
    has_empirical = False
    if 'empirical' in text_lower or 'empirically' in text_lower:
        has_empirical = True
    else:
        intro = text_lower[:2000]
        indicators = ['we conducted', 'user study', 'experiment', 'participants', 'interview', 'survey']
        count = sum(1 for ind in indicators if ind in intro)
        if count >= 2:
            has_empirical = True
    
    if title:
        papers_data[title] = {'year': year, 'empirical': has_empirical}

# Load citations
storage_key = 'var_functions.query_db:26'
citation_result = locals()[storage_key]

if isinstance(citation_result, str) and citation_result.endswith('.json'):
    with open(citation_result, 'r') as f:
        citations = json.load(f)
else:
    citations = citation_result

print('Citation records: ' + str(len(citations)))

# Map titles to citations
citation_map = {}
for cit in citations:
    citation_map[cit['title']] = int(cit['total_citations'])

# Find matching papers
matches = []
for title, data in papers_data.items():
    if data['year'] and data['year'] > 2016 and data['empirical']:
        citations = citation_map.get(title, 0)
        matches.append({'title': title, 'year': data['year'], 'citations': citations})

# Sort
matches_sorted = sorted(matches, key=lambda x: x['citations'], reverse=True)

print('Found papers: ' + str(len(matches_sorted)))
print('Top 10:')
for i in range(min(10, len(matches_sorted))):
    p = matches_sorted[i]
    print(str(i+1) + '. ' + p['title'][:60] + ' (' + str(p['year']) + ') - ' + str(p['citations']))

print('__RESULT__:')
print(json.dumps(matches_sorted))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
