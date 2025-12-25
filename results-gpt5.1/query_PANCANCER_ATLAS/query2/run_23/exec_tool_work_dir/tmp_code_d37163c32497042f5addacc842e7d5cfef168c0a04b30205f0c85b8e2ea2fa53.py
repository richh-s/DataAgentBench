code = """import json, re, pandas as pd

# Load full clinical data
with open(var_call_EjoOsb1yJhURxjwZAnKUng9r, 'r') as f:
    clinical = json.load(f)

clinical_df = pd.DataFrame(clinical)

# Extract patient barcode from Patient_description (pattern TCGA-..-....)
clinical_df['ParticipantBarcode'] = clinical_df['Patient_description'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')[0]

# Keep alive patients (vital status Alive in text) and BRCA cohort (Bladder urothelial carcinoma per hint)
mask_alive = clinical_df['Patient_description'].str.contains('vital status: Alive', case=False, na=False)
mask_brca = clinical_df['Patient_description'].str.contains('Bladder urothelial carcinoma', case=False, na=False)
clinical_brca_alive = clinical_df[mask_alive & mask_brca].dropna(subset=['ParticipantBarcode'])[['ParticipantBarcode','histological_type']]

# Load CDH1 mutation data
with open(var_call_OHeJJ5987AzqIG8OFk6yWjHd, 'r') as f:
    mut = json.load(f)
mut_df = pd.DataFrame(mut)

# Flag BRCA-alive patients with CDH1 mutation
mut_brca = mut_df.merge(clinical_brca_alive, on='ParticipantBarcode', how='inner')

# For each histological type among BRCA-alive, compute % with CDH1 mutation
# First, total alive BRCA patients per hist type
total_per_hist = clinical_brca_alive.groupby('histological_type')['ParticipantBarcode'].nunique().rename('total_patients')
# Then, mutated per hist type
mut_per_hist = mut_brca.groupby('histological_type')['ParticipantBarcode'].nunique().rename('mutated_patients')

summary = pd.concat([total_per_hist, mut_per_hist], axis=1).fillna(0)
summary['mutation_percentage'] = (summary['mutated_patients'] / summary['total_patients'] * 100).round(2)
summary = summary.sort_values('mutation_percentage', ascending=False)

# Get top 3 histological types by mutation percentage
top3 = summary.head(3).reset_index()

result = top3.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_OHeJJ5987AzqIG8OFk6yWjHd': 'file_storage/call_OHeJJ5987AzqIG8OFk6yWjHd.json', 'var_call_3fH3eQfM8bdjJX8HTOlfwUub': ['clinical_info'], 'var_call_JcRyq82Fr3H7v3elKGGYw6Dd': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_8ePIWalbcQTfUePutpFravhZ': [], 'var_call_EjoOsb1yJhURxjwZAnKUng9r': 'file_storage/call_EjoOsb1yJhURxjwZAnKUng9r.json'}

exec(code, env_args)
