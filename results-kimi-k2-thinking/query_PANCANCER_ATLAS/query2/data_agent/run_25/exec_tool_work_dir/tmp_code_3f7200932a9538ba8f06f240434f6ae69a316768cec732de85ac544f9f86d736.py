code = """import json
import re

# Read the clinical data for alive bladder cancer patients
with open('var_functions.query_db:18', 'r') as f:
    brca_clinical = json.load(f)

print('Total alive bladder cancer patients: ', len(brca_clinical))

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
            'histological_type': hist_type
        })

print('Successfully extracted barcodes for patients: ', len(patients_data))

# Count histological types
hist_type_counts = {}
for p in patients_data:
    ht = p['histological_type']
    hist_type_counts[ht] = hist_type_counts.get(ht, 0) + 1

print('Histological type distribution:')
for ht, count in hist_type_counts.items():
    print('  ' + str(ht) + ': ' + str(count))

# Export data for next step
result = {
    'total_patients': len(patients_data),
    'patients': patients_data,
    'hist_type_distribution': hist_type_counts
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
