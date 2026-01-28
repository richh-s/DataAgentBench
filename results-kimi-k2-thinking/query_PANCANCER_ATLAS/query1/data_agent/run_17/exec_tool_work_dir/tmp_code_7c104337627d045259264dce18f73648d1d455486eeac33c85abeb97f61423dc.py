code = """import json
import re
import math
from collections import defaultdict, Counter

print("Starting analysis...")

# Load LGG patients data
lgg_var = locals()['var_functions.query_db:14']
with open(lgg_var, 'r') as f:
    lgg_patients = json.load(f)

print(f"LGG patients loaded: {len(lgg_patients)}")

# Load IGF2 expression data
igf2_var = locals()['var_functions.query_db:22']
with open(igf2_var, 'r') as f:
    igf2_data = json.load(f)

print(f"IGF2 expression records: {len(igf2_data)}")

# Extract barcodes and filter histology
def extract_barcode(description):
    match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', description)
    return match.group() if match else None

lgg_map = {}
for patient in lgg_patients:
    desc = patient['Patient_description']
    histology = patient.get('histological_type', '')
    
    # Skip histology in square brackets
    if histology and histology.startswith('[') and histology.endswith(']'):
        continue
    
    barcode = extract_barcode(desc)
    if barcode and histology:
        lgg_map[barcode] = histology

print(f"LGG patients with valid histology: {len(lgg_map)}")

# Build IGF2 expression map (barcode -> expression)
igf2_map = {}
for rec in igf2_data:
    try:
        expr = float(rec['normalized_count'])
        igf2_map[rec['ParticipantBarcode']] = expr
    except:
        continue

print(f"Valid IGF2 expression records: {len(igf2_map)}")

# Match and compute log10 expression
matched = []
for barcode, histology in lgg_map.items():
    if barcode in igf2_map:
        expr = igf2_map[barcode]
        log_val = math.log10(expr + 1)
        matched.append((histology, log_val))

print(f"Matched LGG+IGF2 records: {len(matched)}")

# Group by histology
histology_groups = defaultdict(list)
for histology, log_val in matched:
    histology_groups[histology].append(log_val)

# Calculate averages
results = {}
for histology in sorted(histology_groups.keys()):
    values = histology_groups[histology]
    avg = sum(values) / len(values)
    results[histology] = {
        'average_log10_expression': round(avg, 4),
        'patient_count': len(values)
    }
    print(f"{histology}: {round(avg, 4)} (n={len(values)})")

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'count': 513, 'histologies': ['Oligodendroglioma', 'Oligoastrocytoma', 'Astrocytoma']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
