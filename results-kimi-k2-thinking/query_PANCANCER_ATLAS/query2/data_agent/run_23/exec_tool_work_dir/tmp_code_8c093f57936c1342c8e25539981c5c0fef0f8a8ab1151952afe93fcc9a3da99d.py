code = """import json
import re

# Load breast cancer clinical data
breast_clinical_path = locals()['var_functions.query_db:40']
with open(breast_clinical_path, 'r') as f:
    breast_patients = json.load(f)

print('Total breast cancer patients:', len(breast_patients))

# Extract patient information
alive_patients = []
all_barcodes = set()

for record in breast_patients:
    desc = record['Patient_description']
    hist_type = record['histological_type']
    
    # Extract barcode
    match = re.search(r'(TCGA-\w+-\w+)', desc)
    if match:
        barcode = match.group(1)
        all_barcodes.add(barcode)
        
        # Check if alive
        if 'alive' in desc.lower():
            alive_patients.append({
                'barcode': barcode,
                'histological_type': hist_type
            })

print('Alive breast cancer patients:', len(alive_patients))
print('Unique barcodes total:', len(all_barcodes))

# Save results for next steps
result = {
    'alive_patients': alive_patients,
    'alive_barcodes': [p['barcode'] for p in alive_patients],
    'all_barcodes': list(all_barcodes),
    'total_alive': len(alive_patients)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_functions.query_db:14': [], 'var_functions.list_db:16': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:18': [], 'var_functions.query_db:26': [{'total_records': '10761'}], 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-06-0190'}, {'ParticipantBarcode': 'TCGA-DD-A1EH'}, {'ParticipantBarcode': 'TCGA-DU-6397'}, {'ParticipantBarcode': 'TCGA-HM-A6W2'}, {'ParticipantBarcode': 'TCGA-28-1760'}, {'ParticipantBarcode': 'TCGA-AA-3666'}, {'ParticipantBarcode': 'TCGA-AG-3883'}, {'ParticipantBarcode': 'TCGA-AN-A046'}, {'ParticipantBarcode': 'TCGA-04-1331'}, {'ParticipantBarcode': 'TCGA-04-1648'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'histological_type': 'Thyroid Papillary Carcinoma - Classical/usual'}, {'histological_type': 'Pancreas-Colloid (mucinous non-cystic) Carcinoma'}, {'histological_type': 'None'}, {'histological_type': 'Stomach  Adenocarcinoma  Diffuse Type'}, {'histological_type': 'Prostate Adenocarcinoma  Other Subtype'}, {'histological_type': 'Fibrolamellar Carcinoma'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Untreated primary (de novo) GBM'}, {'histological_type': 'Synovial Sarcoma - Biphasic'}, {'histological_type': 'Mucinous Adenocarcinoma of Endocervical Type'}, {'histological_type': 'Pancreas-Adenocarcinoma-Other Subtype'}, {'histological_type': 'Thymoma; Type B1|Thymoma; Type B2'}, {'histological_type': 'Seminoma; NOS|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)'}, {'histological_type': 'Non-Seminoma; Choriocarcinoma|Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)'}, {'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Immature)'}, {'histological_type': 'Lung Clear Cell Adenocarcinoma'}, {'histological_type': 'Seminoma; NOS|Non-Seminoma; Embryonal Carcinoma'}, {'histological_type': 'Pheochromocytoma'}, {'histological_type': 'Synovial Sarcoma - Monophasic'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)'}, {'histological_type': 'Non-Seminoma; Teratoma (Immature)|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Embryonal Carcinoma'}, {'histological_type': 'Prostate Adenocarcinoma Acinar Type'}, {'histological_type': 'Kidney Papillary Renal Cell Carcinoma'}, {'histological_type': 'Endocervical Type of Adenocarcinoma'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)|Seminoma; NOS'}, {'histological_type': 'Cervical Squamous Cell Carcinoma'}, {'histological_type': 'Leiomyosarcoma (LMS)'}, {'histological_type': 'Stomach  Intestinal Adenocarcinoma  Not Otherwise Specified (NOS)'}, {'histological_type': 'Mucinous (Colloid) Carcinoma'}, {'histological_type': 'Adrenocortical Carcinoma- Oncocytic Type'}, {'histological_type': 'Kidney Chromophobe'}, {'histological_type': 'Adrenocortical carcinoma- Usual Type'}, {'histological_type': 'Non-Seminoma; Teratoma (Immature)|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Lung Papillary Squamous Cell Caricnoma'}, {'histological_type': 'Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Lung Adenocarcinoma Mixed Subtype'}, {'histological_type': 'Thymoma; Type B2|Thymoma; Type B3'}, {'histological_type': 'Mucinous Carcinoma'}, {'histological_type': 'Sarcoma; synovial; poorly differentiated'}, {'histological_type': 'Diffuse malignant mesothelioma - NOS'}, {'histological_type': 'Stomach  Intestinal Adenocarcinoma  Tubular Type'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Thymoma; Type B3'}, {'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'histological_type': 'Stomach  Adenocarcinoma  Not Otherwise Specified (NOS)'}, {'histological_type': 'Malignant Peripheral Nerve Sheath Tumors (MPNST)'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)|Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Thymoma; Type C'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:46': [{'Hugo_Symbol': 'PCGF5'}, {'Hugo_Symbol': 'TPD52'}, {'Hugo_Symbol': 'SMARCA2'}, {'Hugo_Symbol': 'ING5'}, {'Hugo_Symbol': 'CCDC3'}, {'Hugo_Symbol': 'AKNA'}, {'Hugo_Symbol': 'MAPK8IP2'}, {'Hugo_Symbol': 'SLC22A1'}, {'Hugo_Symbol': 'SLAIN2'}, {'Hugo_Symbol': 'GRIN2A'}, {'Hugo_Symbol': 'ANO10'}, {'Hugo_Symbol': 'TCF21'}, {'Hugo_Symbol': 'HEATR5B'}, {'Hugo_Symbol': 'KIF26B'}, {'Hugo_Symbol': 'CCT6A'}, {'Hugo_Symbol': 'DDX25'}, {'Hugo_Symbol': 'BSDC1'}, {'Hugo_Symbol': 'TAF1L'}, {'Hugo_Symbol': 'TBC1D24'}, {'Hugo_Symbol': 'SLC26A9'}]}

exec(code, env_args)
