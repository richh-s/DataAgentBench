code = """import json
import os

# Try to access the stored variables directly
citations_data = None
papers_data = None

try:
    # Access the citations data
    citations_file = globals().get('var_functions.query_db:2')
    if citations_file and isinstance(citations_file, str) and os.path.exists(citations_file):
        with open(citations_file, 'r') as f:
            citations_data = json.load(f)
        print('Loaded citations from file:', len(citations_data))
    else:
        print('Citations file path issue or not string')
        if citations_file:
            print('Citations file var:', type(citations_file))
            if isinstance(citations_file, list):
                citations_data = citations_file
                print('Using citations as list directly')
        else:
            print('Citations var is None')
except Exception as e:
    print('Error loading citations:', e)

try:
    # Access the papers data
    papers_file = globals().get('var_functions.query_db:5')
    if papers_file and isinstance(papers_file, str) and os.path.exists(papers_file):
        with open(papers_file, 'r') as f:
            papers_data = json.load(f)
        print('Loaded papers from file:', len(papers_data))
    else:
        print('Papers file path issue or not string')
        if papers_file:
            print('Papers file var:', type(papers_file))
            if isinstance(papers_file, list):
                papers_data = papers_file
                print('Using papers as list directly')
        else:
            print('Papers var is None')
except Exception as e:
    print('Error loading papers:', e)

# Debug info
print('Citations data type:', type(citations_data))
print('Papers data type:', type(papers_data))

# If we have data, process it
if citations_data and papers_data:
    print('Both data loaded successfully')
    chi_titles = set()
    for doc in papers_data:
        title = doc['filename'].replace('.txt', '')
        if 'CHI' in doc['text'][:2000]:
            chi_titles.add(title)
    
    total = sum(int(c['citation_count']) for c in citations_data if c['title'] in chi_titles)
    result = {'total_citations': total}
else:
    print('Missing data, returning 0')
    result = {'total_citations': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:26': 0}

exec(code, env_args)
