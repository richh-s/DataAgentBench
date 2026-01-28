code = """import json
import math
import re

# Load LGG patient data
clinical_file_path = locals()['var_functions.query_db:10']
with open(clinical_file_path, 'r') as f:
    lgg_patients = json.load(f)

# Create dictionary mapping barcodes to histological type
lgg_patient_dict = {}
for patient in lgg_patients:
    patient_desc = patient.get('Patient_description', '')
    hist_type = patient.get('histological_type', '')
    
    # Skip if histological_type is empty or enclosed in brackets
    if not hist_type or hist_type.startswith('[') or hist_type.endswith(']'):
        continue
    
    # Extract barcode from Patient_description
    barcode_match = re.search(r'(TCGA-\w{2}-\w{4})', patient_desc)
    if barcode_match:
        barcode = barcode_match.group(1)
        lgg_patient_dict[barcode] = hist_type

print(f"LGG patients with valid histology: {len(lgg_patient_dict)}")
print(f"Sample: {list(lgg_patient_dict.items())[:2]}")

# Load IGF2 expression data
gene_file_path = locals()['var_functions.query_db:20']
with open(gene_file_path, 'r') as f:
    igf2_expression = json.load(f)

# Filter for LGG patients and calculate log10 expression
lgg_igf2_by_histology = {}
valid_count = 0

for record in igf2_expression:
    barcode = record.get('ParticipantBarcode')
    if barcode in lgg_patient_dict:
        try:
            normalized_count = float(record.get('normalized_count', 0))
            if normalized_count > 0:
                hist_type = lgg_patient_dict[barcode]
                log_expr = math.log10(normalized_count + 1)
                
                if hist_type not in lgg_igf2_by_histology:
                    lgg_igf2_by_histology[hist_type] = []
                lgg_igf2_by_histology[hist_type].append(log_expr)
                valid_count += 1
        except (ValueError, TypeError):
            continue

print(f"Total valid IGF2 expression records for LGG: {valid_count}")

# Calculate averages by histology type
results = {}
for hist_type, log_values in lgg_igf2_by_histology.items():
    avg_log = sum(log_values) / len(log_values)
    results[hist_type] = {
        'average_log10_expression': round(avg_log, 4),
        'sample_count': len(log_values)
    }

print(f"Results by histology: {results}")

# Prepare output in required format
output = {
    'total_lgg_patients_analyzed': len(lgg_patient_dict),
    'patients_with_igf2_expression': valid_count,
    'average_log10_expression_by_histology': results
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-S9-A6U1 (UUID A5E10E2E-5157-487B-88DC-6C70AD5E244A) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-TM-A7C3 and UUID D13AC936-87A9-4164-BDAB-02CCF3908CFE is a FEMALE case of Brain lower grade glioma, documented with vital status = Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Case 8E44FB97-C649-4056-80AC-257CEF61D226, linked to barcode TCGA-S9-A7R2, corresponds to a MALE patient diagnosed with Brain lower grade glioma, with vital status Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': "Patient TCGA-S9-A6TU, registered under UUID 688FC346-A14D-4859-8727-057CD0A0B880, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record c3c41fd2-f0d7-4f46-9e18-cce4626538c2 refers to patient TCGA-HW-7490, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record D81B9957-8C82-4006-B111-449FA9FB95ED refers to patient TCGA-P5-A733, a FEMALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Patient TCGA-DH-A7US (MALE, UUID 82FD02AB-D628-469F-8853-4C603CF04964) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Clinical entry bc3b4816-df1d-44ed-a8c6-f32c8e011a1f identifies patient TCGA-HW-8319, a FEMALE subject with Brain lower grade glioma. Their current vital status is Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Patient TCGA-P5-A5F4 (FEMALE, UUID 0557B788-5AED-4919-85EB-A503AD893D75) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-FG-7637 (MALE, UUID c40ab957-fe46-43b1-992d-b4e2040a3f57) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': "Patient TCGA-FG-A4MW, registered under UUID DCE168B1-D2A9-4409-8437-AB382F6D7D31, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': "Patient TCGA-E1-A7Z3, registered under UUID 3AC41CC6-5DFB-40A1-BD13-5DC7CA2BB6F3, belongs to the Brain lower grade glioma cohort. This FEMALE patient's vital status is Dead.", 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Patient TCGA-S9-A7R4 (MALE, UUID 58650D08-7685-41DE-9AE0-21665F8F449F) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Astrocytoma'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'total_lgg_patients': 513, 'patients_with_valid_histology': 513, 'unique_histology_types': ['Astrocytoma', 'Oligoastrocytoma', 'Oligodendroglioma'], 'sample_data': [{'ParticipantBarcode': 'TCGA-RY-A83X', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-FG-A60K', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XH', 'histological_type': 'Oligoastrocytoma'}]}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
