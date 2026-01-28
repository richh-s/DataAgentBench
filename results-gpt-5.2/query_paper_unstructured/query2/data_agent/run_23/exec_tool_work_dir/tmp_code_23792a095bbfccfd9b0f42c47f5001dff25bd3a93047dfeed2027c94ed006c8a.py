code = """import json, pandas as pd

# Load citations 2018
path_cit = var_call_7DNPhy2pc5PIzDFfH5LYWrxb
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
# ensure numeric
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load paper filenames and infer ACM by coverage of citations titles (papers in corpus are ACM HCI venues)
path_files = var_call_fo5kxVLwfcKperpsHhNr9G9q
with open(path_files, 'r', encoding='utf-8') as f:
    files = json.load(f)

df_files = pd.DataFrame(files)
df_files['title'] = df_files['filename'].str.replace(r'\.txt$', '', regex=True)

# Join: keep citations whose title is in the paper_docs corpus (ACM papers)
df = df_cit.merge(df_files[['title']], on='title', how='inner')

avg_citations = df['citation_count'].mean()
res = {
    'average_citation_count_2018_acm': None if pd.isna(avg_citations) else float(avg_citations),
    'num_acm_papers_matched': int(df.shape[0]),
    'num_total_citation_records_2018': int(df_cit.shape[0])
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_7DNPhy2pc5PIzDFfH5LYWrxb': 'file_storage/call_7DNPhy2pc5PIzDFfH5LYWrxb.json', 'var_call_fo5kxVLwfcKperpsHhNr9G9q': 'file_storage/call_fo5kxVLwfcKperpsHhNr9G9q.json'}

exec(code, env_args)
