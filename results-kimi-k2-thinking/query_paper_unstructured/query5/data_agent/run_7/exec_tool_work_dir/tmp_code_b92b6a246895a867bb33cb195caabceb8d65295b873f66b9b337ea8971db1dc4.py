code = """import json
import re

# Load the citations data
citations_file_path = locals()['var_functions.query_db:12']
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

print('Total citations in 2020:', len(citations_data))
print('Sample citations:', citations_data[:3])

# Load the papers data from CHI search
papers_file_path = locals()['var_functions.query_db:14']
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

print('\nTotal papers with CHI in text:', len(papers_data))

# Let's look at the first paper to understand the structure
if papers_data:
    first_paper = papers_data[0]
    filename = first_paper.get('filename', '')
    text = first_paper.get('text', '')
    
    print('\nFirst paper filename:', filename)
    print('Title (from filename):', filename.replace('.txt', ''))
    
    # Check for CHI patterns
    chi_pattern = re.search(r'CHI', text, re.IGNORECASE)
    if chi_pattern:
        print('CHI found in text at position', chi_pattern.start())

print('\nNow creating a more targeted MongoDB query...')
print('__RESULT__:')
print(json.dumps({"status": "ready_for_better_query"}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'status': 'ready_to_query_mongodb', 'citation_count': 188}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'status': 'papers_loaded', 'count': 99}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
