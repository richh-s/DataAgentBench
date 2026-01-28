code = """import json
import re

# Access the stored results using the correct keys
papers_data = locals()['var_functions.query_db:30']
citations_data = locals()['var_functions.query_db:28']

# Extract paper information
papers_info = []
for doc in papers_data:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    
    # Extract year
    year_match = re.search(r'(20\d{2}|19\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    papers_info.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Filter papers with empirical contribution after 2016
filtered_papers = [p for p in papers_info if p['has_empirical'] and p['year'] and p['year'] > 2016]

# Create citation lookup dictionary
citation_dict = {item['title']: int(item['total_citations']) for item in citations_data}

# Match papers with citations
results = []
for paper in filtered_papers:
    title = paper['title']
    if title in citation_dict:
        results.append({
            'title': title,
            'total_citations': citation_dict[title]
        })

# Sort by citation count
text_results = [f"{item['title']}: {item['total_citations']} citations" for item in sorted(results, key=lambda x: x['total_citations'], reverse=True)]

print('__RESULT__:')
print(json.dumps(text_results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
