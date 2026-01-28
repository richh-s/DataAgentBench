code = """import json

# Access the stored results using the provided keys
# The key for citations is 'functions.query_db:6'
citations_key = 'functions.query_db:6'
paper_docs_key = 'functions.query_db:2'

# Check if these keys exist in locals() and get their values
citations_result = locals().get(citations_key)
paper_docs_result = locals().get(paper_docs_key)

print('Citations result type:', type(citations_result))
print('Paper docs result type:', type(paper_docs_result))

# Check if they're file paths
if isinstance(citations_result, str) and citations_result.endswith('.json'):
    with open(citations_result, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_result

if isinstance(paper_docs_result, str) and paper_docs_result.endswith('.json'):
    with open(paper_docs_result, 'r') as f:
        paper_docs_data = json.load(f)
else:
    paper_docs_data = paper_docs_result

print('Loaded citations count:', len(citations_data) if citations_data else 0)
print('Loaded paper docs count:', len(paper_docs_data) if paper_docs_data else 0)

if citations_data and len(citations_data) > 0:
    print('First citation:', citations_data[0])
    
if paper_docs_data and len(paper_docs_data) > 0:
    print('First paper doc filename:', paper_docs_data[0].get('filename'))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
