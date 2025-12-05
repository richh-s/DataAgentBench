code = """import json
import pandas as pd

shell_repos_file = var_call_FbyMTaA1aM1pmMdc8aEKy8IY
license_repos_file = var_call_g8AGlbliJV88hORIAk0q9D7U

shell_df = pd.read_json(shell_repos_file)
license_df = pd.read_json(license_repos_file)

shell_set = set(shell_df['repo_name'])
license_set = set(license_df['repo_name'])

intersect_repos = list(shell_set & license_set)

batch_size = 500
batches = [intersect_repos[i:i+batch_size] for i in range(0, len(intersect_repos), batch_size)]

result = {
  'batches': batches,
  'num_repos': len(intersect_repos)
}

result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_FbyMTaA1aM1pmMdc8aEKy8IY': 'file_storage/call_FbyMTaA1aM1pmMdc8aEKy8IY.json', 'var_call_g8AGlbliJV88hORIAk0q9D7U': 'file_storage/call_g8AGlbliJV88hORIAk0q9D7U.json', 'var_call_CXOtMW9Ov9JD7vUjxVzUcRw8': [{'cnt': '15014'}]}

exec(code, env_args)
