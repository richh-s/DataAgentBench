code = """import json, pandas as pd

# Load full IGF2 expression data from file
path_expr = var_call_8TGgsoz4Tyk3LzcCCTgYcbnK
with open(path_expr, 'r') as f:
    igf2_expr = json.load(f)

# Convert to DataFrame
expr_df = pd.DataFrame(igf2_expr)
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])

# Extract ParticipantBarcode from Patient_description in clinical_info and cancer type
path_clin = var_call_V0lkT1p9WP2RTq7IJ1Vi2sub
with open(path_clin, 'r') as f:
    clin_preview = json.load(f)

clin_df = pd.DataFrame(clin_preview)

# Derive ParticipantBarcode (e.g., 'TCGA-31-1953') from Patient_description text
import re

def extract_barcode(desc):
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    return m.group(1) if m else None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Identify LGG patients using diagnosis/tumor_tissue_site/icd_10 text containing 'glioma' or 'Brain lower grade glioma' or 'LGG'
text_cols = [c for c in clin_df.columns if isinstance(c, str)]

def is_lgg(row):
    for c in text_cols:
        val = row.get(c)
        if isinstance(val, str) and any(k in val for k in ['Brain lower grade glioma', 'lower grade glioma', 'LGG']):
            return True
    return False

clin_df['is_LGG'] = clin_df.apply(is_lgg, axis=1)

lgg_clin = clin_df[clin_df['is_LGG'] & clin_df['ParticipantBarcode'].notna()].copy()

# Filter histology annotations not enclosed in square brackets
def clean_hist(h):
    if not isinstance(h, str):
        return None
    h_strip = h.strip()
    if h_strip.startswith('[') and h_strip.endswith(']'):
        return None
    return h_strip

lgg_clin['histology_clean'] = lgg_clin.get('histological_type')
if 'histology_clean' in lgg_clin:
    lgg_clin['histology_clean'] = lgg_clin['histology_clean'].apply(clean_hist)

lgg_clin = lgg_clin[lgg_clin['histology_clean'].notna()]

# Merge LGG clinical with IGF2 expression on ParticipantBarcode
merged = pd.merge(lgg_clin[['ParticipantBarcode','histology_clean']], expr_df, on='ParticipantBarcode', how='inner')

# Compute log10(normalized_count + 1)
import math
merged['log10_expr'] = (merged['normalized_count'] + 1).apply(lambda x: math.log10(x) if x > 0 else None)
merged = merged.dropna(subset=['log10_expr'])

# Group by histology and compute mean
result = merged.groupby('histology_clean')['log10_expr'].mean().round(4).sort_index()

result_dict = {k: float(v) for k,v in result.to_dict().items()}

out = json.dumps(result_dict)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8TGgsoz4Tyk3LzcCCTgYcbnK': 'file_storage/call_8TGgsoz4Tyk3LzcCCTgYcbnK.json', 'var_call_FqVorZEOJVgYK90ilp1zEbD2': ['clinical_info'], 'var_call_V0lkT1p9WP2RTq7IJ1Vi2sub': 'file_storage/call_V0lkT1p9WP2RTq7IJ1Vi2sub.json'}

exec(code, env_args)
