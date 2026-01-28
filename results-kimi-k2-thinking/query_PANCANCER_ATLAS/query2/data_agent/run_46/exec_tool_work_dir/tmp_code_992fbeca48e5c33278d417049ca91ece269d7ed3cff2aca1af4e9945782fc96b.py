code = """import json
import re
from collections import defaultdict

# Get the file path from storage
storage_path = locals()['var_functions.query_db:18']

# Read the clinical data file
with open(storage_path, 'r') as f:
    clinical_data = json.load(f)

# Extract patient info: barcodes, vital status, and histological type
breast_patients = []
for record in clinical_data:
    desc = record['Patient_description']
    hist_type = record['histological_type']
    
    # Extract barcode from description (TCGA-XX-XXXX format)
    barcode_match = re.search(r'(TCGA-\w+-\w+)', desc)
    if barcode_match:
        barcode = barcode_match.group(1)
    else:
        continue
    
    # Extract vital status
    if 'vital status = Alive' in desc or 'vital status: Alive' in desc:
        vital_status = 'Alive'
    elif 'vital status = Dead' in desc or 'vital status: Dead' in desc:
        vital_status = 'Dead'
    else:
        vital_status = 'Unknown'
    
    breast_patients.append({
        'barcode': barcode,
        'vital_status': vital_status,
        'histological_type': hist_type,
        'original_desc': desc
    })

# Count alive BRCA patients by histological type
alive_patients = [p for p in breast_patients if p['vital_status'] == 'Alive']
hist_counts = defaultdict(int)
for p in alive_patients:
    hist_counts[p['histological_type']] += 1

print('__RESULT__:')
print(json.dumps({
    'total_breast_patients': len(breast_patients),
    'alive_breast_patients': len(alive_patients),
    'histology_counts': dict(hist_counts)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry C07B122E-AC50-4DB2-ADD2-5617A5D0E976 identifies patient TCGA-GM-A2DA, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Dead.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-3C-AAAU and UUID 6E7D5EC6-A469-467C-B748-237353C23416 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-A7-A26I, registered under UUID b2ecbc0f-2c30-4200-8d5e-7b95424bcadb, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 523E24A2-51B9-4658-BE2F-42E5FCCEBB17 refers to patient TCGA-A7-A5ZW, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-C8-A26Z and UUID dc11b1c7-1f00-4813-b4b5-ecf776b2eb37 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-EW-A6SA and UUID ABA5F46A-E67A-4CD2-9C52-C0686968FF04 is a MALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-C8-A273 and UUID 5a5f0f48-2b13-4e78-b130-901b85d9a7f3 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record c2a742fe-3e8b-4210-85a6-7191a1123609 refers to patient TCGA-AN-A0FN, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FD, registered under UUID c6086936-7544-4da0-8c0c-114166848483, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry 10c9be1e-2cc0-45e4-8d2c-c013ea63ef05 identifies patient TCGA-AN-A0FS, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'Record b5b99291-507e-4b68-a039-9a0f571f55df refers to patient TCGA-AO-A12H, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Other  specify'}, {'Patient_description': 'Record 3e9f93c0-aa79-4b4c-bd6c-b3325912362a refers to patient TCGA-AN-A0AL, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A3YI (UUID A45D296E-EFC0-479E-B2F6-BAD834668CDF) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-C8-A137, registered under UUID 03ab1e9f-4918-404d-b178-3a4fd929c5e8, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry 0DD8DBC1-C48B-4E7C-B401-57101F724967 identifies patient TCGA-S3-AA11, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:14': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-A8-A091'}, {'ParticipantBarcode': 'TCGA-A8-A0A1'}, {'ParticipantBarcode': 'TCGA-A8-A0A9'}, {'ParticipantBarcode': 'TCGA-AA-3821'}, {'ParticipantBarcode': 'TCGA-A2-A0YL'}, {'ParticipantBarcode': 'TCGA-AR-A1AT'}, {'ParticipantBarcode': 'TCGA-BS-A0U8'}, {'ParticipantBarcode': 'TCGA-D8-A27G'}, {'ParticipantBarcode': 'TCGA-E6-A1LX'}, {'ParticipantBarcode': 'TCGA-EJ-7782'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
