code = """import json

# Load datasets from storage files
citations_path = locals()['rl3']
papers_path = locals()['rl4']

with open(citations_path, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_path, 'r') as f:
    paper_docs = json.load(f)

print('Loaded citations:', len(citations_2018))
print('Loaded papers:', len(paper_docs))

# Identify ACM papers
acm_titles = []
for doc in paper_docs:
    text = doc['text'] if isinstance(doc, dict) and 'text' in doc else ''
    filename = doc['filename'] if isinstance(doc, dict) and 'filename' in doc else ''
    title = filename.replace('.txt', '')
    
    # Check ACM indicators
    is_acm = False
    
    if 'ACM' in text or 'Association for Computing Machinery' in text:
        is_acm = True
    
    if not is_acm:
        venues = ['UBICOMP', 'CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'PervasiveHealth', 'WWW', 'OzCHI']
        for venue in venues:
            if venue in text and 'Permission to make digital or hard copies' in text:
                is_acm = True
                break
    
    if not is_acm and ('http://dx.doi.org/10.1145/' in text or 'ISBN: 978-1-4503-' in text):
        is_acm = True
    
    if is_acm:
        acm_titles.append(title)

print('ACM papers found:', len(acm_titles))

# Create citation map
citation_counts = {}
for item in citations_2018:
    if isinstance(item, dict) and 'title' in item:
        citation_counts[item['title']] = int(item['citation_count'])

# Match papers
matches = []
for title in acm_titles:
    if title in citation_counts:
        matches.append(citation_counts[title])

print('Matches:', len(matches))

if matches:
    avg = sum(matches) / len(matches)
    result = {'average': round(avg, 2), 'paper_count': len(matches), 'total_citations': sum(matches)}
else:
    result = {'average': 0, 'paper_count': 0, 'total_citations': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
