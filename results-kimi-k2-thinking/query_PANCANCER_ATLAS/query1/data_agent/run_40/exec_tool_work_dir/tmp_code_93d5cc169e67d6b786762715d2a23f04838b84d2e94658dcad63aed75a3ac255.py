code = """import json, re, math
from collections import defaultdict

# Load clinical data
clin_file = locals()['var_functions.query_db:12']
with open(clin_file) as f:
    clinical_data = json.load(f)

# Load expression data
expr_file = locals()['var_functions.query_db:28']
with open(expr_file) as f:
    expression_data = json.load(f)

# Extract barcodes and histologies for LGG patients
barcode_to_histology = {}
for rec in clinical_data:
    desc = rec['Patient_description']
    hist = rec['histological_type']
    m = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    if m:
        barcode_to_histology[m.group(0)] = hist

# Filter IGF2 expression for LGG patients and compute log10 values
histology_values = defaultdict(list)
count_total = 0
count_skipped = 0

for rec in expression_data:
    barcode = rec['ParticipantBarcode']
    if barcode in barcode_to_histology:
        histology = barcode_to_histology[barcode]
        # Skip histologies in square brackets
        if histology.startswith('[') and histology.endswith(']'):
            count_skipped += 1
            continue
        try:
            expr = float(rec['normalized_count'])
            log_expr = math.log10(expr + 1)
            histology_values[histology].append(log_expr)
            count_total += 1
        except (ValueError, TypeError):
            continue

# Calculate averages
averages = {}
for hist, values in histology_values.items():
    avg = sum(values) / len(values) if values else 0
    averages[hist] = round(avg, 4)

# Prepare result
result = {
    'averages': averages,
    'sample_counts': {h: len(v) for h, v in histology_values.items()},
    'total_samples': count_total,
    'skipped_samples': count_skipped
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:26': {'total': 513, 'hist_counts': {'Oligodendroglioma': 189, 'Oligoastrocytoma': 130, 'Astrocytoma': 194}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
