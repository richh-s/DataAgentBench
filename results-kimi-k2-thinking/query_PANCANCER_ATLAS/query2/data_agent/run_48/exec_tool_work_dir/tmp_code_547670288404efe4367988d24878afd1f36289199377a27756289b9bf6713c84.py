code = """import json
import re

# Load BRCA clinical data
clinical_path = locals()['var_functions.query_db:22']
if isinstance(clinical_path, str) and '.json' in clinical_path:
    with open(clinical_path, 'r') as f:
        brca_clinical = json.load(f)
else:
    brca_clinical = clinical_path

print('BRCA records loaded:', len(brca_clinical))

# Filter alive BRCA patients and get their histological types
alive_brca = []
histology_counts = {}
participant_barcodes = []

for rec in brca_clinical:
    if 'Alive' in rec.get('Patient_description', ''):
        patient_id = rec.get('patient_id')
        hist_type = rec.get('histological_type')
        patient_desc = rec.get('Patient_description', '')
        
        alive_brca.append(rec)
        histology_counts[hist_type] = histology_counts.get(hist_type, 0) + 1
        
        # Extract participant barcode from description
        match = re.search(r'TCGA-[A-Z0-9]+-[A-Z0-9]+', patient_desc)
        if match:
            participant_barcodes.append(match.group())

print('Alive BRCA patients count:', len(alive_brca))
print('Histological types found:', len(histology_counts))
print('Sample participant barcodes:', participant_barcodes[:5])

# Print histology type distribution
sorted_histo = sorted(histology_counts.items(), key=lambda x: x[1], reverse=True)
for hist_type, count in sorted_histo:
    print(hist_type + ': ' + str(count))

result = {
    'total_brca': len(brca_clinical),
    'alive_brca': len(alive_brca),
    'histology_distribution': histology_counts,
    'participant_barcodes': participant_barcodes
}
print('__RESULT__:', json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'status': 'checked', 'records': 5}, 'var_functions.query_db:10': [], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'total_clinical': 50, 'brca_patients': 0, 'alive_brca': 0, 'histology_types': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
