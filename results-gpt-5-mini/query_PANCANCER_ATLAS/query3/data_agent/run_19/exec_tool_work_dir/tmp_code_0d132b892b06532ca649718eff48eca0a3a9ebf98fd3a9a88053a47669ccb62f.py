code = """import pandas as pd
import json

clinical = pd.DataFrame(var_call_2Hbz95VIWvJQczjZECJzyMYV)
mut = pd.DataFrame(var_call_NbI2VMmvh0BNBWFTgNEKYiPB)

# Normalize column names
clinical_cols = clinical.columns.tolist()
# clinical has 'patient_id' and 'histological_type'
clinical_df = clinical[['patient_id','histological_type']].copy()
clinical_df['histological_type'] = clinical_df['histological_type'].astype(str).str.strip()

# Extract patient_id from ParticipantBarcode in mutation data
mut['patient_id'] = mut['ParticipantBarcode'].astype(str).str.split('-').str[-1]
mut_patients = set(mut['patient_id'].unique())

# Filter clinical for known histological types
exclude_values = set(['None','[Not Applicable]','Other  specify','Other specify','Unknown','Not Reported','[Not Available]'])
clinical_df = clinical_df[clinical_df['histological_type'].notnull()]
clinical_df = clinical_df[~clinical_df['histological_type'].isin(exclude_values)]

# Determine mutation presence
clinical_df['mutation_present'] = clinical_df['patient_id'].isin(mut_patients)

# Build contingency table
ct = clinical_df.groupby(['histological_type','mutation_present']).size().unstack(fill_value=0)
# Ensure both columns present
for col in [False, True]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[[False, True]]

row_totals = ct.sum(axis=1)
# Exclude categories with marginal totals <= 10
included_mask = row_totals > 10
excluded_hist_types = row_totals[~included_mask].index.tolist()
ct_included = ct.loc[included_mask]

col_totals = ct_included.sum(axis=0)
grand_total = col_totals.sum()

# Compute expected values and chi-square
import numpy as np
chi2 = 0.0
expected = pd.DataFrame(index=ct_included.index, columns=ct_included.columns, dtype=float)
for hist in ct_included.index:
    rtot = row_totals.loc[hist]
    for col in ct_included.columns:
        ctot = col_totals.loc[col]
        exp = (rtot * ctot) / grand_total if grand_total>0 else 0.0
        expected.loc[hist,col] = exp
        obs = ct_included.loc[hist,col]
        if exp > 0:
            chi2 += ( (obs - exp)**2 ) / exp

# Prepare output
contingency_list = []
for hist in ct_included.index:
    no = int(ct_included.loc[hist, False])
    yes = int(ct_included.loc[hist, True])
    contingency_list.append({'histological_type': hist, 'mutation_No': no, 'mutation_Yes': yes, 'row_total': int(row_totals.loc[hist])})

result = {
    'chi2': float(chi2),
    'grand_total': int(grand_total),
    'column_totals': {'mutation_No': int(col_totals.loc[False]) if False in col_totals else 0, 'mutation_Yes': int(col_totals.loc[True]) if True in col_totals else 0},
    'included_histological_types': [r['histological_type'] for r in contingency_list],
    'excluded_histological_types': excluded_hist_types,
    'contingency_table': contingency_list
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_euNu3hqX7o5pimk0JDlcvUZn': ['clinical_info'], 'var_call_TT4YmDFu1feeK1YWDQiVcdcZ': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_c48JMfZf7ddnSH9YptwaPZd0': 'file_storage/call_c48JMfZf7ddnSH9YptwaPZd0.json', 'var_call_2Hbz95VIWvJQczjZECJzyMYV': 'file_storage/call_2Hbz95VIWvJQczjZECJzyMYV.json', 'var_call_NbI2VMmvh0BNBWFTgNEKYiPB': 'file_storage/call_NbI2VMmvh0BNBWFTgNEKYiPB.json'}

exec(code, env_args)
