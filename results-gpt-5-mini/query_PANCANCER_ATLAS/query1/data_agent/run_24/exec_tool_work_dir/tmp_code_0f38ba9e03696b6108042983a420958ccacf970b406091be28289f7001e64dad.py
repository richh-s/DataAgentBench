code = """import pandas as pd
import json
import math
import os
import re

# load function for storage variables

def load_var(v):
    if isinstance(v, str):
        # if it's a path to a .json file
        if os.path.exists(v):
            with open(v, 'r') as f:
                return pd.DataFrame(json.load(f))
        # try parse as json string
        try:
            return pd.DataFrame(json.loads(v))
        except Exception:
            return pd.DataFrame()
    else:
        return pd.DataFrame(v)

# var_call keys from previous tool calls
clin = load_var(var_call_zhDs1mVrNzUdHbsMW0wy3bZ4)
expr = load_var(var_call_WrXcWtibMToalFuFAClBIhjf)

# Ensure columns exist
if 'Patient_description' not in clin.columns:
    clin = pd.DataFrame(clin)

# Extract TCGA barcode from Patient_description
pattern = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', re.IGNORECASE)
clin['barcode'] = clin['Patient_description'].astype(str).apply(lambda x: (pattern.findall(x) or [None])[0])

# Keep rows with a barcode and histological_type
clin = clin[clin['barcode'].notna() & clin['histological_type'].notna()].copy()

# Filter out histological_type enclosed in square brackets (after stripping)
clin['hist_trim'] = clin['histological_type'].astype(str).str.strip()
clin = clin[~(clin['hist_trim'].str.startswith('[') & clin['hist_trim'].str.endswith(']'))]

# Build mapping barcode -> histology (if multiple entries for same barcode, keep first)
barcode_to_hist = clin.drop_duplicates('barcode').set_index('barcode')['hist_trim'].to_dict()

# Ensure expression table has ParticipantBarcode and normalized_count
if 'ParticipantBarcode' not in expr.columns:
    expr = pd.DataFrame(expr)

# Convert normalized_count to numeric, coerce errors
expr['normalized_count'] = pd.to_numeric(expr['normalized_count'], errors='coerce')
# Filter expression rows to those in barcode_to_hist and with valid normalized_count
expr_filt = expr[expr['ParticipantBarcode'].isin(barcode_to_hist.keys()) & expr['normalized_count'].notna()].copy()

# Compute log10(normalized_count + 1)
expr_filt['log10_expr'] = expr_filt['normalized_count'].apply(lambda x: math.log10(x + 1) if x >= 0 else float('nan'))
expr_filt = expr_filt[expr_filt['log10_expr'].notna()]

# Map histology
expr_filt['histology'] = expr_filt['ParticipantBarcode'].map(barcode_to_hist)

# Group by histology and compute mean
result = expr_filt.groupby('histology', dropna=True)['log10_expr'].mean().reset_index()
# Format with at least four decimal places
result['mean_log10'] = result['log10_expr'].apply(lambda x: float(f"{x:.4f}"))
out = {row['histology']: row['mean_log10'] for _, row in result.iterrows()}

# Sort output by histology name
out_sorted = {k: out[k] for k in sorted(out.keys())}

print("__RESULT__:")
print(json.dumps(out_sorted))"""

env_args = {'var_call_fJgwJfY6dj17rdT0zQ8YJjny': 'file_storage/call_fJgwJfY6dj17rdT0zQ8YJjny.json', 'var_call_pIb5KUMJA0ZJn7RLXSK2St9a': 'file_storage/call_pIb5KUMJA0ZJn7RLXSK2St9a.json', 'var_call_zhDs1mVrNzUdHbsMW0wy3bZ4': 'file_storage/call_zhDs1mVrNzUdHbsMW0wy3bZ4.json', 'var_call_WrXcWtibMToalFuFAClBIhjf': 'file_storage/call_WrXcWtibMToalFuFAClBIhjf.json'}

exec(code, env_args)
