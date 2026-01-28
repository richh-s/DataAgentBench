code = """# First check what variables are available
available_vars = [k for k in locals().keys() if k.startswith('var_')]
print('Available variables:', available_vars)

# Get the stored results
citations_result = var_functions.query_db_6
paper_docs_result = var_functions.query_db_2

print('Citations result type:', type(citations_result))
print('Paper docs result type:', type(paper_docs_result))

# Check if they're file paths
import json
print('Are they strings?', isinstance(citations_result, str), isinstance(paper_docs_result, str))

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

print('Citations data length:', len(citations_data) if citations_data else 'None')
print('Paper docs data length:', len(paper_docs_data) if paper_docs_data else 'None')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
