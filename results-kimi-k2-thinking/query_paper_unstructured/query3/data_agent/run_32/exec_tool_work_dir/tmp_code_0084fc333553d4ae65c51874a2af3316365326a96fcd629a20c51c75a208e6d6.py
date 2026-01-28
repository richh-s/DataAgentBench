code = """import json
import re

# Load MongoDB data - get file path from storage
mongo_file = var_functions.query_db:34
with open(mongo_file, 'r') as f:
    all_papers = json.load(f)

print('Total papers: ' + str(len(all_papers)))

# Extract paper info
paper_dict = {}
for p in all_papers:
    filename = p.get('filename', '')
    if not filename:
        continue
    title = filename.replace('.txt', '')
    text = p.get('text', '')
    
    # Find year
    year = None
    m = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if m:
        year = 2000 + int(m.group(1))
    else:
        m = re.search(r"\b(20\d{2})\b", text)
        if m:
            year = int(m.group(1))
    
    # Check empirical
    is_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    paper_dict[title.lower()] = {
        'title': title,
        'year': year,
        'empirical': is_empirical
    }

print('Processed: ' + str(len(paper_dict)))

# Count post-2016 empirical papers
post_2016_count = 0
for t, info in paper_dict.items():
    if info['year'] and info['year'] > 2016 and info['empirical']:
        post_2016_count += 1

print('Post-2016 empirical papers: ' + str(post_2016_count))

# Load citations
citation_file = var_functions.query_db:35
with open(citation_file, 'r') as f:
    citations = json.load(f)

citation_map = {}
for c in citations:
    citation_map[c['title'].lower()] = int(c['total_citations'])

print('Citations: ' + str(len(citation_map)))

# Find matches
matches = []
for key, info in paper_dict.items():
    if info['year'] and info['year'] > 2016 and info['empirical'] and key in citation_map:
        matches.append({
            'title': info['title'],
            'year': info['year'],
            'total_citations': citation_map[key]
        })

# Sort by citations descending
matches_sorted = sorted(matches, key=lambda x: x['total_citations'], reverse=True)

print('Found matches: ' + str(len(matches_sorted)))

# Print top 5
print('\nTop 5 papers:')
for i in range(min(5, len(matches_sorted))):
    p = matches_sorted[i]
    output = str(i+1) + '. ' + p['title'] + ' (' + str(p['year']) + ') - ' + str(p['total_citations']) + ' citations'
    print(output)

# Return full results
result = {
    'papers': matches_sorted,
    'count': len(matches_sorted)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}}

exec(code, env_args)
