code = """import json
import pandas as pd

# Load the BRCA alive clinical records from the previous query result file
clinical_brca_alive_path = var_call_L0x3l59p0HuAgMebaDqXh7Ay
with open(clinical_brca_alive_path, 'r', encoding='utf-8') as f:
    brca_alive = json.load(f)

df_brca_alive = pd.DataFrame(brca_alive)

# Extract barcode
import re

def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,6})', s)
    return m.group(1) if m else None

if 'Patient_description' in df_brca_alive.columns:
    df_brca_alive['barcode'] = df_brca_alive['Patient_description'].apply(extract_barcode)
else:
    df_brca_alive['barcode'] = None

# Standardize barcode
def std_barcode(b):
    if not isinstance(b, str):
        return None
    parts = b.split('-')
    if len(parts) >= 3:
        return '-'.join(parts[:3])
    return b

df_brca_alive['std_barcode'] = df_brca_alive['barcode'].apply(std_barcode)

# Load mutation data for CDH1
mut_path = var_call_ouITkmkNR08gUbsBxD5GwCXh
with open(mut_path, 'r', encoding='utf-8') as f:
    mut_data = json.load(f)

df_mut = pd.DataFrame(mut_data)
cdh1_barcodes = set(df_mut['ParticipantBarcode'].dropna().unique())

# Compute counts per histological_type
summary = []
for ht, grp in df_brca_alive.groupby('histological_type'):
    total = grp['std_barcode'].nunique()
    if total == 0:
        continue
    mutated = grp['std_barcode'].dropna().unique()
    mutated_count = sum(1 for b in mutated if b in cdh1_barcodes)
    pct = (mutated_count / total) * 100
    summary.append({'histological_type': ht, 'total_alive': int(total), 'cdh1_mutated_count': int(mutated_count), 'cdh1_mutation_percentage': round(pct,2)})

summary_sorted = sorted(summary, key=lambda x: x['cdh1_mutation_percentage'], reverse=True)

import json as _json
print('__RESULT__:')
print(_json.dumps({'summary_sorted': summary_sorted, 'total_brca_alive_records': len(df_brca_alive)}))"""

env_args = {'var_call_b5TjlWa4pMQgUc2AWPo7DEmV': ['clinical_info'], 'var_call_qwSNsL5eBpVIzPjS6JQYnvdh': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_7Qs4th3kQUWOBbSHyiV2mhUl': 'file_storage/call_7Qs4th3kQUWOBbSHyiV2mhUl.json', 'var_call_ouITkmkNR08gUbsBxD5GwCXh': 'file_storage/call_ouITkmkNR08gUbsBxD5GwCXh.json', 'var_call_nwIAcW7jHezWbfvsvcu6ejRl': [], 'var_call_v3EBFWZX7VMPoPREzKYoGvEr': {'error': 'No BRCA alive patients found using tumor_tissue_site or Patient_description filters.'}, 'var_call_L0x3l59p0HuAgMebaDqXh7Ay': 'file_storage/call_L0x3l59p0HuAgMebaDqXh7Ay.json'}

exec(code, env_args)
