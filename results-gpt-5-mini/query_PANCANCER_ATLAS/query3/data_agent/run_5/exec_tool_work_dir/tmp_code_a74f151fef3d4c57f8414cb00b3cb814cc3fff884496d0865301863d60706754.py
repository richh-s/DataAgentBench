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
# keep relevant cols
cols = [c for c in ['Patient_description','histological_type'] if c in clin_df.columns]
clin_df = clin_df[cols].copy()

# barcode extraction regex: capture TCGA-XX-XXXX (two letters/digits, then hyphen, then 4+ alnum)
def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,6})', s)
    if m:
        return m.group(1)
    return None

clin_df['barcode'] = clin_df['Patient_description'].apply(extract_barcode)
clin_df = clin_df[clin_df['barcode'].notnull()].copy()
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

# select PASS CDH1 mutations
mut_pass = mut_df[(mut_df['FILTER'] == 'PASS') & (mut_df['Hugo_Symbol'] == 'CDH1')]
mut_participants = set()
for p in mut_pass['ParticipantBarcode'].dropna().unique():
    if not isinstance(p, str):
        continue
    m = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,6})', p)
    if m:
        mut_participants.add(m.group(1))

# Build counts per hist_type
counts = {}
for _, row in clin_df.iterrows():
    ht = row['hist_type']
    barcode = row['barcode']
    mutated = barcode in mut_participants
    if ht not in counts:
        counts[ht] = {'mutated': 0, 'not_mutated': 0}
    if mutated:
        counts[ht]['mutated'] += 1
    else:
        counts[ht]['not_mutated'] += 1

# create dataframe
ct = pd.DataFrame.from_dict(counts, orient='index')
if ct.empty:
    result = {'chi2': None, 'message': 'No data after filtering', 'contingency_table': {}, 'included_hist_types': [], 'excluded_hist_types': []}
    print('__RESULT__:')
    print(json.dumps(result))
else:
    ct['row_total'] = ct['mutated'] + ct['not_mutated']
    included = ct[ct['row_total'] > 10].copy()
    excluded = ct[ct['row_total'] <= 10].copy()
    if included.shape[0] == 0:
        result = {
            'chi2': None,
            'message': 'No histological categories with marginal totals > 10 after filtering.',
            'included_hist_types': [],
            'excluded_hist_types': sorted(excluded.index.tolist()),
            'contingency_table_included': {}
        }
        print('__RESULT__:')
        print(json.dumps(result))
    else:
        observed = included[['mutated','not_mutated']].values.astype(float)
        row_totals = observed.sum(axis=1)
        col_totals = observed.sum(axis=0)
        grand_total = observed.sum()
        expected = (row_totals[:, None] * col_totals[None, :]) / grand_total
        # compute chi2 where expected>0
        mask = expected > 0
        chi2_val = float(((observed - expected)**2 / expected)[mask].sum())
        table_dict = {}
        for idx, r in included.iterrows():
            table_dict[idx] = {'mutated': int(r['mutated']), 'not_mutated': int(r['not_mutated']), 'row_total': int(r['row_total'])}
        result = {
            'chi2': chi2_val,
            'grand_total': int(grand_total),
            'included_hist_types': sorted(included.index.tolist()),
            'excluded_hist_types': sorted(excluded.index.tolist()),
            'contingency_table_included': table_dict
        }
        print('__RESULT__:')
        print(json.dumps(result))"""

env_args = {'var_call_jixHH11xnIHnxvOUtlb7WIZv': ['clinical_info'], 'var_call_w5qNNVxMiNm8C4as94dyZRQN': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_iJDf66QILkSXAQatvjpyFyW5': 'file_storage/call_iJDf66QILkSXAQatvjpyFyW5.json', 'var_call_aKcUl8yssqUfue2BYh41Hh24': 'file_storage/call_aKcUl8yssqUfue2BYh41Hh24.json', 'var_call_Epoy0BD2WZSzx3Q23mTDsGCl': 'file_storage/call_Epoy0BD2WZSzx3Q23mTDsGCl.json', 'var_call_39RcWN4uDAjXHMJaZ6tYp8FZ': 'file_storage/call_39RcWN4uDAjXHMJaZ6tYp8FZ.json'}

exec(code, env_args)
