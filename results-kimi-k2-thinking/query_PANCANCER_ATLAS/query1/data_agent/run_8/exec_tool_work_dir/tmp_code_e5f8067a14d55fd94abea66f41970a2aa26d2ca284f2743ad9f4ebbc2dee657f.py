code = """import json
import re

# Get the file path from storage
db_result_key = 'var_functions.query_db:10'
file_path = locals().get(db_result_key)

if not file_path:
    print('__RESULT__:')
    print(json.dumps({'error': 'File path not found in storage'}))
else:
    # Load LGG clinical data from file
    with open(file_path, 'r') as f:
        lgg_clinical = json.load(f)
    
    # Parse patient barcodes from descriptions and collect valid histology types not in brackets
    lgg_patients = []
    for record in lgg_clinical:
        if 'histological_type' not in record:
            continue
        histology = record['histological_type']
        # Skip histology enclosed in square brackets
        if histology.startswith('[') and histology.endswith(']'):
            continue
        
        # Parse patient barcode from Patient_description
        desc = record.get('Patient_description', '')
        barcode_match = re.search(r'TCGA-[A-Z0-9]+-[A-Z0-9]+', desc)
        if barcode_match:
            barcode = barcode_match.group(0)
            lgg_patients.append({
                'ParticipantBarcode': barcode,
                'histological_type': histology
            })
    
    print('__RESULT__:')
    print(json.dumps({
        'patient_count': len(lgg_patients),
        'unique_histologies': list(set([p['histological_type'] for p in lgg_patients])),
        'sample_patients': lgg_patients[:5]
    }))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
