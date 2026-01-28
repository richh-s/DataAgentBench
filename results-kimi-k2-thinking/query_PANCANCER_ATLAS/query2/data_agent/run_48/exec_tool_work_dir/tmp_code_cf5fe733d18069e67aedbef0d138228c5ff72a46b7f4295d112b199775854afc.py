code = """import json

# Load clinical data
clinical_path = locals()['var_functions.query_db:14']
if isinstance(clinical_path, str) and '.json' in clinical_path:
    with open(clinical_path, 'r') as f:
        clinical_data = json.load(f)
else:
    clinical_data = clinical_path

print('Loaded', len(clinical_data), 'clinical records')

# Find BRCA patients (breast cancer) by analyzing Patient_description
brca_patients = []
for rec in clinical_data:
    desc = rec['Patient_description']
    desc_lower = desc.lower()
    # Check for BRCA mentions (breast cancer or BRCA acronym)
    if 'breast' in desc_lower or 'brca' in desc_lower:
        brca_patients.append(rec)

print('Found', len(brca_patients), 'potential BRCA patients')

# Filter alive BRCA patients
alive_brca = []
for rec in brca_patients:
    if 'alive' in rec['Patient_description'].lower():
        alive_brca.append(rec)

print('Alive BRCA patients:', len(alive_brca))

# Show histological types for alive BRCA patients
histology_counts = {}
for rec in alive_brca:
    hist_type = rec['histological_type']
    histology_counts[hist_type] = histology_counts.get(hist_type, 0) + 1

print('Histological types in alive BRCA:')
for hist, count in sorted(histology_counts.items(), key=lambda x: x[1], reverse=True):
    print('  ', hist, ':', count)

result = {'total_clinical': len(clinical_data), 'brca_patients': len(brca_patients), 'alive_brca': len(alive_brca), 'histology_types': len(histology_counts)}
print('__RESULT__:', json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'status': 'checked', 'records': 5}, 'var_functions.query_db:10': [], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
