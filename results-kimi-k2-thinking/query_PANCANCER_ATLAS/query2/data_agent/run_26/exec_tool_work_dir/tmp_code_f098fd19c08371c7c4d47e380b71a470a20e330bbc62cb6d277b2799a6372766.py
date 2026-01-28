code = """import json
import re

# Get the clinical data from the file
clinical_file = var_functions.query_db:20  # This is the file path string

# Read the full clinical data
with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)

print(f"Total bladder cancer records: {len(clinical_data)}")

# Parse patient descriptions to extract barcode and vital status
alive_patients = []
patient_histology = {}

for record in clinical_data:
    desc = record["Patient_description"]
    hist_type = record["histological_type"]
    
    # Extract barcode (TCGA-XX-XXXX format)
    barcode_match = re.search(r'(TCGA-\w{2}-\w{4})', desc)
    if barcode_match:
        barcode = barcode_match.group(1)
        
        # Check if patient is alive
        if "vital status: Alive" in desc or "vital status = Alive" in desc or "vital status is Alive" in desc:
            alive_patients.append(barcode)
            patient_histology[barcode] = hist_type

print(f"Alive bladder cancer patients: {len(alive_patients)}")
print(f"Sample barcodes: {alive_patients[:5]}")
print(f"Sample histologies: {list(set(patient_histology.values()))[:10]}")

# Prepare data for next query
result = {
    "alive_barcodes": alive_patients,
    "histology_map": patient_histology,
    "total_alive": len(alive_patients)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:2': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'ParticipantBarcode': 'TCGA-S9-A6U9'}, {'ParticipantBarcode': 'TCGA-S9-A7IQ'}, {'ParticipantBarcode': 'TCGA-S9-A7QZ'}, {'ParticipantBarcode': 'TCGA-S9-A7R8'}, {'ParticipantBarcode': 'TCGA-SC-A6LM'}, {'ParticipantBarcode': 'TCGA-SC-A6LN'}, {'ParticipantBarcode': 'TCGA-SG-A6Z7'}, {'ParticipantBarcode': 'TCGA-SI-A71O'}, {'ParticipantBarcode': 'TCGA-SQ-A6I6'}, {'ParticipantBarcode': 'TCGA-TM-A7C5'}], 'var_functions.query_db:16': [], 'var_functions.query_db:18': [], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
