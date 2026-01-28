code = """import json
import pandas as pd
import re

# Load bladder cancer patients data
bladder_file = locals()['var_functions.query_db:46']
with open(bladder_file, 'r') as f:
    bladder_data = json.load(f)
bladder_df = pd.DataFrame(bladder_data)

# Filter for alive patients
alive_mask = bladder_df['Patient_description'].str.contains('Alive', case=False, na=False)
alive_bladder = bladder_df[alive_mask].copy()

# Extract patient barcode
alive_bladder['barcode'] = alive_bladder['Patient_description'].apply(
    lambda x: re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', str(x)).group(0) if re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', str(x)) else None
)

# Load CDH1 mutation data
mutation_file = locals()['var_functions.query_db:48']
with open(mutation_file, 'r') as f:
    mutation_data = json.load(f)
mutation_df = pd.DataFrame(mutation_data)

# Get all unique histological types in alive bladder patients
all_histologies = alive_bladder['histological_type'].unique()
print('All histological types in alive bladder patients:')
print(all_histologies)
print(f'Total: {len(all_histologies)} types')

# Get bladder barcodes
bladder_barcodes = set(alive_bladder['barcode'].dropna())
cdh1_mutated_barcodes = set(mutation_df['ParticipantBarcode']) & bladder_barcodes

# For every histological type, calculate CDH1 mutation percentage
cdh1_results = []
for histology in all_histologies:
    if pd.isna(histology) or histology == 'None':
        continue
    
    group = alive_bladder[alive_bladder['histological_type'] == histology]
    total_in_group = len(group)
    
    # Count how many have CDH1 mutations
    mutated_in_group = group['barcode'].isin(cdh1_mutated_barcodes).sum()
    
    percentage = (mutated_in_group / total_in_group * 100) if total_in_group > 0 else 0
    
    cdh1_results.append({
        'histology': histology,
        'total_patients': total_in_group,
        'cdh1_mutated': mutated_in_group,
        'percentage': round(percentage, 2)
    })

# Convert to DataFrame and sort by percentage
results_df = pd.DataFrame(cdh1_results)
sorted_results = results_df.sort_values('percentage', ascending=False)

print('\nAll histological types sorted by CDH1 mutation percentage:')
print(sorted_results.to_string(index=False))

# Get top 3
top3 = sorted_results.head(3)
print('\nTop 3 histological types:')
print(top3.to_string(index=False))

output = {
    'all_results': sorted_results.to_dict('records'),
    'top3': top3.to_dict('records'),
    'total_alive_bladder': len(alive_bladder),
    'total_cdh1_mutated': len(cdh1_mutated_barcodes)
}

print('\n__RESULT__:')
print(json.dumps(output, default=str))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:10': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:32': {'status': 'analysis_complete'}, 'var_functions.execute_python:34': {'num_brca_alive': 0, 'histology_counts': {}, 'barcodes': []}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:52': {'top3': [{'histology': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'total_patients': 228, 'mutated_patients': 7, 'mutation_percentage': 3.070175438596491}], 'total_cdh1_mutated': 7}}

exec(code, env_args)
