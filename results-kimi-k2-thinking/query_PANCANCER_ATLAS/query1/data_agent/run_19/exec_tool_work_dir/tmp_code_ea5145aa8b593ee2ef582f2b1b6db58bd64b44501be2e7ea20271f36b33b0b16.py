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

# Extract patient barcodes and histology types with improved regex
patient_data = []
for record in lgg_clinical:
    desc = record['Patient_description']
    hist_type = record['histological_type']
    
    # Extract TCGA barcode using improved regex pattern
    # Pattern: TCGA-XX-XXXX (where X can be letters or numbers)
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]+)', desc)
    if match:
        barcode = match.group(1)
        patient_data.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type
        })

# Count unique patients and histology types
unique_patients = set([p['ParticipantBarcode'] for p in patient_data])
histology_counts = {}
for p in patient_data:
    hist = p['histological_type']
    histology_counts[hist] = histology_counts.get(hist, 0) + 1

result = {
    'total_records': len(patient_data),
    'unique_patients': len(unique_patients),
    'histology_counts': histology_counts,
    'sample_patients': patient_data[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)
