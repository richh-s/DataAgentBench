code = """import json
import pandas as pd
import math

# Load clinical barcode_to_hist mapping
with open(var_call_nfTGDjW2v9wwVAYXmp08NAtR, 'r') as f:
    clinical_map = json.load(f)

barcode_to_hist = clinical_map.get('barcode_to_hist', {})

# Load RNASeq IGF2 expression
with open(var_call_HZ7PdyGLiw7EKOm2sw9bHxXJ, 'r') as f:
    expr = json.load(f)

# Create DataFrame
expr_df = pd.DataFrame(expr)
expr_df = expr_df[['ParticipantBarcode','normalized_count']]
# Normalize barcode: make uppercase and only keep first three fields (TCGA-XX-XXXX or TCGA-XX-XXXX)
# Many barcodes in clinical are like TCGA-DB-A4X9 (header) vs expression many are TCGA-XX-#### or TCGA-##-####
# We'll match by the first three dash-separated parts if possible

def norm_barcode(bc):
    if bc is None:
        return None
    bc = str(bc).upper()
    parts = bc.split('-')
    if len(parts) >= 3:
        return '-'.join(parts[:3])
    return bc

expr_df['norm_barcode'] = expr_df['ParticipantBarcode'].apply(norm_barcode)
# Convert normalized_count to float, skip non-numeric
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])

# Map histological types from clinical_map using norm_barcode
# Build reverse mapping from normalized clinical barcode to hist
clin_barcode_to_hist = {}
for k,v in barcode_to_hist.items():
    nk = norm_barcode(k)
    clin_barcode_to_hist[nk] = v

# Add hist to expr_df
expr_df['histological_type'] = expr_df['norm_barcode'].map(clin_barcode_to_hist)
# Filter to rows with non-null histology
expr_df = expr_df[~expr_df['histological_type'].isna()].copy()

# Exclude histologies enclosed in square brackets
expr_df = expr_df[~expr_df['histological_type'].str.contains('\[|\]')]

# Compute log10(normalized_count + 1)
expr_df['log10_expr'] = expr_df['normalized_count'].apply(lambda x: math.log10(x+1))

# Group by histological_type and compute mean with at least 4 decimal places
grouped = expr_df.groupby('histological_type')['log10_expr'].mean().reset_index()
# Format means to 4+ decimals
grouped['mean_log10'] = grouped['log10_expr'].apply(lambda x: float(f"{x:.4f}"))

# Sort by histological_type
grouped = grouped.sort_values('histological_type')

result = grouped[['histological_type','mean_log10']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_CTiuVYQ0GzbevuBkPuuokkjQ': ['clinical_info'], 'var_call_HmLQhigU0Pu3WEKpxZ5We0HE': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_Aqx3og4knI7XgSyuA3gd75Lf': 'file_storage/call_Aqx3og4knI7XgSyuA3gd75Lf.json', 'var_call_qwlEvjfagCOisqlBUmRH2FPF': 'file_storage/call_qwlEvjfagCOisqlBUmRH2FPF.json', 'var_call_YQVTzrXK8Axnm8KDXDZKAgqk': {'num_lgg_matches_raw': 0, 'num_matches_after_hist_filter': 0, 'participant_barcodes': [], 'barcode_to_hist': {}}, 'var_call_0eWGehozTZ9q7pSljkAcAha6': 'file_storage/call_0eWGehozTZ9q7pSljkAcAha6.json', 'var_call_lNLHdfhJLZZN9Kscj9Ybxtgx': 'file_storage/call_lNLHdfhJLZZN9Kscj9Ybxtgx.json', 'var_call_3BdZADeMn017QPPTKqRsgZQD': 'file_storage/call_3BdZADeMn017QPPTKqRsgZQD.json', 'var_call_nfTGDjW2v9wwVAYXmp08NAtR': 'file_storage/call_nfTGDjW2v9wwVAYXmp08NAtR.json', 'var_call_HZ7PdyGLiw7EKOm2sw9bHxXJ': 'file_storage/call_HZ7PdyGLiw7EKOm2sw9bHxXJ.json'}

exec(code, env_args)
