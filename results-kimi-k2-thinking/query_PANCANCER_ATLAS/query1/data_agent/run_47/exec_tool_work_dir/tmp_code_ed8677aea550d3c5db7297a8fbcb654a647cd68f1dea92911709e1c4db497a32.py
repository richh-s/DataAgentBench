code = """import json
import pandas as pd
import numpy as np

# Load data
clinical_file = locals()['var_functions.query_db:24']
expression_file = locals()['var_functions.query_db:34']

with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)
with open(expression_file, 'r') as f:
    expression_data = json.load(f)

print('Loaded', len(clinical_data), 'clinical records')
print('Loaded', len(expression_data), 'expression records')

# Extract LGG patients
lgg_patients = []
for record in clinical_data:
    patient_desc_lower = record.get('Patient_description', '').lower()
    if 'brain lower grade glioma' in patient_desc_lower:
        desc = record.get('Patient_description', '')
        # Extract TCGA barcode (look for TCGA-XX-XXXX pattern)
        parts = desc.split()
        barcode = ''
        for part in parts:
            if part.startswith('TCGA-') and len(part) >= 12:
                barcode = part
                break
        
        histology = record.get('histological_type', '')
        # Only include valid histology not enclosed in square brackets
        if histology.strip() and not (histology.startswith('[') and histology.endswith(']')):
            lgg_patients.append({
                'ParticipantBarcode': barcode,
                'histological_type': histology
            })

clinical_df = pd.DataFrame(lgg_patients)
print('LGG patients found:', len(clinical_df))
print('Histology types:', clinical_df['histological_type'].value_counts().to_dict())

# Process expression data
expression_df = pd.DataFrame(expression_data)
expression_df['normalized_count'] = pd.to_numeric(expression_df['normalized_count'], errors='coerce')
igf2_df = expression_df[expression_df['Symbol'] == 'IGF2']

# Merge datasets
merged_df = clinical_df.merge(igf2_df, on='ParticipantBarcode', how='inner')
print('Patients with IGF2 expression:', len(merged_df))
print('By histology:', merged_df['histological_type'].value_counts().to_dict())

# Calculate log10 expression and averages
merged_df['log10_expression'] = np.log10(merged_df['normalized_count'] + 1)
results = merged_df.groupby('histological_type')['log10_expression'].agg(['count', 'mean']).round(4)

# Create output dictionary
output_dict = {}
for histology in results.index:
    output_dict[histology] = float(results.loc[histology, 'mean'])

print('Final results:', output_dict)
print('__RESULT__:')
print(json.dumps(output_dict))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'available_vars': ['var_functions.query_db:2']}, 'var_functions.query_db:16': [], 'var_functions.query_db:18': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'histological_type': 'Stomach  Adenocarcinoma  Diffuse Type'}, {'histological_type': 'Prostate Adenocarcinoma  Other Subtype'}, {'histological_type': 'Fibrolamellar Carcinoma'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Untreated primary (de novo) GBM'}, {'histological_type': 'Synovial Sarcoma - Biphasic'}, {'histological_type': 'Mucinous Adenocarcinoma of Endocervical Type'}, {'histological_type': 'Pancreas-Adenocarcinoma-Other Subtype'}, {'histological_type': 'Thymoma; Type B1|Thymoma; Type B2'}, {'histological_type': 'Seminoma; NOS|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)'}, {'histological_type': 'Non-Seminoma; Choriocarcinoma|Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)'}, {'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Immature)'}, {'histological_type': 'Lung Clear Cell Adenocarcinoma'}, {'histological_type': 'Seminoma; NOS|Non-Seminoma; Embryonal Carcinoma'}, {'histological_type': 'Pheochromocytoma'}, {'histological_type': 'Synovial Sarcoma - Monophasic'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)'}, {'histological_type': 'Non-Seminoma; Teratoma (Immature)|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Embryonal Carcinoma'}, {'histological_type': 'Prostate Adenocarcinoma Acinar Type'}, {'histological_type': 'Kidney Papillary Renal Cell Carcinoma'}, {'histological_type': 'Endocervical Type of Adenocarcinoma'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)|Seminoma; NOS'}, {'histological_type': 'Cervical Squamous Cell Carcinoma'}, {'histological_type': 'Leiomyosarcoma (LMS)'}, {'histological_type': 'Stomach  Intestinal Adenocarcinoma  Not Otherwise Specified (NOS)'}, {'histological_type': 'Mucinous (Colloid) Carcinoma'}, {'histological_type': 'Adrenocortical Carcinoma- Oncocytic Type'}, {'histological_type': 'Kidney Chromophobe'}, {'histological_type': 'Adrenocortical carcinoma- Usual Type'}, {'histological_type': 'Non-Seminoma; Teratoma (Immature)|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Lung Papillary Squamous Cell Caricnoma'}, {'histological_type': 'Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Lung Adenocarcinoma Mixed Subtype'}, {'histological_type': 'Thymoma; Type B2|Thymoma; Type B3'}, {'histological_type': 'Mucinous Carcinoma'}, {'histological_type': 'Sarcoma; synovial; poorly differentiated'}, {'histological_type': 'Diffuse malignant mesothelioma - NOS'}, {'histological_type': 'Stomach  Intestinal Adenocarcinoma  Tubular Type'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Thymoma; Type B3'}, {'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'histological_type': 'Stomach  Adenocarcinoma  Not Otherwise Specified (NOS)'}, {'histological_type': 'Malignant Peripheral Nerve Sheath Tumors (MPNST)'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)|Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Thymoma; Type C'}, {'histological_type': 'Seminoma; NOS|Non-Seminoma; Teratoma (Mature)'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Seminoma; NOS'}, {'histological_type': 'Lung Bronchioloalveolar Carcinoma Mucinous'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:30': {'total': 36, 'first_few': [{'ParticipantBarcode': 'TCGA-RY-A83X', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-FG-A60K', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XH', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XE', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XC', 'histological_type': 'Oligoastrocytoma'}]}, 'var_functions.query_db:32': [{'ParticipantBarcode': 'TCGA-DH-A7US', 'Symbol': 'IGF2', 'normalized_count': '418.886'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': {'Oligodendroglioma': 2.6231}}

exec(code, env_args)
