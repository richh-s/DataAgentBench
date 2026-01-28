code = """import json, os
import pandas as pd

# Load from files
with open(var_call_2Hbz95VIWvJQczjZECJzyMYV, 'r', encoding='utf-8') as f:
    clinical_list = json.load(f)
with open(var_call_NbI2VMmvh0BNBWFTgNEKYiPB, 'r', encoding='utf-8') as f:
    mut_list = json.load(f)

# Create dataframes
clinical = pd.DataFrame(clinical_list)
mut = pd.DataFrame(mut_list)

# Inspect columns
cols_clin = clinical.columns.tolist()
cols_mut = mut.columns.tolist()

# Extract minimal clinical with patient_id and histological_type
clinical_df = clinical[['patient_id','histological_type']].copy()
clinical_df['histological_type'] = clinical_df['histological_type'].astype(str).str.strip()

# Create patient_id mapping in mutations
mut['patient_id'] = mut['ParticipantBarcode'].astype(str).str.split('-').str[-1]

# Only consider reliable mutation entries: FILTER == 'PASS' already filtered earlier
# But ensure mut_list entries all have FILTER == 'PASS'
mut_pass = [m for m in mut_list if m.get('FILTER')=='PASS']
mut_pass_df = pd.DataFrame(mut_pass)
mut_pass_df['patient_id'] = mut_pass_df['ParticipantBarcode'].astype(str).str.split('-').str[-1]
mut_patients = set(mut_pass_df['patient_id'].unique())

# Filter clinical for females in BRCA: use Patient_description containing 'Breast' or tumor_tissue_site
fem_brca = []
for rec in clinical_list:
    pdsc = rec.get('Patient_description','')
    if pdsc and ('Breast' in pdsc or 'BRCA' in pdsc or 'Breast invasive carcinoma' in pdsc):
        fem_brca.append({'patient_id': rec.get('patient_id'), 'histological_type': rec.get('histological_type')})

fem_brca_df = pd.DataFrame(fem_brca)
# Clean hist types
fem_brca_df['histological_type'] = fem_brca_df['histological_type'].astype(str).str.strip()

# Filter known histological types
exclude_values = set(['None','[Not Applicable]','Other  specify','Other specify','Unknown','Not Reported','[Not Available]'])
fem_brca_df = fem_brca_df[fem_brca_df['histological_type'].notnull()]
fem_brca_df = fem_brca_df[~fem_brca_df['histological_type'].isin(exclude_values)]

# Determine mutation presence
fem_brca_df['mutation_present'] = fem_brca_df['patient_id'].isin(mut_patients)

# Contingency
ct = fem_brca_df.groupby(['histological_type','mutation_present']).size().unstack(fill_value=0)
for col in [False, True]:
    if col not in ct.columns:
        ct[col]=0
ct = ct[[False, True]]
row_totals = ct.sum(axis=1)

# Exclude hist types with marginal totals <=10
included_mask = row_totals > 10
excluded_hist_types = row_totals[~included_mask].to_dict()
ct_included = ct.loc[included_mask]

col_totals = ct_included.sum(axis=0)
grand_total = int(col_totals.sum())

# Compute chi-square
chi2 = 0.0
for hist in ct_included.index:
    rtot = int(row_totals.loc[hist])
    for col in ct_included.columns:
        ctot = int(col_totals.loc[col])
        exp = (rtot * ctot) / grand_total if grand_total>0 else 0.0
        obs = int(ct_included.loc[hist,col])
        if exp>0:
            chi2 += ((obs-exp)**2)/exp

contingency_list = []
for hist in ct_included.index:
    no = int(ct_included.loc[hist, False])
    yes = int(ct_included.loc[hist, True])
    contingency_list.append({'histological_type': hist, 'mutation_No': no, 'mutation_Yes': yes, 'row_total': int(row_totals.loc[hist])})

result = {
    'chi2': float(chi2),
    'grand_total': grand_total,
    'column_totals': {'mutation_No': int(col_totals.loc[False]) if False in col_totals else 0, 'mutation_Yes': int(col_totals.loc[True]) if True in col_totals else 0},
    'included_histological_types': [r['histological_type'] for r in contingency_list],
    'excluded_histological_types': excluded_hist_types,
    'contingency_table': contingency_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_euNu3hqX7o5pimk0JDlcvUZn': ['clinical_info'], 'var_call_TT4YmDFu1feeK1YWDQiVcdcZ': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_c48JMfZf7ddnSH9YptwaPZd0': 'file_storage/call_c48JMfZf7ddnSH9YptwaPZd0.json', 'var_call_2Hbz95VIWvJQczjZECJzyMYV': 'file_storage/call_2Hbz95VIWvJQczjZECJzyMYV.json', 'var_call_NbI2VMmvh0BNBWFTgNEKYiPB': 'file_storage/call_NbI2VMmvh0BNBWFTgNEKYiPB.json', 'var_call_DxXrBq1MATFsl2XFarMAL9Xr': {'var_call_2Hbz95VIWvJQczjZECJzyMYV': {'type': 'str', 'is_file': True, 'list_length': 1076, 'first_keys': ['Patient_description', 'histological_type', 'patient_id']}, 'var_call_NbI2VMmvh0BNBWFTgNEKYiPB': {'type': 'str', 'is_file': True, 'list_length': 261, 'first_keys': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER']}}}

exec(code, env_args)
