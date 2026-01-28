code = """import json
import re

# Read the clinical data file
clinical_file = var_functions.query_db:20

with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)

print('Total bladder cancer records loaded:', len(clinical_data))

# Extract alive patients and their histology types
alive_patients = []
patient_histology = {}

for record in clinical_data:
    desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', 'Unknown')
    
    # Find TCGA barcode pattern
    bc_match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    if bc_match:
        barcode = bc_match.group(0)
        # Check vital status
        if 'Alive' in desc and ('vital status:' in desc or 'vital status =' in desc or 'vital status is' in desc):
            alive_patients.append(barcode)
            patient_histology[barcode] = hist_type

print('Alive bladder cancer patients found:', len(alive_patients))
print('Sample barcodes:', alive_patients[:5])

# Get unique histology types
hist_types = list(set(patient_histology.values()))
print('Unique histology types (first 10):', hist_types[:10])

result = {
    'alive_barcodes': alive_patients,
    'histology_map': patient_histology,
    'count': len(alive_patients)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:2': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'ParticipantBarcode': 'TCGA-S9-A6U9'}, {'ParticipantBarcode': 'TCGA-S9-A7IQ'}, {'ParticipantBarcode': 'TCGA-S9-A7QZ'}, {'ParticipantBarcode': 'TCGA-S9-A7R8'}, {'ParticipantBarcode': 'TCGA-SC-A6LM'}, {'ParticipantBarcode': 'TCGA-SC-A6LN'}, {'ParticipantBarcode': 'TCGA-SG-A6Z7'}, {'ParticipantBarcode': 'TCGA-SI-A71O'}, {'ParticipantBarcode': 'TCGA-SQ-A6I6'}, {'ParticipantBarcode': 'TCGA-TM-A7C5'}], 'var_functions.query_db:16': [], 'var_functions.query_db:18': [], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
