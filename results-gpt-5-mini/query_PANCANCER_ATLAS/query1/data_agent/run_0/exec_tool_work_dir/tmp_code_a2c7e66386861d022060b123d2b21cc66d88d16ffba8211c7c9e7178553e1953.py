code = """import json
import pandas as pd
import math
import re

# Load clinical LGG subset
clinical_var = var_call_Yo6ddXuVOzLwtlUyGU14m97t
if isinstance(clinical_var, str):
    with open(clinical_var, 'r') as f:
        clinical = json.load(f)
else:
    clinical = clinical_var

# Load IGF2 expression data
expr_var = var_call_eWvNv4z9B55JPdjnSXxKXNlX
if isinstance(expr_var, str):
    with open(expr_var, 'r') as f:
        expr = json.load(f)
else:
    expr = expr_var

df_clin = pd.DataFrame(clinical)
df_expr = pd.DataFrame(expr)

# Ensure normalized_count is numeric
df_expr = df_expr[df_expr['normalized_count'].notnull()].copy()
# Convert strings to float safely
def to_float(x):
    try:
        return float(x)
    except:
        return None

df_expr['normalized_count'] = df_expr['normalized_count'].apply(to_float)
# Drop invalid
df_expr = df_expr[df_expr['normalized_count'].notnull()]

# Build mapping from barcode found in Patient_description to histological_type
barcode_to_hist = {}
pattern = re.compile(r"TCGA-[A-Z0-9]{2}-[A-Z0-9]{3,4}")

for _, row in df_clin.iterrows():
    pd_desc = row.get('Patient_description', '')
    hist = row.get('histological_type', None)
    if pd_desc is None or pd_desc == '':
        continue
    matches = pattern.findall(pd_desc)
    if not matches:
        continue
    # Exclude histologies with square brackets
    if hist is None:
        continue
    if '[' in str(hist) or ']' in str(hist):
        continue
    for m in matches:
        # if multiple clinical rows map to same barcode, prefer first encountered
        if m not in barcode_to_hist:
            barcode_to_hist[m] = hist

# Map histologies to expression rows by ParticipantBarcode
def map_hist(barcode):
    return barcode_to_hist.get(barcode)

df_expr['histology'] = df_expr['ParticipantBarcode'].apply(map_hist)
# Keep only rows with mapped histology
df_expr = df_expr[df_expr['histology'].notnull()].copy()

# Compute log10(normalized_count + 1)
df_expr['log10_expr'] = df_expr['normalized_count'].apply(lambda x: math.log10(x + 1))

# Group by histology and compute mean
grouped = df_expr.groupby('histology')['log10_expr'].mean()

# Prepare results with at least four decimal places
result = {str(h): float(f"{v:.4f}") for h, v in grouped.items()}

# Print in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_i4xlmzioxdGb1iV0IczJVNyk': ['clinical_info'], 'var_call_zSTMcLZLEe23fK1Mg8kHk0QS': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_oFsBQgiEpFDUzrrg4E4jDQaL': 'file_storage/call_oFsBQgiEpFDUzrrg4E4jDQaL.json', 'var_call_FmrSEauL9zMqgqOFFoAXQzmn': 'file_storage/call_FmrSEauL9zMqgqOFFoAXQzmn.json', 'var_call_Yo6ddXuVOzLwtlUyGU14m97t': 'file_storage/call_Yo6ddXuVOzLwtlUyGU14m97t.json', 'var_call_eWvNv4z9B55JPdjnSXxKXNlX': 'file_storage/call_eWvNv4z9B55JPdjnSXxKXNlX.json'}

exec(code, env_args)
