code = """import json

# Load the LGG patient file
lgg_file = var_functions.query_db:18
with open(lgg_file, 'r') as f:
    lgg_patients = json.load(f)

print(f"Total LGG patients extracted: {len(lgg_patients)}")

# Show structure of data
if lgg_patients:
    print("\nSample record:")
    print(lgg_patients[0])

# Filter histology that are not bracketed (not enclosed in square brackets)
valid_histology_patients = []
for p in lgg_patients:
    hist = p.get('histological_type', '')
    # Filter out histology strings that are bracketed or contain brackets
    if hist and isinstance(hist, str) and not hist.startswith('[') and not hist.endswith(']') and '[' not in hist and ']' not in hist:
        valid_histology_patients.append(p)

print(f"\nPatients with valid histology annotations (non-bracketed): {len(valid_histology_patients)}")

# Extract participant barcodes from Patient_description
tcga_barcodes = []
for p in valid_histology_patients:
    desc = p.get('Patient_description', '')
    # Extract TCGA barcode pattern (TCGA-XX-YYYY)
    import re
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if match:
        barcode = match.group(1)
        tcga_barcodes.append(barcode)
        # For later use, store the barcode with patient record
        p['ParticipantBarcode'] = barcode

print(f"Extracted {len(tcga_barcodes)} TCGA barcodes for LGG patients")

# Show unique histology types
histology_types = list(set(p['histological_type'] for p in valid_histology_patients))
print(f"\nUnique histology types found: {histology_types}")

# Save the processed data for next steps
print('\n__RESULT__:')
print(json.dumps({'lgg_patients': valid_histology_patients, 
                  'barcodes': tcga_barcodes, 
                  'histology_types': histology_types}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A83X'}, {'Patient_description': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A5F0'}, {'Patient_description': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A84R'}, {'Patient_description': 'Patient TCGA-DH-A7US (MALE, UUID 82FD02AB-D628-469F-8853-4C603CF04964) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A7US'}, {'Patient_description': 'Patient TCGA-P5-A5F4 (FEMALE, UUID 0557B788-5AED-4919-85EB-A503AD893D75) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A5F4'}, {'Patient_description': "Patient TCGA-IK-7675, registered under UUID a5f851c5-6130-4ea1-9f86-be59331a92f7, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Oligodendroglioma', 'patient_id': '7675'}, {'Patient_description': 'Patient TCGA-HW-A5KJ (MALE, UUID 8996DC64-8C5E-4E07-8ED8-2EB11C03626B) is enrolled in the study of Brain lower grade glioma. Vital status: Dead.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A5KJ'}, {'Patient_description': 'In the Brain lower grade glioma dataset, patient TCGA-S9-A7J3 (UUID 032096A6-1923-44B9-A1CB-181BED041C8E) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A7J3'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XG and UUID 7704E4A8-C7AA-4288-B1ED-68C23ABBE924 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A4XG'}, {'Patient_description': 'Patient TCGA-VM-A8CA (UUID CDD1FD4C-3427-496C-8391-4AEB6730D3CC) is a MALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligodendroglioma', 'patient_id': 'A8CA'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
