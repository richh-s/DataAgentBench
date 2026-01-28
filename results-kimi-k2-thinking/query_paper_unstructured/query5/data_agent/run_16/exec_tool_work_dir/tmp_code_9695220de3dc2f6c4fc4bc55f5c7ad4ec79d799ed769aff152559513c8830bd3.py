code = """# Access variables correctly
citations_data = locals()['var_functions.query_db:6']
paper_docs_data = locals()['var_functions.query_db:2']

# Check the types
print('Citations type:', type(citations_data))
print('Paper docs type:', type(paper_docs_data))

# Load from file if needed
import json
import os

# Check if they're file paths
def load_data_if_file(data):
    if isinstance(data, str) and os.path.exists(data):
        with open(data, 'r') as f:
            return json.load(f)
    return data

citations_data = load_data_if_file(citations_data)
paper_docs_data = load_data_if_file(paper_docs_data)

print('Loaded citations count:', len(citations_data) if citations_data else 0)
print('Loaded paper docs count:', len(paper_docs_data) if paper_docs_data else 0)

# Show first few items
if citations_data:
    print('First citation:', citations_data[0])
if paper_docs_data:
    print('First paper doc filename:', paper_docs_data[0].get('filename'))

# Basic check completed
print('__RESULT__:')
print('{"status": "data_loaded"}')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
