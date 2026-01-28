code = """import json
import re
import math

# Load LGG clinical data
clinical_file = '/user_storage/executions/query_db/48.json'
with open(clinical_file, 'r') as f:
    lgg_clinical = json.load(f)

# Load IGF2 expression data  
expression_file = '/user_storage/executions/query_db/44.json'
with open(expression_file, 'r') as f:
    igf2_expression = json.load(f)

# Extract LGG patient barcodes with histology
lgg_patients = {}
for record in lgg_clinical:
    desc = record['Patient_description']
    histology = record['histological_type']
    
    # Skip if histology has brackets
    if '[' in histology or ']' in histology:
        continue
    
    # Extract barcode
    match = re.search(r'(TCGA-\w+-\w+)', desc)
    if match:
        barcode = match.group(1)
        lgg_patients[barcode] = histology

# Create IGF2 expression dict
igf2_dict = {}
for record in igf2_expression:
    barcode = record['ParticipantBarcode']
    if isinstance(record['normalized_count'], str):
        count = float(record['normalized_count'])
    else:
        count = record['normalized_count']
    igf2_dict[barcode] = count

# Find LGG patients with IGF2 expression
matched_data = []
for barcode, histology in lgg_patients.items():
    if barcode in igf2_dict:
        matched_data.append({
            'ParticipantBarcode': barcode,
            'histological_type': histology,
            'normalized_count': igf2_dict[barcode]
        })

# Calculate log10 transformed averages by histology
histology_expressions = {}
for item in matched_data:
    hist = item['histological_type']
    count = item['normalized_count']
    log_val = math.log10(count + 1)
    
    if hist not in histology_expressions:
        histology_expressions[hist] = []
    histology_expressions[hist].append(log_val)

# Calculate averages with 4 decimal places
results = {}
for hist, values in histology_expressions.items():
    avg = sum(values) / len(values)
    results[hist] = round(avg, 4)

# Create JSON-serializable output
output = json.dumps(results)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': "Patient TCGA-23-1124, registered under UUID 8a6d2ce3-cc57-451b-9b07-8263782aa23f, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Dead."}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-2641 (UUID 49e5ee61-a1c9-4038-84ac-92683e573a65) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-23-1118 (FEMALE, UUID 700e91bb-d675-41b2-bbbd-935767c7b447) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-1120 (UUID fdf83fdf-dfbb-4306-9a1b-b4487d18b402) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-23-2081 and UUID 41178cbc-db73-4007-b5d8-febebf7f578d is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Dead.'}], 'var_functions.list_db:10': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'histological_type': 'Adenosquamous'}, {'histological_type': 'Adrenocortical Carcinoma- Myxoid Type'}, {'histological_type': 'Adrenocortical Carcinoma- Oncocytic Type'}, {'histological_type': 'Adrenocortical carcinoma- Usual Type'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Biphasic mesothelioma'}, {'histological_type': 'Cervical Squamous Cell Carcinoma'}, {'histological_type': 'Cholangiocarcinoma; distal'}, {'histological_type': 'Cholangiocarcinoma; hilar/perihilar'}, {'histological_type': 'Cholangiocarcinoma; intrahepatic'}, {'histological_type': 'Colon Adenocarcinoma'}, {'histological_type': 'Colon Mucinous Adenocarcinoma'}, {'histological_type': 'Dedifferentiated liposarcoma'}, {'histological_type': 'Desmoid Tumor'}, {'histological_type': 'Diffuse large B-cell lymphoma (DLBCL) NOS (any anatomic site nodal or extranodal)'}, {'histological_type': 'Diffuse malignant mesothelioma - NOS'}, {'histological_type': 'Endocervical Adenocarcinoma of the Usual Type'}, {'histological_type': 'Endocervical Type of Adenocarcinoma'}, {'histological_type': 'Endometrioid Adenocarcinoma of Endocervix'}, {'histological_type': 'Endometrioid endometrial adenocarcinoma'}, {'histological_type': 'Epithelioid mesothelioma'}, {'histological_type': 'Esophagus Adenocarcinoma  NOS'}, {'histological_type': 'Esophagus Squamous Cell Carcinoma'}, {'histological_type': 'Fibrolamellar Carcinoma'}, {'histological_type': "Giant cell 'MFH' / Undifferentiated pleomorphic sarcoma with giant cells"}, {'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'histological_type': 'Head and Neck Squamous Cell Carcinoma'}, {'histological_type': 'Head and Neck Squamous Cell Carcinoma  Spindle Cell Variant'}, {'histological_type': 'Head and Neck Squamous Cell Carcinoma Basaloid Type'}, {'histological_type': 'Hepatocellular Carcinoma'}, {'histological_type': 'Hepatocholangiocarcinoma (Mixed)'}, {'histological_type': 'Infiltrating Carcinoma NOS'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Infiltrating Lobular Carcinoma'}, {'histological_type': 'Kidney Chromophobe'}, {'histological_type': 'Kidney Clear Cell Renal Carcinoma'}, {'histological_type': 'Kidney Papillary Renal Cell Carcinoma'}, {'histological_type': 'Leiomyosarcoma (LMS)'}, {'histological_type': 'Lung Acinar Adenocarcinoma'}, {'histological_type': 'Lung Adenocarcinoma Mixed Subtype'}, {'histological_type': 'Lung Adenocarcinoma- Not Otherwise Specified (NOS)'}, {'histological_type': 'Lung Basaloid Squamous Cell Carcinoma'}, {'histological_type': 'Lung Bronchioloalveolar Carcinoma Mucinous'}, {'histological_type': 'Lung Bronchioloalveolar Carcinoma Nonmucinous'}, {'histological_type': 'Lung Clear Cell Adenocarcinoma'}, {'histological_type': 'Lung Micropapillary Adenocarcinoma'}, {'histological_type': 'Lung Mucinous Adenocarcinoma'}, {'histological_type': 'Lung Papillary Adenocarcinoma'}, {'histological_type': 'Lung Papillary Squamous Cell Caricnoma'}, {'histological_type': 'Lung Signet Ring Adenocarcinoma'}], 'var_functions.query_db:16': [{'histological_type': 'Oligoastrocytoma'}, {'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Paraganglioma'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}], 'var_functions.query_db:18': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligodendroglioma', 'icd_o_3_histology': '9450/3'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma', 'icd_o_3_histology': '9382/3'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligoastrocytoma', 'icd_o_3_histology': '9382/3'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligoastrocytoma', 'icd_o_3_histology': '9382/3'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma', 'icd_o_3_histology': '9382/3'}, {'Patient_description': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'icd_o_3_histology': '9450/3'}, {'Patient_description': 'Patient TCGA-S9-A6U1 (UUID A5E10E2E-5157-487B-88DC-6C70AD5E244A) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Astrocytoma', 'icd_o_3_histology': '9401/3'}, {'Patient_description': 'The individual with barcode TCGA-TM-A7C3 and UUID D13AC936-87A9-4164-BDAB-02CCF3908CFE is a FEMALE case of Brain lower grade glioma, documented with vital status = Dead.', 'histological_type': 'Astrocytoma', 'icd_o_3_histology': '9401/3'}, {'Patient_description': 'Case 8E44FB97-C649-4056-80AC-257CEF61D226, linked to barcode TCGA-S9-A7R2, corresponds to a MALE patient diagnosed with Brain lower grade glioma, with vital status Dead.', 'histological_type': 'Astrocytoma', 'icd_o_3_histology': '9401/3'}, {'Patient_description': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Oligodendroglioma', 'icd_o_3_histology': '9450/3'}, {'Patient_description': "Patient TCGA-S9-A6TU, registered under UUID 688FC346-A14D-4859-8727-057CD0A0B880, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Astrocytoma', 'icd_o_3_histology': '9400/3'}, {'Patient_description': 'Record c3c41fd2-f0d7-4f46-9e18-cce4626538c2 refers to patient TCGA-HW-7490, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Astrocytoma', 'icd_o_3_histology': '9400/3'}, {'Patient_description': 'Record D81B9957-8C82-4006-B111-449FA9FB95ED refers to patient TCGA-P5-A733, a FEMALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Astrocytoma', 'icd_o_3_histology': '9400/3'}, {'Patient_description': 'Patient TCGA-DH-A7US (MALE, UUID 82FD02AB-D628-469F-8853-4C603CF04964) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'icd_o_3_histology': '9450/3'}, {'Patient_description': 'Clinical entry bc3b4816-df1d-44ed-a8c6-f32c8e011a1f identifies patient TCGA-HW-8319, a FEMALE subject with Brain lower grade glioma. Their current vital status is Dead.', 'histological_type': 'Astrocytoma', 'icd_o_3_histology': '9401/3'}, {'Patient_description': 'Patient TCGA-P5-A5F4 (FEMALE, UUID 0557B788-5AED-4919-85EB-A503AD893D75) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'icd_o_3_histology': '9451/3'}, {'Patient_description': 'Patient TCGA-FG-7637 (MALE, UUID c40ab957-fe46-43b1-992d-b4e2040a3f57) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligoastrocytoma', 'icd_o_3_histology': '9382/3'}, {'Patient_description': "Patient TCGA-FG-A4MW, registered under UUID DCE168B1-D2A9-4409-8437-AB382F6D7D31, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Oligoastrocytoma', 'icd_o_3_histology': '9382/3'}, {'Patient_description': "Patient TCGA-E1-A7Z3, registered under UUID 3AC41CC6-5DFB-40A1-BD13-5DC7CA2BB6F3, belongs to the Brain lower grade glioma cohort. This FEMALE patient's vital status is Dead.", 'histological_type': 'Astrocytoma', 'icd_o_3_histology': '9400/3'}, {'Patient_description': 'Patient TCGA-S9-A7R4 (MALE, UUID 58650D08-7685-41DE-9AE0-21665F8F449F) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Astrocytoma', 'icd_o_3_histology': '9401/3'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:34': [{'ParticipantBarcode': 'TCGA-AB-2908', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'normalized_count': '613.474'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
