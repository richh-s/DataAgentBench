code = """import json
import pandas as pd
import numpy as np
import re

# Get the clinical data from storage
var_name = 'var_functions.query_db:24'
file_path = locals()[var_name]
print('File path:', file_path)

with open(file_path, 'r') as f:
    clinical_data = json.load(f)

print('Total clinical records:', len(clinical_data))

# Filter for LGG patients
lgg_patients = []
for record in clinical_data:
    patient_desc = record.get('Patient_description', '').lower()
    if 'brain lower grade glioma' in patient_desc:
        desc = record.get('Patient_description', '')
        # Extract barcode
        barcode_match = re.search(r'(TCGA-\w+-\w+)', desc)
        if barcode_match:
            barcode = barcode_match.group(1)
            histology = record.get('histological_type', '')
            lgg_patients.append({
                'ParticipantBarcode': barcode,
                'histological_type': histology
            })

print('Found LGG patients:', len(lgg_patients))
result = {'total': len(lgg_patients), 'first_few': lgg_patients[:5]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'available_vars': ['var_functions.query_db:2']}, 'var_functions.query_db:16': [], 'var_functions.query_db:18': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'histological_type': 'Stomach  Adenocarcinoma  Diffuse Type'}, {'histological_type': 'Prostate Adenocarcinoma  Other Subtype'}, {'histological_type': 'Fibrolamellar Carcinoma'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Untreated primary (de novo) GBM'}, {'histological_type': 'Synovial Sarcoma - Biphasic'}, {'histological_type': 'Mucinous Adenocarcinoma of Endocervical Type'}, {'histological_type': 'Pancreas-Adenocarcinoma-Other Subtype'}, {'histological_type': 'Thymoma; Type B1|Thymoma; Type B2'}, {'histological_type': 'Seminoma; NOS|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)'}, {'histological_type': 'Non-Seminoma; Choriocarcinoma|Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)'}, {'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Immature)'}, {'histological_type': 'Lung Clear Cell Adenocarcinoma'}, {'histological_type': 'Seminoma; NOS|Non-Seminoma; Embryonal Carcinoma'}, {'histological_type': 'Pheochromocytoma'}, {'histological_type': 'Synovial Sarcoma - Monophasic'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)'}, {'histological_type': 'Non-Seminoma; Teratoma (Immature)|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Embryonal Carcinoma'}, {'histological_type': 'Prostate Adenocarcinoma Acinar Type'}, {'histological_type': 'Kidney Papillary Renal Cell Carcinoma'}, {'histological_type': 'Endocervical Type of Adenocarcinoma'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)|Seminoma; NOS'}, {'histological_type': 'Cervical Squamous Cell Carcinoma'}, {'histological_type': 'Leiomyosarcoma (LMS)'}, {'histological_type': 'Stomach  Intestinal Adenocarcinoma  Not Otherwise Specified (NOS)'}, {'histological_type': 'Mucinous (Colloid) Carcinoma'}, {'histological_type': 'Adrenocortical Carcinoma- Oncocytic Type'}, {'histological_type': 'Kidney Chromophobe'}, {'histological_type': 'Adrenocortical carcinoma- Usual Type'}, {'histological_type': 'Non-Seminoma; Teratoma (Immature)|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Lung Papillary Squamous Cell Caricnoma'}, {'histological_type': 'Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Lung Adenocarcinoma Mixed Subtype'}, {'histological_type': 'Thymoma; Type B2|Thymoma; Type B3'}, {'histological_type': 'Mucinous Carcinoma'}, {'histological_type': 'Sarcoma; synovial; poorly differentiated'}, {'histological_type': 'Diffuse malignant mesothelioma - NOS'}, {'histological_type': 'Stomach  Intestinal Adenocarcinoma  Tubular Type'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Thymoma; Type B3'}, {'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'histological_type': 'Stomach  Adenocarcinoma  Not Otherwise Specified (NOS)'}, {'histological_type': 'Malignant Peripheral Nerve Sheath Tumors (MPNST)'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)|Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Thymoma; Type C'}, {'histological_type': 'Seminoma; NOS|Non-Seminoma; Teratoma (Mature)'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Seminoma; NOS'}, {'histological_type': 'Lung Bronchioloalveolar Carcinoma Mucinous'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
