code = """import json
import re
import math

# Load data
clin_file = var_functions.query_db:12
expr_file = var_functions.query_db:28

with open(clin_file) as f:
    clinical_data = json.load(f)
with open(expr_file) as f:
    igf2_data = json.load(f)

# Extract LGG patient barcodes and histologies
def get_barcode(desc):
    m = re.search('TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    return m.group(0) if m else None

lgg_patients = {}
for rec in clinical_data:
    bc = get_barcode(rec['Patient_description'])
    if bc:
        hist = rec['histological_type']
        lgg_patients[bc] = hist

# Match with IGF2 expression
valid_data = []
for rec in igf2_data:
    bc = rec['ParticipantBarcode']
    if bc in lgg_patients:
        hist = lgg_patients[bc]
        # Skip if histology in brackets
        if hist.startswith('[') and hist.endswith(']'):
            continue
        try:
            expr = float(rec['normalized_count'])
            log_expr = math.log10(expr + 1)
            valid_data.append([hist, log_expr])
        except:
            continue

# Group by histology
from collections import defaultdict
hist_data = defaultdict(list)
for hist, log_expr in valid_data:
    hist_data[hist].append(log_expr)

# Calculate averages
averages = {}
for hist, values in hist_data.items():
    avg = sum(values) / len(values)
    averages[hist] = round(avg, 4)

# Prepare result
result = {
    'averages': averages,
    'patient_counts': {h: len(v) for h, v in hist_data.items()}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:26': {'total': 513, 'hist_counts': {'Oligodendroglioma': 189, 'Oligoastrocytoma': 130, 'Astrocytoma': 194}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
