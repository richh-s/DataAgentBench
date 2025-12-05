code = """import json, pandas as pd, math

# Load full IGF2 expression data
with open(var_call_MuGaZBtkMO6glVYSJ6FRdldo, 'r') as f:
    igf2_data = json.load(f)

# Load full LGG clinical histology data
with open(var_call_eMLHBuu7lT5d4fjkQDBJs5oo, 'r') as f:
    lgg_clin = json.load(f)

igf2_df = pd.DataFrame(igf2_data)
lgg_df = pd.DataFrame(lgg_clin)

# Extract barcode from Patient_description (pattern 'TCGA-..-....')
import re

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    return m.group(0) if m else None

lgg_df['ParticipantBarcode'] = lgg_df['Patient_description'].map(extract_barcode)

# Drop rows with missing barcode or histological_type enclosed in []
mask_valid_hist = ~lgg_df['histological_type'].astype(str).str.match(r'^\[.*\]$')

lgg_df = lgg_df[mask_valid_hist & lgg_df['ParticipantBarcode'].notna()].copy()

# Merge with IGF2 expression on ParticipantBarcode
merged = pd.merge(igf2_df, lgg_df[['ParticipantBarcode','histological_type']], on='ParticipantBarcode', how='inner')

# Ensure normalized_count numeric and drop invalids
merged['normalized_count'] = pd.to_numeric(merged['normalized_count'], errors='coerce')
merged = merged.dropna(subset=['normalized_count'])

# Compute log10(normalized_count + 1)
merged['log10_expr'] = (merged['normalized_count'] + 1).map(lambda x: math.log10(x))

# Average by histology type
result_series = merged.groupby('histological_type')['log10_expr'].mean().sort_index()

# Round to at least 4 decimal places
result = {k: round(float(v), 4) for k, v in result_series.items()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MuGaZBtkMO6glVYSJ6FRdldo': 'file_storage/call_MuGaZBtkMO6glVYSJ6FRdldo.json', 'var_call_yFUTHV1puRyiLOd8Ctb9ruIH': ['clinical_info'], 'var_call_IKm1yQ7YAwGHYWD3BM6Xk3om': 'file_storage/call_IKm1yQ7YAwGHYWD3BM6Xk3om.json', 'var_call_Zz0TQM14NHTJnLp73r8P8sVK': [], 'var_call_eMLHBuu7lT5d4fjkQDBJs5oo': 'file_storage/call_eMLHBuu7lT5d4fjkQDBJs5oo.json'}

exec(code, env_args)
