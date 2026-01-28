code = """import pandas as pd
import json

# Load clinical and mutation data from storage-provided file paths
clin_path = var_call_Hzg8SE2GSkBOJV1N1F4yprbM
mut_path = var_call_I3NBpL8AZIqpbP9oxT7qqRCx

clin = pd.read_json(clin_path)
mut = pd.read_json(mut_path)

# Filter clinical to alive BRCA patients: Patient_description contains 'Alive'
clin_alive = clin[clin['Patient_description'].str.contains('Alive', na=False)]
# Ensure patient_id and histological_type present
clin_alive = clin_alive[['patient_id', 'histological_type']].dropna()

# Deduplicate patient entries, keep first histological_type occurrence
clin_alive = clin_alive.drop_duplicates(subset=['patient_id'])

# Extract patient code from mutation ParticipantBarcode (last segment after hyphen)
mut['patient_id'] = mut['ParticipantBarcode'].astype(str).str.split('-').str[-1]
# Filter for gene CDH1
mut_cdh1 = mut[mut['Hugo_Symbol']=='CDH1']
# Unique mutated patients
mutated_patients = set(mut_cdh1['patient_id'].astype(str).unique())

# Map clinical patients to histological types
# Consider only patients present in clin_alive
clin_alive['patient_id'] = clin_alive['patient_id'].astype(str)

# Compute counts per histological_type
summary = clin_alive.groupby('histological_type').agg(total_alive=('patient_id','nunique'),
                                                     patients_list=('patient_id', lambda x: list(x))).reset_index()

# For each histological type, count mutated patients
def count_mutated(pat_list):
    return sum(1 for p in pat_list if p in mutated_patients)

summary['mutated_count'] = summary['patients_list'].apply(count_mutated)
summary['mutation_percentage'] = (summary['mutated_count'] / summary['total_alive']) * 100

# Sort by mutation_percentage desc, then by mutated_count desc
summary_sorted = summary.sort_values(['mutation_percentage','mutated_count'], ascending=[False, False])

# Take top 3
top3 = summary_sorted.head(3)

# Prepare output
result_list = []
for _, row in top3.iterrows():
    result_list.append({
        'histological_type': row['histological_type'],
        'total_alive_patients': int(row['total_alive']),
        'mutated_patients': int(row['mutated_count']),
        'mutation_percentage': round(float(row['mutation_percentage']), 2)
    })

output = json.dumps(result_list)
print('__RESULT__:')
print(output)"""

env_args = {'var_call_fRfdQpcdE7fINIzMjBrS7nVT': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_urpBypS58t9KoN52BiFgcdcc': [], 'var_call_JZFR4Dq4xwdAfe7Oq92ujVIA': [], 'var_call_HXTw5kFF5rSa0pDRGpLVGa1p': 'file_storage/call_HXTw5kFF5rSa0pDRGpLVGa1p.json', 'var_call_nFh0NslO8fTrXLdjA966RCUY': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_wM6bftEyGHNKKu8WvhBG4NiM': [{'Hugo_Symbol': 'CDH1'}], 'var_call_I3NBpL8AZIqpbP9oxT7qqRCx': 'file_storage/call_I3NBpL8AZIqpbP9oxT7qqRCx.json', 'var_call_OwUNdXwLAZHUyEWM1Mk9lVx4': 'file_storage/call_OwUNdXwLAZHUyEWM1Mk9lVx4.json', 'var_call_Hzg8SE2GSkBOJV1N1F4yprbM': 'file_storage/call_Hzg8SE2GSkBOJV1N1F4yprbM.json'}

exec(code, env_args)
