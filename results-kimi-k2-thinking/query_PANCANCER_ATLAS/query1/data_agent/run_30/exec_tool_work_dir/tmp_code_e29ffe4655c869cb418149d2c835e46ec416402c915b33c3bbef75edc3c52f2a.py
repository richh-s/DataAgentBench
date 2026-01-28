code = """import json
import math
import re

# Read the LGG clinical data
with open('var_functions.query_db:14', 'r') as f:
    lgg_clinical = json.load(f)

# Read the IGF2 expression data
with open('var_functions.query_db:16', 'r') as f:
    igf2_expression = json.load(f)

# Extract ParticipantBarcode from Patient_description for LGG patients
lgg_patients = []
for record in lgg_clinical:
    patient_desc = record.get('Patient_description', '')
    histology = record.get('histological_type', '')
    
    # Skip histology types enclosed in square brackets
    if histology.startswith('[') and histology.endswith(']'):
        continue
    
    # Extract TCGA barcode from Patient_description
    # Pattern: TCGA-XX-XXXX or similar
    match = re.search(r'(TCGA-\w+)', patient_desc)
    if match:
        barcode = match.group(1)
        lgg_patients.append({
            'ParticipantBarcode': barcode,
            'histological_type': histology
        })

print(f"Found {len(lgg_patients)} LGG patients with valid histology")

# Convert IGF2 expression data to dict for easier lookup
# Key: ParticipantBarcode, Value: normalized_count
igf2_dict = {}
for expr in igf2_expression:
    barcode = expr.get('ParticipantBarcode')
    count = expr.get('normalized_count')
    if barcode and count and count.strip():
        try:
            igf2_dict[barcode] = float(count)
        except (ValueError, TypeError):
            continue

print(f"Found {len(igf2_dict)} patients with IGF2 expression data")

# Merge LGG patients with IGF2 expression
merged_data = []
for patient in lgg_patients:
    barcode = patient['ParticipantBarcode']
    histology = patient['histological_type']
    
    if barcode in igf2_dict:
        count = igf2_dict[barcode]
        # Validate count is positive (or zero)
        if count >= 0:
            log_value = math.log10(count + 1)
            merged_data.append({
                'ParticipantBarcode': barcode,
                'histological_type': histology,
                'log10_expression': log_value,
                'original_count': count
            })

print(f"Found {len(merged_data)} LGG patients with valid IGF2 expression")

# Group by histological_type and compute average
grouped = {}
for record in merged_data:
    histology = record['histological_type']
    log_value = record['log10_expression']
    
    if histology not in grouped:
        grouped[histology] = []
    grouped[histology].append(log_value)

# Compute averages
results = {}
for histology, values in grouped.items():
    avg_log10 = sum(values) / len(values)
    results[histology] = {
        'avg_log10_expression': round(avg_log10, 6),  # Use 6 for now, will format later
        'sample_count': len(values)
    }

# Sort by histology type
sorted_results = dict(sorted(results.items()))

# Format output with at least 4 decimal places
formatted_results = {}
for histology, data in sorted_results.items():
    avg_formatted = f"{data['avg_log10_expression']:.6f}"  # Ensure at least 6 decimal places for display
    formatted_results[histology] = {
        'avg_log10_expression': avg_formatted,
        'sample_count': data['sample_count']
    }

# Create final answer string
result_lines = []
for histology, data in sorted_results.items():
    avg_value = data['avg_log10_expression']
    avg_formatted = f"{avg_value:.4f}"  # At least 4 decimal places as required
    result_lines.append(f"{histology}: {avg_formatted}")

final_answer = "\n".join(result_lines) if result_lines else "No valid data found for LGG patients"

result = {
    'summary': f"Found {len(merged_data)} LGG patients across {len(sorted_results)} histology types",
    'averages_by_histology': sorted_results,
    'formatted_output': final_answer
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:10': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': "Patient TCGA-23-1124, registered under UUID 8a6d2ce3-cc57-451b-9b07-8263782aa23f, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Dead.", 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-2641 (UUID 49e5ee61-a1c9-4038-84ac-92683e573a65) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-23-1118 (FEMALE, UUID 700e91bb-d675-41b2-bbbd-935767c7b447) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-1120 (UUID fdf83fdf-dfbb-4306-9a1b-b4487d18b402) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'The individual with barcode TCGA-23-2081 and UUID 41178cbc-db73-4007-b5d8-febebf7f578d is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
