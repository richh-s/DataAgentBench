code = """import json, re, pandas as pd

# load languages (may be file path)
lang_src = var_call_PBgFQPXk3Ftr0AhyjeYvtmYv
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        lang_rows = json.load(f)
else:
    lang_rows = lang_src

commits_rows = var_call_IIpXmumjmTfDX3R0fJCgyji5

# parse main language as max bytes from description
pat = re.compile(r"([A-Za-z0-9_#+.-]+)\s*\((\d[\d,]*)\s*bytes\)")

def main_lang(desc):
    if not desc:
        return None
    pairs = [(m.group(1), int(m.group(2).replace(',', ''))) for m in pat.finditer(desc)]
    if not pairs:
        return None
    return max(pairs, key=lambda x: x[1])[0]

lang_df = pd.DataFrame(lang_rows)
lang_df['main_language'] = lang_df['language_description'].map(main_lang)

comm_df = pd.DataFrame(commits_rows)
comm_df['commit_count'] = pd.to_numeric(comm_df['commit_count'])

merged = comm_df.merge(lang_df[['repo_name','main_language']], on='repo_name', how='left')
# keep not-python
res = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower() != 'python')].sort_values('commit_count', ascending=False).head(5)
answer_list = res['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_PBgFQPXk3Ftr0AhyjeYvtmYv': 'file_storage/call_PBgFQPXk3Ftr0AhyjeYvtmYv.json', 'var_call_IIpXmumjmTfDX3R0fJCgyji5': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
