code = """import json

# Get file path from storage
file_path = var_functions.query_db_5
papers = json.load(open(file_path, 'r'))

preview = {
    'total_papers': len(papers),
    'sample_keys': list(papers[0].keys()),
    'sample_filename': papers[0]['filename'],
    'sample_text_preview': papers[0]['text'][:200]
}

print('__RESULT__:')
print(json.dumps(preview))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
