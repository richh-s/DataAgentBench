code = """import json, re, pandas as pd

top_commits = pd.DataFrame(var_call_Q7UMT22Ph9JqaRMRHEyiSujx)

with open(var_call_9G4ucTYi7KTmV29xsg3EkXW4, 'r') as f:
    lang_data = json.load(f)
langs = pd.DataFrame(lang_data)

# determine main language from language_description using bytes
pattern = re.compile(r"([A-Za-z+#]+) \((\d[,\d]*) bytes\)")

def main_lang(desc):
    matches = pattern.findall(desc or '')
    if not matches:
        return None
    # pick language with max bytes
    best = None
    best_bytes = -1
    for lang, b in matches:
        val = int(b.replace(',', ''))
        if val > best_bytes:
            best_bytes = val
            best = lang
    return best

langs['main_language'] = langs['language_description'].apply(main_lang)

merged = top_commits.merge(langs[['repo_name','main_language']], how='left', on='repo_name')

filtered = merged[merged['main_language'].str.lower() != 'python']

result_repos = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result_repos)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Q7UMT22Ph9JqaRMRHEyiSujx': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_9G4ucTYi7KTmV29xsg3EkXW4': 'file_storage/call_9G4ucTYi7KTmV29xsg3EkXW4.json'}

exec(code, env_args)
