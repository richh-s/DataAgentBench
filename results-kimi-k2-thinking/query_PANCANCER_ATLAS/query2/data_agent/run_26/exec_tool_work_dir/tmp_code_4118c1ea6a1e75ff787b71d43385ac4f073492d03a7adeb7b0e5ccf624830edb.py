code = """import json, re

# Get the correct file path from storage variable
clinical_file_path = locals()['var_functions.query_db:20']

print('Loading from file path:', clinical_file_path)

with open(clinical_file_path, 'r') as f:
    clinical_data = json.load(f)

print('Total bladder cancer records loaded:', len(clinical_data))

# Extract alive patients and count by histology
alive_by_histology = {}
all_alive_barcodes = []

for record in clinical_data:
    desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', 'Unknown')
    
    # Find TCGA barcode pattern
    bc_match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    if bc_match:
        barcode = bc_match.group(0)
        # Check if patient is alive
        if 'vital status' in desc.lower() and 'alive' in desc.lower():
            alive_by_histology[hist_type] = alive_by_histology.get(hist_type, 0) + 1
            all_alive_barcodes.append(barcode)

print('Alive patients by histology:', alive_by_histology)
print('Total alive patients:', len(all_alive_barcodes))

# Check which histology types have CDH1 mutations (from previous query)
# We found TCGA-DK-A6AW has CDH1 mutation

# Let's query all alive patients' CDH1 mutation status
print('Will query CDH1 mutations for', len(all_alive_barcodes), 'alive patients')

result = {
    'alive_by_histology': alive_by_histology,
    'alive_barcodes': all_alive_barcodes,
    'total_alive': len(all_alive_barcodes)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:2': ['clinical_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'ParticipantBarcode': 'TCGA-S9-A6U9'}, {'ParticipantBarcode': 'TCGA-S9-A7IQ'}, {'ParticipantBarcode': 'TCGA-S9-A7QZ'}, {'ParticipantBarcode': 'TCGA-S9-A7R8'}, {'ParticipantBarcode': 'TCGA-SC-A6LM'}, {'ParticipantBarcode': 'TCGA-SC-A6LN'}, {'ParticipantBarcode': 'TCGA-SG-A6Z7'}, {'ParticipantBarcode': 'TCGA-SI-A71O'}, {'ParticipantBarcode': 'TCGA-SQ-A6I6'}, {'ParticipantBarcode': 'TCGA-TM-A7C5'}], 'var_functions.query_db:16': [], 'var_functions.query_db:18': [], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'alive_barcodes': ['TCGA-DK-A6AW', 'TCGA-GD-A3OQ', 'TCGA-CF-A47W', 'TCGA-CF-A3MF', 'TCGA-DK-A2I6', 'TCGA-XF-A8HE', 'TCGA-FD-A3SN', 'TCGA-BL-A0C8', 'TCGA-FD-A43N', 'TCGA-E7-A7DV', 'TCGA-DK-A1AE', 'TCGA-DK-AA6R', 'TCGA-ZF-A9R7', 'TCGA-GV-A3JX', 'TCGA-FD-A5BU', 'TCGA-E7-A6MD', 'TCGA-GV-A3QI', 'TCGA-BT-A42F', 'TCGA-FD-A3SP', 'TCGA-KQ-A41R', 'TCGA-UY-A9PE', 'TCGA-FD-A43U', 'TCGA-FD-A6TA', 'TCGA-ZF-AA4W', 'TCGA-DK-A6B5', 'TCGA-DK-A6B1', 'TCGA-XF-A9SI', 'TCGA-PQ-A6FI'], 'histology_map': {'TCGA-DK-A6AW': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-GD-A3OQ': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-CF-A47W': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-CF-A3MF': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-A2I6': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-XF-A8HE': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A3SN': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-BL-A0C8': 'None', 'TCGA-FD-A43N': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-E7-A7DV': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-A1AE': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-AA6R': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-ZF-A9R7': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-GV-A3JX': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A5BU': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-E7-A6MD': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-GV-A3QI': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-BT-A42F': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A3SP': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-KQ-A41R': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-UY-A9PE': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A43U': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-FD-A6TA': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-ZF-AA4W': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-A6B5': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-DK-A6B1': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-XF-A9SI': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'TCGA-PQ-A6FI': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, 'count': 28}, 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-DK-A6AW', 'Hugo_Symbol': 'CDH1'}], 'var_functions.query_db:32': [{'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'count': '409'}, {'histological_type': 'None', 'count': '3'}]}

exec(code, env_args)
