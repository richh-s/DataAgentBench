code = """import json
import re

# Read the LGG clinical data file
clinical_file = locals()['var_functions.query_db:34']
with open(clinical_file, 'r') as f:
    lgg_clinical = json.load(f)

# Process LGG patients - extract barcodes and histology info
lgg_patients = []
valid_histology_count = 0

for record in lgg_clinical:
    desc = record['Patient_description']
    
    # Extract barcode from description
    match = re.search(r'(TCGA-\w{2}-\w{4})', desc)
    if match:
        barcode = match.group(1)
    else:
        continue
    
    histological_type = record.get('histological_type', '') or ''
    icd_histology = record.get('icd_o_3_histology', '') or ''
    
    # Check if histology annotations are not enclosed in square brackets
    has_valid_histology = True
    if histological_type.startswith('[') and histological_type.endswith(']'):
        has_valid_histology = False
    if icd_histology.startswith('[') and icd_histology.endswith(']'):
        has_valid_histology = False
    
    if has_valid_histology and histological_type:
        valid_histology_count += 1
    
    lgg_patients.append({
        'barcode': barcode,
        'histological_type': histological_type,
        'icd_histology': icd_histology,
        'valid_histology': has_valid_histology
    })

# Load IGF2 expression data
expression_file = locals()['var_functions.query_db:36']
with open(expression_file, 'r') as f:
    igf2_expression = json.load(f)

# Create dictionary of IGF2 expression values
igf2_dict = {}
for expr in igf2_expression:
    barcode = expr['ParticipantBarcode']
    normalized_count = float(expr['normalized_count'])
    igf2_dict[barcode] = normalized_count

# Match LGG patients with IGF2 expression data
matched_patients = []
for patient in lgg_patients:
    barcode = patient['barcode']
    if barcode in igf2_dict:
        normalized_count = igf2_dict[barcode]
        if normalized_count > 0:  # Only include valid expression values
            matched_patients.append({
                'barcode': barcode,
                'histological_type': patient['histological_type'],
                'icd_histology': patient['icd_histology'],
                'normalized_count': normalized_count,
                'log10_expression': math.log10(normalized_count + 1)
            })

# Group by histological type and compute average
from collections import defaultdict
import math

histology_groups = defaultdict(list)
for patient in matched_patients:
    if patient['valid_histology'] and patient['histological_type']:
        histology_key = patient['histological_type']
        histology_groups[histology_key].append(patient['log10_expression'])

# Calculate averages
results = {}
for histology, log10_values in histology_groups.items():
    avg_log10 = sum(log10_values) / len(log10_values)
    results[histology] = avg_log10

# Format results with 4 decimal places
formatted_results = {}
for histology, avg in sorted(results.items()):
    formatted_results[histology] = round(avg, 4)

__RESULT__ = {
    'total_lgg_patients': len(lgg_patients),
    'patients_with_valid_histology': valid_histology_count,
    'patients_with_igf2_expression': len(matched_patients),
    'histology_type_count': len(results),
    'average_log10_expression': formatted_results
}"""

env_args = {'var_functions.query_db:0': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_functions.list_db:10': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:12': [{'Symbol': 'IGF2', 'normalized_count': '167.272646747735', 'ParticipantBarcode': 'TCGA-AB-2908'}, {'Symbol': 'IGF2', 'normalized_count': '185.236', 'ParticipantBarcode': 'TCGA-19-5960'}, {'Symbol': 'IGF2', 'normalized_count': '80.6827', 'ParticipantBarcode': 'TCGA-21-1071'}, {'Symbol': 'IGF2', 'normalized_count': '13105.3695494317', 'ParticipantBarcode': 'TCGA-30-1862'}, {'Symbol': 'IGF2', 'normalized_count': '613.474', 'ParticipantBarcode': 'TCGA-66-2795'}, {'Symbol': 'IGF2', 'normalized_count': '630.54', 'ParticipantBarcode': 'TCGA-A8-A082'}, {'Symbol': 'IGF2', 'normalized_count': '423.628', 'ParticipantBarcode': 'TCGA-B5-A3FA'}, {'Symbol': 'IGF2', 'normalized_count': '1151.13', 'ParticipantBarcode': 'TCGA-BH-A1EX'}, {'Symbol': 'IGF2', 'normalized_count': '369.106', 'ParticipantBarcode': 'TCGA-BT-A20O'}, {'Symbol': 'IGF2', 'normalized_count': '3936.02070028943', 'ParticipantBarcode': 'TCGA-CD-5799'}], 'var_functions.query_db:14': [{'icd_o_3_histology': '8330/3'}, {'icd_o_3_histology': '8022/3'}, {'icd_o_3_histology': '8382/3'}, {'icd_o_3_histology': '8250/3'}, {'icd_o_3_histology': '8770/3'}, {'icd_o_3_histology': '8821/1'}, {'icd_o_3_histology': '8335/3'}, {'icd_o_3_histology': '8490/3'}, {'icd_o_3_histology': '8480/3'}, {'icd_o_3_histology': '8584/1'}, {'icd_o_3_histology': '9080/0'}, {'icd_o_3_histology': '8582/3'}, {'icd_o_3_histology': '8370/3'}, {'icd_o_3_histology': '8461/3'}, {'icd_o_3_histology': '8370/1'}, {'icd_o_3_histology': '9540/3'}, {'icd_o_3_histology': '8230/3'}, {'icd_o_3_histology': '8541/3'}, {'icd_o_3_histology': '8680/3'}, {'icd_o_3_histology': '8482/3'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
