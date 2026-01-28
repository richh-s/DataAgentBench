code = """import json
import re
import pandas as pd

# Load BRCA clinical data
clinical_data = []
clinical_path = var_functions.query_db:4
if isinstance(clinical_path, str) and clinical_path.endswith('.json'):
    with open(clinical_path, 'r') as f:
        clinical_data = json.load(f)
else:
    clinical_data = clinical_path

print('Loaded', len(clinical_data), 'BRCA clinical records')

# Extract barcode and histological type for alive BRCA patients
patients = []
for record in clinical_data:
    patient_desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', 'Unknown')
    
    # Extract TCGA barcode
    match = re.search(r'(TCGA[\-\w]+)', patient_desc)
    if match:
        barcode = match.group(1)
        patients.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type
        })

print('Extracted', len(patients), 'BRCA patients with barcodes')

# Save to use in next step
with open('/tmp/brca_patients.json', 'w') as f:
    json.dump(patients, f)

print('Saved barcodes to /tmp/brca_patients.json')
print('Sample barcodes:', patients[:3])

result = {'status': 'success', 'patient_count': len(patients)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'storage_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:4']}}

exec(code, env_args)
