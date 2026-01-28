code = """import json
import pandas as pd
import math
import re

# LGG clinical data
lgg_clinical = var_functions_query_db_24

# IGF2 expression data
igf2_expression = var_functions_query_db_10

# Create DataFrames
df_clinical = pd.DataFrame(lgg_clinical)
df_expression = pd.DataFrame(igf2_expression)

# Convert normalized_count to numeric
df_expression['normalized_count'] = pd.to_numeric(df_expression['normalized_count'], errors='coerce')

# Filter for valid IGF2 expression values
df_expression = df_expression[df_expression['normalized_count'].notna()]

# Extract patient barcodes from Patient_description
def extract_barcode(description):
    if pd.isna(description):
        return None
    # Look for TCGA- barcodes
    match = re.search(r'(TCGA-\w+)', str(description))
    if match:
        return match.group(1)
    return None

df_clinical['ParticipantBarcode'] = df_clinical['Patient_description'].apply(extract_barcode)

# Filter out records without barcodes
df_clinical = df_clinical[df_clinical['ParticipantBarcode'].notna()]

# Filter histological types that are not enclosed in square brackets
# and have valid values
df_clinical = df_clinical[
    (df_clinical['histological_type'].notna()) &
    (df_clinical['histological_type'].str.len() > 0) &
    (~df_clinical['histological_type'].str.contains(r'\[|\]', regex=True, na=False))
]

# Merge clinical and expression data
merged_df = pd.merge(
    df_clinical[['ParticipantBarcode', 'histological_type']],
    df_expression[['ParticipantBarcode', 'normalized_count']],
    on='ParticipantBarcode',
    how='inner'
)

# Calculate log10(normalized_count + 1)
merged_df['log10_expression'] = merged_df['normalized_count'].apply(lambda x: math.log10(x + 1))

# Group by histological type and calculate average
results = merged_df.groupby('histological_type')['log10_expression'].mean().reset_index()

# Round to 4 decimal places
results['avg_log10_expression'] = results['log10_expression'].round(4)

# Sort by histology type
results = results.sort_values('histological_type')

print('__RESULT__:')
print(json.dumps({
    'total_lgg_patients': df_clinical['ParticipantBarcode'].nunique(),
    'patients_with_igf2_data': merged_df['ParticipantBarcode'].nunique(),
    'unique_histology_types': results['histological_type'].tolist(),
    'averages': results.to_dict('records')
}))"""

env_args = {'var_functions.query_db:0': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'Symbol': 'LXN'}, {'Symbol': 'ZNF770'}, {'Symbol': 'AMELY'}, {'Symbol': 'TPTE2P1'}, {'Symbol': 'ITGB3'}, {'Symbol': 'DEFB116'}, {'Symbol': 'FGD1'}, {'Symbol': 'P2RY14'}, {'Symbol': 'ARID5B'}, {'Symbol': 'TSPY1'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
