code = """import json

# Load data from files
with open('var_functions.query_db:18', 'r') as f:
    citations_2018 = json.load(f)

with open('var_functions.query_db:20', 'r') as f:
    paper_docs = json.load(f)

print('Loaded {} 2018 citations and {} paper documents'.format(len(citations_2018), len(paper_docs)))

# Show first few titles from each
print('\n=== First 5 Citation Titles===')
for i, c in enumerate(citations_2018[:5]):
    print('{}. {}'.format(i+1, c['title']))

print('\n=== First 5 Paper Document Titles===')
for i, doc in enumerate(paper_docs[:5]):
    title = doc['filename'].replace('.txt', '')
    print('{}. {}'.format(i+1, title))

# Count ACM papers and create title list
acm_titles = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Simple ACM check
    is_acm = False
    if 'ACM' in text:
        is_acm = True
    elif 'Association for Computing Machinery' in text:
        is_acm = True
    elif 'http://dx.doi.org/10.1145/' in text:
        is_acm = True
    
    if is_acm:
        acm_titles.append(title)

print('\n=== ACM Papers Found: {} ==='.format(len(acm_titles)))

# Create citation map
citation_map = {}
for item in citations_2018:
    citation_map[item['title']] = int(item['citation_count'])

# Find matches
matched_values = []
for title in acm_titles:
    if title in citation_map:
        matched_values.append(citation_map[title])

print('Matched papers with 2018 citations: {}'.format(len(matched_values)))

if matched_values:
    avg = sum(matched_values) / len(matched_values)
    result = {'average': round(avg, 2), 'count': len(matched_values), 'total': sum(matched_values)}
else:
    # Debug: show which titles are close
    print('\n=== Debug: Checking for near matches ===') 
    citation_titles = list(citation_map.keys())
    acm_sample = acm_titles[:10] if acm_titles else []
    print('Sample ACM titles:', acm_sample)
    
    result = {'average': 0, 'count': 0, 'total': 0}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'average_citations': 0, 'total_papers': 0, 'total_citations': 0}}

exec(code, env_args)
