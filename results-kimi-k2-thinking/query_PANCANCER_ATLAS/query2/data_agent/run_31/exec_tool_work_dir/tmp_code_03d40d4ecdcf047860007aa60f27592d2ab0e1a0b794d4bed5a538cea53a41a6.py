code = """import json
import re
import pandas as pd

# Load clinical data for BRCA patients
clinical_path = vars()['var_functions.query_db:24']

if isinstance(clinical_path, str) and clinical_path.endswith('.json'):
    with open(clinical_path, 'r') as f:
        clinical_data = json.load(f)
else:
    clinical_data = clinical_path

print('Loaded', len(clinical_data), 'BRCA clinical records')

# Extract barcode and vital status, and histological type
patients = []
for record in clinical_data:
    patient_desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', 'Unknown')
    
    # Extract barcode and vital status
    barcode_match = re.search(r'(TCGA[\-\w]+)', patient_desc)
    vital_match = re.search(r'vital status[\s:]*([Aa]live|[Dd]ead)', patient_desc)
    
    if barcode_match:
        barcode = barcode_match.group(1)
        vital_status = vital_match.group(1) if vital_match else 'Unknown'
        patients.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type,
            'vital_status': vital_status
        })

print('Extracted', len(patients), 'patients')
print('First few patients:', patients[:5])

# Filter for alive patients
alive_patients = [p for p in patients if p['vital_status'].lower() == 'alive']
print('Alive patients:', len(alive_patients))

# Save patients data
with open('/tmp/brca_patients_all.json', 'w') as f:
    json.dump(patients, f)
with open('/tmp/brca_patients_alive.json', 'w') as f:
    json.dump(alive_patients, f)

result = {
    'total_patients': len(patients),
    'alive_patients': len(alive_patients)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'storage_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:4']}, 'var_functions.query_db:14': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
