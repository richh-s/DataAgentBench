code = """import json

# Properly access the storage variable
storage_key = 'var_functions.query_db:11'
brca_result = locals().get(storage_key)

if not brca_result:
    print("No data found in storage")
    exit()

# If it's a string (file path), load it
if isinstance(brca_result, str):
    with open(brca_result, 'r') as f:
        brca_data = json.load(f)
else:
    brca_data = brca_result

# Filter for alive BRCA patients
alive_brca = []
alive_barcodes = []

for patient in brca_data:
    desc = patient['Patient_description']
    if 'Alive' in desc:
        alive_brca.append(patient)
        # Extract barcode
        import re
        barcode_match = re.search(r'(TCGA-\w{2}-\w{4})', desc)
        if barcode_match:
            alive_barcodes.append(barcode_match.group(1))

# Count histological types
histology_counts = {}
for patient in alive_brca:
    hist_type = patient['histological_type']
    histology_counts[hist_type] = histology_counts.get(hist_type, 0) + 1

print(f"Total BRCA patients: {len(brca_data)}")
print(f"Alive BRCA patients: {len(alive_brca)}")
print(f"Alive barcodes: {len(alive_barcodes)}")
print("Histology distribution among alive BRCA:")
for hist, count in sorted(histology_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"  {hist}: {count}")

result = {
    'alive_barcodes': alive_barcodes,
    'total_alive': len(alive_brca)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:10': [], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
