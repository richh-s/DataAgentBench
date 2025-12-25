code = """import re, json, pandas as pd
from collections import defaultdict

# load full clinical breast records
path = var_call_V8X27Qqi47qtATq1n0s5WNnp
with open(path, 'r') as f:
    clinical = json.load(f)

# keep FEMALE only and extract barcode from Patient_description (pattern TCGA-..-....)
rows = []
for r in clinical:
    desc = r.get('Patient_description','') or ''
    if 'FEMALE' not in desc:
        continue
    m = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    if not m:
        continue
    barcode = m.group(0)
    hist = r.get('histological_type')
    if hist in (None, '', 'None'):
        continue
    rows.append({'ParticipantBarcode': barcode, 'histological_type': hist})

clin_df = pd.DataFrame(rows).drop_duplicates()

# load CDH1 mutation data and keep reliable (FILTER == 'PASS')
path2 = var_call_PpgZo7MCICUkRPjgaFsHviic
with open(path2, 'r') as f:
    muts = json.load(f)

muts_df = pd.DataFrame(muts)
pass_df = muts_df[muts_df['FILTER'] == 'PASS'].drop_duplicates(subset=['ParticipantBarcode'])

# merge to female BRCA breast cohort
merged = clin_df.merge(pass_df[['ParticipantBarcode']], on='ParticipantBarcode', how='left', indicator=True)
merged['CDH1_mut'] = (merged['_merge'] == 'both').astype(int)
merged = merged.drop(columns=['_merge'])

# contingency by histological_type
ct = pd.crosstab(merged['histological_type'], merged['CDH1_mut'])

# add marginal totals, filter categories with any marginal <=10 (rows and columns)
row_totals = ct.sum(axis=1)
col_totals = ct.sum(axis=0)
valid_rows = row_totals[row_totals > 10].index
valid_cols = col_totals[col_totals > 10].index
ct_filt = ct.loc[valid_rows, valid_cols]

# compute chi-square
observed = ct_filt.values
row_tot = observed.sum(axis=1, keepdims=True)
col_tot = observed.sum(axis=0, keepdims=True)
grand = observed.sum()
expected = row_tot @ col_tot / grand
chi2 = float(((observed - expected)**2 / expected).sum())

result = {
  'chi_square_statistic': chi2,
  'degrees_of_freedom': int((observed.shape[0]-1)*(observed.shape[1]-1)),
  'contingency_table': ct_filt.reset_index().to_dict(orient='list')
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_PpgZo7MCICUkRPjgaFsHviic': 'file_storage/call_PpgZo7MCICUkRPjgaFsHviic.json', 'var_call_4N9EQBIbbQKtN0zl5zoJ8Dsc': ['clinical_info'], 'var_call_fzqNv2im2v4b3AGltUeEIlEk': 'file_storage/call_fzqNv2im2v4b3AGltUeEIlEk.json', 'var_call_V8X27Qqi47qtATq1n0s5WNnp': 'file_storage/call_V8X27Qqi47qtATq1n0s5WNnp.json'}

exec(code, env_args)
