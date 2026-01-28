code = """import pandas as pd
import json
import re

# Get the file path from storage
clinical_file_path = locals()['var_functions.query_db:2']

# Load clinical data
with open(clinical_file_path, 'r') as f:
    clinical_data = json.load(f)

# Look for LGG patients by examining the data
lgg_keywords = ['glioma', 'astrocytoma', 'oligodendroglioma', 'oligoastrocytoma', 'low grade glioma', 'lower grade glioma']
lgg_patients = []

for record in clinical_data:
    hist_type = str(record.get('histological_type', '')).lower()
    hist_other = str(record.get('histological_type_other', '')).lower()
    
    # Check if this is an LGG patient
    is_lgg = False
    for keyword in lgg_keywords:
        if keyword in hist_type or keyword in hist_other:
            is_lgg = True
            break
    
    if is_lgg:
        # Extract patient barcode
        pat_desc = str(record.get('Patient_description', ''))
        tcga_match = re.search(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', pat_desc)
        if tcga_match:
            patient_barcode = tcga_match.group(1)
            lgg_patients.append({
                'patient_barcode': patient_barcode,
                'histological_type': record.get('histological_type'),
                'histological_type_other': record.get('histological_type_other')
            })

# Get unique histology types
histology_types = {}
for p in lgg_patients:
    hist = p['histological_type']
    if hist and hist != 'None' and not hist.startswith('['):
        histology_types[hist] = histology_types.get(hist, 0) + 1

print('__RESULT__:')
print(json.dumps({
    'lgg_patient_count': len(lgg_patients),
    'unique_histologies': list(histology_types.keys()),
    'histology_counts': histology_types
}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'histological_type': 'Oligodendroglioma', 'histological_type_other': 'None'}, {'histological_type': 'Paraganglioma', 'histological_type_other': 'None'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma', 'histological_type_other': 'None'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'histological_type': 'Thyroid Papillary Carcinoma - Classical/usual'}, {'histological_type': 'Pancreas-Colloid (mucinous non-cystic) Carcinoma'}, {'histological_type': 'None'}, {'histological_type': 'Prostate Adenocarcinoma  Other Subtype'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Pancreas-Adenocarcinoma-Other Subtype'}, {'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Prostate Adenocarcinoma Acinar Type'}, {'histological_type': 'Mucinous Carcinoma'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Pancreas-Adenocarcinoma Ductal Type'}, {'histological_type': 'Metaplastic Carcinoma'}, {'histological_type': 'Oligoastrocytoma'}, {'histological_type': 'Thyroid Papillary Carcinoma - Tall Cell (>= 50% tall cell features)'}, {'histological_type': 'Pancreas-Undifferentiated Carcinoma'}, {'histological_type': 'Mixed Histology (please specify)'}, {'histological_type': 'Infiltrating Lobular Carcinoma'}, {'histological_type': 'Other  specify'}, {'histological_type': 'Medullary Carcinoma'}, {'histological_type': 'Infiltrating Carcinoma NOS'}, {'histological_type': 'Thyroid Papillary Carcinoma - Follicular (>= 99% follicular patterned)'}], 'var_functions.query_db:10': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}]}

exec(code, env_args)
