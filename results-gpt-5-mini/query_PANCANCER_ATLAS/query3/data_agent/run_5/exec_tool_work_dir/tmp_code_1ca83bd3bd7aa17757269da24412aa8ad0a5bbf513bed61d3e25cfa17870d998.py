code = """import json
import pandas as pd
import re

# Load clinical data from storage variable
clinical_var = var_call_Epoy0BD2WZSzx3Q23mTDsGCl
if isinstance(clinical_var, str):
    with open(clinical_var, 'r') as f:
        clinical_records = json.load(f)
else:
    clinical_records = clinical_var

mut_var = var_call_39RcWN4uDAjXHMJaZ6tYp8FZ
if isinstance(mut_var, str):
    with open(mut_var, 'r') as f:
        mut_records = json.load(f)
else:
    mut_records = mut_var

clin_df = pd.DataFrame(clinical_records)
# keep relevant columns
clin_df = clin_df[[c for c in ['Patient_description','histological_type'] if c in clin_df.columns]]
# extract TCGA barcode
def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,6})', s)
    if m:
        return m.group(1)
    return None

clin_df['barcode'] = clin_df['Patient_description'].apply(extract_barcode)
# Filter known histological types
def valid_hist(x):
    if not isinstance(x, str):
        return False
    x_strip = x.strip()
    if x_strip == '' or x_strip in ['None','[Not Applicable]']:
        return False
    if 'Other' in x_strip or 'specify' in x_strip:
        return False
    return True

clin_df = clin_df[clin_df['barcode'].notnull() & clin_df['histological_type'].apply(valid_hist)].copy()

# Normalize histological type
clin_df['hist_type'] = clin_df['histological_type'].str.strip()

# Load mutation data and filter reliable entries (FILTER == 'PASS')
mut_df = pd.DataFrame(mut_records)
if 'FILTER' not in mut_df.columns:
    mut_df['FILTER'] = None

mut_pass = mut_df[mut_df['FILTER'] == 'PASS'].copy()
# get set of participant barcodes with CDH1 PASS
mut_cdh1 = set(mut_pass[mut_pass['Hugo_Symbol'] == 'CDH1']['ParticipantBarcode'].dropna().unique())

# Map mutation presence to clinical patients
clin_df['mutated'] = clin_df['barcode'].isin(mut_cdh1)

# Build contingency table
ct = clin_df.groupby(['hist_type','mutated']).size().unstack(fill_value=0)
# Ensure both columns exist
if True not in ct.columns:
    ct[True] = 0
if False not in ct.columns:
    ct[False] = 0
ct = ct[[True, False]]  # mutated True first
ct = ct.rename(columns={True: 'mutated', False: 'not_mutated'})

# Exclude hist types with marginal totals <= 10
ct['row_total'] = ct['mutated'] + ct['not_mutated']
included = ct[ct['row_total'] > 10].copy()
excluded = ct[ct['row_total'] <= 10].copy()

# If no included categories, return empty result
if included.shape[0] == 0:
    result = {
        'chi2': None,
        'message': 'No histological categories with marginal totals > 10 after filtering.',
        'included_hist_types': [],
        'excluded_hist_types': excluded.index.tolist(),
        'contingency_table_included': {}
    }
else:
    # compute chi-square
    observed = included[['mutated','not_mutated']].values.astype(float)
    row_totals = observed.sum(axis=1)
    col_totals = observed.sum(axis=0)
    grand_total = observed.sum()
    expected = (row_totals[:, None] * col_totals[None, :]) / grand_total
    # compute chi-square
    chi2 = float(((observed - expected)**2 / expected).sum())
    # Build dict table
    table_dict = {}
    for idx, row in included.iterrows():
        table_dict[idx] = {'mutated': int(row['mutated']), 'not_mutated': int(row['not_mutated']), 'row_total': int(row['row_total'])}
    result = {
        'chi2': chi2,
        'grand_total': int(grand_total),
        'included_hist_types': included.index.tolist(),
        'excluded_hist_types': excluded.index.tolist(),
        'contingency_table_included': table_dict
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jixHH11xnIHnxvOUtlb7WIZv': ['clinical_info'], 'var_call_w5qNNVxMiNm8C4as94dyZRQN': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_iJDf66QILkSXAQatvjpyFyW5': 'file_storage/call_iJDf66QILkSXAQatvjpyFyW5.json', 'var_call_aKcUl8yssqUfue2BYh41Hh24': 'file_storage/call_aKcUl8yssqUfue2BYh41Hh24.json', 'var_call_Epoy0BD2WZSzx3Q23mTDsGCl': 'file_storage/call_Epoy0BD2WZSzx3Q23mTDsGCl.json', 'var_call_39RcWN4uDAjXHMJaZ6tYp8FZ': 'file_storage/call_39RcWN4uDAjXHMJaZ6tYp8FZ.json'}

exec(code, env_args)
