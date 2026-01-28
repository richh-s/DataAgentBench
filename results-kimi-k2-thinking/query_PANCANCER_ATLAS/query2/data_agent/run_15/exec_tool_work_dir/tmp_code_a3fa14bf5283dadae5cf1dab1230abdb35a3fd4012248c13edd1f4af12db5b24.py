code = """import json
import pandas as pd
import re

# Load the BRCA patients file (since it's too large, it's stored as a file path)
try:
    # Try to access the direct variable if it's a list
    brca_data = locals()['var_functions.query_db:10']
    if isinstance(brca_data, str) and brca_data.endswith('.json'):
        # It's a file path
        with open(brca_data, 'r') as f:
            brca_data = json.load(f)
    elif isinstance(brca_data, str):
        # Might be a JSON string
        brca_data = json.loads(brca_data)
except Exception as e:
    print(f"Error loading data: {e}")
    # Try to read as a file since it might be stored as a string path
    try:
        import os
        if os.path.exists('result_query_db_10.json'):
            with open('result_query_db_10.json', 'r') as f:
                brca_data = json.load(f)
        else:
            brca_data = []
    except:
        brca_data = []

print(f"Loaded {len(brca_data)} BRCA patients")

# Extract patient barcodes and histological types
patients = []
for record in brca_data:
    patient_desc = record.get('Patient_description', '')
    histo_type = record.get('histological_type', '')
    
    # Extract TCGA barcode using regex
    match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', patient_desc)
    if match:
        barcode = match.group(0)
        patients.append({
            'ParticipantBarcode': barcode,
            'histological_type': histo_type,
            'Patient_description': patient_desc
        })

print(f"Extracted {len(patients)} patients with barcodes")
print("Sample patients:", patients[:3])

# Create DataFrame for easier processing
df_patients = pd.DataFrame(patients)
print(f"DataFrame shape: {df_patients.shape}")
print("Histological types:", df_patients['histological_type'].unique()[:10])

# Save to variable for next steps
result = df_patients.to_dict('records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry C07B122E-AC50-4DB2-ADD2-5617A5D0E976 identifies patient TCGA-GM-A2DA, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Dead.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-3C-AAAU and UUID 6E7D5EC6-A469-467C-B748-237353C23416 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-A7-A26I, registered under UUID b2ecbc0f-2c30-4200-8d5e-7b95424bcadb, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 523E24A2-51B9-4658-BE2F-42E5FCCEBB17 refers to patient TCGA-A7-A5ZW, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-C8-A26Z and UUID dc11b1c7-1f00-4813-b4b5-ecf776b2eb37 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
