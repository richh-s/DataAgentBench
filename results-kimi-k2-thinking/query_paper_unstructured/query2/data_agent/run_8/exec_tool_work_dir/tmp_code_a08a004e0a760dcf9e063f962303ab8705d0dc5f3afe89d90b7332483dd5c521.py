code = """import json

# Get the file paths from storage
citations_file_path = locals()['var_functions.query_db:18']
papers_file_path = locals()['var_functions.query_db:20']

# Load the data
with open(citations_file_path, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_file_path, 'r') as f:
    paper_docs = json.load(f)

print('Loaded {} citations and {} paper documents'.format(len(citations_2018), len(paper_docs)))

# Identify ACM papers
acm_titles = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check if ACM paper
    is_acm = False
    if 'ACM' in text:
        is_acm = True
    elif 'Association for Computing Machinery' in text:
        is_acm = True
    elif 'http://dx.doi.org/10.1145/' in text:
        is_acm = True
    elif 'ISBN: 978-1-4503-' in text:
        is_acm = True
    
    if is_acm:
        acm_titles.append(title)

print('Found {} ACM papers'.format(len(acm_titles)))

# Create citation map
citation_counts = {}
for item in citations_2018:
    citation_counts[item['title']] = int(item['citation_count'])

# Match papers
matches = []
for title in acm_titles:
    if title in citation_counts:
        matches.append(citation_counts[title])

print('Matched {} ACM papers with 2018 citations'.format(len(matches)))

# Calculate average
if matches:
    total = sum(matches)
    average = total / len(matches)
    result = {'average_citations': round(average, 2), 'total_papers': len(matches), 'total_citations': total}
else:
    result = {'average_citations': 0, 'total_papers': 0, 'total_citations': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'average_citations': 0, 'total_papers': 0, 'total_citations': 0}}

exec(code, env_args)
