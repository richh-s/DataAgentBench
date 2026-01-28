code = """import pandas as pd
import re
import json
# Load data from previous tool calls
clinical = pd.DataFrame(var_call_BY39OuKbuoCF4EaoXZLMNMNL)
mut = pd.DataFrame(var_call_vOm4Ac8AoJ6qWI0HdkMhuTdw)
# Extract ParticipantBarcode from Patient_description using regex
def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(TCGA[-A-Za-z0-9]+)', s)
    return m.group(1) if m else None

clinical['ParticipantBarcode'] = clinical['Patient_description'].apply(extract_barcode)
# Drop rows without barcode
clinical = clinical.dropna(subset=['ParticipantBarcode'])
# Ensure unique patients by ParticipantBarcode and keep histological_type
clinical_unique = clinical[['ParticipantBarcode','histological_type']].drop_duplicates(subset=['ParticipantBarcode'])
# Create set of mutated participant barcodes (unique)
mutated_set = set(mut['ParticipantBarcode'].unique())
# Group by histological_type and compute totals and mutated counts
grouped = clinical_unique.groupby('histological_type').agg(total_patients=('ParticipantBarcode','nunique'),
                                                            patient_barcodes=('ParticipantBarcode', lambda x: list(x)))

rows = []
for hist, row in grouped.iterrows():
    barcodes = set(row['patient_barcodes'])
    mutated = len(barcodes & mutated_set)
    total = int(row['total_patients'])
    pct = (mutated / total * 100) if total>0 else 0.0
    rows.append({'histological_type': hist, 'total_patients': total, 'mutated_patients': mutated, 'percentage_mutated': round(pct,2)})

# Sort by percentage_mutated desc, then by mutated_patients desc
rows_sorted = sorted(rows, key=lambda x: (-x['percentage_mutated'], -x['mutated_patients']))
# Take top 3
top3 = rows_sorted[:3]
result = json.dumps(top3)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_p2zG77b0kuRcRYiIIfJsn5tR': 'file_storage/call_p2zG77b0kuRcRYiIIfJsn5tR.json', 'var_call_YDGLHwxaE0Mm61p38X1AF3Wl': 'file_storage/call_YDGLHwxaE0Mm61p38X1AF3Wl.json', 'var_call_BY39OuKbuoCF4EaoXZLMNMNL': 'file_storage/call_BY39OuKbuoCF4EaoXZLMNMNL.json', 'var_call_vOm4Ac8AoJ6qWI0HdkMhuTdw': 'file_storage/call_vOm4Ac8AoJ6qWI0HdkMhuTdw.json'}

exec(code, env_args)
