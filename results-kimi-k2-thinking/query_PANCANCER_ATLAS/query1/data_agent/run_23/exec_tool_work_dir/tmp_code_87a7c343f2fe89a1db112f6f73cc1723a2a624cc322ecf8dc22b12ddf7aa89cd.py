code = """import json
import re
import math

# Load LGG patients mapping from clinical data
clin_path = locals()['var_functions.query_db:12']
with open(clin_path, 'r') as f:
    lgg_records = json.load(f)

# Create mapping of TCGA barcode to histology type
# Only include valid histology annotations (not enclosed in square brackets)
barcode_to_histology = {}
for record in lgg_records:
    patient_desc = record.get('Patient_description', '')
    histology = record.get('histological_type', '')
    
    # Check if histology is valid (not in square brackets like [Not Applicable], etc.)
    if histology and not (histology.startswith('[') and histology.endswith(']')):
        # Extract barcode - look for TCGA-XX-XXXX pattern
        match = re.search(r'(TCGA-\w{2}-[\w\d]{4})', patient_desc)
        if match:
            barcode = match.group(1)
            barcode_to_histology[barcode] = histology

# Load IGF2 expression data
igf2_path = locals()['var_functions.query_db:16']
with open(igf2_path, 'r') as f:
    igf2_records = json.load(f)

# Filter IGF2 expression for LGG patients only and compute log10(normalized_count + 1)
histology_values = {}
for record in igf2_records:
    barcode = record.get('ParticipantBarcode')
    if barcode in barcode_to_histology:
        histology = barcode_to_histology[barcode]
        try:
            # Get normalized count and convert to float
            norm_count = float(record.get('normalized_count', 0))
            # Compute log10(normalized_count + 1) to avoid log10(0)
            log_value = math.log10(norm_count + 1)
            
            if histology not in histology_values:
                histology_values[histology] = []
            histology_values[histology].append(log_value)
        except (ValueError, TypeError):
            # Skip invalid values
            continue

# Compute average log10-transformed expression for each histology type
results = {}
for histology, values in histology_values.items():
    if values:  # Only include histologies with valid expression data
        avg_log = sum(values) / len(values)
        results[histology] = round(avg_log, 4)

# Sort results by histology type alphabetically
sorted_results = dict(sorted(results.items()))

print('__RESULT__:')
print(json.dumps({
    'total_lgg_patients_with_igf2': len(barcode_to_histology),
    'lgg_patients_with_igf2_data': sum(len(v) for v in histology_values.values()),
    'histology_counts': {h: len(v) for h, v in histology_values.items()},
    'average_log10_expression': sorted_results
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'LXN', 'Entrez': '56925', 'normalized_count': '69.7259'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'ZNF770', 'Entrez': '54989', 'normalized_count': '1195.92'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'AMELY', 'Entrez': '266', 'normalized_count': '0.0'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'TPTE2P1', 'Entrez': '646405', 'normalized_count': '214.576'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'ITGB3', 'Entrez': '3690', 'normalized_count': '13.6303'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'patient_count': 513, 'sample_patients': [['TCGA-RY-A83X', 'Oligodendroglioma'], ['TCGA-FG-A60K', 'Oligoastrocytoma'], ['TCGA-DB-A4XH', 'Oligoastrocytoma'], ['TCGA-DB-A4XE', 'Oligoastrocytoma'], ['TCGA-DB-A4XC', 'Oligoastrocytoma']]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
