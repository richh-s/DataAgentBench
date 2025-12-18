code = """import pandas as pd
import json

df_languages = pd.read_json(locals()['var_function-call-8309339118835681289'])

def contains_python(description):
    if isinstance(description, str):
        return 'Python' in description
    return False

# Filter out repositories that contain 'Python' in their language description
# This assumes that if Python is present, it's considered using Python, regardless of primary status for this specific problem.
non_python_repos_df = df_languages[~df_languages['language_description'].apply(contains_python)]

non_python_repos = non_python_repos_df['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(non_python_repos))"""

env_args = {'var_function-call-8309339118835681289': 'file_storage/function-call-8309339118835681289.json'}

exec(code, env_args)
