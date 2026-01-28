code = """import json
import re

# Load BRCA patients data
brca_file = locals()['var_functions.query_db:24']

with open(brca_file, 'r') as f:
    brca_patients_raw = json.load(f)

# Extract patient barcodes and histological types
brca_patients = {}
histological_counts = {}

for patient in brca_patients_raw:
    desc = patient.get('Patient_description', '')
    hist_type = patient.get('histological_type', 'Unknown')
    
    if hist_type == 'None' or not hist_type:
        hist_type = 'Unknown'
    
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if match:
        barcode = match.group(1)
        brca_patients[barcode] = hist_type
        histological_counts[hist_type] = histological_counts.get(hist_type, 0) + 1

print('Total BRCA patients:', len(brca_patients))

# Load CDH1 mutations
cdh1_file = locals()['var_functions.query_db:34']

with open(cdh1_file, 'r') as f:
    cdh1_mutations_raw = json.load(f)

# Count CDH1 mutations
from collections import defaultdict
cdh1_mutations_by_hist = defaultdict(int)
cdh1_patients = set()

for mutation in cdh1_mutations_raw:
    barcode = mutation['ParticipantBarcode']
    if barcode in brca_patients:
        hist_type = brca_patients[barcode]
        cdh1_mutations_by_hist[hist_type] += 1
        cdh1_patients.add(barcode)

# Calculate mutation rates
mutation_rates = {}
for hist_type, total_count in histological_counts.items():
    if total_count > 0:
        mutation_count = cdh1_mutations_by_hist.get(hist_type, 0)
        mutation_rate = (mutation_count / total_count) * 100
        mutation_rates[hist_type] = {
            'total_patients': total_count,
            'mutated_patients': mutation_count,
            'mutation_rate': mutation_rate
        }

# Sort by mutation rate
sorted_rates = sorted(mutation_rates.items(), key=lambda x: x[1]['mutation_rate'], reverse=True)

# Prepare result
result = {'top_3': []}
for hist, data in sorted_rates[:3]:
    result['top_3'].append({
        'histological_type': hist,
        'mutation_rate': round(data['mutation_rate'], 2),
        'mutated_patients': data['mutated_patients'],
        'total_patients': data['total_patients']
    })

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '943.0'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'days_to_death': '446.0'}], 'var_functions.query_db:18': [], 'var_functions.query_db:20': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.query_db:28': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Nonsense_Mutation'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Ins'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
