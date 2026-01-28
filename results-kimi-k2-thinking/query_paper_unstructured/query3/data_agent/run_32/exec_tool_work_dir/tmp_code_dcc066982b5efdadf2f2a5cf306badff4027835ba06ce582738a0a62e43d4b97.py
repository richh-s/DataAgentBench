code = """import json
import re

# Load MongoDB data
storage_key_mongo = 'var_functions.query_db:34'
mongo_result = locals()[storage_key_mongo]

if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        all_papers = json.load(f)
else:
    all_papers = mongo_result

# Sample papers to understand structure
print('Sample papers:')
for i in range(min(3, len(all_papers))):
    paper = all_papers[i]
    filename = paper.get('filename', '')
    print(f"{i+1}. {filename}")

# Extract information from papers
paper_years = {}
for paper in all_papers:
    filename = paper.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    
    year = None
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    if year and 'empirical' in text.lower():
        paper_years[title] = year

print(f"\nEmpirical papers after 2016: {len([y for y in paper_years.values() if y > 2016])}")

# Load citations
storage_key_citations = 'var_functions.query_db:35'
citation_result = locals()[storage_key_citations]

if isinstance(citation_result, str) and citation_result.endswith('.json'):
    with open(citation_result, 'r') as f:
        citations = json.load(f)
else:
    citations = citation_result

print(f"Total citations: {len(citations)}")

# Find matches
results = []
citation_titles = {cit['title'].lower(): cit for cit in citations}

for title, year in paper_years.items():
    if year > 2016:
        if title.lower() in citation_titles:
            cit_data = citation_titles[title.lower()]
            results.append({
                'title': cit_data['title'],
                'year': year,
                'total_citations': int(cit_data['total_citations'])
            })

print(f"Found {len(results)} papers with both empirical contribution and citations")

results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

for i in range(min(10, len(results_sorted))):
    p = results_sorted[i]
    print(f"{i+1}. {p['title']} ({p['year']}) - {p['total_citations']} citations")

print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}}

exec(code, env_args)
