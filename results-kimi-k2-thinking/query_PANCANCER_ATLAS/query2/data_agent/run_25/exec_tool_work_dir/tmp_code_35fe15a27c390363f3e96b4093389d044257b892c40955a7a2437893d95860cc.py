code = """import json
import re

# Read the clinical data for alive bladder cancer patients
with open('var_functions.query_db:12', 'r') as f:
    brca_clinical = json.load(f)

print('Total alive bladder cancer patients: ' + str(len(brca_clinical)))

# Extract patient barcodes and histological types
patients_data = []
for record in brca_clinical:
    desc = record['Patient_description']
    hist_type = record['histological_type']
    
    # Extract TCGA barcode
    match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    if match:
        barcode = match.group()
        patients_data.append({
            'patient_barcode': barcode,
            'histological_type': hist_type,
            'description': desc
        })

print('Successfully extracted ' + str(len(patients_data)) + ' patient barcodes')
print('Sample patient data:')
for i in range(min(3, len(patients_data))):
    print('  ' + patients_data[i]['patient_barcode'] + ': ' + str(patients_data[i]['histological_type']))

# Get unique histological types
hist_types = {}
for p in patients_data:
    ht = p['histological_type']
    if ht not in hist_types:
        hist_types[ht] = []
    hist_types[ht].append(p['patient_barcode'])

print('\nUnique histological types (' + str(len(hist_types)) + '):')
for ht in hist_types:
    print('  ' + str(ht) + ': ' + str(len(hist_types[ht])) + ' patients')

# Store patient barcodes for later use
patient_barcodes = [p['patient_barcode'] for p in patients_data]

print('__RESULT__:')
print(json.dumps({
    'total_patients': len(patients_data),
    'histological_types_count': len(hist_types),
    'patient_barcodes': patient_barcodes,
    'hist_types_distribution': {ht: len(barcodes) for ht, barcodes in hist_types.items()}
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
