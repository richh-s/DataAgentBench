code = """import json
import re

# Load MongoDB data from storage
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

# If they're file paths, read them
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

print('Total papers:', len(mongo_data))
print('Total citations:', len(citations))

# Extract empirical papers published after 2016
empirical_papers_2017plus = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract year from text
    year = None
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    # Check for empirical contribution
    text_lower = text.lower()
    has_empirical = False
    
    if 'empirical' in text_lower or 'empirically' in text_lower:
        has_empirical = True
    
    # Filter: after 2016 and has empirical contribution
    if year and year > 2016 and has_empirical:
        empirical_papers_2017plus.append({'title': title, 'year': year})

print('Empirical papers after 2016:', len(empirical_papers_2017plus))

# Build citation map for efficient lookup
citation_map = {}
for cit in citations:
    citation_title = cit['title'].lower()
    total_citations = int(cit['total_citations'])
    citation_map[citation_title] = total_citations

# Join papers with citation data
results = []
for paper in empirical_papers_2017plus:
    paper_title_lower = paper['title'].lower()
    if paper_title_lower in citation_map:
        results.append({
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': citation_map[paper_title_lower]
        })

# Sort results by total citation count (descending)
def get_citation_count(p):
    return p['total_citations']
results.sort(key=get_citation_count, reverse=True)

print('Papers with citation data:', len(results))

# Create final answer - list of papers with title and total citations
final_answer_list = []
for paper in results:
    final_answer_list.append({
        'title': paper['title'],
        'total_citations': paper['total_citations']
    })

print('__RESULT__:')
print(json.dumps(final_answer_list))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': []}

exec(code, env_args)
