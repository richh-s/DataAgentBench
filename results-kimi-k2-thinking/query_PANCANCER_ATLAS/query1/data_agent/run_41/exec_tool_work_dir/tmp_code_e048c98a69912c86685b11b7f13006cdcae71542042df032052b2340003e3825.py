code = """import json

# Get LGG patient data from storage
lgg_patients = locals()['var_functions.query_db:10']

# If it's a file path, read it
if isinstance(lgg_patients, str) and lgg_patients.endswith('.json'):
    with open(lgg_patients, 'r') as f:
        lgg_patients = json.load(f)

# Extract barcodes and histology
import re
from collections import defaultdict

lgg_patient_data = []
for patient in lgg_patients:
    desc = patient['Patient_description']
    histology = patient['histological_type']
    
    # Skip histology values in square brackets
    if isinstance(histology, str) and histology.startswith('[') and histology.endswith(']'):
        continue
    
    # Extract TCGA barcode using regex
    barcode_match = re.search(r'(TCGA-\w{2}-\w{4})', desc)
    if barcode_match:
        barcode = barcode_match.group(1)
        lgg_patient_data.append({
            'ParticipantBarcode': barcode,
            'histological_type': histology
        })

# Create barcode list for SQL query
barcodes = [p['ParticipantBarcode'] for p in lgg_patient_data]

print(f"Total LGG patients: {len(barcodes)}")
print(f"Sample barcodes: {barcodes[:5]}")

# Create a mapping from barcode to histology
barcode_to_histology = {p['ParticipantBarcode']: p['histological_type'] for p in lgg_patient_data}

print('__RESULT__:')
print(json.dumps({
    'barcode_to_histology': barcode_to_histology
}, indent=2)[:2000] + "...")"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-S9-A6U1 (UUID A5E10E2E-5157-487B-88DC-6C70AD5E244A) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-TM-A7C3 and UUID D13AC936-87A9-4164-BDAB-02CCF3908CFE is a FEMALE case of Brain lower grade glioma, documented with vital status = Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Case 8E44FB97-C649-4056-80AC-257CEF61D226, linked to barcode TCGA-S9-A7R2, corresponds to a MALE patient diagnosed with Brain lower grade glioma, with vital status Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': "Patient TCGA-S9-A6TU, registered under UUID 688FC346-A14D-4859-8727-057CD0A0B880, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record c3c41fd2-f0d7-4f46-9e18-cce4626538c2 refers to patient TCGA-HW-7490, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record D81B9957-8C82-4006-B111-449FA9FB95ED refers to patient TCGA-P5-A733, a FEMALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Patient TCGA-DH-A7US (MALE, UUID 82FD02AB-D628-469F-8853-4C603CF04964) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Clinical entry bc3b4816-df1d-44ed-a8c6-f32c8e011a1f identifies patient TCGA-HW-8319, a FEMALE subject with Brain lower grade glioma. Their current vital status is Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Patient TCGA-P5-A5F4 (FEMALE, UUID 0557B788-5AED-4919-85EB-A503AD893D75) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-FG-7637 (MALE, UUID c40ab957-fe46-43b1-992d-b4e2040a3f57) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': "Patient TCGA-FG-A4MW, registered under UUID DCE168B1-D2A9-4409-8437-AB382F6D7D31, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': "Patient TCGA-E1-A7Z3, registered under UUID 3AC41CC6-5DFB-40A1-BD13-5DC7CA2BB6F3, belongs to the Brain lower grade glioma cohort. This FEMALE patient's vital status is Dead.", 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Patient TCGA-S9-A7R4 (MALE, UUID 58650D08-7685-41DE-9AE0-21665F8F449F) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Astrocytoma'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'total_lgg_patients': 513, 'histology_types': ['Astrocytoma', 'Oligoastrocytoma', 'Oligodendroglioma'], 'by_histology': {'Oligodendroglioma': 189, 'Oligoastrocytoma': 130, 'Astrocytoma': 194}}}

exec(code, env_args)
