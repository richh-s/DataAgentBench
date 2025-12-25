code = """import json, pandas as pd

commits = pd.DataFrame(var_call_YKVIIpOLGa7ii4KGAR8NC52w)
langs_path = var_call_OWUZNTyPiOdV55Badgt1aL01

with open(langs_path, 'r') as f:
    langs = pd.DataFrame(json.load(f))

# determine main language from description by taking the first language mentioned
def main_lang(desc):
    # assume pattern "<Lang> (xxxx bytes)" and take first token before '('
    part = desc.split('bytes')[0]
    lang = part.split('(')[0].split(',')[0].split(':')[-1].strip()
    return lang

langs['main_language'] = langs['language_description'].apply(main_lang)

merged = commits.merge(langs, on='repo_name', how='left')

not_python = merged[merged['main_language'].str.lower() != 'python']

top5 = not_python.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

result = json.dumps(top5)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_YKVIIpOLGa7ii4KGAR8NC52w': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_OWUZNTyPiOdV55Badgt1aL01': 'file_storage/call_OWUZNTyPiOdV55Badgt1aL01.json', 'var_call_s9fIAFTznWURJGNrHZ6267Za': 'file_storage/call_s9fIAFTznWURJGNrHZ6267Za.json'}

exec(code, env_args)
