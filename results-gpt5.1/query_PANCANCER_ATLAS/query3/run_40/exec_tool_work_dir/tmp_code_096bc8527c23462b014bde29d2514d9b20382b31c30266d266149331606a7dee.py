code = """import re, json, pandas as pd
from collections import defaultdict

# Load full mutation data
import os, json as js
mut_path = var_call_b4JQxPk8g31hsFAC30il15Z4
with open(mut_path, 'r') as f:
    mut_data = js.load(f)

mut_df = pd.DataFrame(mut_data)
# Reliable mutations: FILTER == 'PASS'
mut_pass = mut_df[mut_df['FILTER'] == 'PASS'].copy()
mut_patients = set(mut_pass['ParticipantBarcode'].dropna().unique())

# Load clinical breast cohort
clin_path = var_call_xIm16pu8Fk9yVZT991mrtRpq
with open(clin_path, 'r') as f:
    clin_data = js.load(f)
clin_df = pd.DataFrame(clin_data)

# Restrict to FEMALE BRCA based on Patient_description text containing 'FEMALE' and 'Breast invasive carcinoma'
female_mask = clin_df['Patient_description'].str.contains('FEMALE', case=False, na=False)
brca_mask = clin_df['Patient_description'].str.contains('Breast invasive carcinoma', case=False, na=False)
clin_brca_f = clin_df[female_mask & brca_mask].copy()

# Extract barcode (TCGA-..-....) from Patient_description
pat_ids = []
for desc in clin_brca_f['Patient_description']:
    m = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    pat_ids.append(m.group(0) if m else None)
clin_brca_f['ParticipantBarcode'] = pat_ids
clin_brca_f = clin_brca_f.dropna(subset=['ParticipantBarcode', 'histological_type'])

# Keep only patients present in mutation table cohort (BRCA PanCancer Atlas overlap)
clin_brca_f = clin_brca_f.drop_duplicates(subset=['ParticipantBarcode'])

# Define mutation presence (at least one PASS CDH1 mutation)
clin_brca_f['CDH1_mut'] = clin_brca_f['ParticipantBarcode'].isin(mut_patients)

# Build contingency table histological_type x CDH1_mut
ct = pd.crosstab(clin_brca_f['histological_type'], clin_brca_f['CDH1_mut'])
ct.columns = ['No_mut', 'Mut'] if False in ct.columns and True in ct.columns else ct.columns

# Add margins
ct['row_total'] = ct.sum(axis=1)
col_totals = ct.sum(axis=0)

# Exclude hist types with marginal totals <=10 (row_total criterion and also ensure column totals >10?)
ct_filt = ct[ct['row_total'] > 10].copy()

# Compute chi-square manually on 2D table without the row_total column
cols = [c for c in ct_filt.columns if c != 'row_total']
obs = ct_filt[cols].values
row_tot = obs.sum(axis=1, keepdims=True)
col_tot = obs.sum(axis=0, keepdims=True)
grand_total = obs.sum()

# Expected counts
exp = row_tot @ col_tot / grand_total

# Avoid division by zero
with pd.option_context('mode.use_inf_as_na', True):
    chi_sq = float(((obs - exp) ** 2 / exp).sum())

# Prepare output summary
out = {
    'contingency_table': ct_filt.reset_index().to_dict(orient='records'),
    'chi_square_statistic': chi_sq,
    'grand_total': int(grand_total)
}

res = json.dumps(out)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_b4JQxPk8g31hsFAC30il15Z4': 'file_storage/call_b4JQxPk8g31hsFAC30il15Z4.json', 'var_call_LnoZQR1UdS2NPBxPatg2VARs': ['clinical_info'], 'var_call_QcNCLZxKn9Lwzy1H3TAPF82S': 'file_storage/call_QcNCLZxKn9Lwzy1H3TAPF82S.json', 'var_call_xIm16pu8Fk9yVZT991mrtRpq': 'file_storage/call_xIm16pu8Fk9yVZT991mrtRpq.json'}

exec(code, env_args)
