code = """import json
import re

# Load data
clinical_data = var_functions.query_db:30
cdh1_data = var_functions.query_db:42

if isinstance(clinical_data, str):
    with open(clinical_data) as f:
        alive_patients = json.load(f)
else:
    alive_patients = clinical_data

if isinstance(cdh1_data, str):
    with open(cdh1_data) as f:
        cdh1_muts = json.load(f)
else:
    cdh1_muts = cdh1_data

# Build mapping
alive_map = {}
for p in alive_patients:
    m = re.search(r'(TCGA-\w{2}-\w{4})', p['Patient_description'])
    if m:
        alive_map[m.group(1)] = p['histological_type']

cdh1_set = set([m['ParticipantBarcode'] for m in cdh1_muts])

# Get intersection
common = set(alive_map.keys()) & cdh1_set

# Count by histology
hist_stats = {}
for barcode, hist_type in alive_map.items():
    if hist_type not in hist_stats:
        hist_stats[hist_type] = {'total': 0, 'cdh1': 0}
    hist_stats[hist_type]['total'] += 1
    if barcode in common:
        hist_stats[hist_type]['cdh1'] += 1

# Calculate percentages
for h in hist_stats:
    hist_stats[h]['pct'] = (hist_stats[h]['cdh1'] / hist_stats[h]['total'] * 100) if hist_stats[h]['total'] > 0 else 0

result = json.dumps(hist_stats)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:10': [], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:16': {'alive_barcodes': ['TCGA-GD-A3OQ', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-K4-A6FZ', 'TCGA-ZF-A9RF', 'TCGA-DK-A6AV', 'TCGA-GD-A6C6', 'TCGA-GU-A766', 'TCGA-E7-A8O7', 'TCGA-GC-A4ZW', 'TCGA-G2-A2EK', 'TCGA-GV-A3JZ', 'TCGA-UY-A9PH', 'TCGA-UY-A78O', 'TCGA-DK-A1AC', 'TCGA-C4-A0F6', 'TCGA-KQ-A41O', 'TCGA-4Z-AA7M', 'TCGA-UY-A78L', 'TCGA-S5-AA26', 'TCGA-XF-A9T3', 'TCGA-E7-A678', 'TCGA-FT-A61P', 'TCGA-K4-A3WV', 'TCGA-GD-A3OP', 'TCGA-G2-A3VY', 'TCGA-FD-A5C1', 'TCGA-E7-A5KF', 'TCGA-DK-A2I1', 'TCGA-H4-A2HO'], 'total_alive': 30}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-XF-A9T3'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
