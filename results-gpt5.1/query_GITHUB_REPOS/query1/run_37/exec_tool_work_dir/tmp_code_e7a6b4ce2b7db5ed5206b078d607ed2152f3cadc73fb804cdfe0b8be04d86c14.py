code = """import json, pandas as pd
contents = var_call_JOsSpOHslvOefYvKEAX0EAnp
languages = var_call_vGVN4y0Mvg7JvckHpOVZHPoF

if isinstance(contents, str):
    import os, json as js
    with open(contents, 'r') as f:
        contents = js.load(f)
if isinstance(languages, str):
    import os, json as js
    with open(languages, 'r') as f:
        languages = js.load(f)

contents_df = pd.DataFrame(contents)[['sample_repo_name','content']]
langs_df = pd.DataFrame(languages)[['repo_name','language_description']]

non_py_langs = langs_df[~langs_df['language_description'].str.contains('Python', case=False, na=False)]
merged = contents_df.merge(non_py_langs, left_on='sample_repo_name', right_on='repo_name', how='inner')

readmes = merged['content'].fillna('').str.lower()
pattern_terms = ['copyright', '©', '(c)']
mask = readmes.apply(lambda txt: any(term in txt for term in pattern_terms))

total = len(readmes)
with_copyright = int(mask.sum())
proportion = with_copyright / total if total > 0 else None

result = json.dumps({'total_non_python_readmes': total, 'with_copyright': with_copyright, 'proportion': proportion})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_JOsSpOHslvOefYvKEAX0EAnp': 'file_storage/call_JOsSpOHslvOefYvKEAX0EAnp.json', 'var_call_vGVN4y0Mvg7JvckHpOVZHPoF': 'file_storage/call_vGVN4y0Mvg7JvckHpOVZHPoF.json'}

exec(code, env_args)
