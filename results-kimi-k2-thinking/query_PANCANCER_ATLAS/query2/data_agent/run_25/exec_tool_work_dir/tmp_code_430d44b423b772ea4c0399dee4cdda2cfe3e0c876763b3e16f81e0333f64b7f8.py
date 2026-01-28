code = """import json

# Read the data from the stored files
brca_al Clinical_path = var_functions.query_db:8

# Read the file to get full data
with open(var_functions.query_db:8, 'r') as f:
    brca_alive = json.load(f)

print(f"Total BRCA alive patients: {len(brca_alive)}")
print("\nSample records:")
for i, record in enumerate(brca_alive[:3]):
    print(f"\nRecord {i+1}:")
    print(f"  Patient_description: {record['Patient_description'][:100]}...")
    print(f"  histological_type: {record['histological_type']}")

# Let's also check if we can extract patient barcodes from Patient_description
import re

# Extract patient barcodes from the descriptions
patient_barcodes = []
for record in brca_alive:
    desc = record['Patient_description']
    # Look for patterns like TCGA-XX-XXXX
    match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    if match:
        patient_barcodes.append(match.group())
    else:
        patient_barcodes.append(None)

print(f"\nNumber of patient barcodes extracted: {len([x for x in patient_barcodes if x])}")
print(f"Sample barcodes: {patient_barcodes[:5]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
