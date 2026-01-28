code = """import json
import re

# Load the result from previous query
result = var_functions.query_db:14

# Parse the JSON string if needed
if isinstance(result, str) and result.endswith('.json'):
    with open(result, 'r') as f:
        alive_brca_patients_raw = json.load(f)
else:
    alive_brca_patients_raw = result

print("Total alive BRCA patients:", len(alive_brca_patients_raw))
print("\nFirst record:")
print(alive_brca_patients_raw[0])

# Extract participant barcodes
barcode_pattern = r'TCGA-[A-Z0-9]+-[A-Z0-9]+'
record_list = []

for rec in alive_brca_patients_raw:
    desc = rec['Patient_description']
    match = re.search(barcode_pattern, desc)
    if match:
        barcode = match.group(0)
        hist_type = rec['histological_type']
        record_list.append({
            'participant_barcode': barcode,
            'histological_type': hist_type
        })

print("\nSuccessfully extracted", len(record_list), "participant barcodes")

# Show histological type distribution
from collections import Counter
hist_counter = Counter([rec['histological_type'] for rec in record_list])
print("\nHistological type distribution:")
for hist, count in hist_counter.most_common():
    print(f"{hist or 'None'}: {count}")

# Prepare result for next step
print("__RESULT__:")
print(json.dumps(record_list[:10]))  # Return first 10 as preview"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:9': [], 'var_functions.query_db:11': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': "Patient TCGA-23-1124, registered under UUID 8a6d2ce3-cc57-451b-9b07-8263782aa23f, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Dead.", 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-2641 (UUID 49e5ee61-a1c9-4038-84ac-92683e573a65) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-23-1118 (FEMALE, UUID 700e91bb-d675-41b2-bbbd-935767c7b447) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-1120 (UUID fdf83fdf-dfbb-4306-9a1b-b4487d18b402) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'The individual with barcode TCGA-23-2081 and UUID 41178cbc-db73-4007-b5d8-febebf7f578d is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_functions.query_db:10': [{'Patient_description': 'Patient TCGA-BL-A0C8 (UUID a6003b1c-56a9-430a-a5e2-b70af3f81bdb) is a MALE diagnosed with Bladder urothelial carcinoma. Current vital status: Alive.', 'histological_type': 'None'}, {'Patient_description': "Patient TCGA-BL-A13J, registered under UUID 556fcbc8-172a-4af1-8822-ae036e8d68e8, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Clinical entry ebc094a6-cdc9-4c02-b8ec-a181b25a364d identifies patient TCGA-BL-A13I, a FEMALE subject with Bladder urothelial carcinoma. Their current vital status is Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Patient TCGA-BL-A3JM (UUID 0F4FB205-B13C-4A85-97B3-779429E6CCDD) is a MALE diagnosed with Bladder urothelial carcinoma. Current vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Record C1AFC5EB-8C1D-4B6C-8453-48728FC023BA refers to patient TCGA-BL-A5ZZ, a FEMALE diagnosed with Bladder urothelial carcinoma. Vital status recorded as Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': "Patient TCGA-MQ-A6BL, registered under UUID 0C8BD0EB-9C26-4FB0-A365-26354129F0DA, belongs to the Mesothelioma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Biphasic mesothelioma'}, {'Patient_description': 'Patient TCGA-KC-A4BL (MALE, UUID 5089A8D2-A353-4150-8A6B-6478C5BB29BB) is enrolled in the study of Prostate adenocarcinoma. Vital status: Alive.', 'histological_type': 'Prostate Adenocarcinoma Acinar Type'}, {'Patient_description': 'In the Thyroid carcinoma dataset, patient TCGA-FY-A3BL (UUID C6F08366-F30D-45BD-B949-B59D2493995D) is recorded as a MALE with vital status: Alive.', 'histological_type': 'Thyroid Papillary Carcinoma - Classical/usual'}, {'Patient_description': 'In the Breast invasive carcinoma dataset, patient TCGA-BH-A0BL (UUID 92b5de82-0221-4df1-8094-80f40c0bb4fa) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-C5-A1BL (FEMALE, UUID 03c3fe57-ae85-4e45-9657-c3182ab5e124) is enrolled in the study of Cervical squamous cell carcinoma and endocervical adenocarcinoma. Vital status: Alive.', 'histological_type': 'Cervical Squamous Cell Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-DX-A8BL and UUID E987C47D-6ECB-41BB-A66F-A0489E56449F is a MALE case of Sarcoma, documented with vital status = Alive.', 'histological_type': "Pleomorphic 'MFH'/ Undifferentiated pleomorphic sarcoma"}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['Mutation_Data', 'RNASeq_Expression']}

exec(code, env_args)
