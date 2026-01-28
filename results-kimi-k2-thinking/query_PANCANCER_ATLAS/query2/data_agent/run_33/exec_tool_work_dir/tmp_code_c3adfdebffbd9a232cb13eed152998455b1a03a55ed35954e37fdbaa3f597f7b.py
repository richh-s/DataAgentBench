code = """import json
import re
from collections import Counter

# Load bladder patients
bladder_file = locals()['var_functions.query_db:44']
with open(bladder_file, 'r') as f:
    bladder_patients = json.load(f)

# Load CDH1 mutations  
cdh1_file = locals()['var_functions.query_db:52']
with open(cdh1_file, 'r') as f:
    cdh1_data = json.load(f)

# Get CDH1 mutated barcodes
cdh1_barcodes = set([item['ParticipantBarcode'] for item in cdh1_data])

# Count statistics
hist_total = Counter()
hist_cdh1 = Counter()

for record in bladder_patients:
    days_to_death = record.get('days_to_death')
    is_alive = days_to_death in [None, 'None', '[Not Applicable]', 'nan', '']
    
    if is_alive:
        desc = record.get('Patient_description', '')
        hist_type = record.get('histological_type', 'Unknown')
        
        match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
        if match:
            barcode = match.group(1)
            hist_total[hist_type] += 1
            
            if barcode in cdh1_barcodes:
                hist_cdh1[hist_type] += 1

results = []
for hist, total in hist_total.items():
    cdh1_count = hist_cdh1.get(hist, 0)
    percentage = (cdh1_count / total * 100) if total > 0 else 0
    results.append({
        'hist_type': hist,
        'total': total,
        'cdh1_count': cdh1_count,
        'percentage': round(percentage, 1)
    })

# Sort by percentage
results_sorted = sorted(results, key=lambda x: x['percentage'], reverse=True)

print('Top 3 histological types:')
for i, item in enumerate(results_sorted[:3], 1):
    print(f"{i}. {item['hist_type']}: {item['percentage']}% ({item['cdh1_count']}/{item['total']})")

output = {
    'top_3': results_sorted[:3],
    'all_results': results_sorted
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:18': 'test', 'var_functions.execute_python:20': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5', 'var_functions.query_db:8', 'var_functions.query_db:11', 'var_functions.execute_python:18'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:32': 'test', 'var_functions.query_db:40': [], 'var_functions.query_db:42': [{'Patient_description': "Patient TCGA-DK-A6AW, registered under UUID 01C815BA-7BDA-4F7E-865C-0C5776FEBF2C, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-GD-A3OQ (UUID 2E85C30C-C4C4-4096-9EEF-4EB2C7D991A3) is recorded as a MALE with vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'The individual with barcode TCGA-CF-A47W and UUID 122FC134-8915-47DB-96C9-AB1853C3CD18 is a MALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Patient TCGA-CF-A3MF (MALE, UUID 1E308B12-0590-4DAE-94D0-A539FCF25DF7) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Case DE810AF0-4C18-4E8F-9836-F8ABC425E3EB, linked to barcode TCGA-DK-A2I6, corresponds to a MALE patient diagnosed with Bladder urothelial carcinoma, with vital status Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Patient TCGA-BT-A20V (FEMALE, UUID 24f21425-b001-4986-aedf-5b4dd851c6ad) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '154.0'}, {'Patient_description': 'Record 35C7BB8A-7B5C-488D-9D3A-725B24D14478 refers to patient TCGA-4Z-AA81, a MALE diagnosed with Bladder urothelial carcinoma. Vital status recorded as Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '1270.0'}, {'Patient_description': 'Case A648D9BF-CF37-41FC-9515-E8F5AC85FCD4, linked to barcode TCGA-XF-A9SX, corresponds to a FEMALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '719'}, {'Patient_description': 'Patient TCGA-XF-A8HE (MALE, UUID 841B4582-A268-4A55-A9A2-47C7E5C3B69F) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Case 679a6869-2ce9-4472-8db1-8869e2c1a440, linked to barcode TCGA-CU-A0YN, corresponds to a MALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '393.0'}, {'Patient_description': "Patient TCGA-FD-A3SN, registered under UUID 0FB043D3-D86B-4CD8-8C01-9E2B3E965BB0, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Patient TCGA-BL-A0C8 (UUID a6003b1c-56a9-430a-a5e2-b70af3f81bdb) is a MALE diagnosed with Bladder urothelial carcinoma. Current vital status: Alive.', 'histological_type': 'None', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Clinical entry 3CCCFFEA-BD7D-4548-BB38-FE5EDA630DE6 identifies patient TCGA-FD-A43N, a MALE subject with Bladder urothelial carcinoma. Their current vital status is Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Record 234086DD-5A74-4FF1-94AB-BAD43EE69D5C refers to patient TCGA-DK-A2I2, a FEMALE diagnosed with Bladder urothelial carcinoma. Vital status recorded as Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '237.0'}, {'Patient_description': 'Patient TCGA-E7-A7DV (UUID 3EFFD691-570C-478A-8903-3771A1B43F2E) is a MALE diagnosed with Bladder urothelial carcinoma. Current vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'The individual with barcode TCGA-DK-A1AE and UUID 493a4ff2-37a5-4b79-928d-83dbfe534556 is a MALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Case 72FE54B5-C1C8-468A-954A-09992429512A, linked to barcode TCGA-4Z-AA7R, corresponds to a MALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '522.0'}, {'Patient_description': "Patient TCGA-DK-AA6R, registered under UUID 5DB4B168-A6BA-482C-B067-2274EBA96AAD, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-XF-A8HH (UUID 02964D82-CC94-4286-A66F-03567101950C) is recorded as a FEMALE with vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '57'}, {'Patient_description': 'The individual with barcode TCGA-ZF-A9R7 and UUID CE4E4549-BEFC-447F-9B79-ED46E302E6D7 is a FEMALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:50': {'count': 232, 'barcodes': ['TCGA-DK', 'TCGA-GD', 'TCGA-CF', 'TCGA-CF', 'TCGA-DK', 'TCGA-XF', 'TCGA-FD', 'TCGA-BL', 'TCGA-FD', 'TCGA-E7', 'TCGA-DK', 'TCGA-DK', 'TCGA-ZF', 'TCGA-GV', 'TCGA-FD', 'TCGA-E7', 'TCGA-GV', 'TCGA-BT', 'TCGA-FD', 'TCGA-KQ', 'TCGA-UY', 'TCGA-FD', 'TCGA-FD', 'TCGA-ZF', 'TCGA-DK', 'TCGA-DK', 'TCGA-XF', 'TCGA-PQ', 'TCGA-4Z', 'TCGA-G2', 'TCGA-XF', 'TCGA-FD', 'TCGA-MV', 'TCGA-4Z', 'TCGA-E7', 'TCGA-ZF', 'TCGA-DK', 'TCGA-YF', 'TCGA-K4', 'TCGA-E7', 'TCGA-UY', 'TCGA-ZF', 'TCGA-ZF', 'TCGA-YF', 'TCGA-DK', 'TCGA-DK', 'TCGA-CF', 'TCGA-CF', 'TCGA-CF', 'TCGA-XF', 'TCGA-FD', 'TCGA-DK', 'TCGA-GD', 'TCGA-FJ', 'TCGA-G2', 'TCGA-E7', 'TCGA-GV', 'TCGA-4Z', 'TCGA-XF', 'TCGA-DK', 'TCGA-HQ', 'TCGA-GC', 'TCGA-K4', 'TCGA-CF', 'TCGA-ZF', 'TCGA-DK', 'TCGA-K4', 'TCGA-CU', 'TCGA-CF', 'TCGA-ZF', 'TCGA-DK', 'TCGA-DK', 'TCGA-DK', 'TCGA-4Z', 'TCGA-CF', 'TCGA-XF', 'TCGA-E5', 'TCGA-GV', 'TCGA-CU', 'TCGA-CF', 'TCGA-LT', 'TCGA-CF', 'TCGA-K4', 'TCGA-KQ', 'TCGA-FD', 'TCGA-DK', 'TCGA-GD', 'TCGA-GU', 'TCGA-CF', 'TCGA-E7', 'TCGA-H4', 'TCGA-C4', 'TCGA-CU', 'TCGA-GC', 'TCGA-E7', 'TCGA-UY', 'TCGA-ZF', 'TCGA-ZF', 'TCGA-G2', 'TCGA-K4', 'TCGA-CF', 'TCGA-KQ', 'TCGA-DK', 'TCGA-GD', 'TCGA-GC', 'TCGA-GC', 'TCGA-GV', 'TCGA-E7', 'TCGA-DK', 'TCGA-FD', 'TCGA-XF', 'TCGA-UY', 'TCGA-GU', 'TCGA-FD', 'TCGA-HQ', 'TCGA-XF', 'TCGA-XF', 'TCGA-CF', 'TCGA-CF', 'TCGA-XF', 'TCGA-DK', 'TCGA-FD', 'TCGA-ZF', 'TCGA-R3', 'TCGA-FD', 'TCGA-UY', 'TCGA-DK', 'TCGA-4Z', 'TCGA-KQ', 'TCGA-XF', 'TCGA-XF', 'TCGA-UY', 'TCGA-GU', 'TCGA-ZF', 'TCGA-ZF', 'TCGA-XF', 'TCGA-E7', 'TCGA-BT', 'TCGA-GC', 'TCGA-GC', 'TCGA-ZF', 'TCGA-DK', 'TCGA-FD', 'TCGA-CF', 'TCGA-DK', 'TCGA-E5', 'TCGA-DK', 'TCGA-C4', 'TCGA-XF', 'TCGA-K4', 'TCGA-K4', 'TCGA-FD', 'TCGA-KQ', 'TCGA-G2', 'TCGA-K4', 'TCGA-CF', 'TCGA-YC', 'TCGA-4Z', 'TCGA-BT', 'TCGA-XF', 'TCGA-DK', 'TCGA-DK', 'TCGA-UY', 'TCGA-DK', 'TCGA-BL', 'TCGA-CF', 'TCGA-GV', 'TCGA-G2', 'TCGA-FJ', 'TCGA-S5', 'TCGA-UY', 'TCGA-ZF', 'TCGA-FD', 'TCGA-ZF', 'TCGA-ZF', 'TCGA-C4', 'TCGA-K4', 'TCGA-E7', 'TCGA-DK', 'TCGA-DK', 'TCGA-2F', 'TCGA-XF', 'TCGA-FD', 'TCGA-E7', 'TCGA-G2', 'TCGA-DK', 'TCGA-CF', 'TCGA-CF', 'TCGA-E7', 'TCGA-GC', 'TCGA-PQ', 'TCGA-YC', 'TCGA-GV', 'TCGA-DK', 'TCGA-ZF', 'TCGA-BT', 'TCGA-GU', 'TCGA-FT', 'TCGA-E7', 'TCGA-K4', 'TCGA-UY', 'TCGA-UY', 'TCGA-ZF', 'TCGA-LC', 'TCGA-GV', 'TCGA-GD', 'TCGA-FD', 'TCGA-G2', 'TCGA-GD', 'TCGA-4Z', 'TCGA-FD', 'TCGA-FD', 'TCGA-FD', 'TCGA-E7', 'TCGA-DK', 'TCGA-SY', 'TCGA-BT', 'TCGA-E7', 'TCGA-UY', 'TCGA-2F', 'TCGA-DK', 'TCGA-DK', 'TCGA-DK', 'TCGA-CF', 'TCGA-KQ', 'TCGA-XF', 'TCGA-H4', 'TCGA-E7', 'TCGA-K4', 'TCGA-LT', 'TCGA-GC', 'TCGA-4Z'], 'histogram': {'Muscle invasive urothelial carcinoma (pT2 or above)': 230, 'None': 2}}, 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:54': {'total_mutations': 318, 'unique_patients': 301}, 'var_functions.execute_python:60': 'test', 'var_functions.execute_python:62': {'cdh1_patients': 301, 'bladder_patients': 232, 'overlapping': 0}, 'var_functions.execute_python:64': 'test', 'var_functions.execute_python:66': {'bladder_patients': 232, 'cdh1_patients': 301, 'overlap': 7, 'sample_overlap': ['TCGA-XF-A9T3', 'TCGA-DK-A1AG', 'TCGA-H4-A2HQ', 'TCGA-HQ-A2OF', 'TCGA-DK-A6AW', 'TCGA-C4-A0F0', 'TCGA-KQ-A41S']}}

exec(code, env_args)
