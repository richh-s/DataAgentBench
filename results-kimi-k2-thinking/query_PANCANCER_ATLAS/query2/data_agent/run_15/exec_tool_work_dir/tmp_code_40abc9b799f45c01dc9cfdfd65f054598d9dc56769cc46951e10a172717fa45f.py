code = """import json
import os
import glob
import re

# Get all JSON files
json_files = glob.glob('*.json')
print("Found JSON files:", json_files[:10])

cdh1_mutations = []
brca_patients = []

# Load CDH1 mutations
for fname in json_files:
    try:
        with open(fname, 'r') as f:
            data = json.load(f)
            if data and isinstance(data, list) and len(data) > 0:
                if isinstance(data[0], dict) and 'Hugo_Symbol' in data[0]:
                    cdh1_mutations = data
                    print(f"Loaded CDH1 mutations: {len(cdh1_mutations)}")
                    break
    except:
        continue

# Load BRCA patients
for fname in json_files:
    try:
        with open(fname, 'r') as f:
            data = json.load(f)
            if data and isinstance(data, list) and len(data) > 0:
                if isinstance(data[0], dict) and 'Patient_description' in data[0]:
                    brca_patients = data
                    print(f"Loaded BRCA patients: {len(brca_patients)}")
                    break
    except:
        continue

# Extract BRCA barcodes and histology
brca_data_dict = {}
for patient in brca_patients:
    desc = patient.get('Patient_description', '')
    match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    if match:
        barcode = match.group(0)
        histo = patient.get('histological_type', 'Unknown')
        brca_data_dict[barcode] = histo

print(f"BRCA patients: {len(brca_data_dict)}")

# Extract CDH1 mutation barcodes
cdh1_barcodes = set([m.get('ParticipantBarcode') for m in cdh1_mutations if m.get('ParticipantBarcode')])
print(f"CDH1 mutations (all cancers): {len(cdh1_barcodes)}")

# Find overlap
brca_barcodes = set(brca_data_dict.keys())
brca_cdh1_overlap = brca_barcodes.intersection(cdh1_barcodes)
print(f"BRCA patients with CDH1 mutations: {len(brca_cdh1_overlap)}")

# Count by histology
from collections import Counter, defaultdict

total_by_histo = Counter()
mutated_by_histo = defaultdict(int)

for barcode, histo in brca_data_dict.items():
    total_by_histo[histo] += 1

for barcode in brca_cdh1_overlap:
    histo = brca_data_dict[barcode]
    mutated_by_histo[histo] += 1

# Calculate percentages
results = []
for histo in total_by_histo:
    total = total_by_histo[histo]
    mutated = mutated_by_histo.get(histo, 0)
    percent = (mutated / total * 100) if total > 0 else 0
    if total >= 3:  # At least 3 patients
        results.append({
            'histological_type': str(histo),
            'total_patients': int(total),
            'cdh1_mutated_patients': int(mutated),
            'mutation_percentage': round(float(percent), 2)
        })

# Sort and get top 3
results.sort(key=lambda x: x['mutation_percentage'], reverse=True)
top_3 = results[:3]

print("Results:")
for item in top_3:
    print(f"{item['histological_type']}: {item['mutation_percentage']}% ({item['cdh1_mutated_patients']}/{item['total_patients']})")

print('__RESULT__:')
print(json.dumps(top_3))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry C07B122E-AC50-4DB2-ADD2-5617A5D0E976 identifies patient TCGA-GM-A2DA, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Dead.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-3C-AAAU and UUID 6E7D5EC6-A469-467C-B748-237353C23416 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-A7-A26I, registered under UUID b2ecbc0f-2c30-4200-8d5e-7b95424bcadb, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 523E24A2-51B9-4658-BE2F-42E5FCCEBB17 refers to patient TCGA-A7-A5ZW, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-C8-A26Z and UUID dc11b1c7-1f00-4813-b4b5-ecf776b2eb37 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.list_db:14': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'barcodes': [], 'patient_data': []}, 'var_functions.execute_python:22': {'cdh1_barcodes': [], 'cdh1_mutations': [], 'brca_patients': []}}

exec(code, env_args)
