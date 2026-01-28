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

print('Total papers in MongoDB: ' + str(len(all_papers)))

# Sample the first few papers to see structure
for i, paper in enumerate(all_papers[:5]):
    filename = paper.get('filename', 'No filename')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')[:200]
    print('\nPaper ' + str(i+1) + ':')
    print('  Filename: ' + filename)
    print('  Title: ' + title)
    print('  Text preview: ' + text[:100])

# Check year extraction
year_counts = {}
post_2016_count = 0

for paper in all_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    # Try different year patterns
    year = None
    
    # Pattern 1: Look for venue notation
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Pattern 2: Look for full year
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1
        if year > 2016:
            post_2016_count += 1

print('\nYears found:')
sorted_years = sorted(year_counts.items())
for year, count in sorted_years[-10:]:  # Last 10 years
    print('  ' + str(year) + ': ' + str(count))

print('\nTotal papers after 2016: ' + str(post_2016_count))

# Check for empirical mentions
empirical_count = 0
empirical_papers = []

for paper in all_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    # Extract year first
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
    if 'empirical' in text_lower or 'empirically' in text_lower:
        empirical_count += 1
        if year and year > 2016:
            empirical_papers.append({'title': title, 'year': year})

print('\nTotal papers with empirical keyword: ' + str(empirical_count))
print('Empirical papers after 2016: ' + str(len(empirical_papers)))

for i, paper in enumerate(empirical_papers[:10]):
    print('  ' + str(i+1) + '. ' + paper['title'] + ' (' + str(paper['year']) + ')')

# Now check citations
storage_key_citations = 'var_functions.query_db:35'
citation_result = locals()[storage_key_citations]

if isinstance(citation_result, str) and citation_result.endswith('.json'):
    with open(citation_result, 'r') as f:
        citations = json.load(f)
else:
    citations = citation_result

print('\nTotal citation records: ' + str(len(citations)))

# Sample citations
for i in range(min(5, len(citations))):
    cit = citations[i]
    print('Citation ' + str(i+1) + ': ' + cit['title'] + ' = ' + cit['total_citations'])

# Check if any empirical papers have citations
citation_titles = [cit['title'].lower() for cit in citations]

matching_titles = []
for paper in empirical_papers:
    if paper['title'].lower() in citation_titles:
        matching_titles.append(paper['title'])

print('\nEmpirical papers after 2016 with citation records: ' + str(len(matching_titles)))
if matching_titles:
    print('Sample matching titles:')
    for title in matching_titles[:5]:
        print('  ' + title)
else:
    print('No matches found!')

print('__RESULT__:')
print(json.dumps({'empirical_papers_2017+': len(empirical_papers), 'matches': len(matching_titles)}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}}

exec(code, env_args)
