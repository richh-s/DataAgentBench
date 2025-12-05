code = """import json, pandas as pd, math

# Load full IGF2 expression data
path_expr = var_call_UKlhSe4bR858o1A3pUSMrOCa
with open(path_expr, 'r') as f:
    expr = json.load(f)

df_expr = pd.DataFrame(expr)
# ensure numeric
df_expr['normalized_count'] = pd.to_numeric(df_expr['normalized_count'], errors='coerce')

# Extract barcode (TCGA-XX-XXXX) from Patient_description for LGG
path_lgg = var_call_RdhqfVBqUw4j8Djgpzf5z2fk
with open(path_lgg, 'r') as f:
    lgg = json.load(f)

df_lgg = pd.DataFrame(lgg)

import re

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    return m.group(0) if m else None

# add ParticipantBarcode column derived from description
df_lgg['ParticipantBarcode'] = df_lgg['Patient_description'].apply(extract_barcode)

# Filter out missing barcodes
df_lgg = df_lgg.dropna(subset=['ParticipantBarcode'])

# Merge LGG clinical with expression by ParticipantBarcode
merged = pd.merge(df_lgg[['ParticipantBarcode','histological_type']], df_expr, on='ParticipantBarcode', how='inner')

# Filter valid expression values
merged = merged.dropna(subset=['normalized_count'])

# Filter histology annotations not enclosed in square brackets (i.e., don't start with '[' and end with ']')
mask = ~merged['histological_type'].astype(str).str.match(r'^\[.*\]$')
merged = merged[mask]

# Compute log10(normalized_count + 1)
merged['log10_expr'] = (merged['normalized_count'] + 1).apply(lambda x: math.log10(x) if x > 0 else None)
merged = merged.dropna(subset=['log10_expr'])

# Group by histology and compute mean
result_series = merged.groupby('histological_type')['log10_expr'].mean().sort_index()

# Format with at least 4 decimal places
result = {k: float(f"{v:.4f}") for k, v in result_series.to_dict().items()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_UKlhSe4bR858o1A3pUSMrOCa': 'file_storage/call_UKlhSe4bR858o1A3pUSMrOCa.json', 'var_call_oGJGozoFjLTdpb3PLLCYO32F': ['clinical_info'], 'var_call_h26TuavJUg8ZXnrdcKL9R91o': 'file_storage/call_h26TuavJUg8ZXnrdcKL9R91o.json', 'var_call_RdhqfVBqUw4j8Djgpzf5z2fk': 'file_storage/call_RdhqfVBqUw4j8Djgpzf5z2fk.json'}

exec(code, env_args)
