code = """import json
import pandas as pd
import re
import math

# Load data from previous tool calls (file paths provided in storage variables)
with open(var_call_Tfg7buZ6AcKLZPqZ1Zjppr8L, 'r') as f:
    clinical = json.load(f)
with open(var_call_CQrglBnFJ3kAKzT9XuJNu14U, 'r') as f:
    expr = json.load(f)

# Create DataFrames
df_clin = pd.DataFrame(clinical)
df_expr = pd.DataFrame(expr)

# Ensure expected columns exist
if 'Patient_description' not in df_clin.columns:
    raise ValueError('Patient_description column not found in clinical data')

# Extract ParticipantBarcode (TCGA-XX-####) from Patient_description
def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'TCGA-[A-Z0-9]{2}-\d{4}', s)
    return m.group(0) if m else None

df_clin['ParticipantBarcode'] = df_clin['Patient_description'].apply(extract_barcode)

# Identify LGG records: look for 'lower grade' or 'LGG' in Patient_description
mask_lgg = df_clin['Patient_description'].astype(str).str.contains('lower grade', case=False, na=False) | df_clin['Patient_description'].astype(str).str.contains('\bLGG\b', case=False, na=False)

df_clin_lgg = df_clin[mask_lgg].copy()

# Determine histology column to use
hist_col_candidates = ['histological_type', 'histology', 'icd_o_3_histology', 'histological_diagnosis', 'histological_type_other']
hist_col = None
for c in hist_col_candidates:
    if c in df_clin_lgg.columns:
        hist_col = c
        break
if hist_col is None:
    # fallback: try any column name containing 'hist' substring
    for c in df_clin_lgg.columns:
        if 'hist' in c.lower():
            hist_col = c
            break

if hist_col is None:
    raise ValueError('No histology-like column found in clinical data')

# Filter out histology annotations enclosed in square brackets (e.g., "[Not Applicable]")
# Keep rows where hist_col is not null and does NOT match ^\[.*\]$

df_clin_lgg[hist_col] = df_clin_lgg[hist_col].astype(str)
mask_valid_hist = ~df_clin_lgg[hist_col].str.match(r'^\[.*\]$')
df_clin_lgg = df_clin_lgg[mask_valid_hist]

# Keep only rows with a ParticipantBarcode
df_clin_lgg = df_clin_lgg[df_clin_lgg['ParticipantBarcode'].notna()]

# For clinical, reduce to unique ParticipantBarcode -> histology mapping (if multiple, keep first)
df_clin_map = df_clin_lgg[['ParticipantBarcode', hist_col]].drop_duplicates(subset=['ParticipantBarcode'])

# Prepare expression data: ensure normalized_count is numeric and Symbol == 'IGF2'
if 'Symbol' in df_expr.columns:
    df_expr = df_expr[df_expr['Symbol'] == 'IGF2'].copy()

# Normalize numeric column
if 'normalized_count' not in df_expr.columns:
    raise ValueError('normalized_count column not found in expression data')

df_expr['normalized_count'] = pd.to_numeric(df_expr['normalized_count'], errors='coerce')
# Keep only valid numeric counts
df_expr = df_expr[df_expr['normalized_count'].notna()]

# Filter expression to LGG participants
df_expr_lgg = df_expr[df_expr['ParticipantBarcode'].isin(df_clin_map['ParticipantBarcode'])].copy()

# Merge to get histology for each expression sample
merged = pd.merge(df_expr_lgg, df_clin_map, on='ParticipantBarcode', how='left')

# Drop any rows without histology
merged = merged[merged[hist_col].notna()].copy()

# Compute log10(normalized_count + 1)
import numpy as np
merged['log10_expr'] = np.log10(merged['normalized_count'] + 1)

# Group by histology and compute mean
grouped = merged.groupby(hist_col)['log10_expr'].mean()

# Prepare results with at least four decimal places
result = {str(k): float(round(v, 4)) for k, v in grouped.items()}

# Sort results by histology name for consistency
result = dict(sorted(result.items()))

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_BnOs3qTuUKJVm1yYaAwIGg6B': ['clinical_info'], 'var_call_Xb1mga1kcDrxacJ3WHx7OOWy': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_CQrglBnFJ3kAKzT9XuJNu14U': 'file_storage/call_CQrglBnFJ3kAKzT9XuJNu14U.json', 'var_call_Tfg7buZ6AcKLZPqZ1Zjppr8L': 'file_storage/call_Tfg7buZ6AcKLZPqZ1Zjppr8L.json'}

exec(code, env_args)
