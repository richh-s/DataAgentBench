code = """import json
import re

# Load clinical data (BRCA alive patients)
clinical_file = locals()['var_functions.query_db:34']
with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)

print(f"Loaded {len(clinical_data)} BRCA alive patients")

# Extract patient barcodes and histological types
patient_barcode_pattern = r'TCGA-\w{2}-\w{4}'
brca_patients = []

for record in clinical_data:
    patient_desc = record.get('Patient_description', '')
    histological_type = record.get('histological_type', 'Unknown')
    
    # Extract patient barcode
    barcode_match = re.search(patient_barcode_pattern, patient_desc)
    if barcode_match:
        barcode = barcode_match.group(0)
        brca_patients.append({
            'barcode': barcode,
            'histological_type': histological_type
        })

print(f"Extracted {len(brca_patients)} patients with barcodes")

# Load CDH1 mutation data
mutation_file = locals()['var_functions.query_db:36']
with open(mutation_file, 'r') as f:
    mutation_data = json.load(f)

print(f"Loaded {len(mutation_data)} patients with CDH1 mutations")

# Create set of patients with CDH1 mutations
cdh1_patients = set([item['ParticipantBarcode'] for item in mutation_data])
print(f"Found {len(cdh1_patients)} unique patients with CDH1 mutations")

# Group BRCA patients by histological type
from collections import defaultdict
histology_patients = defaultdict(list)
for patient in brca_patients:
    histology_patients[patient['histological_type']].append(patient['barcode'])

# Calculate CDH1 mutation percentage for each histological type
results = []
for histology, patients in histology_patients.items():
    total_patients = len(patients)
    cdh1_mutated = len([p for p in patients if p in cdh1_patients])
    percentage = (cdh1_mutated / total_patients * 100) if total_patients > 0 else 0
    
    results.append({
        'histological_type': histology,
        'total_patients': total_patients,
        'cdh1_mutated': cdh1_mutated,
        'percentage': round(percentage, 2)
    })

# Sort by percentage and get top 3
top_3 = sorted(results, key=lambda x: x['percentage'], reverse=True)[:3]

print("\nTop 3 histological types by CDH1 mutation percentage:")
for i, item in enumerate(top_3, 1):
    print(f"{i}. {item['histological_type']}: {item['percentage']}% ({item['cdh1_mutated']}/{item['total_patients']})")

# Also show all histologies sorted
print("\nAll histological types sorted by CDH1 mutation percentage:")
all_sorted = sorted(results, key=lambda x: x['percentage'], reverse=True)
for item in all_sorted:
    if item['total_patients'] >= 5:  # Only show histologies with at least 5 patients for reliability
        print(f"{item['histological_type']}: {item['percentage']}% ({item['cdh1_mutated']}/{item['total_patients']})")

result_output = {
    'top_3_histologies': top_3,
    'all_histology_data': all_sorted
}

print('__RESULT__:')
print(json.dumps(result_output))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': "Patient TCGA-23-1124, registered under UUID 8a6d2ce3-cc57-451b-9b07-8263782aa23f, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Dead."}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-2641 (UUID 49e5ee61-a1c9-4038-84ac-92683e573a65) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-23-1118 (FEMALE, UUID 700e91bb-d675-41b2-bbbd-935767c7b447) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-1120 (UUID fdf83fdf-dfbb-4306-9a1b-b4487d18b402) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-23-2081 and UUID 41178cbc-db73-4007-b5d8-febebf7f578d is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Dead.'}, {'Patient_description': 'Case 1db60f09-7f5a-4f21-8003-06a6abc781db, linked to barcode TCGA-29-1694, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-WR-A838 (UUID B8023162-5E82-40E6-AD8C-8ACF81821F01) is recorded as a FEMALE with vital status: Dead.'}, {'Patient_description': "Patient TCGA-31-1955, registered under UUID cce34351-1700-405b-818f-a598f63a33e8, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Alive."}, {'Patient_description': 'Patient TCGA-32-4209 (MALE, UUID 5438322c-9db0-4974-ba01-801020559f97) is enrolled in the study of Glioblastoma multiforme. Vital status: Dead.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-29-1696 (UUID 8a98a6e6-b763-4824-858b-fd2738e6c9a3) is recorded as a FEMALE with vital status: Dead.'}, {'Patient_description': 'Record 40635bf3-d8ba-4833-b623-547e55e5d07e refers to patient TCGA-29-2425, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Case 05019013-7ea5-4905-ac79-901146ba2ee2, linked to barcode TCGA-29-1688, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': 'Record 13319c20-02f6-4b5f-b24f-3d8f4084094c refers to patient TCGA-25-1318, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'Record 79fd602b-3e8e-4353-aa78-4f5f170b607d refers to patient TCGA-25-1328, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'The individual with barcode TCGA-57-1584 and UUID ed21615c-0de3-421c-9e8d-8996026c4431 is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Alive.'}], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:20': ['clinical_info'], 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-B9-A8YI'}, {'ParticipantBarcode': 'TCGA-A8-A09Z'}, {'ParticipantBarcode': 'TCGA-A8-A091'}, {'ParticipantBarcode': 'TCGA-D8-A27G'}, {'ParticipantBarcode': 'TCGA-BH-A0HP'}, {'ParticipantBarcode': 'TCGA-AC-A2FO'}, {'ParticipantBarcode': 'TCGA-A2-A4S2'}, {'ParticipantBarcode': 'TCGA-A7-A425'}, {'ParticipantBarcode': 'TCGA-BS-A0UV'}, {'ParticipantBarcode': 'TCGA-CD-A4MG'}], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive."}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.'}, {'Patient_description': 'Clinical entry C07B122E-AC50-4DB2-ADD2-5617A5D0E976 identifies patient TCGA-GM-A2DA, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Dead.'}, {'Patient_description': 'The individual with barcode TCGA-3C-AAAU and UUID 6E7D5EC6-A469-467C-B748-237353C23416 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.'}, {'Patient_description': "Patient TCGA-A7-A26I, registered under UUID b2ecbc0f-2c30-4200-8d5e-7b95424bcadb, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive."}, {'Patient_description': 'Record 523E24A2-51B9-4658-BE2F-42E5FCCEBB17 refers to patient TCGA-A7-A5ZW, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'The individual with barcode TCGA-C8-A26Z and UUID dc11b1c7-1f00-4813-b4b5-ecf776b2eb37 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
