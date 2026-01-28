code = """import pandas as pd, json
# Load datasets from previous calls
# var_call_TJ1ks7VekWV136vhyypEz9zJ: clinical female BRCA patients with barcode and histological_type
# var_call_AIV1oO3jeg3edobfJfJoeBZb: CDH1 PASS mutations

cln = pd.read_json(var_call_TJ1ks7VekWV136vhyypEz9zJ)
mut = pd.read_json(var_call_AIV1oO3jeg3edobfJfJoeBZb)

# Standardize ParticipantBarcode to match barcode format: keep first 12 chars like TCGA-XX-XXXX
mut['barcode'] = mut['ParticipantBarcode'].str.slice(0,12)

# Filter clinical to only female BRCA by earlier query already; ensure uniqueness per patient
cln = cln[['barcode','histological_type']].drop_duplicates()

# Merge to mark which BRCA patients have CDH1 mutation
merged = cln.merge(mut[['barcode','HGVSp_Short','Variant_Classification']], on='barcode', how='left')
merged['CDH1_mutation'] = merged['HGVSp_Short'].notna()

# Only include patients with known histological types (already filtered), ensure reliable mutations only (PASS already done in query)
# Create contingency table: rows histological_type, cols mutation present True/False
ct = merged.groupby(['histological_type','CDH1_mutation']).size().unstack(fill_value=0)
ct.columns = ct.columns.astype(str)

# Exclude histological categories with marginal totals <= 10
ct['row_total'] = ct.sum(axis=1)
ct_filtered = ct[ct['row_total'] > 10].drop(columns=['row_total'])

# Also ensure columns have totals > 10? The instruction was exclude categories with marginal totals <=10 - interpreted as rows only

# Compute chi-square statistic manually
obs = ct_filtered.copy()
obs = obs.rename(columns={'True':'1.0','False':'0.0'}) if ('True' in obs.columns and 'False' in obs.columns) else obs
# ensure columns exist
for col in ['True','False']:
    if col not in obs.columns:
        obs[col] = 0

obs = obs[['True','False']]
obs = obs.astype(int)

row_totals = obs.sum(axis=1)
col_totals = obs.sum(axis=0)
grand_total = col_totals.sum()

expected = pd.DataFrame(index=obs.index, columns=obs.columns)
for r in obs.index:
    for c in obs.columns:
        expected.loc[r,c] = (row_totals.loc[r] * col_totals.loc[c]) / grand_total
expected = expected.astype(float)

chi2 = (((obs - expected)**2) / expected).to_numpy().sum()

# Prepare output
output = {
    'contingency_table_observed': obs.reset_index().to_dict(orient='records'),
    'contingency_table_expected': expected.reset_index().to_dict(orient='records'),
    'chi2_statistic': float(chi2),
    'rows_included': list(obs.index)
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_r8OPeiYuBjiIDADzFsHwbmgo': ['clinical_info'], 'var_call_naKV7hjJoTrZDSdSGOBZMQat': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_HlLs4CzpOKA44fzacjpVG6HH': 'file_storage/call_HlLs4CzpOKA44fzacjpVG6HH.json', 'var_call_jKcJCW1ltQBomJamQj4MuUSc': 'file_storage/call_jKcJCW1ltQBomJamQj4MuUSc.json', 'var_call_TJ1ks7VekWV136vhyypEz9zJ': 'file_storage/call_TJ1ks7VekWV136vhyypEz9zJ.json', 'var_call_AIV1oO3jeg3edobfJfJoeBZb': 'file_storage/call_AIV1oO3jeg3edobfJfJoeBZb.json'}

exec(code, env_args)
