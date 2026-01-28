code = """import json

# Load the clinical data
result_path = locals()['var_functions.query_db:14']
if isinstance(result_path, str) and '.json' in result_path:
    with open(result_path, 'r') as f:
        clinical_data = json.load(f)
else:
    clinical_data = result_path

print(f'Loaded {len(clinical_data)} clinical records')

# Check for BRCA cases by looking for TCGA barcode patterns
cancer_types_counts = {}
alive_cancer_types = {}

for record in clinical_data:
    desc = record['Patient_description']
    desc_lower = desc.lower()
    
    # Count histological types
    hist_type = record['histological_type']
    cancer_types_counts[hist_type] = cancer_types_counts.get(hist_type, 0) + 1
    
    # Check if alive
    if 'alive' in desc_lower:
        alive_cancer_types[hist_type] = alive_cancer_types.get(hist_type, 0) + 1

print(f'\nTotal cancer type counts: {len(cancer_types_counts)}')
print(f'\nTop histological types:')
sorted_by_count = sorted(cancer_types_counts.items(), key=lambda x: x[1], reverse=True)
for hist_type, count in sorted_by_count[:10]:
    alive_count = alive_cancer_types.get(hist_type, 0)
    print(f'  {hist_type}: {count} total, {alive_count} alive')

# Find BRCA patterns - looking for specific TCGA codes
brca_potential = []
for record in clinical_data:
    desc = record['Patient_description']
    # Look for BRCA TCGA barcodes (breast cancer)
    if 'TCGA' in desc and ('breast' in desc.lower() or 'BRCA' in desc):
        brca_potential.append(record)

print(f'\nPotential BRCA records found: {len(brca_potential)}')
if brca_potential:
    for rec in brca_potential[:3]:
        print(f'  - {rec["Patient_description"][:100]}...')

print('__RESULT__:', json.dumps({'total_records': len(clinical_data), 'brca_candidates': len(brca_potential)}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'status': 'checked', 'records': 5}, 'var_functions.query_db:10': [], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
