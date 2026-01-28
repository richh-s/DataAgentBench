code = """import json
import pandas as pd

# Load clinical data
clinical_var = var_call_qsS4fCfb5FLZpYmMGSMtMo1m
if isinstance(clinical_var, str):
    with open(clinical_var, 'r') as f:
        clinical_data = json.load(f)
else:
    clinical_data = clinical_var

# Load mutation data
mut_var = var_call_IqSPe6mwMYa0FePeJZrJ4usM
if isinstance(mut_var, str):
    with open(mut_var, 'r') as f:
        mut_data = json.load(f)
else:
    mut_data = mut_var

# Create DataFrames
clin_df = pd.DataFrame(clinical_data)
mut_df = pd.DataFrame(mut_data)

# Normalize patient ids
clin_df['patient_id'] = clin_df['patient_id'].astype(str).str.upper()
# Extract patient_id from ParticipantBarcode
mut_df['ParticipantBarcode'] = mut_df['ParticipantBarcode'].astype(str)
mut_df['patient_id'] = mut_df['ParticipantBarcode'].str.split('-').str[-1].str.upper()

# Unique mutated patient ids
mutated_ids = set(mut_df['patient_id'].unique())

# Filter clinical to only those with known histological_type
clin_df = clin_df[clin_df['histological_type'].notna()]
clin_df = clin_df[clin_df['histological_type'].str.strip() != '']

# Compute counts per histological type
summary = []
for ht, group in clin_df.groupby('histological_type'):
    total = len(group)
    mutated = group['patient_id'].isin(mutated_ids).sum()
    not_mut = total - mutated
    summary.append({'histological_type': ht, 'total': total, 'mutated': int(mutated), 'not_mutated': int(not_mut)})

summary_df = pd.DataFrame(summary)
# Exclude categories with marginal totals <= 10
included = summary_df[summary_df['total'] > 10].copy()
excluded = summary_df[summary_df['total'] <= 10].copy()

# Build contingency table
if included.empty:
    contingency = {}
    chi2 = None
    df_deg = None
else:
    contingency_df = included.set_index('histological_type')[['mutated','not_mutated']]
    # Ensure integer
    contingency_df = contingency_df.astype(int)
    grand_total = contingency_df.values.sum()
    row_totals = contingency_df.sum(axis=1)
    col_totals = contingency_df.sum(axis=0)
    # Expected
    expected = pd.DataFrame(index=contingency_df.index, columns=contingency_df.columns, dtype=float)
    for r in contingency_df.index:
        for c in contingency_df.columns:
            expected.loc[r,c] = (row_totals.loc[r] * col_totals.loc[c]) / grand_total
    # Chi-square
    chi2 = (((contingency_df - expected) ** 2) / expected).to_numpy().sum()
    # Degrees of freedom
    r = contingency_df.shape[0]
    c = contingency_df.shape[1]
    df_deg = (r - 1) * (c - 1)
    contingency = contingency_df.to_dict(orient='index')
    expected_table = expected.astype(float).to_dict(orient='index')

result = {
    'included_histological_types': list(included['histological_type']),
    'excluded_histological_types': list(excluded['histological_type']),
    'contingency_table': contingency,
    'expected_table': expected_table if included.shape[0]>0 else {},
    'chi2': float(chi2) if chi2 is not None else None,
    'degrees_of_freedom': int(df_deg) if df_deg is not None else None,
    'grand_total': int(grand_total) if included.shape[0]>0 else 0
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wLHPPN2WMif3CAD5aqL1yDLd': ['clinical_info'], 'var_call_PAxgjw2PycrJIvNMGcjuVh7w': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_3jgL7Qj2bAj3kd8toS58uOby': 'file_storage/call_3jgL7Qj2bAj3kd8toS58uOby.json', 'var_call_Z8UEhdEgCHhmxfA78BKNWigf': 'file_storage/call_Z8UEhdEgCHhmxfA78BKNWigf.json', 'var_call_qsS4fCfb5FLZpYmMGSMtMo1m': 'file_storage/call_qsS4fCfb5FLZpYmMGSMtMo1m.json', 'var_call_IqSPe6mwMYa0FePeJZrJ4usM': 'file_storage/call_IqSPe6mwMYa0FePeJZrJ4usM.json'}

exec(code, env_args)
