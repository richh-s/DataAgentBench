code = """import json

# Get the full query result from the file
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    publications = json.load(f)

# Display sample data to understand structure
print('__RESULT__:')
print(json.dumps({
    "sample_publications": publications[:2],
    "total_publications": len(publications)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
