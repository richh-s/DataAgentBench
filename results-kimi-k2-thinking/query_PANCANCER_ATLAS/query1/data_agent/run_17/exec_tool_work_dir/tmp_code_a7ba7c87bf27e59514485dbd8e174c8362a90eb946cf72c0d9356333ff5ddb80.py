code = """import json
import re
import math

# Read the files provided from previous queries
lgg_file = locals()['var_functions.query_db:14']
with open(lgg_file, 'r') as f:
    lgg_patients = json.load(f)

igf2_file = locals()['var_functions.query_db:22']  
with open(igf2_file, 'r') as f:
    igf2_data = json.load(f)

print(f"LGG patients: {len(lgg_patients)}")
print(f"IGF2 expression records: {len(igf2_data)}")

# Extract barcodes from Patient_description
def extract_barcode(description):
    match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', description)
    return match.group() if match else None

# Build LGG patient mapping: barcode -> histological_type
lgg_patients_map = {}
for patient in lgg_patients:
    desc = patient['Patient_description']
    histology = patient.get('histological_type', '')
    
    # Skip histology values enclosed in square brackets
    if histology and histology.startswith('[') and histology.endswith(']'):
        continue
    
    barcode = extract_barcode(desc)
    if barcode and histology:
        lgg_patients_map[barcode] = histology

print(f"LGG patients with valid histology: {len(lgg_patients_map)}")

# Build IGF2 expression map: barcode -> expression value
# Note: some normalized_count values may be strings
igf2_map = {}
for record in igf2_data:
    barcode = record['ParticipantBarcode']
    # Convert to float, handling string values
    try:
        expr = float(record['normalized_count'])
        igf2_map[barcode] = expr
    except (ValueError, TypeError):
        continue

print(f"IGF2 expression records (valid): {len(igf2_map)}")

# Match LGG patients with IGF2 expression
matched_data = []
for barcode, histology in lgg_patients_map.items():
    if barcode in igf2_map:
        expr = igf2_map[barcode]
        log_expr = math.log10(expr + 1)
        matched_data.append({
            'ParticipantBarcode': barcode,
            'histological_type': histology, 
            'normalized_count': expr,
            'log10_expr': log_expr
        })

print(f"Matched LGG patients with IGF2 expression: {len(matched_data)}")

# Group by histology and compute average log10 expression
from collections import defaultdict
histology_groups = defaultdict(list)
for record in matched_data:
    histology_groups[record['histological_type']].append(record['log10_expr'])

results = {}
for histology, log_values in sorted(histology_groups.items()):
    avg_log = sum(log_values) / len(log_values)
    results[histology] = {
        'average_log10_expression': round(avg_log, 4),
        'patient_count': len(log_values)
    }

print('\nResults:')
for histology, stats in results.items():
    print(f"{histology}: {stats['average_log10_expression']} (n={stats['patient_count']})")

# Return final results as JSON
print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'count': 513, 'histologies': ['Oligodendroglioma', 'Oligoastrocytoma', 'Astrocytoma']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
