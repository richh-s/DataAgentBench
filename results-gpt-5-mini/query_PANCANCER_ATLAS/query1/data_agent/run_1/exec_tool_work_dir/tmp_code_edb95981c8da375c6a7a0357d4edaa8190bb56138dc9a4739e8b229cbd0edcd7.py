code = """import json
import pandas as pd
import math

# Load clinical and RNA results from storage files
clinical_path = var_call_2pwdzCzK0lBE4uLCmCgsmzr8
rna_path = var_call_5Lrm65xZg8nD2KN57yTMirQq

with open(clinical_path, 'r') as f:
    clinical = json.load(f)
with open(rna_path, 'r') as f:
    rna = json.load(f)

clin_df = pd.DataFrame(clinical)
rna_df = pd.DataFrame(rna)

# Clean clinical: keep patient_id and histological_type, drop nulls
clin_df = clin_df[['patient_id', 'histological_type']].dropna()
# Exclude histological_type entries enclosed in square brackets (any '[' or ']')
clin_df = clin_df[~clin_df['histological_type'].astype(str).str.contains(r"\[|\]")]

# Prepare RNA: ensure normalized_count numeric, filter IGF2
rna_df = rna_df[rna_df['Symbol'] == 'IGF2'].copy()
# Convert normalized_count to float
def to_float(x):
    try:
        return float(x)
    except:
        return None
rna_df['normalized_count'] = rna_df['normalized_count'].map(to_float)
rna_df = rna_df.dropna(subset=['normalized_count'])

# Extract patient_id from ParticipantBarcode as the last segment after '-'
rna_df['patient_id'] = rna_df['ParticipantBarcode'].astype(str).apply(lambda s: s.split('-')[-1])

# Merge on patient_id
merged = pd.merge(rna_df, clin_df, on='patient_id', how='inner')

# Compute log10(normalized_count + 1)
import numpy as np
merged['log10_expr'] = np.log10(merged['normalized_count'] + 1)

# Group by histological_type and compute mean
grouped = merged.groupby('histological_type', dropna=False)['log10_expr'].mean().reset_index()

# Format results with at least four decimal places
result = {}
for _, row in grouped.iterrows():
    hist = row['histological_type']
    val = row['log10_expr']
    # format with 4 decimal places
    result[str(hist)] = format(float(val), '.4f')

# Print result as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VLxL1IAWDHqWjTg7LhXexfe7': ['clinical_info'], 'var_call_siBw3GH5p1huwNd5atuvOmvF': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_LQbFeZcN5zeap7CqmFgR3Rlo': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_T8rE6dcz4UYIyYSuNJt2yw9B': 'file_storage/call_T8rE6dcz4UYIyYSuNJt2yw9B.json', 'var_call_iliNvXk5XaQbitPoYBNgGf4T': 'file_storage/call_iliNvXk5XaQbitPoYBNgGf4T.json', 'var_call_BP8DPFgIDBdoGexvCMsGBjLC': 'file_storage/call_BP8DPFgIDBdoGexvCMsGBjLC.json', 'var_call_2pwdzCzK0lBE4uLCmCgsmzr8': 'file_storage/call_2pwdzCzK0lBE4uLCmCgsmzr8.json', 'var_call_5Lrm65xZg8nD2KN57yTMirQq': 'file_storage/call_5Lrm65xZg8nD2KN57yTMirQq.json'}

exec(code, env_args)
