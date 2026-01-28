code = """import json
import re
import pandas as pd
from collections import Counter, defaultdict

# Load BRCA clinical data
clinical_path = vars()['var_functions.query_db:24']
if isinstance(clinical_path, str) and clinical_path.endswith('.json'):
    with open(clinical_path, 'r') as f:
        clinical_data = json.load(f)
else:
    clinical_data = clinical_path

# Load CDH1 mutation data
mutation_path = vars()['var_functions.query_db:30']
if isinstance(mutation_path, str) and mutation_path.endswith('.json'):
    with open(mutation_path, 'r') as f:
        mutation_data = json.load(f)
else:
    mutation_data = mutation_path

print('Loaded', len(clinical_data), 'BRCA clinical records')
print('Loaded', len(mutation_data), 'CDH1 mutation records')

# Extract BRCA patient data with barcodes, histological types, and vital status
brca_patients = []
for record in clinical_data:
    patient_desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', 'Unknown')
    
    # Extract barcode and vital status
    barcode_match = re.search(r'(TCGA[\-\w]+)', patient_desc)
    vital_match = re.search(r'vital status[\s:]*([Aa]live|[Dd]ead)', patient_desc)
    
    if barcode_match:
        barcode = barcode_match.group(1)
        vital_status = vital_match.group(1).lower() if vital_match else 'unknown'
        brca_patients.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type,
            'vital_status': vital_status
        })

# Get unique CDH1 mutation barcodes
cdh1_barcodes = set()
for record in mutation_data:
    cdh1_barcodes.add(record['ParticipantBarcode'])

print('Extracted', len(brca_patients), 'BRCA patients')
print('Found', len(cdh1_barcodes), 'unique patients with CDH1 mutations')

# Filter for alive BRCA patients
alive_brca_patients = [p for p in brca_patients if p['vital_status'] == 'alive']
print('Found', len(alive_brca_patients), 'alive BRCA patients')

# Analyze by histological type
hist_type_stats = defaultdict(lambda: {'total': 0, 'cdh1_mutated': 0, 'percent': 0.0})

for patient in alive_brca_patients:
    hist_type = patient['histological_type']
    barcode = patient['ParticipantBarcode']
    
    hist_type_stats[hist_type]['total'] += 1
    if barcode in cdh1_barcodes:
        hist_type_stats[hist_type]['cdh1_mutated'] += 1

# Calculate percentages
for hist_type, stats in hist_type_stats.items():
    stats['percent'] = (stats['cdh1_mutated'] / stats['total'] * 100) if stats['total'] > 0 else 0

# Convert to list for sorting
results = []
for hist_type, stats in hist_type_stats.items():
    results.append({
        'histological_type': hist_type,
        'total_patients': stats['total'],
        'cdh1_mutated': stats['cdh1_mutated'],
        'mutation_percentage': round(stats['percent'], 2)
    })

# Sort by mutation percentage
results_sorted = sorted(results, key=lambda x: x['mutation_percentage'], reverse=True)

print('\nAll histological types (sorted by mutation %):')
for r in results_sorted:
    print(f"{r['histological_type']}: {r['cdh1_mutated']}/{r['total_patients']} ({r['mutation_percentage']}%)")

# Get top 3
top_3 = results_sorted[:3]
print('\nTop 3 histological types:')
for i, r in enumerate(top_3, 1):
    print(f"{i}. {r['histological_type']}: {r['mutation_percentage']}% (n={r['total_patients']})")

# Save results
with open('/tmp/analysis_results.json', 'w') as f:
    json.dump({
        'all_results': results_sorted,
        'top_3': top_3
    }, f, indent=2)

result = {
    'all_histological_types': len(results_sorted),
    'top_3': top_3
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'storage_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:4']}, 'var_functions.query_db:14': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'total_patients': 412, 'alive_patients': 77}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
