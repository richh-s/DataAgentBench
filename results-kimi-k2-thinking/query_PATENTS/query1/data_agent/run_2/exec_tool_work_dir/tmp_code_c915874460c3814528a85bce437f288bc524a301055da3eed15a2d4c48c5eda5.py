code = """# Let's load the full result from the file path provided
filepath = var_functions.query_db:2
print('Filepath type:', type(filepath))
print('Filepath value:', filepath)
# Read the file
with open(filepath, 'r') as f:
    data = f.read()
    print('Data type:', type(data))
    print('Data length:', len(data))
    print('Data preview:', data[:500])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
