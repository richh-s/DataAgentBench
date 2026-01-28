code = """import json
import os
import glob
import re

# Get all JSON files
json_files = glob.glob('*.json')
print(f"Found {len(json_files)} JSON files: {json_files[:10]}")

cdh1_mutations = []
brca_patients = []

# Load the data from files
for fname in json_files:
    try:
        with open(fname, 'r') as f:
            data = json.load(f)
            
            # Check if this contains mutation data (has Hugo_Symbol field)
            if data and isinstance(data, list) and len(data) > 0:
                if isinstance(data[0], dict) and 'Hugo_Symbol' in data[0]:
                    cdh1_mutations = data
                    print(f"Loaded CDH1 mutations from {fname}: {len(cdh1_mutations)} records")
                elif isinstance(data[0], dict) and 'Patient_description' in data[0]:
                    brca_patients = data
                    print(f"Loaded BRCA patients from {fname}: {len(brca_patients)} records")
    except Exception as e:
        print(f"Error reading {fname}: {e}")
        continue

# Process BRCA patients
brca_barcodes = {}
for patient in brca_patients:
    desc = patient.get('Patient_description', '')
    match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    if match:
        barcode = match.group(0)
        histology = patient.get('histological_type', 'Unknown')
        brca_barcodes[barcode] = {
            'histological_type': histology,
            'barcode': barcode
        }

print(f"Extracted {len(brca_barcodes)} BRCA patient barcodes")

# Process CDH1 mutations
cdh1_barcodes = set([m.get('ParticipantBarcode', '') for m in cdh1_mutations if m.get('ParticipantBarcode')])
print(f"Found {len(cdh1_barcodes)} patients with CDH1 mutations in all cancer types")

# Find BRCA patients with CDH1 mutations
brca_barcodes_set = set(brca_barcodes.keys())
brca_with_cdh1 = brca_barcodes_set.intersection(cdh1_barcodes)
print(f"BRCA patients with CDH1 mutations: {len(brca_with_cdh1)}")

# Count by histological type
from collections import defaultdict

histology_total = defaultdict(int)
histology_mutated = defaultdict(int)

# Count total patients per histology
for barcode, data in brca_barcodes.items():
    hist = data['histological_type']
    histology_total[hist] += 1

# Count mutated patients per histology
for barcode in brca_with_cdh1:
    hist = brca_barcodes.get(barcode, {}).get('histological_type', 'Unknown')
    histology_mutated[hist] += 1

# Calculate percentages and create results
results = []
for hist in histology_total:
    total = histology_total[hist]
    mutated = histology_mutated.get(hist, 0)
    percentage = (mutated / total * 100) if total > 0 else 0
    if total >= 5:  # Only include histological types with at least 5 patients
        results.append({
            'histological_type': hist,
            'total_patients': total,
            'cdh1_mutated_patients': mutated,
            'mutation_percentage': round(percentage, 2)
        })

# Sort by mutation percentage descending
results_sorted = sorted(results, key=lambda x: x['mutation_percentage'], reverse=True)

# Get top 3
top_3 = results_sorted[:3]

print(f"\nTop 3 histological types:")
for i, item in enumerate(top_3, 1):
    print(f"{i}. {item['histological_type']}: {item['mutation_percentage']}% "
          f"({item['cdh1_mutated_patients']}/{item['total_patients']} patients)")

# If we have results, save them
if top_3:
    final_result = top_3
else:
    # Fallback with empty results
    final_result = [
        {"histological_type": "No data", "total_patients": 0, "cdh1_mutated_patients": 0, "mutation_percentage": 0.0},
        {"histological_type": "No data", "total_patients": 0, "cdh1_mutated_patients": 0, "mutation_percentage": 0.0},
        {"histological_type": "No data", "total_patients": 0, "cdh1_mutated_patients": 0, "mutation_percentage": 0.0}
    ]

print('__RESULT__:')
print(json.dumps(final_result, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry C07B122E-AC50-4DB2-ADD2-5617A5D0E976 identifies patient TCGA-GM-A2DA, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Dead.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-3C-AAAU and UUID 6E7D5EC6-A469-467C-B748-237353C23416 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-A7-A26I, registered under UUID b2ecbc0f-2c30-4200-8d5e-7b95424bcadb, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 523E24A2-51B9-4658-BE2F-42E5FCCEBB17 refers to patient TCGA-A7-A5ZW, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-C8-A26Z and UUID dc11b1c7-1f00-4813-b4b5-ecf776b2eb37 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.list_db:14': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'barcodes': [], 'patient_data': []}, 'var_functions.execute_python:22': {'cdh1_barcodes': [], 'cdh1_mutations': [], 'brca_patients': []}}

exec(code, env_args)
