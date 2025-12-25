code = """import json, pandas as pd
from collections import defaultdict

cdh1_file = var_call_RqvEzYWtKjvh87uk0NgWkPkq
alive_file = var_call_0JWY8UOz4rCrq4mtBgfMACmk

with open(cdh1_file) as f:
    cdh1 = json.load(f)
with open(alive_file) as f:
    alive = json.load(f)

cdh1_df = pd.DataFrame(cdh1)
alive_df = pd.DataFrame(alive)

# extract patient barcode from description, pattern 'patient TCGA-... ('
alive_df['ParticipantBarcode'] = alive_df['Patient_description'].str.extract(r'patient (TCGA-[A-Z0-9-]+)')

# BRCA cohort is Breast invasive carcinoma; restrict to those
# We already filtered by dataset text, so all are BRCA patients

# mark mutation status
cdh1_patients = set(cdh1_df['ParticipantBarcode'].unique())
alive_df['CDH1_mutated'] = alive_df['ParticipantBarcode'].isin(cdh1_patients)

# compute per-histological_type counts
summary = alive_df.groupby('histological_type')['CDH1_mutated'].agg(['mean','count', 'sum']).reset_index()
summary = summary[summary['count']>=1]
summary = summary.sort_values('mean', ascending=False)

# get top 3
top3 = summary.head(3)
result = []
for _, row in top3.iterrows():
    result.append({
        'histological_type': row['histological_type'],
        'cdh1_mutation_percentage': round(row['mean']*100,2),
        'n_alive_brca_patients': int(row['count']),
        'n_with_cdh1_mutation': int(row['sum'])
    })

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_RqvEzYWtKjvh87uk0NgWkPkq': 'file_storage/call_RqvEzYWtKjvh87uk0NgWkPkq.json', 'var_call_OHsV6nyUANPnfUI0lMKkDTI0': ['clinical_info'], 'var_call_WtZiUNMMwJdbGmB8i0MjviCN': 'file_storage/call_WtZiUNMMwJdbGmB8i0MjviCN.json', 'var_call_t4tnjBwe7MGwJaGtCowK6N6X': [], 'var_call_0JWY8UOz4rCrq4mtBgfMACmk': 'file_storage/call_0JWY8UOz4rCrq4mtBgfMACmk.json'}

exec(code, env_args)
