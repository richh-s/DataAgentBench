code = """import json
import re

# Access the paper documents from storage
paper_docs = var_functions.query_db_8

# Access the citations data from storage
citations = var_functions.query_db_2

print('Total papers loaded:', len(paper_docs))
print('Total citation records loaded:', len(citations))

# Extract paper information
papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    year_match = re.search(r'(20\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
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

# Prepare final output
output = []
for item in results_sorted:
    output.append(item['title'] + ': ' + str(item['total_citations']) + ' citations')

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
