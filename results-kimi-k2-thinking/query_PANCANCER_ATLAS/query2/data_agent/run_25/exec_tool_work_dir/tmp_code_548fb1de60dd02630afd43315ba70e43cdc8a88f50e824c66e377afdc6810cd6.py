code = """import json
import re

# Read the clinical data for alive bladder cancer patients
clinical_file_path = locals()['var_functions.query_db:26']
with open(clinical_file_path, 'r') as f:
    brca_clinical = json.load(f)

# Read CDH1 mutation data
mutations_file_path = locals()['var_functions.query_db:22']
with open(mutations_file_path, 'r') as f:
    cdh1_mutations = json.load(f)

print('Total alive bladder cancer patients from clinical data: ' + str(len(brca_clinical)))
print('Total CDH1 mutations found: ' + str(len(cdh1_mutations)))

# Extract patient barcodes and histological types from clinical data
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

# Get unique patient barcodes with CDH1 mutations
cdh1_mutated_barcodes = set()
for mutation in cdh1_mutations:
    cdh1_mutated_barcodes.add(mutation['ParticipantBarcode'])

print('Successfully processed ' + str(len(patients_data)) + ' clinical records')
print('Found ' + str(len(cdh1_mutated_barcodes)) + ' unique patients with CDH1 mutations')

# Group patients by histological type and calculate CDH1 mutation rates
hist_type_stats = {}
for patient in patients_data:
    ht = patient['histological_type']
    barcode = patient['patient_barcode']
    
    if ht not in hist_type_stats:
        hist_type_stats[ht] = {'total': 0, 'mutated': 0, 'patients': []}
    
    hist_type_stats[ht]['total'] += 1
    hist_type_stats[ht]['patients'].append(barcode)
    
    if barcode in cdh1_mutated_barcodes:
        hist_type_stats[ht]['mutated'] += 1

# Calculate percentages and find top 3 histological types
results = []
for ht, stats in hist_type_stats.items():
    percentage = (stats['mutated'] / stats['total'] * 100) if stats['total'] > 0 else 0
    results.append({
        'histological_type': ht,
        'total_patients': stats['total'],
        'mutated_patients': stats['mutated'],
        'cdh1_mutation_percentage': round(percentage, 2)
    })

# Sort by percentage descending, then by total patients
top_3 = sorted(results, key=lambda x: (-x['cdh1_mutation_percentage'], -x['total_patients']))[:3]

print('Top 3 histological types by CDH1 mutation percentage:')
for i, result in enumerate(top_3, 1):
    print('  ' + str(i) + '. ' + str(result['histological_type']) + ' - ' + str(result['cdh1_mutation_percentage']) + '% (' + str(result['mutated_patients']) + '/' + str(result['total_patients']) + ')')

print('__RESULT__:')
print(json.dumps(top_3))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
