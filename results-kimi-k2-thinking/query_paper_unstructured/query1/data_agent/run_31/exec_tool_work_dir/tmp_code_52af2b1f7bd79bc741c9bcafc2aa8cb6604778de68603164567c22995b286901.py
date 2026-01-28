code = """import os, json

# Find all JSON files recursively
data_files = []
print('Searching for data files...')
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            full_path = os.path.join(root, file)
            print(f'Found: {full_path}')
            data_files.append(full_path)

# Try each file to see which one contains citations vs papers
citations_file = None
papers_file = None

for filepath in data_files:
    with open(filepath) as f:
        data = json.load(f)
    if data and isinstance(data, list):
        # Check if it has citations data structure
        if len(data) > 0 and 'title' in data[0] and 'total_citations' in data[0]:
            citations_file = filepath
            print(f'Identified as citations file: {filepath}')
        # Check if it has papers data structure  
        elif len(data) > 0 and 'filename' in data[0] and 'text' in data[0]:
            papers_file = filepath
            print(f'Identified as papers file: {filepath}')

print(f'\nFinal selection:')
print(f'Citations: {citations_file}')
print(f'Papers: {papers_file}')

if citations_file and papers_file:
    with open(citations_file) as f:
        citations = json.load(f)
    with open(papers_file) as f:
        papers = json.load(f)
    
    print(f'Loaded {len(citations)} citations and {len(papers)} papers')
    
    # Food paper identification
    food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
    food_titles = []
    for paper in papers:
        text = paper.get('text', '').lower()
        filename = paper.get('filename', '')
        if any(kw in text for kw in food_keywords):
            food_titles.append(filename.replace('.txt', ''))
    
    # Calculate citations
    citation_lookup = {c['title']: int(c['total_citations']) for c in citations}
    total_citations = sum(citation_lookup[t] for t in food_titles if t in citation_lookup)
    
    result = {"total_citations": total_citations}
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:52': {'total_citations': 0}}

exec(code, env_args)
