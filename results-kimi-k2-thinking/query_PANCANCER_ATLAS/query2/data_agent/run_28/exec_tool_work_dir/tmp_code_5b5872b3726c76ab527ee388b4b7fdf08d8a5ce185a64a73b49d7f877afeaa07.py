code = """import json
import re

# Load alive BRCA patients data
clinical_data = var_functions.query_db:30
if isinstance(clinical_data, str):
    with open(clinical_data, 'r') as f:
        alive_brca_patients = json.load(f)
else:
    alive_brca_patients = clinical_data

print(f"Loaded {len(alive_brca_patients)} alive BRCA patients")

# Create dictionary to store barcode -> histological_type
alive_brca_info = {}
histology_counts = {}

for patient in alive_brca_patients:
    desc = patient['Patient_description']
    hist_type = patient['histological_type']
    
    # Extract barcode
    barcode_match = re.search(r'(TCGA-\w{2}-\w{4})', desc)
    if barcode_match:
        barcode = barcode_match.group(1)
        alive_brca_info[barcode] = hist_type
        
        # Count histological types
        if hist_type not in histology_counts:
            histology_counts[hist_type] = {'total': 0, 'barcodes': []}
        histology_counts[hist_type]['total'] += 1
        histology_counts[hist_type]['barcodes'].append(barcode)

print(f"Total patients with extractable barcodes: {len(alive_brca_info)}")
print("\nHistological type distribution:")
for hist_type, data in histology_counts.items():
    print(f"  {hist_type}: {data['total']} patients")

result = {
    'total_patients': len(alive_brca_info),
    'barcode_to_histology': alive_brca_info,
    'histology_counts': histology_counts
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:10': [], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:16': {'alive_barcodes': ['TCGA-GD-A3OQ', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-K4-A6FZ', 'TCGA-ZF-A9RF', 'TCGA-DK-A6AV', 'TCGA-GD-A6C6', 'TCGA-GU-A766', 'TCGA-E7-A8O7', 'TCGA-GC-A4ZW', 'TCGA-G2-A2EK', 'TCGA-GV-A3JZ', 'TCGA-UY-A9PH', 'TCGA-UY-A78O', 'TCGA-DK-A1AC', 'TCGA-C4-A0F6', 'TCGA-KQ-A41O', 'TCGA-4Z-AA7M', 'TCGA-UY-A78L', 'TCGA-S5-AA26', 'TCGA-XF-A9T3', 'TCGA-E7-A678', 'TCGA-FT-A61P', 'TCGA-K4-A3WV', 'TCGA-GD-A3OP', 'TCGA-G2-A3VY', 'TCGA-FD-A5C1', 'TCGA-E7-A5KF', 'TCGA-DK-A2I1', 'TCGA-H4-A2HO'], 'total_alive': 30}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-XF-A9T3'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
