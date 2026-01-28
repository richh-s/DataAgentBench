code = """import json

# Load the clinical data
clinical_result = var_functions.query_db:18

if isinstance(clinical_result, str):
    with open(clinical_result, 'r') as f:
        brca_data = json.load(f)
else:
    brca_data = clinical_result

# Filter for alive BRCA patients and extract barcodes
alive_brca = []
alive_barcodes = []
histology_dict = {}  # barcode -> histological_type

for patient in brca_data:
    desc = patient['Patient_description']
    # Extract barcode
    import re
    barcode_match = re.search(r'(TCGA-\w{2}-\w{4})', desc)
    if barcode_match:
        barcode = barcode_match.group(1)
        # Check if alive
        if 'Alive' in desc:
            alive_brca.append(patient)
            alive_barcodes.append(barcode)
            histology_dict[barcode] = patient['histological_type']

print(f"Total BRCA patients: {len(brca_data)}")
print(f"Alive BRCA patients: {len(alive_brca)}")
print(f"Alive barcodes: {len(alive_barcodes)}")

# Get CDH1 mutations for alive BRCA patients
result = {
    'alive_barcodes': alive_barcodes,
    'histology_dict': histology_dict
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:10': [], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:16': {'alive_barcodes': ['TCGA-GD-A3OQ', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-K4-A6FZ', 'TCGA-ZF-A9RF', 'TCGA-DK-A6AV', 'TCGA-GD-A6C6', 'TCGA-GU-A766', 'TCGA-E7-A8O7', 'TCGA-GC-A4ZW', 'TCGA-G2-A2EK', 'TCGA-GV-A3JZ', 'TCGA-UY-A9PH', 'TCGA-UY-A78O', 'TCGA-DK-A1AC', 'TCGA-C4-A0F6', 'TCGA-KQ-A41O', 'TCGA-4Z-AA7M', 'TCGA-UY-A78L', 'TCGA-S5-AA26', 'TCGA-XF-A9T3', 'TCGA-E7-A678', 'TCGA-FT-A61P', 'TCGA-K4-A3WV', 'TCGA-GD-A3OP', 'TCGA-G2-A3VY', 'TCGA-FD-A5C1', 'TCGA-E7-A5KF', 'TCGA-DK-A2I1', 'TCGA-H4-A2HO'], 'total_alive': 30}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
