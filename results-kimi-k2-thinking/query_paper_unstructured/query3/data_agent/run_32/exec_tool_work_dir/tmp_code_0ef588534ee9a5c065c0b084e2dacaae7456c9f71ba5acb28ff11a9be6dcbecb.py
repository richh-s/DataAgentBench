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

print('Loaded papers: ' + str(len(all_papers)))

# Extract year and check for empirical papers
year_counts = {}
empirical_papers = {}

for paper in all_papers:
    filename = paper.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    
    # Extract year
    year = None
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1
        
        # Check if empirical
        if 'empirical' in text.lower() or 'empirically' in text.lower():
            empirical_papers[title] = year

print('Years found: ' + str(len(year_counts)))
print('Years 2017+: ' + str(len([y for y in year_counts.keys() if y > 2016])))
print('Empirical papers found: ' + str(len(empirical_papers)))

# Filter for post-2016 empirical papers
empirical_post_2016 = {title: year for title, year in empirical_papers.items() if year > 2016}
print('Empirical papers after 2016: ' + str(len(empirical_post_2016)))

# Load citations
storage_key_citations = 'var_functions.query_db:35'
citation_result = locals()[storage_key_citations]

if isinstance(citation_result, str) and citation_result.endswith('.json'):
    with open(citation_result, 'r') as f:
        citations = json.load(f)
else:
    citations = citation_result

print('Citation records: ' + str(len(citations)))

# Find intersections
results = []
citation_titles = {}

for cit in citations:
    title_key = cit['title'].lower()
    citation_titles[title_key] = int(cit['total_citations'])

for title in empirical_post_2016:
    title_key = title.lower()
    if title_key in citation_titles:
        results.append({
            'title': title,
            'year': empirical_post_2016[title],
            'total_citations': citation_titles[title_key]
        })

print('Matches found: ' + str(len(results)))

# Sort by citations
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Show top 10
print('\nTop 10 papers:')
for i in range(min(10, len(results_sorted))):
    p = results_sorted[i]
    print(str(i+1) + '. ' + p['title'] + ' (' + str(p['year']) + ') - ' + str(p['total_citations']) + ' citations')

print('\n__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}}

exec(code, env_args)
