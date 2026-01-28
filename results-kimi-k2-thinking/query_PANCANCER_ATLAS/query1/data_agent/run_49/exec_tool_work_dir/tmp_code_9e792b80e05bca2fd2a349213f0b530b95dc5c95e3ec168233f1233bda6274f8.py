code = """import json
import re
from math import log10

# Read LGG patients data
lgg_file = locals()['var_functions.query_db:20']
with open(lgg_file, 'r') as f:
    lgg_patients = json.load(f)

# Create IGF2 expression map
igf2_file = locals()['var_functions.query_db:28']
with open(igf2_file, 'r') as f:
    igf2_expression = json.load(f)

igf2_map = {}
for expr in igf2_expression:
    barcode = expr['ParticipantBarcode']
    try:
        count = float(expr['normalized_count'])
        igf2_map[barcode] = count
    except (ValueError, TypeError):
        continue

# Match LGG patients with IGF2 expression and valid histology
histology_expression = {}
matched_count = 0

for patient in lgg_patients:
    desc = patient.get('Patient_description', '')
    histology = patient.get('histological_type', '')
    
    # Skip if histology is empty or contains square brackets
    if not histology or ('[' in histology and ']' in histology):
        continue
    
    # Extract TCGA barcode (TCGA-XX-XXXX format)
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if match:
        barcode = match.group(1)
        if barcode in igf2_map:
            count = igf2_map[barcode]
            log10_expr = log10(count + 1)
            
            if histology not in histology_expression:
                histology_expression[histology] = []
            histology_expression[histology].append(log10_expr)
            matched_count += 1

# Calculate averages
final_results = {}
for histology in sorted(histology_expression.keys()):
    expressions = histology_expression[histology]
    avg_val = sum(expressions) / len(expressions)
    final_results[histology] = round(avg_val, 4)

# Create output string
output_parts = []
for histology, avg_val in sorted(final_results.items()):
    output_parts.append(histology + ': ' + format(avg_val, '.4f'))

final_output = ', '.join(output_parts)

print('__RESULT__:')
print(json.dumps(final_output))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_functions.query_db:7': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:8': [], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}, {'diagnosis': 'None'}], 'var_functions.query_db:14': [{'total_rows': '10761'}], 'var_functions.query_db:16': [{'histological_type': 'Adenosquamous'}, {'histological_type': 'Adrenocortical Carcinoma- Myxoid Type'}, {'histological_type': 'Adrenocortical Carcinoma- Oncocytic Type'}, {'histological_type': 'Adrenocortical carcinoma- Usual Type'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Biphasic mesothelioma'}, {'histological_type': 'Cervical Squamous Cell Carcinoma'}, {'histological_type': 'Cholangiocarcinoma; distal'}, {'histological_type': 'Cholangiocarcinoma; hilar/perihilar'}, {'histological_type': 'Cholangiocarcinoma; intrahepatic'}, {'histological_type': 'Colon Adenocarcinoma'}, {'histological_type': 'Colon Mucinous Adenocarcinoma'}, {'histological_type': 'Dedifferentiated liposarcoma'}, {'histological_type': 'Desmoid Tumor'}, {'histological_type': 'Diffuse large B-cell lymphoma (DLBCL) NOS (any anatomic site nodal or extranodal)'}, {'histological_type': 'Diffuse malignant mesothelioma - NOS'}, {'histological_type': 'Endocervical Adenocarcinoma of the Usual Type'}, {'histological_type': 'Endocervical Type of Adenocarcinoma'}, {'histological_type': 'Endometrioid Adenocarcinoma of Endocervix'}, {'histological_type': 'Endometrioid endometrial adenocarcinoma'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': 220, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'lgg_patients_count': 220, 'igf2_expression_count': 496}, 'var_functions.execute_python:32': {'total_lgg_patients': 220, 'lgg_with_valid_histology': 220, 'matched_with_igf2': 11, 'histology_types_analyzed': 2, 'results': {'Oligodendroglioma': {'average_log10_expression': 2.6825, 'sample_count': 8}, 'Paraganglioma; Extra-adrenal Pheochromocytoma': {'average_log10_expression': 5.5571, 'sample_count': 3}}}}

exec(code, env_args)
