code = """import json, pandas as pd

# load citations 2018
path_cit = var_call_Zlc4BmhM4LD0Vayalk519oFs
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
# ensure numeric
if not df_cit.empty:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# load acm papers list
path_acm = var_call_r4Cs5rcrqDcAvtZYOxIhsMIW
with open(path_acm, 'r', encoding='utf-8') as f:
    acm = json.load(f)

df_acm = pd.DataFrame(acm)
if df_acm.empty:
    avg = None
    n = 0
else:
    df_acm['title'] = df_acm['filename'].str.replace(r'\.txt$', '', regex=True)
    acm_titles = set(df_acm['title'].dropna().tolist())
    df_match = df_cit[df_cit['title'].isin(acm_titles)].copy()
    avg = None if df_match.empty else float(df_match['citation_count'].mean())
    n = int(df_match.shape[0])

out = json.dumps({'avg_citation_count_2018_for_acm_papers': avg, 'matched_papers_with_2018_citations': n})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_Zlc4BmhM4LD0Vayalk519oFs': 'file_storage/call_Zlc4BmhM4LD0Vayalk519oFs.json', 'var_call_r4Cs5rcrqDcAvtZYOxIhsMIW': 'file_storage/call_r4Cs5rcrqDcAvtZYOxIhsMIW.json'}

exec(code, env_args)
