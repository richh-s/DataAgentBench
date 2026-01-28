code = """import json
import pandas as pd
import re

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
clin_df = clin_df[[c for c in ['Patient_description','histological_type'] if c in clin_df.columns]]

# extract participant barcode of form TCGA-XX-XXXX
def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4})', s)
    if m:
        return m.group(1)
    return None

clin_df['barcode'] = clin_df['Patient_description'].apply(extract_barcode)
# drop rows without barcode
clin_df = clin_df[clin_df['barcode'].notnull()].copy()
# keep first record per barcode
clin_df = clin_df.drop_duplicates(subset='barcode', keep='first')

# filter valid hist types
def valid_hist(x):
    if not isinstance(x, str):
        return False
    x2 = x.strip()
    if x2 == '' or x2 in ['None','[Not Applicable]']:
        return False
    if 'Other' in x2 or 'specify' in x2:
        return False
    return True

clin_df = clin_df[clin_df['histological_type'].apply(valid_hist)].copy()
clin_df['hist_type'] = clin_df['histological_type'].str.strip()

mut_df = pd.DataFrame(mut_records)
if 'FILTER' not in mut_df.columns:
    mut_df['FILTER'] = None

mut_pass = mut_df[(mut_df['FILTER'] == 'PASS') & (mut_df['Hugo_Symbol'] == 'CDH1')].copy()
mut_participants = set(mut_pass['ParticipantBarcode'].dropna().unique())

# For matching, ensure participant barcodes are same 12-char format
# Some mutation ParticipantBarcode may include more; extract first 12 if starts with TCGA-
clean_mut = set()
for p in mut_participants:
    if not isinstance(p, str):
        continue
    m = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4})', p)
    if m:
        clean_mut.add(m.group(1))

clin_df['mutated'] = clin_df['barcode'].apply(lambda x: x in clean_mut)

# contingency
ct = clin_df.groupby(['hist_type','mutated']).size().unstack(fill_value=0)
# ensure columns exist
for col in [False, True]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[[True, False]] if True in ct.columns else ct
ct = ct.rename(columns={True: 'mutated', False: 'not_mutated'})
ct['row_total'] = ct['mutated'] + ct['not_mutated']

included = ct[ct['row_total'] > 10].copy()
excluded = ct[ct['row_total'] <= 10].copy()

if included.shape[0] == 0:
    result = {
        'chi2': None,
        'message': 'No histological categories with marginal totals > 10 after filtering.',
        'included_hist_types': [],
        'excluded_hist_types': excluded.index.tolist(),
        'contingency_table_included': {}
    }
else:
    observed = included[['mutated','not_mutated']].values.astype(float)
    row_totals = observed.sum(axis=1)
    col_totals = observed.sum(axis=0)
    grand_total = observed.sum()
    # avoid division by zero
    expected = (row_totals[:, None] * col_totals[None, :]) / grand_total
    # mask zero expected to avoid divby0
    with pd.option_context('mode.use_inf_as_na', True):
        chi2_val = float(((observed - expected)**2 / expected)[~(expected==0)].sum())
    table_dict = {}
    for idx, row in included.iterrows():
        table_dict[idx] = {'mutated': int(row['mutated']), 'not_mutated': int(row['not_mutated']), 'row_total': int(row['row_total'])}
    result = {
        'chi2': chi2_val,
        'grand_total': int(grand_total),
        'included_hist_types': included.index.tolist(),
        'excluded_hist_types': excluded.index.tolist(),
        'contingency_table_included': table_dict
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jixHH11xnIHnxvOUtlb7WIZv': ['clinical_info'], 'var_call_w5qNNVxMiNm8C4as94dyZRQN': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_iJDf66QILkSXAQatvjpyFyW5': 'file_storage/call_iJDf66QILkSXAQatvjpyFyW5.json', 'var_call_aKcUl8yssqUfue2BYh41Hh24': 'file_storage/call_aKcUl8yssqUfue2BYh41Hh24.json', 'var_call_Epoy0BD2WZSzx3Q23mTDsGCl': 'file_storage/call_Epoy0BD2WZSzx3Q23mTDsGCl.json', 'var_call_39RcWN4uDAjXHMJaZ6tYp8FZ': 'file_storage/call_39RcWN4uDAjXHMJaZ6tYp8FZ.json'}

exec(code, env_args)
