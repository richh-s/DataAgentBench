code = """import json
import re

# Get the file path from the storage
file_path = var_functions.query_db:14
print(f"File path: {file_path}")

# Read the full LGG patients data
with open(file_path, 'r') as f:
    lgg_patients = json.load(f)

print(f"Total LGG patients: {len(lgg_patients)}")

# Extract ParticipantBarcode from Patient_description and collect histological_type
lgg_data = []
for patient in lgg_patients:
    patient_desc = patient.get('Patient_description', '')
    hist_type = patient.get('histological_type', '')
    
    # Extract TCGA barcode from Patient_description
    # Looking for patterns like TCGA-XX-XXXX or TCGA-XXX-XXXXX
    barcode_match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4,5})', patient_desc)
    if barcode_match:
        barcode = barcode_match.group(1)
        # Only include if histological_type is not enclosed in square brackets
        if hist_type and not (hist_type.startswith('[') and hist_type.endswith(']')):
            lgg_data.append({
                'ParticipantBarcode': barcode,
                'histological_type': hist_type,
                'Patient_description': patient_desc
            })

print(f"LGG patients with valid histology: {len(lgg_data)}")
print("Sample:", lgg_data[:3])

# Count by histology type
from collections import Counter
histology_counts = Counter([p['histological_type'] for p in lgg_data])
print("Histology type counts:", dict(histology_counts))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'LXN', 'Entrez': '56925', 'normalized_count': '69.7259'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'ZNF770', 'Entrez': '54989', 'normalized_count': '1195.92'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'AMELY', 'Entrez': '266', 'normalized_count': '0.0'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'TPTE2P1', 'Entrez': '646405', 'normalized_count': '214.576'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'ITGB3', 'Entrez': '3690', 'normalized_count': '13.6303'}], 'var_functions.list_db:10': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [{'ParticipantBarcode': 'TCGA-AB-2908', 'Symbol': 'IGF2', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'Symbol': 'IGF2', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'Symbol': 'IGF2', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'Symbol': 'IGF2', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'Symbol': 'IGF2', 'normalized_count': '613.474'}, {'ParticipantBarcode': 'TCGA-A8-A082', 'Symbol': 'IGF2', 'normalized_count': '630.54'}, {'ParticipantBarcode': 'TCGA-B5-A3FA', 'Symbol': 'IGF2', 'normalized_count': '423.628'}, {'ParticipantBarcode': 'TCGA-BH-A1EX', 'Symbol': 'IGF2', 'normalized_count': '1151.13'}, {'ParticipantBarcode': 'TCGA-BT-A20O', 'Symbol': 'IGF2', 'normalized_count': '369.106'}, {'ParticipantBarcode': 'TCGA-CD-5799', 'Symbol': 'IGF2', 'normalized_count': '3936.02070028943'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
