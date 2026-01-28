code = """import json
import re

# Load CDH1 mutation data
cdh1_mutations_path = locals()['var_functions.query_db:34']
with open(cdh1_mutations_path, 'r') as f:
    cdh1_mutations = json.load(f)

# Load alive BRCA patients data
brca_clinical_path = locals()['var_functions.query_db:24']
with open(brca_clinical_path, 'r') as f:
    brca_clinical = json.load(f)

# Build set of alive BRCA patient barcodes
alive_brca_barcodes = set()
brca_histology = {}

for record in brca_clinical:
    patient_desc = record['Patient_description'].lower()
    # Filter for alive patients
    if 'alive' in patient_desc and 'dead' not in patient_desc:
        # Extract barcode
        match = re.search(r'(TCGA-\w{2}-\w{4})', record['Patient_description'])
        if match:
            barcode = match.group(1)
            alive_brca_barcodes.add(barcode)
            hist_type = record.get('histological_type', 'Unknown')
            brca_histology[barcode] = hist_type

# Filter CDH1 mutations for alive BRCA patients
alive_brca_cdh1_mutations = []
for mutation in cdh1_mutations:
    participant = mutation['ParticipantBarcode']
    # Check if participant is an alive BRCA patient
    if participant in alive_brca_barcodes:
        alive_brca_cdh1_mutations.append({
            'barcode': participant,
            'hist_type': brca_histology[participant],
            'mutation': mutation['Variant_Classification']
        })

# Count patients by histological type
total_by_hist = {}
for barcode, hist_type in brca_histology.items():
    total_by_hist[hist_type] = total_by_hist.get(hist_type, 0) + 1

# Count CDH1 mutations by histological type
mutated_by_hist = {}
for mutation in alive_brca_cdh1_mutations:
    hist_type = mutation['hist_type']
    mutated_by_hist[hist_type] = mutated_by_hist.get(hist_type, 0) + 1

# Calculate mutation percentages
mutation_percentages = []
for hist_type, total in total_by_hist.items():
    if total >= 10:  # Only consider hist types with at least 10 patients
        mutated = mutated_by_hist.get(hist_type, 0)
        percentage = (mutated / total) * 100
        mutation_percentages.append({
            'histological_type': hist_type,
            'total_patients': total,
            'mutated_patients': mutated,
            'mutation_percentage': percentage
        })

# Sort by mutation percentage and get top 3
mutation_percentages.sort(key=lambda x: x['mutation_percentage'], reverse=True)
top_three = mutation_percentages[:3]

print('__RESULT__:')
print(json.dumps({
    'total_alive_brca': len(alive_brca_barcodes),
    'alive_brca_with_cdh1_mutations': len(alive_brca_cdh1_mutations),
    'hist_types_considered': len(mutation_percentages),
    'top_three_hist_types': top_three
}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_records': 5, 'first_record_keys': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status'], 'sample_patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'sample_histological_type': 'Serous Cystadenocarcinoma'}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry C07B122E-AC50-4DB2-ADD2-5617A5D0E976 identifies patient TCGA-GM-A2DA, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Dead.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-3C-AAAU and UUID 6E7D5EC6-A469-467C-B748-237353C23416 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-A7-A26I, registered under UUID b2ecbc0f-2c30-4200-8d5e-7b95424bcadb, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 523E24A2-51B9-4658-BE2F-42E5FCCEBB17 refers to patient TCGA-A7-A5ZW, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-C8-A26Z and UUID dc11b1c7-1f00-4813-b4b5-ecf776b2eb37 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-EW-A6SA and UUID ABA5F46A-E67A-4CD2-9C52-C0686968FF04 is a MALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-C8-A273 and UUID 5a5f0f48-2b13-4e78-b130-901b85d9a7f3 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record c2a742fe-3e8b-4210-85a6-7191a1123609 refers to patient TCGA-AN-A0FN, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FD, registered under UUID c6086936-7544-4da0-8c0c-114166848483, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry 10c9be1e-2cc0-45e4-8d2c-c013ea63ef05 identifies patient TCGA-AN-A0FS, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'Record b5b99291-507e-4b68-a039-9a0f571f55df refers to patient TCGA-AO-A12H, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Other  specify'}, {'Patient_description': 'Record 3e9f93c0-aa79-4b4c-bd6c-b3325912362a refers to patient TCGA-AN-A0AL, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A3YI (UUID A45D296E-EFC0-479E-B2F6-BAD834668CDF) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-C8-A137, registered under UUID 03ab1e9f-4918-404d-b178-3a4fd929c5e8, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry 0DD8DBC1-C48B-4E7C-B401-57101F724967 identifies patient TCGA-S3-AA11, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_functions.execute_python:22': {'brca_samples': 20, 'sample_records': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_brca': 1087, 'alive_brca': 936, 'sample_alive': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}]}, 'var_functions.execute_python:28': {'alive_patient_barcodes_count': 936, 'sample_barcodes': ['TCGA-AC-A5EH', 'TCGA-LL-A7SZ', 'TCGA-AN-A0FY', 'TCGA-AC-A2FB', 'TCGA-AO-A1KR', 'TCGA-3C-AAAU', 'TCGA-A7-A26I', 'TCGA-A7-A5ZW', 'TCGA-C8-A26Z', 'TCGA-EW-A6SA'], 'sample_hist_types': {'TCGA-AC-A5EH': 'Infiltrating Ductal Carcinoma', 'TCGA-LL-A7SZ': 'Infiltrating Ductal Carcinoma', 'TCGA-AN-A0FY': 'Infiltrating Ductal Carcinoma', 'TCGA-AC-A2FB': 'Infiltrating Lobular Carcinoma', 'TCGA-AO-A1KR': 'Infiltrating Ductal Carcinoma'}}, 'var_functions.execute_python:30': {'total_alive_brca': 936, 'sample_barcodes': ['TCGA-AC-A5EH', 'TCGA-LL-A7SZ', 'TCGA-AN-A0FY', 'TCGA-AC-A2FB', 'TCGA-AO-A1KR', 'TCGA-3C-AAAU', 'TCGA-A7-A26I', 'TCGA-A7-A5ZW', 'TCGA-C8-A26Z', 'TCGA-EW-A6SA'], 'hist_type_distribution': {'Mixed Histology (please specify)': 24, 'Infiltrating Carcinoma NOS': 1, 'Infiltrating Ductal Carcinoma': 671, 'Other  specify': 36, 'Mucinous Carcinoma': 14, 'Medullary Carcinoma': 4, 'Metaplastic Carcinoma': 7, 'Infiltrating Lobular Carcinoma': 178, 'None': 1}}, 'var_functions.query_db:32': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Nonsense_Mutation'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Ins'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'alive_brca_patients_count': 936, 'sample_patients': [['TCGA-AC-A5EH', 'Infiltrating Ductal Carcinoma'], ['TCGA-LL-A7SZ', 'Infiltrating Ductal Carcinoma'], ['TCGA-AN-A0FY', 'Infiltrating Ductal Carcinoma'], ['TCGA-AC-A2FB', 'Infiltrating Lobular Carcinoma'], ['TCGA-AO-A1KR', 'Infiltrating Ductal Carcinoma']]}}

exec(code, env_args)
