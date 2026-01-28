code = """import json
import re

# Get the file path for LGG clinical data
lgg_clinical_file = locals()['var_functions.query_db:24']

# Load the data
with open(lgg_clinical_file, 'r') as f:
    lgg_patients = json.load(f)

# Extract patient barcodes and histology
patient_histology = {}
for record in lgg_patients:
    pat_desc = str(record.get('Patient_description', ''))
    hist_type = str(record.get('histological_type', ''))
    
    # Extract TCGA barcode
    match = re.search(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', pat_desc)
    if match and hist_type and hist_type != 'None' and not hist_type.startswith('['):
        patient_barcode = match.group(1)
        patient_histology[patient_barcode] = hist_type

print('__RESULT__:')
print(json.dumps({
    'total_lgg_patients': len(patient_histology),
    'sample_patients': list(patient_histology.items())[:10],
    'unique_histologies': list(set(patient_histology.values()))
}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'histological_type': 'Oligodendroglioma', 'histological_type_other': 'None'}, {'histological_type': 'Paraganglioma', 'histological_type_other': 'None'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma', 'histological_type_other': 'None'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'histological_type': 'Thyroid Papillary Carcinoma - Classical/usual'}, {'histological_type': 'Pancreas-Colloid (mucinous non-cystic) Carcinoma'}, {'histological_type': 'None'}, {'histological_type': 'Prostate Adenocarcinoma  Other Subtype'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Pancreas-Adenocarcinoma-Other Subtype'}, {'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Prostate Adenocarcinoma Acinar Type'}, {'histological_type': 'Mucinous Carcinoma'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Pancreas-Adenocarcinoma Ductal Type'}, {'histological_type': 'Metaplastic Carcinoma'}, {'histological_type': 'Oligoastrocytoma'}, {'histological_type': 'Thyroid Papillary Carcinoma - Tall Cell (>= 50% tall cell features)'}, {'histological_type': 'Pancreas-Undifferentiated Carcinoma'}, {'histological_type': 'Mixed Histology (please specify)'}, {'histological_type': 'Infiltrating Lobular Carcinoma'}, {'histological_type': 'Other  specify'}, {'histological_type': 'Medullary Carcinoma'}, {'histological_type': 'Infiltrating Carcinoma NOS'}, {'histological_type': 'Thyroid Papillary Carcinoma - Follicular (>= 99% follicular patterned)'}], 'var_functions.query_db:10': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.execute_python:16': {'lgg_patient_count': 0, 'unique_histologies': [], 'histology_counts': {}}, 'var_functions.query_db:18': [{'total_patients': '544', 'unique_histologies': '5'}], 'var_functions.query_db:22': [{'histological_type': 'Astrocytoma'}, {'histological_type': 'Oligoastrocytoma'}, {'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Paraganglioma'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
