code = """import json
import re
import math

# Access the clinical data from storage
clinical_data = locals()['var_functions.query_db:8']

# If it's a file path, read it
if isinstance(clinical_data, str) and 'json' in clinical_data:
    with open(clinical_data, 'r') as f:
        lgg_clinical = json.load(f)
else:
    lgg_clinical = clinical_data

# Extract patient barcodes and histology types with improved regex
patient_data = []
for record in lgg_clinical:
    desc = record['Patient_description']
    hist_type = record['histological_type']
    
    # Extract TCGA barcode using improved regex pattern
    # Pattern: TCGA-XX-XXXX or TCGA-XX-XXXXX (can have variable length after second dash)
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]+)', desc)
    if match:
        barcode = match.group(1)
        patient_data.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type
        })

# Access the molecular data from storage  
molecular_data = locals()['var_functions.query_db:16']

# If it's a file path, read it
if isinstance(molecular_data, str) and 'json' in molecular_data:
    with open(molecular_data, 'r') as f:
        igf2_expression = json.load(f)
else:
    igf2_expression = molecular_data

# Convert to dictionary for easier lookup
expression_dict = {}
for record in igf2_expression:
    barcode = record['ParticipantBarcode']
    # Convert normalized_count to float, handle missing/invalid values
    try:
        expr_val = float(record['normalized_count'])
        expression_dict[barcode] = expr_val
    except (ValueError, TypeError):
        expression_dict[barcode] = None

# Merge clinical and molecular data
merged_data = []
for patient in patient_data:
    barcode = patient['ParticipantBarcode']
    expr_val = expression_dict.get(barcode)
    
    # Only include patients with valid expression values
    if expr_val is not None and not math.isnan(expr_val):
        log_expr = math.log10(expr_val + 1)  # log10(normalized_count + 1)
        merged_data.append({
            'ParticipantBarcode': barcode,
            'histological_type': patient['histological_type'],
            'normalized_count': expr_val,
            'log10_expr': log_expr
        })

# Group by histological type and compute averages
from collections import defaultdict
histology_stats = defaultdict(list)
for record in merged_data:
    hist_type = record['histological_type']
    histology_stats[hist_type].append(record['log10_expr'])

# Compute averages
results = {}
for hist_type, log_exprs in histology_stats.items():
    if log_exprs:  # Ensure list is not empty
        avg_log_expr = sum(log_exprs) / len(log_exprs)
        results[hist_type] = {
            'average_log10_expr': round(avg_log_expr, 4),
            'sample_count': len(log_exprs)
        }

# Sort by histological type for consistent output
sorted_results = dict(sorted(results.items()))

final_output = {
    'histology_averages': sorted_results,
    'total_patients_with_data': len(merged_data),
    'total_unique_histologies': len(results)
}

print('__RESULT__:')
print(json.dumps(final_output, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': {'total_records': 513, 'unique_patients': 513, 'histology_counts': {'Oligodendroglioma': 189, 'Oligoastrocytoma': 130, 'Astrocytoma': 194}, 'sample_patients': [{'ParticipantBarcode': 'TCGA-RY-A83X', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-FG-A60K', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XH', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XE', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XC', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-P5-A5F0', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-S9-A6U1', 'histological_type': 'Astrocytoma'}, {'ParticipantBarcode': 'TCGA-TM-A7C3', 'histological_type': 'Astrocytoma'}, {'ParticipantBarcode': 'TCGA-S9-A7R2', 'histological_type': 'Astrocytoma'}, {'ParticipantBarcode': 'TCGA-TM-A84R', 'histological_type': 'Oligodendroglioma'}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
