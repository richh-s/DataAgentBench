code = """import os, json

# Explore directory structure
def explore_dir(path='.'):
    results = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('query_') and file.endswith('.json'):
                full_path = os.path.join(root, file)
                results.append(full_path)
    return results

data_files = explore_dir()
print('Found data files:', data_files)

# Try to find citations and papers files
citations_file = None
papers_file = None

for file_path in data_files:
    if 'Citations' in file_path:
        citations_file = file_path
    elif 'paper_docs' in file_path:
        papers_file = file_path

print('Citations file path:', citations_file)
print('Papers file path:', papers_file)

# Load data
citations = []
if citations_file and os.path.exists(citations_file):
    with open(citations_file) as f:
        citations = json.load(f)
    print('Citations loaded:', len(citations))

papers = []
if papers_file and os.path.exists(papers_file):
    with open(papers_file) as f:
        papers = json.load(f)
    print('Papers loaded:', len(papers))

# Find food papers and calculate citations
if papers and citations:
    food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
    food_titles = []
    
    for paper in papers:
        text = paper.get('text', '').lower()
        filename = paper.get('filename', '')
        if any(kw in text for kw in food_keywords):
            food_titles.append(filename.replace('.txt', ''))
    
    citation_map = {c.get('title', ''): int(c.get('total_citations', 0)) for c in citations}
    total_citations = sum(citation_map[t] for t in food_titles if t in citation_map)
    
    result = str(total_citations)
    print('__RESULT__:')
    print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
