code = """import json, pandas as pd

# Load citations 2018
cit_path = var_call_F9dqPv44AkZC0k2LQaTkg2kb
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
# ensure numeric
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load mongo filenames list
fn_path = var_call_ajWxKzEZZwIyEPPDafl5oe8C
with open(fn_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
df_docs = pd.DataFrame(docs)
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

# Heuristic: in this dataset, papers are ACM venue papers. So treat all listed doc titles as ACM.
acm_titles = set(df_docs['title'].dropna().tolist())

df_acm_cit = df_cit[df_cit['title'].isin(acm_titles)].copy()
avg_citations = float(df_acm_cit['citation_count'].mean()) if len(df_acm_cit) else None
out = {
    'average_citation_count_2018_for_acm_papers': avg_citations,
    'num_papers_matched': int(df_acm_cit.shape[0]),
    'num_citation_records_2018': int(df_cit.shape[0])
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_F9dqPv44AkZC0k2LQaTkg2kb': 'file_storage/call_F9dqPv44AkZC0k2LQaTkg2kb.json', 'var_call_ajWxKzEZZwIyEPPDafl5oe8C': 'file_storage/call_ajWxKzEZZwIyEPPDafl5oe8C.json'}

exec(code, env_args)
