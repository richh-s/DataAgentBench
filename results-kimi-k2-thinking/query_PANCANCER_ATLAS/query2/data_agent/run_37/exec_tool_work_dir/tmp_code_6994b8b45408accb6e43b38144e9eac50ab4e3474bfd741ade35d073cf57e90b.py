code = """import json
import re

# Load BRCA clinical data for alive patients
clinical_file = locals()['var_functions.query_db:28']
with open(clinical_file, 'r') as f:
    brca_clinical = json.load(f)

# Load all CDH1 mutated patients across all cancers
cdh1_file = locals()['var_functions.query_db:42']
with open(cdh1_file, 'r') as f:
    cdh1_patients = json.load(f)

# Build dictionary of alive BRCA patients and their histotypes
alive_brca = {}
for patient in brca_clinical:
    desc = patient.get('Patient_description', '')
    histotype = patient.get('histological_type', 'Unknown')
    if 'TCGA-' in desc:
        match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
        if match:
            barcode = match.group()
            alive_brca[barcode] = histotype

# Create set of CDH1 mutated barcodes
cdh1_barcodes = set(p['ParticipantBarcode'] for p in cdh1_patients)

# Count patients and CDH1 mutations by histotype
histotype_total = {}
histotype_cdh1 = {}

for barcode, histotype in alive_brca.items():
    histotype_total[histotype] = histotype_total.get(histotype, 0) + 1
    if barcode in cdh1_barcodes:
        histotype_cdh1[histotype] = histotype_cdh1.get(histotype, 0) + 1

# Calculate percentages for each histotype
results = []
for histotype, total in histotype_total.items():
    cdh1_count = histotype_cdh1.get(histotype, 0)
    percentage = (cdh1_count / total * 100) if total > 0 else 0
    results.append({
        'histotype': histotype,
        'total': total,
        'cdh1_mutations': cdh1_count,
        'percentage': round(percentage, 2)
    })

results.sort(key=lambda x: x['percentage'], reverse=True)

print('Top histological types:')
for r in results[:5]:
    print(f"{r['histotype']}: {r['percentage']}% ({r['cdh1_mutations']}/{r['total']})")

print('__RESULT__:')
print(json.dumps(results[:5]))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [], 'var_functions.query_db:10': [{'Patient_description': "Patient TCGA-DK-A6AW, registered under UUID 01C815BA-7BDA-4F7E-865C-0C5776FEBF2C, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-GD-A3OQ (UUID 2E85C30C-C4C4-4096-9EEF-4EB2C7D991A3) is recorded as a MALE with vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'The individual with barcode TCGA-CF-A47W and UUID 122FC134-8915-47DB-96C9-AB1853C3CD18 is a MALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Patient TCGA-CF-A3MF (MALE, UUID 1E308B12-0590-4DAE-94D0-A539FCF25DF7) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Case DE810AF0-4C18-4E8F-9836-F8ABC425E3EB, linked to barcode TCGA-DK-A2I6, corresponds to a MALE patient diagnosed with Bladder urothelial carcinoma, with vital status Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Patient TCGA-BT-A20V (FEMALE, UUID 24f21425-b001-4986-aedf-5b4dd851c6ad) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '154.0'}, {'Patient_description': 'Record 35C7BB8A-7B5C-488D-9D3A-725B24D14478 refers to patient TCGA-4Z-AA81, a MALE diagnosed with Bladder urothelial carcinoma. Vital status recorded as Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '1270.0'}, {'Patient_description': 'Case A648D9BF-CF37-41FC-9515-E8F5AC85FCD4, linked to barcode TCGA-XF-A9SX, corresponds to a FEMALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '719'}, {'Patient_description': 'Patient TCGA-XF-A8HE (MALE, UUID 841B4582-A268-4A55-A9A2-47C7E5C3B69F) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Case 679a6869-2ce9-4472-8db1-8869e2c1a440, linked to barcode TCGA-CU-A0YN, corresponds to a MALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '393.0'}, {'Patient_description': "Patient TCGA-FD-A3SN, registered under UUID 0FB043D3-D86B-4CD8-8C01-9E2B3E965BB0, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Patient TCGA-BL-A0C8 (UUID a6003b1c-56a9-430a-a5e2-b70af3f81bdb) is a MALE diagnosed with Bladder urothelial carcinoma. Current vital status: Alive.', 'histological_type': 'None', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Clinical entry 3CCCFFEA-BD7D-4548-BB38-FE5EDA630DE6 identifies patient TCGA-FD-A43N, a MALE subject with Bladder urothelial carcinoma. Their current vital status is Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Record 234086DD-5A74-4FF1-94AB-BAD43EE69D5C refers to patient TCGA-DK-A2I2, a FEMALE diagnosed with Bladder urothelial carcinoma. Vital status recorded as Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '237.0'}, {'Patient_description': 'Patient TCGA-E7-A7DV (UUID 3EFFD691-570C-478A-8903-3771A1B43F2E) is a MALE diagnosed with Bladder urothelial carcinoma. Current vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'The individual with barcode TCGA-DK-A1AE and UUID 493a4ff2-37a5-4b79-928d-83dbfe534556 is a MALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Case 72FE54B5-C1C8-468A-954A-09992429512A, linked to barcode TCGA-4Z-AA7R, corresponds to a MALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '522.0'}, {'Patient_description': "Patient TCGA-DK-AA6R, registered under UUID 5DB4B168-A6BA-482C-B067-2274EBA96AAD, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-XF-A8HH (UUID 02964D82-CC94-4286-A66F-03567101950C) is recorded as a FEMALE with vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '57'}, {'Patient_description': 'The individual with barcode TCGA-ZF-A9R7 and UUID CE4E4549-BEFC-447F-9B79-ED46E302E6D7 is a FEMALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'days_to_death': '[Not Applicable]'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-LL-A9Q3'}, {'ParticipantBarcode': 'TCGA-AA-3949'}, {'ParticipantBarcode': 'TCGA-A2-A0CK'}, {'ParticipantBarcode': 'TCGA-B9-A8YI'}, {'ParticipantBarcode': 'TCGA-A2-A4S2'}, {'ParticipantBarcode': 'TCGA-A7-A425'}, {'ParticipantBarcode': 'TCGA-BS-A0UV'}, {'ParticipantBarcode': 'TCGA-CD-A4MG'}, {'ParticipantBarcode': 'TCGA-A8-A09Z'}, {'ParticipantBarcode': 'TCGA-A8-A091'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:50': {'total_patients': 231, 'barcodes_count': 231}}

exec(code, env_args)
