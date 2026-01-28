code = """import json

# Access the data from storage
brca_result = var_functions.query_db:11

# If it's a string (file path), load it
if isinstance(brca_result, str):
    with open(brca_result, 'r') as f:
        brca_data = json.load(f)
else:
    brca_data = brca_result

print("BRCA patients found:", len(brca_data))

# Filter for alive patients
alive_brca = []
alive_barcodes = []

for patient in brca_data:
    if 'Alive' in patient['Patient_description']:
        alive_brca.append(patient)
        # Extract barcode from Patient_description
        desc = patient['Patient_description']
        # Looking for pattern like "TCGA-GD-A3OQ"
        import re
        barcode_match = re.search(r'(TCGA-\w{2}-\w{4})', desc)
        if barcode_match:
            alive_barcodes.append(barcode_match.group(1))

print("Alive BRCA patients:", len(alive_brca))
print("Alive barcodes extracted:", len(alive_barcodes))
print("First 5 barcodes:", alive_barcodes[:5])

# Create result dictionary
result = {
    'total_brca': len(brca_data),
    'alive_brca': len(alive_brca),
    'alive_barcodes': alive_barcodes
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:10': [], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
