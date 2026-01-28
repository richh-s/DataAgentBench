code = """import json
import re

# Load the clinical data from the file
clin_data_path = locals()['var_functions.query_db:12']
with open(clin_data_path, 'r') as f:
    lgg_patients = json.load(f)

# Extract TCGA barcodes and histological types from the Patient_description
# Valid histological types are those not enclosed in square brackets
barcode_histology_map = {}
for record in lgg_patients:
    patient_desc = record.get('Patient_description', '')
    histology = record.get('histological_type', '')
    
    # Check if histology is valid (not enclosed in square brackets)
    if histology and not (histology.startswith('[') and histology.endswith(']')):
        # Extract TCGA barcode from patient description
        # Pattern looks for TCGA-xx-xxxx or similar format
        match = re.search(r'(TCGA-\w{2}-[\w\d]{4})', patient_desc)
        if match:
            barcode = match.group(1)
            barcode_histology_map[barcode] = histology

# Check how many patients we have
print('__RESULT__:')
print(json.dumps({
    'patient_count': len(barcode_histology_map),
    'sample_patients': list(barcode_histology_map.items())[:5] if barcode_histology_map else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'LXN', 'Entrez': '56925', 'normalized_count': '69.7259'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'ZNF770', 'Entrez': '54989', 'normalized_count': '1195.92'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'AMELY', 'Entrez': '266', 'normalized_count': '0.0'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'TPTE2P1', 'Entrez': '646405', 'normalized_count': '214.576'}, {'ParticipantBarcode': 'TCGA-06-0675', 'SampleBarcode': 'TCGA-06-0675-11A', 'AliquotBarcode': 'TCGA-06-0675-11A-32R-A36H-07', 'SampleTypeLetterCode': 'NT', 'SampleType': 'Solid Tissue Normal', 'Symbol': 'ITGB3', 'Entrez': '3690', 'normalized_count': '13.6303'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
