code = """import json

# Load the file paths
citation_path = locals()['var_functions.query_db:0']
papers_path = locals()['var_functions.query_db:2']

print('=== File Information ===')
print('Citation file: ' + str(citation_path))
print('Papers file: ' + str(papers_path))

# Just try to read and debug the JSON data
print('\n=== Debug JSON Loading ===')

try:
    with open(citation_path, 'r') as f:
        citation_preview = f.read(1000)  # Read first 1000 chars
        print('Citation file preview (first 1000 chars):')
        print(citation_preview[:500])
except Exception as e:
    print('Error loading citation file: ' + str(e))

try:
    with open(papers_path, 'r') as f:
        papers_preview = f.read(1000)
        print('\nPapers file preview (first 1000 chars):')
        print(papers_preview[:500])
except Exception as e:
    print('Error loading papers file: ' + str(e))

# Try loading full data
print('\n=== Loading Full Data ===')

try:
    with open(citation_path, 'r') as f:
        citations_data = json.load(f)
    print('Successfully loaded citations: ' + str(len(citations_data)) + ' records')
except Exception as e:
    print('Error parsing citations as JSON: ' + str(e))
    citations_data = []

try:
    with open(papers_path, 'r') as f:
        papers_data = json.load(f)
    print('Successfully loaded papers: ' + str(len(papers_data)) + ' records')
except Exception as e:
    print('Error parsing papers as JSON: ' + str(e))
    papers_data = []

# Show first few records
if citations_data:
    print('\nFirst citation record:')
    print(json.dumps(citations_data[0], indent=2))

if papers_data:
    print('\nFirst paper record:')
    print(json.dumps({
        'filename': papers_data[0].get('filename', 'N/A'),
        'text_preview': papers_data[0].get('text', '')[:200]
    }, indent=2))

print('__RESULT__:')
print(json.dumps({'loaded': True, 'citations': len(citations_data), 'papers': len(papers_data)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': []}

exec(code, env_args)
