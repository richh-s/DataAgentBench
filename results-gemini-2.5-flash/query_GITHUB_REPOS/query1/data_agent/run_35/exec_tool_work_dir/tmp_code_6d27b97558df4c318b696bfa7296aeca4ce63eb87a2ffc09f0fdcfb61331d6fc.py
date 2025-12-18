code = """import pandas as pd
repo_names_data = locals()['var_function-call-1438989499663588195']['results']
repo_names = [repo['repo_name'] for repo in repo_names_data]
repo_names_chunks = [repo_names[i:i + 100] for i in range(0, len(repo_names), 100)]
print("__RESULT__:")
print(pd.Series(repo_names_chunks).to_json(orient='records'))"""

env_args = {'var_function-call-1438989499663588195': 'file_storage/function-call-1438989499663588195.json'}

exec(code, env_args)
