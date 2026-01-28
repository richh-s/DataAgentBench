code = """import json
import re

# Load data from storage
clinical_data = var_functions.query_db:30
cdh1_data = var_functions.query_db:42

# Parse clinical data
if isinstance(clinical_data, str):
    with open(clinical_data) as f:
        alive_patients = json.load(f)
else:
    alive_patients = clinical_data

# Parse CDH1 data
if isinstance(cdh1_data, str):
    with open(cdh1_data) as f:
        cdh1_muts = json.load(f)
else:
    cdh1_muts = cdh1_data

# Extract alive BRCA info
alive_barcodes = {}
for p in alive_patients:
    m = re.search(r'(TCGA-\w{2}-\w{4})', p['Patient_description'])
    if m:
        barcode = m.group(1)
        hist = p['histological_type']
        alive_barcodes[barcode] = hist

# Get CDH1 mutation barcodes
cdh1_set = set([m['ParticipantBarcode'] for m in cdh1_muts])

# Find common barcodes
common = set(alive_barcodes.keys()).intersection(cdh1_set)

print('Alive BRCA:', len(alive_barcodes))
print('CDH1 mutations:', len(cdh1_set))
print('Common:', len(common))

# Count by histology
hist_counts = {}
for barcode, hist in alive_barcodes.items():
    if hist not in hist_counts:
        hist_counts[hist] = {'total': 0, 'cdh1': 0}
    hist_counts[hist]['total'] += 1
    if barcode in cdh1_set:
        hist_counts[hist]['cdh1'] += 1

# Calculate percentages
for hist, counts in hist_counts.items():
    if counts['total'] > 0:
        counts['percentage'] = (counts['cdh1'] / counts['total']) * 100
    else:
        counts['percentage'] = 0

print('Histology counts:', hist_counts)

result = json.dumps(hist_counts)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:10': [], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:16': {'alive_barcodes': ['TCGA-GD-A3OQ', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-K4-A6FZ', 'TCGA-ZF-A9RF', 'TCGA-DK-A6AV', 'TCGA-GD-A6C6', 'TCGA-GU-A766', 'TCGA-E7-A8O7', 'TCGA-GC-A4ZW', 'TCGA-G2-A2EK', 'TCGA-GV-A3JZ', 'TCGA-UY-A9PH', 'TCGA-UY-A78O', 'TCGA-DK-A1AC', 'TCGA-C4-A0F6', 'TCGA-KQ-A41O', 'TCGA-4Z-AA7M', 'TCGA-UY-A78L', 'TCGA-S5-AA26', 'TCGA-XF-A9T3', 'TCGA-E7-A678', 'TCGA-FT-A61P', 'TCGA-K4-A3WV', 'TCGA-GD-A3OP', 'TCGA-G2-A3VY', 'TCGA-FD-A5C1', 'TCGA-E7-A5KF', 'TCGA-DK-A2I1', 'TCGA-H4-A2HO'], 'total_alive': 30}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-XF-A9T3'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
