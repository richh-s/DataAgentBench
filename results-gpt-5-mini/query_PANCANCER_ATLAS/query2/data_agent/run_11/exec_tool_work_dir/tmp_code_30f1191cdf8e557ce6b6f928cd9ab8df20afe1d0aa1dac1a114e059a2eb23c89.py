code = """import json
import pandas as pd
import re

# Load clinical data from stored JSON file
clinical_path = var_call_7Qs4th3kQUWOBbSHyiV2mhUl
with open(clinical_path, 'r', encoding='utf-8') as f:
    clinical_data = json.load(f)

df_clin = pd.DataFrame(clinical_data)

# Extract TCGA barcode from Patient_description
def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,6})', s)
    return m.group(1) if m else None

if 'Patient_description' in df_clin.columns:
    df_clin['barcode'] = df_clin['Patient_description'].apply(extract_barcode)
else:
    df_clin['barcode'] = df_clin.apply(lambda row: extract_barcode(str(row)), axis=1)

# Identify BRCA patients: use tumor_tissue_site == 'Breast' or Patient_description contains 'breast' or 'BRCA'
mask_breast = False
if 'tumor_tissue_site' in df_clin.columns:
    mask_breast = df_clin['tumor_tissue_site'].astype(str).str.contains('Breast', case=False, na=False)
mask_desc = df_clin['Patient_description'].astype(str).str.contains('breast', case=False, na=False) | df_clin['Patient_description'].astype(str).str.contains('BRCA', case=False, na=False)

mask_brca = mask_breast | mask_desc

# Alive patients: Patient_description contains 'Alive'
mask_alive = df_clin['Patient_description'].astype(str).str.contains('Alive', case=False, na=False)

df_brca_alive = df_clin[mask_brca & mask_alive].copy()

# Load mutation data for CDH1 from stored JSON file
mut_path = var_call_ouITkmkNR08gUbsBxD5GwCXh
with open(mut_path, 'r', encoding='utf-8') as f:
    mut_data = json.load(f)

df_mut = pd.DataFrame(mut_data)
# Unique set of barcodes with CDH1
cdh1_barcodes = set(df_mut['ParticipantBarcode'].dropna().unique())

# For df_brca_alive, ensure barcode format matches ParticipantBarcode by taking first three components
def std_barcode(b):
    if not isinstance(b, str):
        return None
    parts = b.split('-')
    if len(parts) >= 3:
        return '-'.join(parts[:3])
    return b

if 'barcode' in df_brca_alive.columns:
    df_brca_alive['std_barcode'] = df_brca_alive['barcode'].apply(std_barcode)
else:
    df_brca_alive['std_barcode'] = df_brca_alive.apply(lambda r: std_barcode(extract_barcode(r.get('Patient_description',''))), axis=1)

# Now compute counts per histological_type
if 'histological_type' not in df_brca_alive.columns:
    df_brca_alive['histological_type'] = None

summary = []
for ht, grp in df_brca_alive.groupby('histological_type'):
    total = grp['std_barcode'].nunique()
    if total == 0:
        continue
    mutated = grp['std_barcode'].dropna().unique()
    mutated_count = sum(1 for b in mutated if b in cdh1_barcodes)
    pct = (mutated_count / total) * 100
    summary.append({'histological_type': ht, 'total_alive': int(total), 'cdh1_mutated_count': int(mutated_count), 'cdh1_mutation_percentage': round(pct,2)})

# Sort by percentage desc and take top 3
summary_sorted = sorted(summary, key=lambda x: x['cdh1_mutation_percentage'], reverse=True)
top3 = summary_sorted[:3]

# If no BRCA alive patients found, prepare message
if len(df_brca_alive) == 0:
    result = {'error': 'No BRCA alive patients found using tumor_tissue_site or Patient_description filters.'}
else:
    result = {'top3_histological_types_by_cdh1_mutation_percentage': top3, 'total_brca_alive_patients': int(df_brca_alive['std_barcode'].nunique())}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_b5TjlWa4pMQgUc2AWPo7DEmV': ['clinical_info'], 'var_call_qwSNsL5eBpVIzPjS6JQYnvdh': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_7Qs4th3kQUWOBbSHyiV2mhUl': 'file_storage/call_7Qs4th3kQUWOBbSHyiV2mhUl.json', 'var_call_ouITkmkNR08gUbsBxD5GwCXh': 'file_storage/call_ouITkmkNR08gUbsBxD5GwCXh.json', 'var_call_nwIAcW7jHezWbfvsvcu6ejRl': []}

exec(code, env_args)
