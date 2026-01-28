code = """import json
import pandas as pd
import numpy as np
import re

# Load LGG patient data with histology
lgg_clinical_file = locals()['var_functions.query_db:24']
with open(lgg_clinical_file, 'r') as f:
    lgg_patients = json.load(f)

# Load IGF2 expression data
igf2_expression_file = locals()['var_functions.query_db:30']
with open(igf2_expression_file, 'r') as f:
    igf2_data = json.load(f)

# Create mapping of patient barcode to histology
patient_histology = {}
for record in lgg_patients:
    pat_desc = str(record.get('Patient_description', ''))
    hist_type = str(record.get('histological_type', ''))
    
    # Extract patient barcode
    match = re.search(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', pat_desc)
    if match and hist_type and hist_type != 'None' and not hist_type.startswith('['):
        patient_barcode = match.group(1)
        patient_histology[patient_barcode] = hist_type

# Convert IGF2 expression to DataFrame
igf2_df = pd.DataFrame(igf2_data)
igf2_df['normalized_count'] = pd.to_numeric(igf2_df['normalized_count'])

# Filter for LGG patients only
igf2_lgg = igf2_df[igf2_df['ParticipantBarcode'].isin(patient_histology.keys())].copy()

# Add histology column
igf2_lgg['histology'] = igf2_lgg['ParticipantBarcode'].map(patient_histology)

# Remove rows with missing histology or expression values
igf2_lgg = igf2_lgg.dropna(subset=['histology', 'normalized_count'])

# Filter out histology types that start with square brackets (already done but double-check)
igf2_lgg = igf2_lgg[~igf2_lgg['histology'].str.startswith('[')]

# Compute log10(normalized_count + 1)
igf2_lgg['log10_expression'] = np.log10(igf2_lgg['normalized_count'] + 1)

# Calculate average by histology type
results = igf2_lgg.groupby('histology')['log10_expression'].agg(['count', 'mean']).reset_index()

# Round to 4 decimal places
results['mean'] = results['mean'].round(4)

print('__RESULT__:')
print(results.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'histological_type': 'Oligodendroglioma', 'histological_type_other': 'None'}, {'histological_type': 'Paraganglioma', 'histological_type_other': 'None'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma', 'histological_type_other': 'None'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'histological_type': 'Thyroid Papillary Carcinoma - Classical/usual'}, {'histological_type': 'Pancreas-Colloid (mucinous non-cystic) Carcinoma'}, {'histological_type': 'None'}, {'histological_type': 'Prostate Adenocarcinoma  Other Subtype'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Pancreas-Adenocarcinoma-Other Subtype'}, {'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Prostate Adenocarcinoma Acinar Type'}, {'histological_type': 'Mucinous Carcinoma'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Pancreas-Adenocarcinoma Ductal Type'}, {'histological_type': 'Metaplastic Carcinoma'}, {'histological_type': 'Oligoastrocytoma'}, {'histological_type': 'Thyroid Papillary Carcinoma - Tall Cell (>= 50% tall cell features)'}, {'histological_type': 'Pancreas-Undifferentiated Carcinoma'}, {'histological_type': 'Mixed Histology (please specify)'}, {'histological_type': 'Infiltrating Lobular Carcinoma'}, {'histological_type': 'Other  specify'}, {'histological_type': 'Medullary Carcinoma'}, {'histological_type': 'Infiltrating Carcinoma NOS'}, {'histological_type': 'Thyroid Papillary Carcinoma - Follicular (>= 99% follicular patterned)'}], 'var_functions.query_db:10': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.execute_python:16': {'lgg_patient_count': 0, 'unique_histologies': [], 'histology_counts': {}}, 'var_functions.query_db:18': [{'total_patients': '544', 'unique_histologies': '5'}], 'var_functions.query_db:22': [{'histological_type': 'Astrocytoma'}, {'histological_type': 'Oligoastrocytoma'}, {'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Paraganglioma'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_lgg_patients': 513, 'sample_patients': [['TCGA-RY-A83X', 'Oligodendroglioma'], ['TCGA-FG-A60K', 'Oligoastrocytoma'], ['TCGA-DB-A4XH', 'Oligoastrocytoma'], ['TCGA-DB-A4XE', 'Oligoastrocytoma'], ['TCGA-DB-A4XC', 'Oligoastrocytoma'], ['TCGA-P5-A5F0', 'Oligodendroglioma'], ['TCGA-S9-A6U1', 'Astrocytoma'], ['TCGA-TM-A7C3', 'Astrocytoma'], ['TCGA-S9-A7R2', 'Astrocytoma'], ['TCGA-TM-A84R', 'Oligodendroglioma']], 'unique_histologies': ['Astrocytoma', 'Oligoastrocytoma', 'Oligodendroglioma']}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
