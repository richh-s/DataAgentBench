code = """import json
import re

# Load BRCA patient data from previous query
file_path = var_functions['execute_python:26']
print(f"Loading BRCA patient data from: {file_path}")

with open(file_path, 'r') as f:
    brca_data = json.load(f)

brca_patients = {p['ParticipantBarcode']: p['histological_type'] for p in brca_data['patients']}
print(f"Number of BRCA patients: {len(brca_patients)}")
print(f"Sample barcodes: {list(brca_patients.keys())[:5]}")

# Load CDH1 mutation data
file_path2 = var_functions['query_db:28']
print(f"\nLoading CDH1 mutations from: {file_path2}")

with open(file_path2, 'r') as f:
    cdh1_mutations = json.load(f)

print(f"Total CDH1 mutations found: {len(cdh1_mutations)}")
print(f"Sample mutations: {cdh1_mutations[:3]}")

# Check which CDH1 mutations belong to BRCA patients
brca_cdh1_mutations = []
for mutation in cdh1_mutations:
    if mutation['ParticipantBarcode'] in brca_patients:
        brca_cdh1_mutations.append({
            'ParticipantBarcode': mutation['ParticipantBarcode'],
            'histological_type': brca_patients[mutation['ParticipantBarcode']],
            'Variant_Classification': mutation['Variant_Classification']
        })

print(f"\nCDH1 mutations in BRCA patients: {len(brca_cdh1_mutations)}")

result = {
    'brca_patient_count': len(brca_patients),
    'brca_cdh1_mutation_count': len(brca_cdh1_mutations),
    'brca_cdh1_mutations': brca_cdh1_mutations
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '943.0'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '446.0'}], 'var_functions.query_db:18': [], 'var_functions.query_db:20': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.query_db:28': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Nonsense_Mutation'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Ins'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}]}

exec(code, env_args)
