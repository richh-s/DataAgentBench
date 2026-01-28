code = """import json
import pandas as pd
import os

# Load clinical results
clinical_var = var_call_eQrPkgCU87ZtdbWdtJYebLvO
if isinstance(clinical_var, str) and os.path.exists(clinical_var):
    with open(clinical_var, 'r') as f:
        clinical = json.load(f)
else:
    clinical = clinical_var

# Load mutation results
mut_var = var_call_wiwWwslJBIJf81FzBG5WB8Jn
if isinstance(mut_var, str) and os.path.exists(mut_var):
    with open(mut_var, 'r') as f:
        mutations = json.load(f)
else:
    mutations = mut_var

# Create DataFrames
df_clin = pd.DataFrame(clinical)
# Ensure barcode and histological_type columns exist
if 'barcode' not in df_clin.columns:
    # try alternative column names
    possible = [c for c in df_clin.columns if 'barcode' in c.lower()]
    if possible:
        df_clin = df_clin.rename(columns={possible[0]: 'barcode'})

if 'histological_type' not in df_clin.columns:
    possible = [c for c in df_clin.columns if 'histolog' in c.lower()]
    if possible:
        df_clin = df_clin.rename(columns={possible[0]: 'histological_type'})

# Clean clinical df
df_clin = df_clin[['barcode', 'histological_type']].dropna()
# Standardize barcode strings
df_clin['barcode'] = df_clin['barcode'].astype(str).str.strip()

# Load mutation df
df_mut = pd.DataFrame(mutations)
# Ensure ParticipantBarcode exists
if 'ParticipantBarcode' not in df_mut.columns and 'participantbarcode' in map(str.lower, df_mut.columns):
    # find actual column
    for c in df_mut.columns:
        if c.lower() == 'participantbarcode':
            df_mut = df_mut.rename(columns={c: 'ParticipantBarcode'})
            break

# Standardize mutation barcodes
if 'ParticipantBarcode' in df_mut.columns:
    df_mut['ParticipantBarcode'] = df_mut['ParticipantBarcode'].astype(str).str.strip()
    mutated_set = set(df_mut['ParticipantBarcode'].unique())
else:
    mutated_set = set()

# Compute totals and mutated per histological type
results = []
for hist, group in df_clin.groupby('histological_type'):
    # filter out 'None' or empty
    if hist is None or str(hist).strip().upper() in ('NONE', '', 'NAN'):
        continue
    unique_barcodes = set(group['barcode'].unique())
    total = len(unique_barcodes)
    mutated = len(unique_barcodes & mutated_set)
    percent = round((mutated / total * 100) if total>0 else 0.0, 2)
    results.append({'histological_type': hist, 'total_patients': total, 'mutated_patients': mutated, 'percent_mutated': percent})

# Sort by percent desc, then by total desc
results_sorted = sorted(results, key=lambda x: (-x['percent_mutated'], -x['total_patients']))
# Take top 3
top3 = results_sorted[:3]

# Prepare JSON string
output = json.dumps(top3)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_reFWy9QIbBcJuBseXlCY2gd3': ['clinical_info'], 'var_call_j4io99tVRTXQ8LRmMg3yMzzV': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_LPLZ1xpfTZKvNhrI0wWi8DB2': 'file_storage/call_LPLZ1xpfTZKvNhrI0wWi8DB2.json', 'var_call_MRS1VrCy7eEJIvkWMRLJMwGu': 'file_storage/call_MRS1VrCy7eEJIvkWMRLJMwGu.json', 'var_call_jEZktAAz1ljzM3H0iFW0TjHq': [], 'var_call_eQrPkgCU87ZtdbWdtJYebLvO': 'file_storage/call_eQrPkgCU87ZtdbWdtJYebLvO.json', 'var_call_wiwWwslJBIJf81FzBG5WB8Jn': 'file_storage/call_wiwWwslJBIJf81FzBG5WB8Jn.json'}

exec(code, env_args)
