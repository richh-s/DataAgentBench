code = """import json, re, pandas as pd

commits = pd.DataFrame(var_call_ZtDVtJ7ysDRg5gM219AcInTO)
commits['commit_count'] = commits['commit_count'].astype(int)

# load full languages table
path = var_call_xrMDhTZlKUGH1bpINPnZe8zn
with open(path, 'r', encoding='utf-8') as f:
    langs_records = json.load(f)
langs = pd.DataFrame(langs_records)

# parse primary language as the one with max bytes in language_description
pat = re.compile(r"([A-Za-z0-9+#\-\. ]+) \((\d[\d,]*) bytes\)")

def primary_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        b_int = int(b.replace(',', ''))
        if b_int > best_bytes:
            best_bytes = b_int
            best_lang = lang.strip()
    return best_lang

langs['primary_language'] = langs['language_description'].apply(primary_lang)

# join and filter non-Python
merged = commits.merge(langs[['repo_name','primary_language']], on='repo_name', how='left')
non_py = merged[merged['primary_language'].notna() & (merged['primary_language'].str.lower() != 'python')]

# top five by commits
result = non_py.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ZtDVtJ7ysDRg5gM219AcInTO': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_xrMDhTZlKUGH1bpINPnZe8zn': 'file_storage/call_xrMDhTZlKUGH1bpINPnZe8zn.json'}

exec(code, env_args)
