code = """import json

# Access the file path
citations_file_path = globals().get('var_functions.query_db:2')

# Read the JSON file
with open(citations_file_path, 'r') as f:
    citations_2020 = json.load(f)

# Now extract titles to query MongoDB for CHI papers
titles = [citation['title'] for citation in citations_2020]

print('__RESULT__:')
print(json.dumps({
    'total_citations_2020': len(citations_2020),
    'sample_titles': titles[:5]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'type': "<class 'str'>", 'is_string': True, 'is_list': False}}

exec(code, env_args)
