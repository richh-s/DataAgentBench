code = """import json, pandas as pd, re

# Load repo sets
import os

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

non_python_repos = load_records(var_call_tTzHVZ0EzzwO6dooDZs5YUJ3)
readme_files = load_records(var_call_WaTLTkElRwYIAKEHC4INQMqX)

non_py_set = set(r['repo_name'] for r in non_python_repos if r.get('repo_name'))

# README paths in query were filtered to LOWER(path)='readme.md', but original path may have mixed case in result.
readme_df = pd.DataFrame(readme_files)
readme_df = readme_df[readme_df['repo_name'].isin(non_py_set)].copy()

# For each repo, pick a stable README id (first)
readme_one = readme_df.dropna(subset=['id']).drop_duplicates(subset=['repo_name'])[['repo_name','id']]
ids = readme_one['id'].tolist()

# Query contents for these ids in chunks
chunks = [ids[i:i+500] for i in range(0, len(ids), 500)]

import sqlite3

# We'll query duckdb via query_db tool is not available here; must do via db tool.
# Instead, prepare list of chunk queries for subsequent tool calls is not possible inside python.
# So we only compute ids and repo mapping now.

out = {
    'n_non_python_repos': len(non_py_set),
    'n_non_python_repos_with_readme_md': int(readme_one.shape[0]),
    'ids_count': len(ids),
    'id_repo_sample': readme_one.head(5).to_dict(orient='records'),
    'ids_first_20': ids[:20]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_tTzHVZ0EzzwO6dooDZs5YUJ3': 'file_storage/call_tTzHVZ0EzzwO6dooDZs5YUJ3.json', 'var_call_WaTLTkElRwYIAKEHC4INQMqX': 'file_storage/call_WaTLTkElRwYIAKEHC4INQMqX.json'}

exec(code, env_args)
