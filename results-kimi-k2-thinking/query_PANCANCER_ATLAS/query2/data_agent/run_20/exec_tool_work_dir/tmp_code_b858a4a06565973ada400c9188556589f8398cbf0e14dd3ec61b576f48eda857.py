code = """import json
import re

# Get the file path from storage for alive BRCA patients
stored_key = 'var_functions.query_db:24'
file_path = locals().get(stored_key)

if file_path:
    print(f"Loading BRCA patient data from: {file_path}")
    with open(file_path, 'r') as f:
        brca_patients = json.load(f)
    
    print(f"Total BRCA patients found: {len(brca_patients)}")
    
    # Extract patient barcodes and histological types
    patient_data = []
    for patient in brca_patients:
        desc = patient.get('Patient_description', '')
        hist_type = patient.get('histological_type', 'Unknown')
        
        # Extract TCGA barcode using regex
        barcode_match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
        if barcode_match:
            barcode = barcode_match.group(1)
            patient_data.append({
                'ParticipantBarcode': barcode,
                'histological_type': hist_type
            })
    
    print(f"Successfully extracted {len(patient_data)} patient barcodes")
    
    # Show unique histological types
    hist_types = set([p['histological_type'] for p in patient_data])
    print(f"Unique histological types: {hist_types}")
    
    # Save patient data for next step
    output = {
        'patient_count': len(patient_data),
        'patients': patient_data,
        'histological_types': list(hist_types)
    }
    
    print("__RESULT__:")
    print(json.dumps(output))
else:
    print(f"Could not find data with key: {stored_key}")
    print("__RESULT__:")
    print(json.dumps({'error': 'file_path_not_found'}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '943.0'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '446.0'}], 'var_functions.query_db:18': [], 'var_functions.query_db:20': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
