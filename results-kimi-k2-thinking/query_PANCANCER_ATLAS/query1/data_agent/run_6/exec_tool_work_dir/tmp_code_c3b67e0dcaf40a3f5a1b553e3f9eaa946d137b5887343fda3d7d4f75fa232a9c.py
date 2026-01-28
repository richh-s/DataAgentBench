code = """import json
# Access the clinical data from storage
clinical_data_key = 'var_functions.query_db:2'
clinical_data_path = locals()[clinical_data_key]

with open(clinical_data_path, 'r') as f:
    clinical_data = json.load(f)

if clinical_data:
    columns = list(clinical_data[0].keys())
    print("=== Clinical Info Table Columns ===")
    for i, col in enumerate(sorted(columns)):
        print(f"{i+1:3d}. {col}")
    
print("\nTotal records: " + str(len(clinical_data)))

# Find cancer types in the dataset
cancer_types = set()
for record in clinical_data:
    patient_desc = record.get('Patient_description', '')
    if 'LGG' in patient_desc or 'Brain lower grade glioma' in patient_desc:
        cancer_types.add('LGG')
    elif 'BRCA' in patient_desc or 'Bladder' in patient_desc:
        cancer_types.add('BRCA')
    elif 'OV' in patient_desc or 'Ovarian' in patient_desc:
        cancer_types.add('OV')
print("\nCancer types found: " + str(sorted(cancer_types)))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
