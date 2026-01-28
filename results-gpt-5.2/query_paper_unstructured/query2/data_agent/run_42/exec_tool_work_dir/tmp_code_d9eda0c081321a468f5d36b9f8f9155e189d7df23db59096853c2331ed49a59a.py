code = """import json, pandas as pd

# Load citations 2018
cit_path = var_call_5AXEbofhCQ4aynYGb6TCaazI
with open(cit_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

df_cit = pd.DataFrame(citations)
# normalize types
if not df_cit.empty:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load ACM-ish filenames list
acm_path = var_call_2hTmnjtFB0QrFZGgWMiSYp6v
with open(acm_path, 'r', encoding='utf-8') as f:
    acm_files = json.load(f)

df_acm = pd.DataFrame(acm_files)
if df_acm.empty:
    acm_titles = set()
else:
    acm_titles = set(df_acm['filename'].str.replace(r'\.txt$', '', regex=True))

# Filter citations to titles in ACM list
if df_cit.empty:
    avg = None
    n = 0
else:
    df_acm_cit = df_cit[df_cit['title'].isin(acm_titles)].copy()
    n = int(df_acm_cit.shape[0])
    avg = None if n == 0 else float(df_acm_cit['citation_count'].mean())

out = {
    'average_citation_count_2018_for_acm_papers': avg,
    'num_papers': n
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5AXEbofhCQ4aynYGb6TCaazI': 'file_storage/call_5AXEbofhCQ4aynYGb6TCaazI.json', 'var_call_2hTmnjtFB0QrFZGgWMiSYp6v': 'file_storage/call_2hTmnjtFB0QrFZGgWMiSYp6v.json'}

exec(code, env_args)
