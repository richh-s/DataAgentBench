code = """import json, math, pandas as pd, numpy as np
# Load clinical mapping
clin_path = var_call_sb5SzvHFPJ5bt6MswM081XeN
with open(clin_path, 'r') as f:
    clin = json.load(f)
# Load IGF2 expression
expr_path = var_call_nD31crTsQchNRF04GUGFCTQX
with open(expr_path, 'r') as f:
    expr = json.load(f)

df_clin = pd.DataFrame(clin)
# Ensure ParticipantBarcode column exists
if 'ParticipantBarcode' not in df_clin.columns:
    raise ValueError('ParticipantBarcode missing in clinical mapping')
# Normalize participant barcodes
df_clin['ParticipantBarcode'] = df_clin['ParticipantBarcode'].str.strip().str.upper()
# Filter out histologies enclosed in square brackets (already filtered, but double-check)
def valid_hist(h):
    if not isinstance(h, str):
        return False
    s = h.strip()
    return not (s.startswith('[') and s.endswith(']'))

df_clin = df_clin[df_clin['histological_type'].apply(valid_hist)].copy()

# Expression df
df_expr = pd.DataFrame(expr)
# Some rows may not have ParticipantBarcode or normalized_count
if 'ParticipantBarcode' not in df_expr.columns or 'normalized_count' not in df_expr.columns:
    raise ValueError('Expression fields missing')
# Normalize
df_expr['ParticipantBarcode'] = df_expr['ParticipantBarcode'].astype(str).str.strip().str.upper()
# Convert normalized_count to float, coerce errors to NaN
df_expr['normalized_count'] = pd.to_numeric(df_expr['normalized_count'], errors='coerce')
# Keep only valid numeric counts
df_expr = df_expr[df_expr['normalized_count'].notna()].copy()

# Merge on ParticipantBarcode (inner join)
df_merged = pd.merge(df_expr, df_clin, on='ParticipantBarcode', how='inner')

# Compute log10(normalized_count + 1)
df_merged['log10_igf2'] = np.log10(df_merged['normalized_count'] + 1)

# Group by histological_type and compute mean
grouped = df_merged.groupby('histological_type')['log10_igf2'].mean()

# Prepare output: map histology -> string with 4 decimal places (at least)
out = {str(idx): f"{val:.4f}" for idx, val in grouped.items()}

# If no data matched, return empty dict
result_json = json.dumps(out)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_QAvxw7s3ZU4ykF0SSRDPAOhG': ['clinical_info'], 'var_call_xFmgT4sC7AzdEEJXSSi3huE3': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_LlUwkwZudcbKIoYqJCR0gneT': 'file_storage/call_LlUwkwZudcbKIoYqJCR0gneT.json', 'var_call_VCqogynOE3C6dz2dkn0ikboD': 'file_storage/call_VCqogynOE3C6dz2dkn0ikboD.json', 'var_call_sr3U50m0gueI782wn5P1q4Gy': 'file_storage/call_sr3U50m0gueI782wn5P1q4Gy.json', 'var_call_sb5SzvHFPJ5bt6MswM081XeN': 'file_storage/call_sb5SzvHFPJ5bt6MswM081XeN.json', 'var_call_nD31crTsQchNRF04GUGFCTQX': 'file_storage/call_nD31crTsQchNRF04GUGFCTQX.json'}

exec(code, env_args)
