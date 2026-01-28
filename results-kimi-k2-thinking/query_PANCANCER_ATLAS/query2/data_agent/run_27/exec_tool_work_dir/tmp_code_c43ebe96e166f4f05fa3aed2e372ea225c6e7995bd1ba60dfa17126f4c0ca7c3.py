code = """import json
import re

# Load BRCA patients
brca_file = var_functions.query_db_78
with open(brca_file, 'r') as f:
    brca_patients = json.load(f)

# Load CDH1 mutation patients
cdh1_file = var_functions.query_db_80
with open(cdh1_file, 'r') as f:
    cdh1_patients = json.load(f)

# Create set of CDH1 mutated barcodes
cdh1_barcodes = set(p['ParticipantBarcode'] for p in cdh1_patients)

# Extract alive BRCA patients with barcodes and histological types
barcode_pattern = r'TCGA-[A-Z0-9]+-[A-Z0-9]+'
alive_brca = []

for patient in brca_patients:
    desc = patient['Patient_description']
    if 'Alive' in desc:
        match = re.search(barcode_pattern, desc)
        if match:
            barcode = match.group(0)
            hist_type = patient['histological_type']
            if hist_type == 'None':
                hist_type = 'Unknown'
            alive_brca.append({
                'barcode': barcode,
                'hist_type': hist_type
            })

# Analyze histological types
hist_analysis = {}
for patient in alive_brca:
    hist = patient['hist_type']
    barcode = patient['barcode']
    
    if hist not in hist_analysis:
        hist_analysis[hist] = {'total': 0, 'cdh1_mutated': 0}
    
    hist_analysis[hist]['total'] += 1
    if barcode in cdh1_barcodes:
        hist_analysis[hist]['cdh1_mutated'] += 1

# Calculate percentages
for hist, data in hist_analysis.items():
    data['percentage'] = (data['cdh1_mutated'] / data['total'] * 100) if data['total'] > 0 else 0

# Get top 3 by percentage
top_3 = sorted(hist_analysis.items(), key=lambda x: x[1]['percentage'], reverse=True)[:3]

# Prepare result
result = {
    'top_3': [(hist, round(data['percentage'], 2)) for hist, data in top_3],
    'details': {hist: {
        'total_patients': data['total'],
        'cdh1_mutated': data['cdh1_mutated'],
        'percentage': round(data['percentage'], 2)
    } for hist, data in top_3}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:9': [], 'var_functions.query_db:11': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': "Patient TCGA-23-1124, registered under UUID 8a6d2ce3-cc57-451b-9b07-8263782aa23f, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Dead.", 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-2641 (UUID 49e5ee61-a1c9-4038-84ac-92683e573a65) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-23-1118 (FEMALE, UUID 700e91bb-d675-41b2-bbbd-935767c7b447) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-1120 (UUID fdf83fdf-dfbb-4306-9a1b-b4487d18b402) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'The individual with barcode TCGA-23-2081 and UUID 41178cbc-db73-4007-b5d8-febebf7f578d is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_functions.query_db:10': [{'Patient_description': 'Patient TCGA-BL-A0C8 (UUID a6003b1c-56a9-430a-a5e2-b70af3f81bdb) is a MALE diagnosed with Bladder urothelial carcinoma. Current vital status: Alive.', 'histological_type': 'None'}, {'Patient_description': "Patient TCGA-BL-A13J, registered under UUID 556fcbc8-172a-4af1-8822-ae036e8d68e8, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Clinical entry ebc094a6-cdc9-4c02-b8ec-a181b25a364d identifies patient TCGA-BL-A13I, a FEMALE subject with Bladder urothelial carcinoma. Their current vital status is Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Patient TCGA-BL-A3JM (UUID 0F4FB205-B13C-4A85-97B3-779429E6CCDD) is a MALE diagnosed with Bladder urothelial carcinoma. Current vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Record C1AFC5EB-8C1D-4B6C-8453-48728FC023BA refers to patient TCGA-BL-A5ZZ, a FEMALE diagnosed with Bladder urothelial carcinoma. Vital status recorded as Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': "Patient TCGA-MQ-A6BL, registered under UUID 0C8BD0EB-9C26-4FB0-A365-26354129F0DA, belongs to the Mesothelioma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Biphasic mesothelioma'}, {'Patient_description': 'Patient TCGA-KC-A4BL (MALE, UUID 5089A8D2-A353-4150-8A6B-6478C5BB29BB) is enrolled in the study of Prostate adenocarcinoma. Vital status: Alive.', 'histological_type': 'Prostate Adenocarcinoma Acinar Type'}, {'Patient_description': 'In the Thyroid carcinoma dataset, patient TCGA-FY-A3BL (UUID C6F08366-F30D-45BD-B949-B59D2493995D) is recorded as a MALE with vital status: Alive.', 'histological_type': 'Thyroid Papillary Carcinoma - Classical/usual'}, {'Patient_description': 'In the Breast invasive carcinoma dataset, patient TCGA-BH-A0BL (UUID 92b5de82-0221-4df1-8094-80f40c0bb4fa) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-C5-A1BL (FEMALE, UUID 03c3fe57-ae85-4e45-9657-c3182ab5e124) is enrolled in the study of Cervical squamous cell carcinoma and endocervical adenocarcinoma. Vital status: Alive.', 'histological_type': 'Cervical Squamous Cell Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-DX-A8BL and UUID E987C47D-6ECB-41BB-A66F-A0489E56449F is a MALE case of Sarcoma, documented with vital status = Alive.', 'histological_type': "Pleomorphic 'MFH'/ Undifferentiated pleomorphic sarcoma"}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:34': [{'ParticipantBarcode': 'TCGA-EO-A3AZ', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-G2-A3IE', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-OL-A6VQ', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Ins'}, {'ParticipantBarcode': 'TCGA-S3-A6ZG', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Ins'}, {'ParticipantBarcode': 'TCGA-VQ-A91K', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-AO-A0J8', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-AC-A6IX', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-A2-A0EX', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Nonsense_Mutation'}, {'ParticipantBarcode': 'TCGA-A5-A0GA', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json', 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json'}

exec(code, env_args)
