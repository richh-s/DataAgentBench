code = """import json
import pandas as pd
import math

# Load data from previous tool results (file paths)
with open(var_call_29gweP3Wh3olg3xRH6kSvcyu, 'r') as f:
    clinical = json.load(f)
with open(var_call_TkOjC8dhpxmnEciIn4KqMswr, 'r') as f:
    mutations = json.load(f)

clin_df = pd.DataFrame(clinical)
mut_df = pd.DataFrame(mutations)

# Clean clinical dataframe: keep patient_id and histological_type, female BRCA already filtered
clin_df = clin_df[['patient_id', 'histological_type']].dropna()
# Exclude unknown histological types
unknown_vals = set(['None', '[Not Applicable]', '', 'Not Available', 'NA', 'Unknown', 'Other  specify'])
clin_df['histological_type'] = clin_df['histological_type'].astype(str).str.strip()
clin_df = clin_df[~clin_df['histological_type'].isin(unknown_vals)]

# Build set of mutated patient ids from mutation records (FILTER = PASS already)
# Map ParticipantBarcode -> patient_id as suffix after last '-'
mut_df['patient_id'] = mut_df['ParticipantBarcode'].astype(str).apply(lambda x: x.split('-')[-1])
mutated_ids = set(mut_df['patient_id'].unique())

# Determine mutation status for each clinical patient
clin_df['patient_id'] = clin_df['patient_id'].astype(str).str.strip()
clin_df['mutated'] = clin_df['patient_id'].apply(lambda pid: pid in mutated_ids)

# Aggregate counts by histological_type
agg = clin_df.groupby('histological_type')['mutated'].agg(['sum','count']).reset_index()
agg = agg.rename(columns={'sum':'mutated_count','count':'total'})

# Exclude histological types with marginal totals <= 10
agg_included = agg[agg['total'] > 10].copy()
included_types = agg_included['histological_type'].tolist()

# Prepare contingency table
contingency = {}
for _, row in agg_included.iterrows():
    h = row['histological_type']
    m = int(row['mutated_count'])
    t = int(row['total'])
    contingency[h] = {'mutated': m, 'not_mutated': t - m, 'total': t}

# Compute chi-square statistic
# Columns: mutated, not_mutated
row_totals = [v['total'] for v in contingency.values()]
col_totals = [sum(v['mutated'] for v in contingency.values()), sum(v['not_mutated'] for v in contingency.values())]
grand_total = sum(row_totals)

chi2 = 0.0
for h,v in contingency.items():
    row_total = v['total']
    for col_name, observed in [('mutated', v['mutated']), ('not_mutated', v['not_mutated'])]:
        col_total = col_totals[0] if col_name=='mutated' else col_totals[1]
        expected = (row_total * col_total) / grand_total if grand_total>0 else 0
        if expected > 0:
            chi2 += (observed - expected)**2 / expected

# Prepare output
output = {
    'chi_square': chi2,
    'grand_total': grand_total,
    'col_totals': {'mutated': col_totals[0], 'not_mutated': col_totals[1]},
    'contingency': contingency,
    'included_histological_types_count': len(included_types),
    'included_histological_types': included_types
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_kvqgRDn0Jqly28DS9OZuLbca': ['clinical_info'], 'var_call_ayDt4n3Sq4aNHOL5aL5fXEcJ': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_fgxC6gxnCvFmHszIjDad2DqT': 'file_storage/call_fgxC6gxnCvFmHszIjDad2DqT.json', 'var_call_RPYd5GdLY3Vxrjygrw06DwJC': [], 'var_call_52acDAuYMnmVwCVQwwllEdKS': 'file_storage/call_52acDAuYMnmVwCVQwwllEdKS.json', 'var_call_29gweP3Wh3olg3xRH6kSvcyu': 'file_storage/call_29gweP3Wh3olg3xRH6kSvcyu.json', 'var_call_TkOjC8dhpxmnEciIn4KqMswr': 'file_storage/call_TkOjC8dhpxmnEciIn4KqMswr.json'}

exec(code, env_args)
