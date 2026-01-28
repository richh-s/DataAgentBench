code = """import json, re, pandas as pd

# helper to load possibly-filepath

def load(obj):
    if isinstance(obj, str):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

non_py_list = load(var_call_EZllNtAVgV1Z4WDaCB1OJetd)
readmes_list = load(var_call_IisRjZ7NCgy8KL80CRYwrKsi)

non_py = pd.DataFrame(non_py_list)
readmes_df = pd.DataFrame(readmes_list)

merged = readmes_df.merge(non_py, on='repo_name', how='inner')
merged = merged.dropna(subset=['content'])
merged = merged.sort_values(['repo_name']).drop_duplicates(subset=['repo_name'], keep='first')

pat = re.compile(r"(?is)(?:\bcopyright\b|\b©\b|\(c\)\s*\d{2,4}|\ball rights reserved\b)")
merged['has_copyright'] = merged['content'].astype(str).apply(lambda s: bool(pat.search(s)))

total = int(merged['repo_name'].nunique())
with_c = int(merged['has_copyright'].sum())
prop = (with_c / total) if total else None

result = {
    'non_python_repos_with_readme_md_count': total,
    'readme_with_copyright_count': with_c,
    'proportion': prop
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EZllNtAVgV1Z4WDaCB1OJetd': 'file_storage/call_EZllNtAVgV1Z4WDaCB1OJetd.json', 'var_call_IisRjZ7NCgy8KL80CRYwrKsi': 'file_storage/call_IisRjZ7NCgy8KL80CRYwrKsi.json'}

exec(code, env_args)
