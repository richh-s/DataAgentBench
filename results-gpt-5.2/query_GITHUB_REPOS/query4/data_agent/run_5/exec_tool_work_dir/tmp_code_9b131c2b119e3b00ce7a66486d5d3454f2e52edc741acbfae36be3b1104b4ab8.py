code = """import json, re
import pandas as pd

commit_counts = pd.DataFrame(var_call_rKjHCwBZWJ9WMzEmgFqiZzCB)
commit_counts['commit_count'] = commit_counts['commit_count'].astype(int)

# load languages (may be file path)
langs_data = var_call_xN8UOuve2j4LZgGYbVp6RWdB
if isinstance(langs_data, str):
    with open(langs_data, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = langs_data
langs_df = pd.DataFrame(langs)

# parse main language by max bytes
pat = re.compile(r"([A-Za-z0-9_+#\-\. ]+) \(([0-9,]+) bytes\)")

def main_lang(desc):
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

langs_df['main_language'] = langs_df['language_description'].apply(main_lang)

merged = commit_counts.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')
filtered = merged[merged['main_language'].notna() & (merged['main_language'].str.lower() != 'python')]

top5 = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer_list = top5['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_rKjHCwBZWJ9WMzEmgFqiZzCB': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}], 'var_call_xN8UOuve2j4LZgGYbVp6RWdB': 'file_storage/call_xN8UOuve2j4LZgGYbVp6RWdB.json'}

exec(code, env_args)
