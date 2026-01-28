code = """import json
import re
import pandas as pd

storage_keys = [key for key in vars().keys() if key.startswith('var_')]
print("Available storage keys:", storage_keys)

# Load the clinical data BRCA alive patients
clinical_key = 'var_functions.query_db:4'
if clinical_key in vars():
    clinical_data_path = vars()[clinical_key]
    if isinstance(clinical_data_path, str) and clinical_data_path.endswith('.json'):
        with open(clinical_data_path, 'r') as f:
            clinical_data = json.load(f)
    else:
        clinical_data = vars()[clinical_key]
    
    if clinical_data:
        print(f"\nLoaded {len(clinical_data)} BRCA patients from clinical data")
        print("Sample patient:", clinical_data[0] if clinical_data else "No data")
        
        # Extract patient barcodes and histological types
        patients = []
        for record in clinical_data:
            patient_desc = record.get('Patient_description', '')
            hist_type = record.get('histological_type', 'Unknown')
            
            # Extract barcode from Patient_description (format: TCGA-XX-XXXX)
            # Looking for pattern like "Patient TCGA-DK-A6AW" or "patient TCGA-36-1576"
            match = re.search(r'(TCGA[\-\w]+)', patient_desc)
            if match:
                barcode = match.group(1)
                patients.append({
                    'ParticipantBarcode': barcode,
                    'histological_type': hist_type
                })
        
        print(f"\nExtracted {len(patients)} patients with barcodes")
        
        # Create DataFrame
        df_clinical = pd.DataFrame(patients)
        print("\nClinical data preview:")
        print(df_clinical.head())
        print("\nHistological types distribution:")
        print(df_clinical['histological_type'].value_counts())
        
        # Save for further processing
        with open('/tmp/brca_clinical_patients.json', 'w') as f:
            json.dump(patients, f)
        print("\nSaved patients data to /tmp/brca_clinical_patients.json")
    else:
        print("No clinical data found")"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
