code = """import json, re, pandas as pd

# Load full clinical data
with open(var_call_0uDBYAGqdnoI3R3YHMpc63jb, 'r') as f:
    clinical = json.load(f)

clinical_df = pd.DataFrame(clinical)

# Extract patient barcode and vital status from Patient_description
pat = clinical_df['Patient_description'].str.extract(r'(TCGA-[A-Z0-9-]+).*vital status: (Alive|Dead)', expand=True)
clinical_df['ParticipantBarcode'] = pat[0]
clinical_df['vital_status'] = pat[1]

# Filter to BRCA patients by ICD_O_3_site if available or histology keywords if bladder specified in hint (note hint says BRCA=Bladder)
# Check if icd_o_3_site exists
if 'icd_o_3_site' in clinical_df.columns:
    brca_mask = clinical_df['icd_o_3_site'].str.contains('Bladder', case=False, na=False)
else:
    brca_mask = clinical_df['diagnosis'].str.contains('Bladder', case=False, na=False)

brca_clin = clinical_df[brca_mask].copy()

# Alive patients
alive_brca = brca_clin[brca_clin['vital_status'] == 'Alive'].copy()

# Keep needed cols
alive_brca = alive_brca[['ParticipantBarcode','histological_type']].dropna()

# Load CDH1 mutation participants
with open(var_call_OZqS86JZE0erKcsVXNtH5xEz, 'r') as f:
    muts = json.load(f)

muts_df = pd.DataFrame(muts).drop_duplicates(subset=['ParticipantBarcode'])

# Merge to indicate mutation presence
merged = alive_brca.merge(muts_df[['ParticipantBarcode']], on='ParticipantBarcode', how='left', indicator='mut')
merged['has_CDH1_mut'] = merged['mut'].eq('both')

# For each histological type, compute % with mutation
summary = merged.groupby('histological_type').agg(
    total_alive=('ParticipantBarcode','nunique'),
    mutated=('has_CDH1_mut','sum')
).reset_index()
summary['percent_mutated'] = (summary['mutated'] / summary['total_alive'] * 100).round(2)

# Get top 3 hist types by percent_mutated (break ties by total_alive descending)
summary = summary[summary['total_alive'] >= 5]  # require at least 5 alive patients per type for stability
summary_sorted = summary.sort_values(['percent_mutated','total_alive'], ascending=[False, False]).head(3)

result = summary_sorted[['histological_type','percent_mutated','mutated','total_alive']].to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_OZqS86JZE0erKcsVXNtH5xEz': 'file_storage/call_OZqS86JZE0erKcsVXNtH5xEz.json', 'var_call_7jpLv7nomoTyCkaH9XQLu1p9': ['clinical_info'], 'var_call_47fK8hMYSEyDaC1MGNG60Kwm': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_0uDBYAGqdnoI3R3YHMpc63jb': 'file_storage/call_0uDBYAGqdnoI3R3YHMpc63jb.json'}

exec(code, env_args)
