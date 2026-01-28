code = """import json
import re
from collections import defaultdict

# Load the LGG patient records
data_path = "var_functions.query_db:8"  # This is a file path since result was too large
try:
    with open(data_path, 'r') as f:
        lgg_patients = json.load(f)
except:
    # Try as direct variable
    lgg_patients = locals().get('var_functions.query_db:8', [])

# If it's already a list, use it directly
if not isinstance(lgg_patients, list):
    # Try to read from file
    import os
    if os.path.exists(data_path):
        with open(data_path, 'r') as f:
            lgg_patients = json.load(f)
    else:
        lgg_patients = []

print(f"Loaded {len(lgg_patients)} LGG patient records")

# Extract patient barcodes and histology
lgg_data = []
for record in lgg_patients:
    patient_desc = record.get('Patient_description', '')
    histology = record.get('histological_type', '')
    
    # Extract barcode (TCGA-XX-XXXX format)
    barcode_match = re.search(r'(TCGA-\w{2}-\w{4})', patient_desc)
    if barcode_match:
        barcode = barcode_match.group(1)
        lgg_data.append({
            'barcode': barcode,
            'histology': histology,
            'patient_desc': patient_desc
        })

print(f"Extracted {len(lgg_data)} valid barcodes")
print("Sample records:", lgg_data[:3])

# Save to JSON for next step
import json as js
output = js.dumps(lgg_data)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.'}, {'Patient_description': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.'}, {'Patient_description': 'Patient TCGA-S9-A6U1 (UUID A5E10E2E-5157-487B-88DC-6C70AD5E244A) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-TM-A7C3 and UUID D13AC936-87A9-4164-BDAB-02CCF3908CFE is a FEMALE case of Brain lower grade glioma, documented with vital status = Dead.'}, {'Patient_description': 'Case 8E44FB97-C649-4056-80AC-257CEF61D226, linked to barcode TCGA-S9-A7R2, corresponds to a MALE patient diagnosed with Brain lower grade glioma, with vital status Dead.'}, {'Patient_description': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
