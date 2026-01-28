code = """import json

# Load BRCA clinical data
clinical_path = locals()['var_functions.query_db:22']
if isinstance(clinical_path, str) and '.json' in clinical_path:
    with open(clinical_path, 'r') as f:
        brca_clinical = json.load(f)
else:
    brca_clinical = clinical_path

print(f'Loaded {len(brca_clinical)} BRCA clinical records')

# Process records to find alive patients and histological types
alive_brca_patients = []
histology_type_counts = {}

for rec in brca_clinical:
    # Check if patient is alive
    if 'Alive' in rec['Patient_description']:
        patient_id = rec['patient_id']
        hist_type = rec['histological_type']
        
        alive_brca_patients.append({
            'patient_id': patient_id,
            'histological_type': hist_type,
            'patient_description': rec['Patient_description']
        })
        
        histology_type_counts[hist_type] = histology_type_counts.get(hist_type, 0) + 1

print(f'Alive BRCA patients: {len(alive_brca_patients)}')
print(f'Histological types found: {len(histology_type_counts)}')

# Show top histological types
print('\nTop histological types among alive BRCA patients:')
sorted_histo = sorted(histology_type_counts.items(), key=lambda x: x[1], reverse=True)
for hist_type, count in sorted_histo:
    print(f'  {hist_type}: {count} patients')

# Extract participant barcodes from patient descriptions
import re

for i, patient in enumerate(alive_brca_patients[:5]):
    desc = patient['patient_description']
    # Look for TCGA barcode pattern
    match = re.search(r'TCGA-[A-Z0-9]+-[A-Z0-9]+', desc)
    if match:
        patient['participant_barcode'] = match.group()
    else:
        patient['participant_barcode'] = None
    print(f"Patient {i+1}: {patient['participant_barcode']} - {patient['histological_type']}")

result = {
    'total_brca': len(brca_clinical),
    'alive_brca': len(alive_brca_patients),
    'histology_types': histology_type_counts
}
print('__RESULT__:', json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'status': 'checked', 'records': 5}, 'var_functions.query_db:10': [], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'total_clinical': 50, 'brca_patients': 0, 'alive_brca': 0, 'histology_types': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
