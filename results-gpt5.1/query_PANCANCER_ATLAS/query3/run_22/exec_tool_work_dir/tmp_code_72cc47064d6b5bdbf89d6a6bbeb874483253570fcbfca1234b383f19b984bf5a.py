code = """import json, pandas as pd
from collections import Counter

# Load full mutation data
path = var_call_OXedKbrP0GacBGOT2Yytn8nn
with open(path, 'r') as f:
    mutation_data = json.load(f)
mut_df = pd.DataFrame(mutation_data)

# Keep only reliable entries (FILTER == 'PASS')
mut_pass = mut_df[mut_df['FILTER'] == 'PASS'].copy()

# Extract patient barcode from Patient_description in clinical BRCA breast females
path_clin = var_call_pboYo5aF5MUP1WCfNui84Rai
with open(path_clin, 'r') as f:
    clin_data = json.load(f)
clin_df = pd.DataFrame(clin_data)

# Helper to parse TCGA barcode from Patient_description
import re

def extract_barcode(desc):
    m = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    return m.group(0) if m else None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)
clin_df = clin_df.dropna(subset=['ParticipantBarcode'])

# Focus on BRCA (Breast invasive carcinoma already filtered by query) female patients with known histological type
clin_df = clin_df[['ParticipantBarcode','histological_type']].copy()

# Determine mutation presence per patient
mut_pass_brca = mut_pass.copy()
mut_pass_brca['CDH1_mutated'] = True
mut_status = mut_pass_brca.groupby('ParticipantBarcode')['CDH1_mutated'].any().reset_index()

# Merge clinical with mutation status
merged = pd.merge(clin_df, mut_status, on='ParticipantBarcode', how='left')
merged['CDH1_mutated'] = merged['CDH1_mutated'].fillna(False)

# Build contingency table histological_type x mutation (True/False)
ct = pd.crosstab(merged['histological_type'], merged['CDH1_mutated'])

# Exclude categories with marginal totals <= 10 (row sums and column sums)
row_sums = ct.sum(axis=1)
col_sums = ct.sum(axis=0)
ct_filtered = ct.loc[row_sums > 10, col_sums > 10]

# Compute chi-square statistic manually
import numpy as np

if ct_filtered.shape[0] == 0 or ct_filtered.shape[1] == 0:
    result = {'chi_square': None, 'note': 'No categories pass marginal total > 10 filter', 'contingency_table': ct.to_dict()}
else:
    observed = ct_filtered.values.astype(float)
    row_totals = observed.sum(axis=1, keepdims=True)
    col_totals = observed.sum(axis=0, keepdims=True)
    grand_total = observed.sum()
    expected = row_totals @ col_totals / grand_total
    chi_square = float(((observed - expected) ** 2 / expected).sum())
    result = {
        'chi_square': chi_square,
        'contingency_table_filtered': ct_filtered.to_dict(),
        'contingency_table_full': ct.to_dict(),
        'grand_total': float(grand_total)
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_OXedKbrP0GacBGOT2Yytn8nn': 'file_storage/call_OXedKbrP0GacBGOT2Yytn8nn.json', 'var_call_wQGE6PqY2uUz31mDhWkFAb8I': ['clinical_info'], 'var_call_NS7FpwQHme9C7Idi5MIcdibv': 'file_storage/call_NS7FpwQHme9C7Idi5MIcdibv.json', 'var_call_HClmYTPPUCSHLJevBtC8tJPf': [], 'var_call_pboYo5aF5MUP1WCfNui84Rai': 'file_storage/call_pboYo5aF5MUP1WCfNui84Rai.json'}

exec(code, env_args)
