code = """import json
import re

# Access the paper documents from storage (paper_docs key is functions.query_db:16)
papers_data = var_functions.query_db_16
citations_data = var_functions.query_db_18

# Initialize list to store extracted paper information
papers_info = []

# Process each paper document
for doc in papers_data:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year - look for 4-digit years starting with 20
    year_match = re.search(r'(20\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check if paper has empirical contribution (case-insensitive)
    has_empirical = 'empirical' in text.lower()
    
    papers_info.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Filter papers: empirical contribution AND published after 2016
filtered_papers = [p for p in papers_info if p['has_empirical'] and p['year'] and p['year'] > 2016]

# Create dictionary for citation lookups
citation_dict = {}
for cit in citations_data:
    citation_dict[cit['title']] = int(cit['total_citations'])

# Match papers with citations
results = []
for paper in filtered_papers:
    title = paper['title']
    if title in citation_dict:
        results.append({
            'title': title,
            'year': paper['year'],
            'total_citations': citation_dict[title]
        })

# Sort by citation count descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Format output as strings
output = []
for item in results_sorted:
    output.append(f"{item['title']}: {item['total_citations']} citations")

# Print results count
print(f"Found {len(results_sorted)} papers with empirical contribution after 2016")
print(f"Top example: {output[0] if output else 'None'}")

# Return the formatted list
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
