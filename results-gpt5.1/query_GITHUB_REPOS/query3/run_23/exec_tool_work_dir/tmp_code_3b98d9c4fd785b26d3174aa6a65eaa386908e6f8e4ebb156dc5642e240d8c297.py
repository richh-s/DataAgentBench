code = """import json, pandas as pd

shell_file = var_call_2D46pc7KBPHkqvEf40mUTLaN
apache_file = var_call_X1iywMlQtF1evGiqmGnWDDQy

shell_df = pd.read_json(shell_file)
apache_df = pd.read_json(apache_file)

shell_repos = set(shell_df['repo_name'].str.lower())
apache_repos = set(apache_df['repo_name'].str.lower())

common_repos = shell_repos & apache_repos

result = list(common_repos)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2D46pc7KBPHkqvEf40mUTLaN': 'file_storage/call_2D46pc7KBPHkqvEf40mUTLaN.json', 'var_call_X1iywMlQtF1evGiqmGnWDDQy': 'file_storage/call_X1iywMlQtF1evGiqmGnWDDQy.json'}

exec(code, env_args)
