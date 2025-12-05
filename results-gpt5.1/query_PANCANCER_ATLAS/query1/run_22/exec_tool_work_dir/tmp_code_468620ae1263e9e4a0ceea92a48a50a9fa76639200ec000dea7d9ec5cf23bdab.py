code = """import json, pandas as pd, math
from pathlib import Path

# Load IGF2 expression results
file_path = Path(var_call_yrKZ8lC9Ds6wKUXizweVZmEv)
with open(file_path, 'r') as f:
    igf2_data = json.load(f)

igf2_df = pd.DataFrame(igf2_data)
# ensure numeric
igf2_df['normalized_count'] = pd.to_numeric(igf2_df['normalized_count'], errors='coerce')
igf2_df = igf2_df.dropna(subset=['normalized_count'])

# Extract patient barcode from Patient_description and identify LGG cases
file_path2 = Path(var_call_swjKKsgQkyrl4mrLjRICHHRu)
with open(file_path2, 'r') as f:
    clin_data = json.load(f)

clin_df = pd.DataFrame(clin_data)

# Keep only rows whose Patient_description contains 'Brain Lower Grade Glioma'
lgg_mask = clin_df['Patient_description'].str.contains('Brain Lower Grade Glioma', case=False, na=False)
clin_lgg = clin_df[lgg_mask].copy()

# Extract TCGA barcode (e.g., TCGA-XX-YYYY)
import re

def extract_barcode(desc):
    m = re.search(r'(TCGA-\w\w-\w\w\w\w)', desc)
    return m.group(1) if m else None

clin_lgg['ParticipantBarcode'] = clin_lgg['Patient_description'].apply(extract_barcode)
clin_lgg = clin_lgg.dropna(subset=['ParticipantBarcode'])

# Exclude histology annotations enclosed in square brackets
clin_lgg = clin_lgg[~clin_lgg['histological_type'].astype(str).str.match(r"^\[.*\]$")]

# Merge with expression data
merged = pd.merge(igf2_df, clin_lgg[['ParticipantBarcode', 'histological_type']], on='ParticipantBarcode', how='inner')

# Compute log10(normalized_count + 1)
merged['log10_expr'] = (merged['normalized_count'] + 1).apply(lambda x: math.log10(x) if x > 0 else None)
merged = merged.dropna(subset=['log10_expr'])

result = merged.groupby('histological_type')['log10_expr'].mean().round(6)

out = result.to_dict()

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_yrKZ8lC9Ds6wKUXizweVZmEv': 'file_storage/call_yrKZ8lC9Ds6wKUXizweVZmEv.json', 'var_call_P0WwbJZ3QWRh4tahNl7AGkv3': ['clinical_info'], 'var_call_swjKKsgQkyrl4mrLjRICHHRu': 'file_storage/call_swjKKsgQkyrl4mrLjRICHHRu.json'}

exec(code, env_args)
