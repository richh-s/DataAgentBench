code = """import json, pandas as pd, re

# languages data is in a JSON file path string
with open(var_call_m2pf2lWDQqgiWipE3ePCrUs1, 'r') as f:
    langs = json.load(f)

languages = pd.DataFrame(langs)

with open(var_call_yYJ8pLRu6PhwwaUDKnBDMc1e, 'r') as f:
    readmes = json.load(f)

readme_df = pd.DataFrame(readmes)

# Identify repos that do NOT use Python
non_python_langs = languages[~languages['language_description'].str.contains('python', case=False, na=False)]
non_python_repos = set(non_python_langs['repo_name'])

# Filter READMEs to those repos
readme_non_python = readme_df[readme_df['repo_name'].isin(non_python_repos)].copy()

pattern = re.compile(r'copyright|\u00a9|\(c\)', re.IGNORECASE)

def has_copyright(text):
    if not isinstance(text, str):
        return False
    return bool(pattern.search(text))

readme_non_python['has_copyright'] = readme_non_python['content'].apply(has_copyright)

total_non_python_readmes = int(len(readme_non_python))
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

env_args = {'var_call_yYJ8pLRu6PhwwaUDKnBDMc1e': 'file_storage/call_yYJ8pLRu6PhwwaUDKnBDMc1e.json', 'var_call_m2pf2lWDQqgiWipE3ePCrUs1': 'file_storage/call_m2pf2lWDQqgiWipE3ePCrUs1.json', 'var_call_9CyTstV4TmcOj7DkKH907oML': [{'total_repos': '3325634'}], 'var_call_mEoVrjTx9zAs2cbtc4jRixk2': [{'total_repos': '12837'}], 'var_call_FPUYKIlsH8cu4o5Ralu7JCq1': [{'total_readmes': '133'}], 'var_call_L719jjsrGHZrwjBUtL92q64Y': {'type_var_call_m2pf2lWDQqgiWipE3ePCrUs1': "<class 'str'>", 'sample_var_call_m2pf2lWDQqgiWipE3ePCrUs1': None}}

exec(code, env_args)
