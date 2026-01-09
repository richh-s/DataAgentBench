code = """import json
import pandas as pd

# Load citations 2018
with open(var_call_CM813wiHjgDzVwRARdCNEZro, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load ACM filenames list (regex matched)
with open(var_call_WCZ5ku62dtNTEmoyvDnUO0jC, 'r', encoding='utf-8') as f:
    acm_files = json.load(f)
df_acm = pd.DataFrame(acm_files)
df_acm['title'] = df_acm['filename'].str.replace(r'\\.txt$', '', regex=True)
acm_titles = set(df_acm['title'].dropna().tolist())

# Filter citations to ACM titles
mask = df_cit['title'].isin(acm_titles)
df = df_cit[mask].copy()

avg_citations = float(df['citation_count'].mean()) if len(df) else None
result = {
    'average_citation_count_2018_for_acm_papers': avg_citations,
    'n_acm_papers_with_2018_citations': int(len(df)),
    'n_total_papers_with_2018_citations': int(len(df_cit))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_CM813wiHjgDzVwRARdCNEZro': 'file_storage/call_CM813wiHjgDzVwRARdCNEZro.json', 'var_call_W9uR92eUbhoM470QgCHdkQBz': 'file_storage/call_W9uR92eUbhoM470QgCHdkQBz.json', 'var_call_W9mjQhp9izgUk8k9VgTbNt71': {'need_more_query': True, 'n_cit_2018': 158, 'n_files': 99}, 'var_call_WCZ5ku62dtNTEmoyvDnUO0jC': 'file_storage/call_WCZ5ku62dtNTEmoyvDnUO0jC.json'}

exec(code, env_args)
