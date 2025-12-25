code = """import re, json, pandas as pd

# load full clinical info from file
path = var_call_tcae8u9SVE7F0m6qzEeNA8Fx
with open(path, 'r') as f:
    clinical = json.load(f)

clin_df = pd.DataFrame(clinical)

# extract ParticipantBarcode from Patient_description using regex TCGA-..-.... pattern
clin_df['ParticipantBarcode'] = clin_df['Patient_description'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')

# filter LGG patients: look for 'Glioma' and 'lower grade' or 'Brain lower grade glioma' in description
mask_lgg = clin_df['Patient_description'].str.contains('Brain lower grade glioma|lower grade glioma|LGG', case=False, na=False)
clin_lgg = clin_df[mask_lgg].copy()

# also keep histological_type
clin_lgg = clin_lgg[['ParticipantBarcode','histological_type']]

# load RNA expression result
path_expr = var_call_0Ayg4mzyM99ozT1GIhZOQpsb
with open(path_expr, 'r') as f:
    expr = json.load(f)
expr_df = pd.DataFrame(expr)
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])

# merge on ParticipantBarcode
merged = pd.merge(clin_lgg, expr_df, left_on='ParticipantBarcode', right_on='ParticipantBarcode', how='inner')

# remove histology annotations enclosed in square brackets: keep rows where histological_type not like "[... ]"
mask_brackets = merged['histological_type'].str.match(r'^\[.*\]$', na=False)
merged = merged[~mask_brackets].copy()

# compute log10(normalized_count + 1)
import numpy as np
merged['log10_expr'] = np.log10(merged['normalized_count'] + 1)

# group by histology and compute mean
result = merged.groupby('histological_type')['log10_expr'].mean().round(4).sort_index()

out = result.reset_index().to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_0Ayg4mzyM99ozT1GIhZOQpsb': 'file_storage/call_0Ayg4mzyM99ozT1GIhZOQpsb.json', 'var_call_MjWeoIlp5JW88trSXQ7zKUv3': ['clinical_info'], 'var_call_Tf8powYPI0EwtXbDww0IJy2m': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}], 'var_call_vGqu3JuM1YiZV65oPTUR73bx': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_tcae8u9SVE7F0m6qzEeNA8Fx': 'file_storage/call_tcae8u9SVE7F0m6qzEeNA8Fx.json'}

exec(code, env_args)
