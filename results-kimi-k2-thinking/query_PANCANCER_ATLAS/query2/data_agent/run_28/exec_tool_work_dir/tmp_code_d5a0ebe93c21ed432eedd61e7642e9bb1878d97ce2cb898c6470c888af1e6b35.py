code = """import json
import re

# Access alive BRCA data file path from storage
clinical_file_path = var_functions.query_db:68

# Load the clinical data
with open(clinical_file_path) as f:
    alive_brca_patients = json.load(f)

print(f"Total alive BRCA patients loaded: {len(alive_brca_patients)}")

# Show first few patients to verify structure
for i, patient in enumerate(alive_brca_patients[:3]):
    print(f"\nPatient {i+1}:")
    print(f"  Description: {patient['Patient_description'][:100]}...")
    print(f"  Histological type: {patient['histological_type']}")

# Extract barcodes and histology mapping
alive_brca_barcodes = {}
for patient in alive_brca_patients:
    desc = patient['Patient_description']
    hist_type = patient['histological_type']
    
    # Extract barcode using regex
    match = re.search(r'(TCGA-\w{2}-\w{4})', desc)
    if match:
        barcode = match.group(1)
        alive_brca_barcodes[barcode] = hist_type

print(f"\nExtracted barcodes: {len(alive_brca_barcodes)}")
print("Sample barcodes and histology:")
for barcode, hist in list(alive_brca_barcodes.items())[:5]:
    print(f"  {barcode}: {hist}")

result = json.dumps({
    'total_patients': len(alive_brca_barcodes),
    'barcode_histology': alive_brca_barcodes
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:10': [], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:16': {'alive_barcodes': ['TCGA-GD-A3OQ', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-K4-A6FZ', 'TCGA-ZF-A9RF', 'TCGA-DK-A6AV', 'TCGA-GD-A6C6', 'TCGA-GU-A766', 'TCGA-E7-A8O7', 'TCGA-GC-A4ZW', 'TCGA-G2-A2EK', 'TCGA-GV-A3JZ', 'TCGA-UY-A9PH', 'TCGA-UY-A78O', 'TCGA-DK-A1AC', 'TCGA-C4-A0F6', 'TCGA-KQ-A41O', 'TCGA-4Z-AA7M', 'TCGA-UY-A78L', 'TCGA-S5-AA26', 'TCGA-XF-A9T3', 'TCGA-E7-A678', 'TCGA-FT-A61P', 'TCGA-K4-A3WV', 'TCGA-GD-A3OP', 'TCGA-G2-A3VY', 'TCGA-FD-A5C1', 'TCGA-E7-A5KF', 'TCGA-DK-A2I1', 'TCGA-H4-A2HO'], 'total_alive': 30}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-XF-A9T3'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
