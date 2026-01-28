code = """import json

# Load data from file paths
citations_path = var_functions.query_db_0
papers_path = var_functions.query_db_2

with open(citations_path, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_path, 'r') as f:
    paper_docs = json.load(f)
    
print('Citations 2018 count:', len(citations_2018))
print('Paper docs count:', len(paper_docs))

# Identify ACM papers
acm_titles = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for ACM indicators
    is_acm = False
    
    # Explicit ACM mention
    if 'ACM' in text or 'Association for Computing Machinery' in text:
        is_acm = True
    
    # ACM venues with copyright pattern
    if not is_acm:
        venues = ['UBICOMP', 'CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'PervasiveHealth', 'WWW']
        for venue in venues:
            if venue in text and 'Permission to make digital or hard copies' in text:
                is_acm = True
                break
    
    if is_acm:
        acm_titles.append(title)

print('ACM papers identified:', len(acm_titles))

# Create citation map
citation_map = {}
for item in citations_2018:
    citation_map[item['title']] = int(item['citation_count'])

# Find matches
matches = []
for title in acm_titles:
    if title in citation_map:
        matches.append(citation_map[title])

print('Matches found:', len(matches))

if matches:
    avg = sum(matches) / len(matches)
    result = {'average': round(avg, 2), 'papers': len(matches), 'total_citations': sum(matches)}
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('No matches found')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
