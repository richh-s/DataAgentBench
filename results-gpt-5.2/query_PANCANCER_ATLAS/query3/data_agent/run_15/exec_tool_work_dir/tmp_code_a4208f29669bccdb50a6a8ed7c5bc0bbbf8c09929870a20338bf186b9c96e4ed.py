code = """import json, re, pandas as pd

# Load clinical records (may be a json file path)
clin_src = var_call_YtCo66YCrBjtzUbnLAtJd0VB
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

mut_src = var_call_lnjVmLnBcQoFeEZnysyICwB3
if isinstance(mut_src, str):
    with open(mut_src, 'r') as f:
        muts = json.load(f)
else:
    muts = mut_src

# Extract TCGA barcode from Patient_description text
barcode_re = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
rows=[]
for r in clin:
    desc = r.get('participant_barcode')
    ht = r.get('histological_type')
    if not desc or not ht:
        continue
    m = barcode_re.search(desc)
    if not m:
        continue
    rows.append({'participant_barcode': m.group(1), 'histological_type': ht})

clin_df = pd.DataFrame(rows).drop_duplicates(subset=['participant_barcode'])

mut_df = pd.DataFrame(muts).drop_duplicates()
mut_set = set(mut_df['participant_barcode'].dropna().astype(str))

# Keep only BRCA-like participants: approximate by barcode prefix? We cannot filter by acronym due to missing column.
# Proceed with all females not available; so restrict to participants in mutation set union? We'll compute within those with histological type.
# Define mutation presence
clin_df['CDH1_mut'] = clin_df['participant_barcode'].isin(mut_set)

# Contingency table
ct = pd.crosstab(clin_df['histological_type'], clin_df['CDH1_mut'])
ct.columns = ['no_mut','mut'] if len(ct.columns)==2 else [str(c) for c in ct.columns]

# Exclude categories with marginal totals <=10 (row totals)
ct = ct.loc[ct.sum(axis=1) > 10]

# Also ensure both columns exist
if 'mut' not in ct.columns:
    ct['mut']=0
if 'no_mut' not in ct.columns:
    ct['no_mut']=0
ct = ct[['no_mut','mut']]

# Exclude columns with marginal totals <=10
ct = ct.loc[:, ct.sum(axis=0) > 10]

# If after filtering insufficient dimensions
chi2 = None
if ct.shape[0] >= 2 and ct.shape[1] >= 2:
    obs = ct.values.astype(float)
    row_tot = obs.sum(axis=1, keepdims=True)
    col_tot = obs.sum(axis=0, keepdims=True)
    grand = obs.sum()
    exp = row_tot @ col_tot / grand
    chi2 = float(((obs-exp)**2/exp).sum())

out = {
    'n_patients_with_histology': int(clin_df.shape[0]),
    'n_cdh1_mut_pass_unique_participants': int(len(mut_set)),
    'contingency_table_after_filters': ct.reset_index().to_dict(orient='records'),
    'chi_square': chi2,
    'grand_total_used': (int(ct.values.sum()) if ct is not None else None),
    'rows': int(ct.shape[0]),
    'cols': int(ct.shape[1])
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lnjVmLnBcQoFeEZnysyICwB3': 'file_storage/call_lnjVmLnBcQoFeEZnysyICwB3.json', 'var_call_bm5s9pnnac9TQh6uiQfZqz0S': ['clinical_info'], 'var_call_DuS2TsKMrVA9ubicRofRiRkH': [{'column_name': 'Patient_description'}, {'column_name': 'histological_type'}], 'var_call_YtCo66YCrBjtzUbnLAtJd0VB': 'file_storage/call_YtCo66YCrBjtzUbnLAtJd0VB.json'}

exec(code, env_args)
