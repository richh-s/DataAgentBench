code = """import json
import re

# Access the clinical data from storage
clinical_data = locals()['var_functions.query_db:8']

# If it's a file path, read it
if isinstance(clinical_data, str) and 'json' in clinical_data:
    with open(clinical_data, 'r') as f:
        lgg_clinical = json.load(f)
else:
    lgg_clinical = clinical_data

# Extract patient barcodes and histology types
patient_data = []
for record in lgg_clinical:
    desc = record['Patient_description']
    hist_type = record['histological_type']
    
    # Extract TCGA barcode using regex
    match = re.search(r'(TCGA-\w+)', desc)
    if match:
        barcode = match.group(1)
        patient_data.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type
        })

print('__RESULT__:')
print(json.dumps(patient_data))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
