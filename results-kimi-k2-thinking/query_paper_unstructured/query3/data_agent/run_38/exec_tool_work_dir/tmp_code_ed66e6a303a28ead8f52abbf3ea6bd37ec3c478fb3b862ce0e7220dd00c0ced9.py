code = """import json
import re

# Load the paper documents
with open('var_functions.query_db:8.json', 'r') as f:
    paper_docs = json.load(f)

# Load the citations data
with open('var_functions.query_db:2.json', 'r') as f:
    citations = json.load(f)

print('Total papers loaded:', len(paper_docs))
print('Total citation records loaded:', len(citations))

# Extract paper information
papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title (filename without .txt)
    title = filename.replace('.txt', '')
    
    # Extract year - look for 4-digit years starting with 20
    year_match = re.search(r'(20\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check for empirical contribution (case-insensitive)
    has_empirical = 'empirical' in text.lower()
    
    papers.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Filter papers: empirical and published after 2016
filtered_papers = [p for p in papers if p['has_empirical'] and p['year'] and p['year'] > 2016]
print('Papers with empirical contribution after 2016:', len(filtered_papers))

# Process citations: sum by title
citation_sums = {}
for cit in citations:
    title = cit['title']
    count = int(cit['citation_count'])
    citation_sums[title] = citation_sums.get(title, 0) + count

# Match papers with citations and create results
results = []
for paper in filtered_papers:
    title = paper['title']
    if title in citation_sums:
        results.append({
            'title': title,
            'total_citations': citation_sums[title],
            'year': paper['year']
        })

# Sort by total citations descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

print('Matching papers with citation data:', len(results_sorted))
print('\nTop 10 papers:')
for i, item in enumerate(results_sorted[:10], 1):
    print(f"{i}. {item['title']} ({item['year']}) - {item['total_citations']} citations")

# Prepare final output
output = []
for item in results_sorted:
    output.append(f"{item['title']}: {item['total_citations']} citations")

__RESULT__ = json.dumps(output)
print('\n__RESULT__:')
print(__RESULT__)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
