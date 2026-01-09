code = """import json, re, pandas as pd

# Load languages (may be stored as file path)
langs = var_call_WA9npYXcyLY3YY0eoCL2vvoj
if isinstance(langs, str):
    with open(langs, 'r', encoding='utf-8') as f:
        langs = json.load(f)

commits = var_call_31HURm7a7fXmcMqJnAqqNarI

lang_df = pd.DataFrame(langs)
commit_df = pd.DataFrame(commits)

# parse main language from language_description
pat = re.compile(r"([A-Za-z0-9_+#.-]+) \((\d[\d,]*) bytes\)")

def main_lang(desc):
    if desc is None:
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    # choose max bytes
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_lang, best_bytes = lang, n
    return best_lang

lang_df['main_language'] = lang_df['language_description'].map(main_lang)

merged = pd.merge(commit_df, lang_df[['repo_name','main_language']], on='repo_name', how='left')
# commit_count is string from duckdb; convert
merged['commit_count'] = pd.to_numeric(merged['commit_count'], errors='coerce')

# filter main language not Python (including null treated as not Python? likely exclude null)
filtered = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower()!='python')]

# take top 5 by commit_count already ordered but ensure
top5 = filtered.sort_values('commit_count', ascending=False).head(5)
answer_list = top5['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_WA9npYXcyLY3YY0eoCL2vvoj': 'file_storage/call_WA9npYXcyLY3YY0eoCL2vvoj.json', 'var_call_31HURm7a7fXmcMqJnAqqNarI': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
