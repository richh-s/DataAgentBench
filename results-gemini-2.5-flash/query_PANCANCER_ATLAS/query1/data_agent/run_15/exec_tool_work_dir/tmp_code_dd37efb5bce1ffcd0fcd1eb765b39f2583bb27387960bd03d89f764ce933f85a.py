code = """import pandas as pd
import json
import numpy as np

# Load the full results from the storage keys
with open(locals()["var_function-call-16944893329104091185"], 'r') as f:
    clinical_data = json.load(f)
with open(locals()["var_function-call-3132891237812737955"], 'r') as f:
    expression_data = json.load(f)

# Convert to pandas DataFrames
clinical_df = pd.DataFrame(clinical_data)
expression_df = pd.DataFrame(expression_data)

# Extract ParticipantBarcode from Patient_description in clinical_df
clinical_df['ParticipantBarcode'] = clinical_df['Patient_description'].str.extract(r'(TCGA-\w{2}-\w{4})')

# Filter for LGG patients where histological_type contains 'Brain lower grade glioma' (case-insensitive)
# and valid histology types (not null and not enclosed in square brackets)
lgg_clinical_df = clinical_df[
    clinical_df['histological_type'].str.contains('Brain lower grade glioma', na=False, case=False)
    & clinical_df['histological_type'].notna()
    & ~clinical_df['histological_type'].str.contains(r'\[.*\]', regex=True)
]

# Merge the two dataframes
merged_df = pd.merge(lgg_clinical_df, expression_df, on='ParticipantBarcode', how='inner')

# Convert normalized_count to numeric, handling errors by coercing to NaN
merged_df['normalized_count'] = pd.to_numeric(merged_df['normalized_count'], errors='coerce')

# Filter out rows with NaN in normalized_count
merged_df = merged_df.dropna(subset=['normalized_count'])

# Compute log10-transformed expression
merged_df['log10_expression'] = np.log10(merged_df['normalized_count'] + 1)

# Compute the average log10-transformed expression of IGF2 across different histology types
average_expression = merged_df.groupby('histological_type')['log10_expression'].mean().reset_index()

# Format the average values to at least four decimal places
average_expression['log10_expression'] = average_expression['log10_expression'].apply(lambda x: f'{x:.4f}')

print('__RESULT__:')
print(average_expression.to_json(orient='records'))"""

env_args = {'var_function-call-8802112951926730673': ['clinical_info'], 'var_function-call-9207009310809608146': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-830939399977309174': [], 'var_function-call-3132891237812737955': 'file_storage/function-call-3132891237812737955.json', 'var_function-call-11870531932887037701': [], 'var_function-call-2523567822683536758': 'file_storage/function-call-2523567822683536758.json', 'var_function-call-3278290834217809052': 'file_storage/function-call-3278290834217809052.json', 'var_function-call-1708262848495038031': [], 'var_function-call-18045456725144733795': 'file_storage/function-call-18045456725144733795.json', 'var_function-call-4677567907560326204': [], 'var_function-call-4550823675032615667': [], 'var_function-call-16944893329104091185': 'file_storage/function-call-16944893329104091185.json', 'var_function-call-10247324740713799602': []}

exec(code, env_args)
