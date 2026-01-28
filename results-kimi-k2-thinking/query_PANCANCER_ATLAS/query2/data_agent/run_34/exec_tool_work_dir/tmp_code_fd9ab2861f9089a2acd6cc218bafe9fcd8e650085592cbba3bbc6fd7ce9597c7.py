code = """import json
import pandas as pd
import re

# Read the BRCA patient data
with open('var_functions.query_db:11.json', 'r') as f:
    brca_data = json.load(f)

print('Total BRCA patients found:', len(brca_data))

# Let's understand the structure and vital status
vital_status_count = {}
histological_types = {}

for patient in brca_data:
    desc = patient.get('Patient_description', '')
    
    # Determine vital status
    if 'Alive' in desc:
        vital_status = 'Alive'
    elif 'Dead' in desc:
        vital_status = 'Dead'
    else:
        continue
    
    vital_status_count[vital_status] = vital_status_count.get(vital_status, 0) + 1
    
    # Get histological type
    hist_type = patient.get('histological_type', 'Unknown')
    if hist_type and hist_type != 'None' and hist_type != '[Not Applicable]':
        histological_types[hist_type] = histological_types.get(hist_type, 0) + 1

print('Vital status distribution:', vital_status_count)
print('Histological types found:', len(histological_types))
print('Top 5 histological types:')
sorted_hists = sorted(histological_types.items(), key=lambda x: x[1], reverse=True)[:5]
for hist_type, count in sorted_hists:
    print('  ' + hist_type + ': ' + str(count))

# Filter for alive patients only
alive_brca = [p for p in brca_data if 'Alive' in p.get('Patient_description', '')]
print('\nAlive BRCA patients:', len(alive_brca))

# Extract patient barcodes from alive BRCA patients
patient_barcodes = []
for patient in alive_brca:
    desc = patient.get('Patient_description', '')
    match = re.search(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', desc)
    if match:
        patient_barcodes.append(match.group(1))

print('Extracted patient barcodes from alive BRCA patients:', len(patient_barcodes))
if patient_barcodes:
    print('Example barcodes:', patient_barcodes[:5])

# Count alive BRCA patients by histological type
alive_hist_types = {}
for patient in alive_brca:
    hist_type = patient.get('histological_type', 'Unknown')
    if hist_type and hist_type != 'None' and hist_type != '[Not Applicable]':
        alive_hist_types[hist_type] = alive_hist_types.get(hist_type, 0) + 1

print('\nAlive BRCA patients by histological type:')
for hist_type, count in sorted(alive_hist_types.items(), key=lambda x: x[1], reverse=True):
    print('  ' + hist_type + ': ' + str(count))

# Save for later use
print('\nRESULT SUMMARY:')
print('Total BRCA patients:', len(brca_data))
print('Alive BRCA patients:', len(alive_brca))
print('Patient barcodes extracted:', len(patient_barcodes))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
