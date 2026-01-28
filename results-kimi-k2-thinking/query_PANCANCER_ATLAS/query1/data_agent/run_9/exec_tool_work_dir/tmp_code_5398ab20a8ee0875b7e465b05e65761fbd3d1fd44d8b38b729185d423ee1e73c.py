code = """import json, math, re
from collections import defaultdict

# Load data from storage variables
lgg_patients = var_functions.query_db:22
igf2_expression = var_functions.query_db:26

# Filter valid LGG patients with non-bracketed histology
lgg_map = {}  # barcode -> histology
for p in lgg_patients:
    hist = p.get('histological_type')
    if not hist or not isinstance(hist, str):
        continue
    hist_clean = hist.strip()
    if hist_clean.startswith('[') and hist_clean.endswith(']'):
        continue
    desc = p.get('Patient_description', '')
    matches = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if matches:
        barcode = matches.group(1)
        lgg_map[barcode] = hist_clean

# Build IGF2 expression map for all patients
igf2_map = {rec['ParticipantBarcode']: float(rec['normalized_count']) 
            for rec in igf2_expression if rec['Symbol'] == 'IGF2'}

# Find intersection and compute log10 values
hist_values = defaultdict(list)
for barcode in set(lgg_map.keys()) & set(igf2_map.keys()):
    hist = lgg_map[barcode]
    log_val = math.log10(igf2_map[barcode] + 1)
    hist_values[hist].append(log_val)

# Calculate averages with 4 decimal places
averages = {hist: round(sum(vals)/len(vals), 4) 
           for hist, vals in sorted(hist_values.items()) if len(vals) > 0}

# Print results in required format
print('Total LGG patients:', len(lgg_patients))
print('Valid LGG with histology:', len(lgg_map))
print('IGF2 records:', len(igf2_map))
print('Matching patients:', len(set(lgg_map.keys()) & set(igf2_map.keys())))
print('Histology groups:', len(averages))
print('__RESULT__:')
print(json.dumps(averages))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A83X'}, {'Patient_description': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A5F0'}, {'Patient_description': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A84R'}, {'Patient_description': 'Patient TCGA-DH-A7US (MALE, UUID 82FD02AB-D628-469F-8853-4C603CF04964) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A7US'}, {'Patient_description': 'Patient TCGA-P5-A5F4 (FEMALE, UUID 0557B788-5AED-4919-85EB-A503AD893D75) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A5F4'}, {'Patient_description': "Patient TCGA-IK-7675, registered under UUID a5f851c5-6130-4ea1-9f86-be59331a92f7, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Oligodendroglioma', 'patient_id': '7675'}, {'Patient_description': 'Patient TCGA-HW-A5KJ (MALE, UUID 8996DC64-8C5E-4E07-8ED8-2EB11C03626B) is enrolled in the study of Brain lower grade glioma. Vital status: Dead.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A5KJ'}, {'Patient_description': 'In the Brain lower grade glioma dataset, patient TCGA-S9-A7J3 (UUID 032096A6-1923-44B9-A1CB-181BED041C8E) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A7J3'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XG and UUID 7704E4A8-C7AA-4288-B1ED-68C23ABBE924 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A4XG'}, {'Patient_description': 'Patient TCGA-VM-A8CA (UUID CDD1FD4C-3427-496C-8391-4AEB6730D3CC) is a MALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A8CA'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
