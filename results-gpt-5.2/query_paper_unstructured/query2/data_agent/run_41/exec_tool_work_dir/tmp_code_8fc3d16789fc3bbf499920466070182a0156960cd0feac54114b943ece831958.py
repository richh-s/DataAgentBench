code = """import json, re
import pandas as pd

# Load citations 2018
path_cit = var_call_CM813wiHjgDzVwRARdCNEZro
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load filenames and derive titles
path_files = var_call_W9uR92eUbhoM470QgCHdkQBz
with open(path_files, 'r', encoding='utf-8') as f:
    files = json.load(f)
df_files = pd.DataFrame(files)
df_files['title'] = df_files['filename'].str.replace(r'\.txt$', '', regex=True)

# Fetch only ACM papers' text for parsing source
acm_titles = set()
# query all docs with ACM near top (first 2000 chars) might miss; instead pull text for all and parse quickly in python not feasible.
# We'll re-query Mongo for docs containing 'ACM' in first 2000 chars using regex on text.

print('__RESULT__:')
print(json.dumps({'need_more_query': True, 'n_cit_2018': int(len(df_cit)), 'n_files': int(len(df_files))}))"""

env_args = {'var_call_CM813wiHjgDzVwRARdCNEZro': 'file_storage/call_CM813wiHjgDzVwRARdCNEZro.json', 'var_call_W9uR92eUbhoM470QgCHdkQBz': 'file_storage/call_W9uR92eUbhoM470QgCHdkQBz.json'}

exec(code, env_args)
