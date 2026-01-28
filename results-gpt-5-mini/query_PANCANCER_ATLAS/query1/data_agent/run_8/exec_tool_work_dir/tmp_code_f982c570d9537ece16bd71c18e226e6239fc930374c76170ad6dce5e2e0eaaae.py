code = """import json
import re
import pandas as pd
import math

# Load data from storage file paths
with open(var_call_WMvJkrbWxLewAmPnHBsd70hM, 'r') as f:
    clinical_records = json.load(f)
with open(var_call_jcNeNhHKvEyJTIcFwWqzxZS9, 'r') as f:
    igf2_records = json.load(f)

clin_df = pd.DataFrame(clinical_records)
igf2_df = pd.DataFrame(igf2_records)

# Extract ParticipantBarcode from Patient_description using regex
# Pattern: TCGA-XX-XXXX or TCGA-XX-XXX where X are alphanumeric
pattern = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{3,4})', re.IGNORECASE)

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = pattern.search(desc)
    return m.group(1).upper() if m else None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Normalize histological_type, filter out entries with missing or bracketed annotations
def valid_hist(h):
    if not isinstance(h, str):
        return False
    h_str = h.strip()
    if h_str == '' or h_str.upper() == 'NONE':
        return False
    # Exclude annotations enclosed in square brackets or containing '['
    if '[' in h_str or ']' in h_str:
        return False
    return True

clin_df = clin_df[clin_df['ParticipantBarcode'].notnull()].copy()
clin_df = clin_df[clin_df['histological_type'].apply(valid_hist)]

# Prepare IGF2 dataframe: ensure ParticipantBarcode uppercase and normalized_count numeric
igf2_df = igf2_df[igf2_df['ParticipantBarcode'].notnull()].copy()
igf2_df['ParticipantBarcode'] = igf2_df['ParticipantBarcode'].str.upper()

# Convert normalized_count to float, filter valid
def to_float(x):
    try:
        return float(x)
    except Exception:
        return None

igf2_df['normalized_count'] = igf2_df['normalized_count'].apply(to_float)
igf2_df = igf2_df[igf2_df['normalized_count'].notnull()]

# Merge clinical LGG patients with IGF2 expression by ParticipantBarcode
merged = pd.merge(clin_df[['ParticipantBarcode','histological_type']], igf2_df[['ParticipantBarcode','normalized_count']], on='ParticipantBarcode', how='inner')

# If no merged rows, return empty
result = {}
if merged.shape[0] > 0:
    # Compute log10(normalized_count + 1)
    merged['log10_expr'] = merged['normalized_count'].apply(lambda x: math.log10(x + 1.0))
    # Group by histological_type and compute mean
    grouped = merged.groupby('histological_type')['log10_expr'].mean()
    # Format with at least four decimal places
    for hist, val in grouped.items():
        # Ensure float, round to 6 decimals for safety
        result[hist] = float(f"{val:.6f}")

# Print result as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_IgpmSN6R1euIXHDLnmReCoNa': ['clinical_info'], 'var_call_BZLcHhSP7bfEWTzp1KhI6e3t': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_VNeSiqt8bbqujVUsjIEWXO3u': 'file_storage/call_VNeSiqt8bbqujVUsjIEWXO3u.json', 'var_call_bLqwpO0ewBbprsq8Qpae4gci': 'file_storage/call_bLqwpO0ewBbprsq8Qpae4gci.json', 'var_call_WMvJkrbWxLewAmPnHBsd70hM': 'file_storage/call_WMvJkrbWxLewAmPnHBsd70hM.json', 'var_call_8YZsMlrZqomhIL5WLmIzhfXR': [{'ParticipantBarcode': 'TCGA-AB-2908', 'Symbol': 'IGF2', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'Symbol': 'IGF2', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'Symbol': 'IGF2', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'Symbol': 'IGF2', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'Symbol': 'IGF2', 'normalized_count': '613.474'}, {'ParticipantBarcode': 'TCGA-A8-A082', 'Symbol': 'IGF2', 'normalized_count': '630.54'}, {'ParticipantBarcode': 'TCGA-B5-A3FA', 'Symbol': 'IGF2', 'normalized_count': '423.628'}, {'ParticipantBarcode': 'TCGA-BH-A1EX', 'Symbol': 'IGF2', 'normalized_count': '1151.13'}, {'ParticipantBarcode': 'TCGA-BT-A20O', 'Symbol': 'IGF2', 'normalized_count': '369.106'}, {'ParticipantBarcode': 'TCGA-CD-5799', 'Symbol': 'IGF2', 'normalized_count': '3936.02070028943'}], 'var_call_jcNeNhHKvEyJTIcFwWqzxZS9': 'file_storage/call_jcNeNhHKvEyJTIcFwWqzxZS9.json'}

exec(code, env_args)
