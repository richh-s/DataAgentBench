code = """import json
import pandas as pd

# Read the BRCA patient data
with open('var_functions.query_db:11.json', 'r') as f:
    brca_data = json.load(f)

print(f"Total BRCA patients found: {len(brca_data)}")

# Let's understand the structure and vital status
vital_status_count = {}
histological_types = {}

for patient in brca_data:
    # Check vital status from Patient_description
    desc = patient.get('Patient_description', '')
    
    # Determine vital status - look for 'Alive' or 'Dead' in description
    vital_status = None
    if 'Alive' in desc:
        vital_status = 'Alive'
    elif 'Dead' in desc:
        vital_status = 'Dead'
    
    if vital_status:
        vital_status_count[vital_status] = vital_status_count.get(vital_status, 0) + 1
    
    # Get histological type
    hist_type = patient.get('histological_type', 'Unknown')
    if hist_type and hist_type != 'None' and hist_type != '[Not Applicable]':
        histological_types[hist_type] = histological_types.get(hist_type, 0) + 1

print(f"Vital status distribution: {vital_status_count}")
print(f"Histological types found: {len(histological_types)}")
print("Top 5 histological types:")
for hist_type, count in sorted(histological_types.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"  {hist_type}: {count}")

# Filter for alive patients only
alive_brca = [p for p in brca_data if 'Alive' in p.get('Patient_description', '')]
print(f"\nAlive BRCA patients: {len(alive_brca)}")

# Extract patient barcodes from alive BRCA patients
patient_barcodes = []
for patient in alive_brca:
    desc = patient.get('Patient_description', '')
    # Extract barcode (format: TCGA-XX-XXXX or similar)
    import re
    match = re.search(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', desc)
    if match:
        patient_barcodes.append(match.group(1))

print(f"Extracted {len(patient_barcodes)} patient barcodes from alive BRCA patients")
if patient_barcodes:
    print(f"Example barcodes: {patient_barcodes[:5]}")

# Save alive BRCA patients for later use
alive_brca_df = pd.DataFrame(alive_brca)
patient_barcodes_list = patient_barcodes

print(f"\nAlive BRCA patients by histological type:")
alive_hist_types = {}
for patient in alive_brca:
    hist_type = patient.get('histological_type', 'Unknown')
    if hist_type and hist_type != 'None' and hist_type != '[Not Applicable]':
        alive_hist_types[hist_type] = alive_hist_types.get(hist_type, 0) + 1

for hist_type, count in sorted(alive_hist_types.items(), key=lambda x: x[1], reverse=True):
    print(f"  {hist_type}: {count}")"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
