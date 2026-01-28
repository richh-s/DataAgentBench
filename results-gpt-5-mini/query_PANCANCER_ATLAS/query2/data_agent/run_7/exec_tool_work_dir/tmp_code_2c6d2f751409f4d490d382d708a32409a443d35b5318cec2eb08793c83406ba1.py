code = """import pandas as pd
import re
import json
import os

# keys from storage
clinical_key = 'var_call_BY39OuKbuoCF4EaoXZLMNMNL'
mut_key = 'var_call_vOm4Ac8AoJ6qWI0HdkMhuTdw'

# Helper to load variable which might be a filepath or already a list
def load_var(var):
    if isinstance(var, str) and os.path.exists(var) and var.lower().endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return var

clinical_data = load_var(var_call_BY39OuKbuoCF4EaoXZLMNMNL)
mut_data = load_var(var_call_vOm4Ac8AoJ6qWI0HdkMhuTdw)

clinical = pd.DataFrame(clinical_data)
mut = pd.DataFrame(mut_data)

# Extract ParticipantBarcode from Patient_description using regex
def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(TCGA[-A-Za-z0-9]+)', s)
    return m.group(1) if m else None

clinical['ParticipantBarcode'] = clinical['Patient_description'].apply(extract_barcode)
clinical = clinical.dropna(subset=['ParticipantBarcode'])
clinical_unique = clinical[['ParticipantBarcode','histological_type']].drop_duplicates(subset=['ParticipantBarcode'])

mutated_set = set(mut['ParticipantBarcode'].unique())

grouped = clinical_unique.groupby('histological_type').agg(total_patients=('ParticipantBarcode','nunique'),
                                                            patient_barcodes=('ParticipantBarcode', lambda x: list(x)))

rows = []
for hist, row in grouped.iterrows():
    barcodes = set(row['patient_barcodes'])
    mutated = len(barcodes & mutated_set)
    total = int(row['total_patients'])
    pct = (mutated / total * 100) if total>0 else 0.0
    rows.append({'histological_type': hist if pd.notna(hist) else None, 'total_patients': total, 'mutated_patients': mutated, 'percentage_mutated': round(pct,2)})

rows_sorted = sorted(rows, key=lambda x: (-x['percentage_mutated'], -x['mutated_patients']))
top3 = rows_sorted[:3]

print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_p2zG77b0kuRcRYiIIfJsn5tR': 'file_storage/call_p2zG77b0kuRcRYiIIfJsn5tR.json', 'var_call_YDGLHwxaE0Mm61p38X1AF3Wl': 'file_storage/call_YDGLHwxaE0Mm61p38X1AF3Wl.json', 'var_call_BY39OuKbuoCF4EaoXZLMNMNL': 'file_storage/call_BY39OuKbuoCF4EaoXZLMNMNL.json', 'var_call_vOm4Ac8AoJ6qWI0HdkMhuTdw': 'file_storage/call_vOm4Ac8AoJ6qWI0HdkMhuTdw.json'}

exec(code, env_args)
