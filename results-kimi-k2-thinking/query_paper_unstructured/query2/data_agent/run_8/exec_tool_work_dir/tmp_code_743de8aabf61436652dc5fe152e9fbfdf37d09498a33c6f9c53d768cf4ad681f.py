code = """import json

# Load the data files
try:
    with open('var_functions.query_db:18', 'r') as f:
        citations_2018 = json.load(f)
except:
    citations_2018 = []

try:
    with open('var_functions.query_db:20', 'r') as f:
        paper_docs = json.load(f)
except:
    paper_docs = []

# Show some sample titles from both datasets
print('=== SAMPLE CITATION TITLES (2018) ===')
citation_titles = [c['title'] for c in citations_2018[:10]]
for i, title in enumerate(citation_titles, 1):
    print(f"{i}. {title}")

print('\n=== SAMPLE PAPER DOCUMENT TITLES ===')
paper_titles = [doc['filename'].replace('.txt', '') for doc in paper_docs[:10]]
for i, title in enumerate(paper_titles, 1):
    print(f"{i}. {title}")

# Check if any titles match exactly
common_titles = set(citation_titles) & set(paper_titles)
print(f'\n=== EXACT MATCHES ===')
print(f'Number of exact matches: {len(common_titles)}')

# Check if any ACM papers exist in the documents
acm_count = 0
sample_acm_titles = []
for doc in paper_docs[:50]:  # Check first 50
    text = doc.get('text', '')
    if 'ACM' in text or 'Association for Computing Machinery' in text:
        acm_count += 1
        if len(sample_acm_titles) < 5:
            sample_acm_titles.append(doc['filename'].replace('.txt', ''))

print(f'\n=== ACM PAPERS IN FIRST 50 DOCS ===')
print(f'ACM papers found: {acm_count}')
print('Sample ACM titles:', sample_acm_titles)

result = {
    'citation_sample': citation_titles[:5],
    'paper_sample': paper_titles[:5],
    'exact_matches': len(common_titles),
    'acm_in_first_50': acm_count
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'average_citations': 0, 'total_papers': 0, 'total_citations': 0}}

exec(code, env_args)
