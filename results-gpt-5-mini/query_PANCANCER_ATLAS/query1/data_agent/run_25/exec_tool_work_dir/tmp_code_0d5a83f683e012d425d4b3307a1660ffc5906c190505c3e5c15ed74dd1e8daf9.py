code = """import json
import pandas as pd
import re

# Load data from storage variables (they may be file paths if large)
clinical_path = var_call_4nTJAXFzcjCghW8I0wS37rzH
rna_path = var_call_kia775xy4L3UdJ3E4K3Eq1zX

with open(clinical_path, 'r') as f:
    clinical = json.load(f)
with open(rna_path, 'r') as f:
    rna = json.load(f)

# Create DataFrames
df_clin = pd.DataFrame(clinical)
# Keep only relevant columns
if 'Patient_description' not in df_clin.columns:
    raise ValueError('Patient_description missing')
if 'histological_type' not in df_clin.columns:
    raise ValueError('histological_type missing')

def extract_tcga(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc.upper())
    return m.group(0) if m else None

# Extract barcode
df_clin['ParticipantBarcode'] = df_clin['Patient_description'].apply(extract_tcga)
# Filter rows with a barcode and histological_type present and not enclosed in square brackets
mask_hist = df_clin['histological_type'].notnull() & df_clin['histological_type'].apply(lambda x: isinstance(x, str) and ('[' not in x and ']' not in x))
df_clin = df_clin[ df_clin['ParticipantBarcode'].notnull() & mask_hist ][['ParticipantBarcode','histological_type']]

# RNA DataFrame
df_rna = pd.DataFrame(rna)
# Ensure normalized_count is numeric
df_rna = df_rna[df_rna['normalized_count'].notnull()]
# Convert to float, coerce errors
df_rna['normalized_count'] = pd.to_numeric(df_rna['normalized_count'], errors='coerce')
df_rna = df_rna[df_rna['normalized_count'].notnull()]

# Merge on ParticipantBarcode
merged = pd.merge(df_clin, df_rna, on='ParticipantBarcode', how='inner')

# Compute log10(normalized_count + 1)
import math
merged['log10_expr'] = merged['normalized_count'].apply(lambda x: math.log10(x+1))

# Group by histological_type and compute mean
grouped = merged.groupby('histological_type')['log10_expr'].mean().reset_index()

# Format results with at least four decimal places
result_dict = {}
for _, row in grouped.iterrows():
    hist = row['histological_type']
    val = row['log10_expr']
    # Format to 4 decimal places (but keep more if needed)
    result_dict[hist] = float(f"{val:.4f}")

# Sort keys for consistency
result_sorted = {k: result_dict[k] for k in sorted(result_dict.keys())}

print("__RESULT__:")
print(json.dumps(result_sorted))"""

env_args = {'var_call_3HxGIGzeClSoQvp8FRUbD5Lu': ['clinical_info'], 'var_call_spn1IZ4uWcqmZxXoEBRA4nfi': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_kjLNPZ2FKmBFjVQc8vGx8SRZ': 'file_storage/call_kjLNPZ2FKmBFjVQc8vGx8SRZ.json', 'var_call_4nTJAXFzcjCghW8I0wS37rzH': 'file_storage/call_4nTJAXFzcjCghW8I0wS37rzH.json', 'var_call_kia775xy4L3UdJ3E4K3Eq1zX': 'file_storage/call_kia775xy4L3UdJ3E4K3Eq1zX.json'}

exec(code, env_args)
