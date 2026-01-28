code = """import json
import re
import math

# Load clinical data (LGG patients)
clin_file = var_functions.query_db:12
with open(clin_file) as f:
    clinical_data = json.load(f)

# Load IGF2 expression data
expr_file = var_functions.query_db:28
with open(expr_file) as f:
    igf2_data = json.load(f)

print('Clinical records: ' + str(len(clinical_data)))
print('IGF2 expression records: ' + str(len(igf2_data)))

# Extract barcodes from clinical data
def extract_barcode(desc):
    match = re.search(r'TCGA-\w{2}-\w{4}', desc)
    return match.group(0) if match else None

clinical_barcodes = {}
for rec in clinical_data:
    barcode = extract_barcode(rec['Patient_description'])
    if barcode:
        histology = rec['histological_type']
        clinical_barcodes[barcode] = histology

print('Clinical barcodes extracted: ' + str(len(clinical_barcodes)))

# Filter IGF2 data for LGG patients and valid histology
filtered_data = []
for rec in igf2_data:
    barcode = rec['ParticipantBarcode']
    if barcode in clinical_barcodes:
        histology = clinical_barcodes[barcode]
        # Check if histology is not enclosed in square brackets
        if not (histology.startswith('[') and histology.endswith(']')):
            try:
                expr_val = float(rec['normalized_count'])
                filtered_data.append({
                    'barcode': barcode,
                    'histology': histology,
                    'expression': expr_val
                })
            except ValueError:
                continue

print('Filtered records (IGF2 in LGG patients): ' + str(len(filtered_data)))

# Group by histology and compute averages
histology_groups = {}
for rec in filtered_data:
    h = rec['histology']
    if h not in histology_groups:
        histology_groups[h] = []
    # Compute log10(expression + 1)
    log_val = math.log10(rec['expression'] + 1)
    histology_groups[h].append(log_val)

# Calculate averages
averages = {}
for histology, values in histology_groups.items():
    avg = sum(values) / len(values)
    averages[histology] = avg

# Print results with 4 decimal places
print('\nAverage log10(IGF2+1) by histology:')
for histology in sorted(averages.keys()):
    print(f"{histology}: {averages[histology]:.4f}")

result_dict = {
    'averages': {h: round(v, 4) for h, v in averages.items()},
    'total_patients': len(filtered_data),
    'histology_counts': {h: len(vals) for h, vals in histology_groups.items()}
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:26': {'total': 513, 'hist_counts': {'Oligodendroglioma': 189, 'Oligoastrocytoma': 130, 'Astrocytoma': 194}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
