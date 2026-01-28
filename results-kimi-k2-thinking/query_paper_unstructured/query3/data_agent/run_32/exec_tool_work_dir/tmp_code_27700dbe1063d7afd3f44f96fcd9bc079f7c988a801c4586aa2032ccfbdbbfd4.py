code = """import json
import re

# Load MongoDB data
mongo_key = 'var_functions.query_db:34'
with open(locals()[mongo_key], 'r') as f:
    mongo_data = json.load(f)

print('MongoDB papers: ' + str(len(mongo_data)))

# Find post-2016 empirical papers
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
    
    # Check for empirical keyword
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    if year and year > 2016 and has_empirical:
        empirical_papers.append(title)

print('Post-2016 empirical papers: ' + str(len(empirical_papers)))

# Show first 10
for i in range(min(10, len(empirical_papers))):
    print('  ' + str(i+1) + '. ' + empirical_papers[i])

# Load citation data
citation_key = 'var_functions.query_db:35'
with open(locals()[citation_key], 'r') as f:
    citations = json.load(f)

print('Citation records: ' + str(len(citations)))

# Show first 10 citation titles
print('\nFirst 10 citation titles:')
for i in range(min(10, len(citations))):
    print('  ' + str(i+1) + '. ' + citations[i]['title'])

# Check for exact matches
citation_titles = [c['title'] for c in citations]
citation_titles_lower = [t.lower() for t in citation_titles]

exact_matches = []
for paper in empirical_papers:
    if paper.lower() in citation_titles_lower:
        exact_matches.append(paper)

print('\nExact matches: ' + str(len(exact_matches)))

# If no exact matches, try to find similar ones
if len(exact_matches) == 0:
    print('No exact matches found. Looking for similar titles...')
    
    # Try partial matching
    for paper in empirical_papers[:20]:
        paper_lower = paper.lower()
        for cit_title in citation_titles[:20]:
            cit_lower = cit_title.lower()
            if paper_lower in cit_lower or cit_lower in paper_lower:
                print('  Similar: "' + paper + '" and "' + cit_title + '"')
                break

# Generate final results
citation_map = {c['title'].lower(): int(c['total_citations']) for c in citations}
final_papers = []

for paper in empirical_papers:
    key = paper.lower()
    if key in citation_map:
        final_papers.append({
            'title': paper,
            'total_citations': citation_map[key]
        })

final_papers.sort(key=lambda x: x['total_citations'], reverse=True)

print('\nFinal papers with citations: ' + str(len(final_papers)))

print('__RESULT__:')
print(json.dumps(final_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': []}

exec(code, env_args)
