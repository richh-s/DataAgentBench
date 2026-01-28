code = """import json
import re

# Load all LGG patient records from the previous query
lgg_patients = locals().get('var_functions.query_db:8')

# If it's a string (file path), load it
if isinstance(lgg_patients, str):
    with open(lgg_patients, 'r') as f:
        lgg_patients = json.load(f)

print(f"Total LGG patient records: {len(lgg_patients)}")

# Extract barcodes and histology, excluding records with histology in square brackets
lgg_data = []
excluded_count = 0

for record in lgg_patients:
    patient_desc = record.get('Patient_description', '')
    histology = record.get('histological_type', '')
    
    # Skip histology values that are enclosed in square brackets like [Not Applicable]
    if histology.startswith('[') and histology.endswith(']'):
        excluded_count += 1
        continue
    
    # Extract barcode (TCGA-XX-XXXX format)
    barcode_match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', patient_desc)
    if barcode_match:
        barcode = barcode_match.group(1)
        lgg_data.append({
            'barcode': barcode,
            'histology': histology,
            'patient_desc': patient_desc
        })

print(f"Valid records extracted: {len(lgg_data)}")
print(f"Records excluded (square brackets): {excluded_count}")

# Create a set of all barcodes for the SQL query
barcode_list = [item['barcode'] for item in lgg_data]
print(f"Total unique barcodes to query: {len(barcode_list)}")

# Save the complete lgg_data for later use
result = {
    'lgg_data': lgg_data,
    'barcode_list': barcode_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.'}, {'Patient_description': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.'}, {'Patient_description': 'Patient TCGA-S9-A6U1 (UUID A5E10E2E-5157-487B-88DC-6C70AD5E244A) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-TM-A7C3 and UUID D13AC936-87A9-4164-BDAB-02CCF3908CFE is a FEMALE case of Brain lower grade glioma, documented with vital status = Dead.'}, {'Patient_description': 'Case 8E44FB97-C649-4056-80AC-257CEF61D226, linked to barcode TCGA-S9-A7R2, corresponds to a MALE patient diagnosed with Brain lower grade glioma, with vital status Dead.'}, {'Patient_description': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [{'barcode': 'TCGA-RY-A83X', 'histology': 'Oligodendroglioma', 'patient_desc': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.'}, {'barcode': 'TCGA-FG-A60K', 'histology': 'Oligoastrocytoma', 'patient_desc': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.'}, {'barcode': 'TCGA-DB-A4XH', 'histology': 'Oligoastrocytoma', 'patient_desc': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.'}, {'barcode': 'TCGA-DB-A4XE', 'histology': 'Oligoastrocytoma', 'patient_desc': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.'}, {'barcode': 'TCGA-DB-A4XC', 'histology': 'Oligoastrocytoma', 'patient_desc': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.'}, {'barcode': 'TCGA-P5-A5F0', 'histology': 'Oligodendroglioma', 'patient_desc': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.'}, {'barcode': 'TCGA-S9-A6U1', 'histology': 'Astrocytoma', 'patient_desc': 'Patient TCGA-S9-A6U1 (UUID A5E10E2E-5157-487B-88DC-6C70AD5E244A) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.'}, {'barcode': 'TCGA-TM-A7C3', 'histology': 'Astrocytoma', 'patient_desc': 'The individual with barcode TCGA-TM-A7C3 and UUID D13AC936-87A9-4164-BDAB-02CCF3908CFE is a FEMALE case of Brain lower grade glioma, documented with vital status = Dead.'}, {'barcode': 'TCGA-S9-A7R2', 'histology': 'Astrocytoma', 'patient_desc': 'Case 8E44FB97-C649-4056-80AC-257CEF61D226, linked to barcode TCGA-S9-A7R2, corresponds to a MALE patient diagnosed with Brain lower grade glioma, with vital status Dead.'}, {'barcode': 'TCGA-TM-A84R', 'histology': 'Oligodendroglioma', 'patient_desc': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.'}], 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-DB-A4XD', 'Symbol': 'IGF2', 'normalized_count': '347.495'}, {'ParticipantBarcode': 'TCGA-DH-A7US', 'Symbol': 'IGF2', 'normalized_count': '418.886'}, {'ParticipantBarcode': 'TCGA-TM-A84T', 'Symbol': 'IGF2', 'normalized_count': '291.586'}]}

exec(code, env_args)
