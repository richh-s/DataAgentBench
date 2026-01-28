code = """import json
import os
import glob

# Find all JSON files in the current directory
json_files = glob.glob('*.json')
print("Available JSON files:", json_files)

# Try to find CDH1 mutations and BRCA patients data
for fname in json_files:
    try:
        with open(fname, 'r') as f:
            data = json.load(f)
            print(f"\nFile: {fname}")
            print(f"Length: {len(data)}")
            if len(data) > 0:
                print("Sample item:", data[0])
                # Check if this is CDH1 mutations (has Hugo_Symbol field)
                if isinstance(data[0], dict) and 'Hugo_Symbol' in data[0]:
                    cdh1_file = fname
                    print("** This is CDH1 mutations file **")
                # Check if this is BRCA patients (has Patient_description with Breast)
                elif isinstance(data[0], dict) and 'Patient_description' in data[0]:
                    if 'Breast' in data[0]['Patient_description']:
                        brca_file = fname
                        print("** This is BRCA patients file **")
    except Exception as e:
        print(f"Error reading {fname}: {e}")
        continue

# If we found both files, process them
try:
    # Load CDH1 mutations
    with open(cdh1_file, 'r') as f:
        cdh1_mutations = json.load(f)
    
    # Load BRCA patients
    with open(brca_file, 'r') as f:
        brca_patients = json.load(f)
    
    # Extract barcodes from BRCA patients
    import re
    brca_barcodes = []
    for patient in brca_patients:
        desc = patient.get('Patient_description', '')
        match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
        if match:
            brca_barcodes.append(match.group(0))
    
    print(f"\nTotal BRCA patients: {len(brca_barcodes)}")
    print(f"Total CDH1 mutations (all cancers): {len(cdh1_mutations)}")
    
    # Find BRCA patients with CDH1 mutations
    cdh1_barcodes = set([m['ParticipantBarcode'] for m in cdh1_mutations])
    brca_with_cdh1 = set(brca_barcodes).intersection(cdh1_barcodes)
    
    print(f"BRCA patients with CDH1 mutations: {len(brca_with_cdh1)}")
    
    # Create histological type mapping
    histology_map = {}
    for patient in brca_patients:
        desc = patient.get('Patient_description', '')
        match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
        if match:
            barcode = match.group(0)
            histology = patient.get('histological_type', 'Unknown')
            histology_map[barcode] = histology
    
    # Count by histological type
    from collections import defaultdict, Counter
    histo_total = Counter()
    histo_mutated = Counter()
    
    for barcode in brca_barcodes:
        histology = histology_map.get(barcode, 'Unknown')
        histo_total[histology] += 1
    
    for barcode in brca_with_cdh1:
        histology = histology_map.get(barcode, 'Unknown')
        histo_mutated[histology] += 1
    
    # Calculate percentages
    results = []
    for histology in histo_total:
        total = histo_total[histology]
        mutated = histo_mutated[histology]
        percentage = (mutated / total * 100) if total > 0 else 0
        results.append({
            'histological_type': histology,
            'total_patients': total,
            'cdh1_mutated_patients': mutated,
            'mutation_percentage': round(percentage, 2)
        })
    
    # Sort by percentage descending
    results_sorted = sorted(results, key=lambda x: x['mutation_percentage'], reverse=True)
    top_3 = results_sorted[:3]
    
    print("\nTop 3 histological types by CDH1 mutation percentage:")
    for i, item in enumerate(top_3, 1):
        print(f"{i}. {item['histological_type']}: {item['mutation_percentage']}% ({item['cdh1_mutated_patients']}/{item['total_patients']})")
    
    result = top_3
    
except Exception as e:
    print(f"Error processing: {e}")
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Clinical entry C07B122E-AC50-4DB2-ADD2-5617A5D0E976 identifies patient TCGA-GM-A2DA, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Dead.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-3C-AAAU and UUID 6E7D5EC6-A469-467C-B748-237353C23416 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': "Patient TCGA-A7-A26I, registered under UUID b2ecbc0f-2c30-4200-8d5e-7b95424bcadb, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 523E24A2-51B9-4658-BE2F-42E5FCCEBB17 refers to patient TCGA-A7-A5ZW, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-C8-A26Z and UUID dc11b1c7-1f00-4813-b4b5-ecf776b2eb37 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.list_db:14': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'barcodes': [], 'patient_data': []}, 'var_functions.execute_python:22': {'cdh1_barcodes': [], 'cdh1_mutations': [], 'brca_patients': []}}

exec(code, env_args)
