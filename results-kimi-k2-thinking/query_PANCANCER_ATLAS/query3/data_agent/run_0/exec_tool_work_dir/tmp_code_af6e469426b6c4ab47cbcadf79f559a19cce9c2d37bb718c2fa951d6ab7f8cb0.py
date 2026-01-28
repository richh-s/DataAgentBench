code = """import json
import re
from collections import defaultdict
import math

# Access the stored data
clinical_file = var_functions.query_db_90
mutation_file = var_functions.query_db_94

# Load clinical data
with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)

# Load mutation data  
with open(mutation_file, 'r') as f:
    mutation_data = json.load(f)

print('Clinical records loaded:', len(clinical_data))
print('Mutation records loaded:', len(mutation_data))

# Process clinical data - extract female BRCA patients
patients = []
tcga_pattern = r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}'
gender_pattern = re.compile(r'FEMALE', re.IGNORECASE)

for record in clinical_data:
    desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', '')
    
    if gender_pattern.search(desc):
        match = re.search(tcga_pattern, desc)
        if match:
            full_barcode = match.group(0)
            parts = full_barcode.split('-')
            if len(parts) >= 3:
                participant_barcode = '-'.join(parts[:3])
                # Include only known histological types
                if hist_type and hist_type.strip():
                    patients.append({
                        'participant_barcode': participant_barcode,
                        'histological_type': hist_type
                    })

print('Female BRCA patients with histological type:', len(patients))

# Get CDH1 mutation patients
mutation_patients = set()
for record in mutation_data:
    mutation_patients.add(record['ParticipantBarcode'])

print('CDH1 mutation patients:', len(mutation_patients))

# Build contingency table
contingency = defaultdict(lambda: {'mutated': 0, 'wildtype': 0})

for patient in patients:
    barcode = patient['participant_barcode']
    hist_type = patient['histological_type']
    
    # Skip categories that will have marginal totals <= 10 later
    if barcode in mutation_patients:
        contingency[hist_type]['mutated'] += 1
    else:
        contingency[hist_type]['wildtype'] += 1

# Filter out histological types with total <= 10
filtered_contingency = {}
for hist_type, counts in contingency.items():
    total = counts['mutated'] + counts['wildtype']
    if total > 10:
        filtered_contingency[hist_type] = counts

print('Histological types after filtering (total > 10):', len(filtered_contingency))

# Calculate chi-square statistic
# First, build the 2xN table
hist_types = list(filtered_contingency.keys())
if len(hist_types) < 2:
    print('Not enough categories for chi-square test after filtering')
    chi_square = None
    p_value = None
else:
    # Create observed frequencies matrix
    observed = []
    for hist_type in hist_types:
        counts = filtered_contingency[hist_type]
        observed.append([counts['wildtype'], counts['mutated']])
    
    # Convert to row and column totals
    observed_matrix = observed
    row_totals = [sum(row) for row in observed_matrix]
    col_totals = [sum(observed_matrix[i][j] for i in range(len(hist_types))) for j in range(2)]
    grand_total = sum(row_totals)
    
    print('Row totals (by hist type):', row_totals)
    print('Column totals (wildtype, mutated):', col_totals)
    print('Grand total:', grand_total)
    
    # Calculate expected frequencies and chi-square
    chi_square = 0
    for i in range(len(hist_types)):
        for j in range(2):
            expected = (row_totals[i] * col_totals[j]) / grand_total
            observed_val = observed_matrix[i][j]
            chi_square += ((observed_val - expected) ** 2) / expected
    
    print('Chi-square statistic:', chi_square)
    
    # Degrees of freedom
    df = (len(hist_types) - 1) * (2 - 1)
    print('Degrees of freedom:', df)

# Show final table
print('\nFinal contingency table (total > 10 per category):')
for hist_type, counts in sorted(filtered_contingency.items(), key=lambda x: x[1]['mutated'] + x[1]['wildtype'], reverse=True):
    total = counts['mutated'] + counts['wildtype']
    print(f"{hist_type[:50]}: mutated={counts['mutated']}, wildtype={counts['wildtype']}, total={total}")

result = {
    'chi_square_statistic': chi_square if 'chi_square' in locals() else None,
    'categories_analyzed': len(filtered_contingency),
    'total_patients': sum(counts['mutated'] + counts['wildtype'] for counts in filtered_contingency.values()),
    'total_mutations': sum(counts['mutated'] for counts in filtered_contingency.values())
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'name': 'Mutation_Data'}, {'name': 'RNASeq_Expression'}], 'var_functions.query_db:14': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-A2-A25A'}, {'ParticipantBarcode': 'TCGA-AC-A2FO'}, {'ParticipantBarcode': 'TCGA-A2-A4S2'}, {'ParticipantBarcode': 'TCGA-A7-A425'}, {'ParticipantBarcode': 'TCGA-BS-A0UV'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'message': 'Proceeding to query molecular data', 'sample_size': 'pending'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:42': {'status': 'file_check_complete'}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:56': {'files': []}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.execute_python:86': {'status': 'variable_check'}, 'var_functions.query_db:88': [{'ParticipantBarcode': 'TCGA-LL-A9Q3'}, {'ParticipantBarcode': 'TCGA-A2-A0CK'}, {'ParticipantBarcode': 'TCGA-BH-A0HP'}, {'ParticipantBarcode': 'TCGA-B9-A8YI'}, {'ParticipantBarcode': 'TCGA-D8-A27G'}, {'ParticipantBarcode': 'TCGA-A2-A25A'}, {'ParticipantBarcode': 'TCGA-AC-A2FO'}, {'ParticipantBarcode': 'TCGA-E2-A1L8'}, {'ParticipantBarcode': 'TCGA-A2-A4S2'}, {'ParticipantBarcode': 'TCGA-A7-A425'}], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.execute_python:92': {'status': 'clinical_data_check', 'record_count': 39}, 'var_functions.query_db:94': 'file_storage/functions.query_db:94.json'}

exec(code, env_args)
