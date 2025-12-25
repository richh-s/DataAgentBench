code = """import json, pandas as pd

readmes_path = var_call_PCT4MQhmKYWDUcg6afFaBKqk
langs_path = var_call_TSvpDWaXfOFvEQCjDKaqYZHC

with open(readmes_path) as f:
    readmes = json.load(f)
with open(langs_path) as f:
    langs = json.load(f)

readmes_df = pd.DataFrame(readmes)
langs_df = pd.DataFrame(langs)

mask_no_python = ~langs_df['language_description'].str.contains('Python', case=False, na=False)
no_py_repos = set(langs_df[mask_no_python]['repo_name'])

readmes_df = readmes_df[readmes_df['repo_name'].isin(no_py_repos)]

copyright_terms = ['copyright', '©', '(c)']
pattern = '|'.join(copyright_terms)

readmes_df['has_copyright'] = readmes_df['content'].str.contains(pattern, case=False, na=False)

num_readmes = len(readmes_df)
num_with_copyright = int(readmes_df['copyright'].sum()) if num_readmes>0 else 0
prop = num_with_copyright / num_readmes if num_readmes>0 else None

result = {'num_readmes_no_python': num_readmes,
          'num_with_copyright': num_with_copyright,
          'proportion': prop}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_PCT4MQhmKYWDUcg6afFaBKqk': 'file_storage/call_PCT4MQhmKYWDUcg6afFaBKqk.json', 'var_call_TSvpDWaXfOFvEQCjDKaqYZHC': 'file_storage/call_TSvpDWaXfOFvEQCjDKaqYZHC.json', 'var_call_6RAZQCAtuWKoaGpTn4UJiRBC': 'file_storage/call_6RAZQCAtuWKoaGpTn4UJiRBC.json', 'var_call_k5wrrv8WUdTWsZBlQTWquLGR': 'file_storage/call_k5wrrv8WUdTWsZBlQTWquLGR.json', 'var_call_bp6Y02k7bXQZRnJ8wO7hvuym': [{'total_readmes': '133'}]}

exec(code, env_args)
