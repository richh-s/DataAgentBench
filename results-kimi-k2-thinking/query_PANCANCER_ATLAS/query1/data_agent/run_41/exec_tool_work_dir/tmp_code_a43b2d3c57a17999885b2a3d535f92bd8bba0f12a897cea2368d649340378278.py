code = """import json
import pandas as pd
import numpy as np

# Read the LGG patient data
lgg_result_key = 'var_functions.query_db:10'
lgg_patients_data = locals()[lgg_result_key]

# If it's a file path, read it
if isinstance(lgg_patients_data, str):
    with open(lgg_patients_data, 'r') as f:
        lgg_patients_data = json.load(f)

# Create a mapping from barcode to histology
lgg_patients = []
barcode_to_histology = {}
for patient in lgg_patients_data:
    desc = patient['Patient_description']
    histology = patient['histological_type']
    
    # Skip histology values in square brackets
    if isinstance(histology, str) and histology.startswith('[') and histology.endswith(']'):
        continue
    
    # Extract TCGA barcode using regex
    import re
    barcode_match = re.search(r'(TCGA-\w{2}-\w{4})', desc)
    if barcode_match:
        barcode = barcode_match.group(1)
        lgg_patients.append({
            'ParticipantBarcode': barcode,
            'histological_type': histology
        })
        barcode_to_histology[barcode] = histology

# Read the IGF2 expression data
igf2_key = 'var_functions.query_db:22'
igf2_data = locals()[igf2_key]

# If it's a file path, read it
if isinstance(igf2_data, str):
    with open(igf2_data, 'r') as f:
        igf2_data = json.load(f)

# Convert to DataFrame for easier processing
df_igf2 = pd.DataFrame(igf2_data)
df_igf2['normalized_count'] = pd.to_numeric(df_igf2['normalized_count'])

# Get only LGG patients
lgg_barcodes = set(barcode_to_histology.keys())
df_lgg_igf2 = df_igf2[df_igf2['ParticipantBarcode'].isin(lgg_barcodes)].copy()

# Add histology Type and compute log10 expression
df_lgg_igf2['histological_type'] = df_lgg_igf2['ParticipantBarcode'].map(barcode_to_histology)
df_lgg_igf2['log10_expression'] = np.log10(df_lgg_igf2['normalized_count'] + 1)

# Compute average log10 expression by histology type
histology_stats = df_lgg_igf2.groupby('histological_type')['log10_expression'].agg(['count', 'mean']).reset_index()

# Sort by histological type and format with 4 decimal places
histology_stats_sorted = histology_stats.sort_values('histological_type')
histology_stats_sorted['mean'] = histology_stats_sorted['mean'].round(4)

# Prepare final results
results = {}
for _, row in histology_stats_sorted.iterrows():
    hist_type = row['histological_type']
    avg_log10 = row['mean']
    results[hist_type] = float(avg_log10)

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-S9-A6U1 (UUID A5E10E2E-5157-487B-88DC-6C70AD5E244A) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-TM-A7C3 and UUID D13AC936-87A9-4164-BDAB-02CCF3908CFE is a FEMALE case of Brain lower grade glioma, documented with vital status = Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Case 8E44FB97-C649-4056-80AC-257CEF61D226, linked to barcode TCGA-S9-A7R2, corresponds to a MALE patient diagnosed with Brain lower grade glioma, with vital status Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': "Patient TCGA-S9-A6TU, registered under UUID 688FC346-A14D-4859-8727-057CD0A0B880, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record c3c41fd2-f0d7-4f46-9e18-cce4626538c2 refers to patient TCGA-HW-7490, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record D81B9957-8C82-4006-B111-449FA9FB95ED refers to patient TCGA-P5-A733, a FEMALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Patient TCGA-DH-A7US (MALE, UUID 82FD02AB-D628-469F-8853-4C603CF04964) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Clinical entry bc3b4816-df1d-44ed-a8c6-f32c8e011a1f identifies patient TCGA-HW-8319, a FEMALE subject with Brain lower grade glioma. Their current vital status is Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Patient TCGA-P5-A5F4 (FEMALE, UUID 0557B788-5AED-4919-85EB-A503AD893D75) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-FG-7637 (MALE, UUID c40ab957-fe46-43b1-992d-b4e2040a3f57) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': "Patient TCGA-FG-A4MW, registered under UUID DCE168B1-D2A9-4409-8437-AB382F6D7D31, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': "Patient TCGA-E1-A7Z3, registered under UUID 3AC41CC6-5DFB-40A1-BD13-5DC7CA2BB6F3, belongs to the Brain lower grade glioma cohort. This FEMALE patient's vital status is Dead.", 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Patient TCGA-S9-A7R4 (MALE, UUID 58650D08-7685-41DE-9AE0-21665F8F449F) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Astrocytoma'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'total_lgg_patients': 513, 'histology_types': ['Astrocytoma', 'Oligoastrocytoma', 'Oligodendroglioma'], 'by_histology': {'Oligodendroglioma': 189, 'Oligoastrocytoma': 130, 'Astrocytoma': 194}}, 'var_functions.query_db:18': [{'ParticipantBarcode': 'TCGA-AB-2908', 'Symbol': 'IGF2', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'Symbol': 'IGF2', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'Symbol': 'IGF2', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'Symbol': 'IGF2', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'Symbol': 'IGF2', 'normalized_count': '613.474'}, {'ParticipantBarcode': 'TCGA-A8-A082', 'Symbol': 'IGF2', 'normalized_count': '630.54'}, {'ParticipantBarcode': 'TCGA-B5-A3FA', 'Symbol': 'IGF2', 'normalized_count': '423.628'}, {'ParticipantBarcode': 'TCGA-BH-A1EX', 'Symbol': 'IGF2', 'normalized_count': '1151.13'}, {'ParticipantBarcode': 'TCGA-BT-A20O', 'Symbol': 'IGF2', 'normalized_count': '369.106'}, {'ParticipantBarcode': 'TCGA-CD-5799', 'Symbol': 'IGF2', 'normalized_count': '3936.02070028943'}], 'var_functions.execute_python:20': {'total_lgg_patients': 513, 'unique_barcodes': 513, 'mapping_size': 513}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
