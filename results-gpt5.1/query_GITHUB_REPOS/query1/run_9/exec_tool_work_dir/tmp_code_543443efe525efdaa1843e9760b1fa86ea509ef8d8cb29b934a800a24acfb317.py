code = """import json, pandas as pd
import re

# Load large query results from files
with open(var_call_yYJ8pLRu6PhwwaUDKnBDMc1e, 'r') as f:
    readmes = json.load(f)

languages = pd.DataFrame(var_call_m2pf2lWDQqgiWipE3ePCrUs1)

# Identify repos that do NOT use Python
non_python_langs = languages[~languages['language_description'].str.contains('python', case=False, na=False)]
non_python_repos = set(non_python_langs['repo_name'])

# Prepare README data
readme_df = pd.DataFrame(readmes)

# Filter to repos that do not use Python
readme_non_python = readme_df[readme_df['repo_name'].isin(non_python_repos)].copy()

# Define heuristic for detecting copyright information
pattern = re.compile(r'copyright|\u00a9|\(c\)', re.IGNORECASE)

def has_copyright(text):
    if not isinstance(text, str):
        return False
    return bool(pattern.search(text))

readme_non_python['has_copyright'] = readme_non_python['content'].apply(has_copyright)

total_non_python_readmes = len(readme_non_python)
with_copyright = int(readme_non_python['has_copyright'].sum()) if total_non_python_readmes > 0 else 0
proportion = with_copyright / total_non_python_readmes if total_non_python_readmes > 0 else None

result = {
    'total_non_python_readmes': total_non_python_readmes,
    'with_copyright': with_copyright,
    'proportion': proportion
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_yYJ8pLRu6PhwwaUDKnBDMc1e': 'file_storage/call_yYJ8pLRu6PhwwaUDKnBDMc1e.json', 'var_call_m2pf2lWDQqgiWipE3ePCrUs1': 'file_storage/call_m2pf2lWDQqgiWipE3ePCrUs1.json', 'var_call_9CyTstV4TmcOj7DkKH907oML': [{'total_repos': '3325634'}], 'var_call_mEoVrjTx9zAs2cbtc4jRixk2': [{'total_repos': '12837'}], 'var_call_FPUYKIlsH8cu4o5Ralu7JCq1': [{'total_readmes': '133'}]}

exec(code, env_args)
