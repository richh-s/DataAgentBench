code = """import json, pandas as pd

# load citations 2020
p_cit = var_call_tOrfOfS7F6VVoJINRmrP69V8
if isinstance(p_cit, str):
    with open(p_cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)
else:
    cit = p_cit

df_cit = pd.DataFrame(cit)
if not df_cit.empty:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

# load CHI papers from mongo (filenames)
p_chi = var_call_CAGuHIBcpBNiaFJ8q13SqOa8
if isinstance(p_chi, str):
    with open(p_chi, 'r', encoding='utf-8') as f:
        chi = json.load(f)
else:
    chi = p_chi

df_chi = pd.DataFrame(chi)
if not df_chi.empty:
    df_chi['title'] = df_chi['filename'].str.replace(r'\\.txt$', '', regex=True)

df = df_cit.merge(df_chi[['title']], on='title', how='inner')

total = int(df['citation_count'].sum())

out = {
    'total_citations_2020_for_CHI_papers': total,
    'num_CHI_papers_with_citations_2020': int(df['title'].nunique()),
    'num_citation_records_matched': int(len(df))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_tOrfOfS7F6VVoJINRmrP69V8': 'file_storage/call_tOrfOfS7F6VVoJINRmrP69V8.json', 'var_call_CAGuHIBcpBNiaFJ8q13SqOa8': 'file_storage/call_CAGuHIBcpBNiaFJ8q13SqOa8.json'}

exec(code, env_args)
