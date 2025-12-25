code = """import json, re, pandas as pd

# Load full clinical data
with open(var_call_RKdvuurd6q6AUcSJVXAaF63i, 'r') as f:
    clinical = json.load(f)
clinical_df = pd.DataFrame(clinical)

# Extract patient barcode and vital status from Patient_description
pat = clinical_df['Patient_description'].str.extract(r'(TCGA-[A-Z0-9\-]+).*vital status: ([A-Za-z]+)', expand=True)
clinical_df['ParticipantBarcode'] = pat[0]
clinical_df['vital_status'] = pat[1]

# Keep BRCA only, based on hint "BRCA means Bladder urothelial carcinoma" is likely an error; actually BRCA is breast invasive carcinoma.
# But we don't have cancer_type field, so approximate by selecting rows whose description contains 'breast' or 'BRCA'
mask_brca = clinical_df['Patient_description'].str.contains('breast', case=False, na=False) | clinical_df['Patient_description'].str.contains('BRCA', case=False, na=False)
brca_clin = clinical_df[mask_brca].copy()

# Alive patients
brca_alive = brca_clin[brca_clin['vital_status'].str.upper() == 'ALIVE'].copy()

# Load CDH1 mutation data (already filtered by gene)
with open(var_call_2cOtTkFHVO5XA70gR5z47o24, 'r') as f:
    mut = json.load(f)
mut_df = pd.DataFrame(mut).drop_duplicates(subset=['ParticipantBarcode'])

# Flag CDH1 mutation
brca_alive['CDH1_mut'] = brca_alive['ParticipantBarcode'].isin(mut_df['ParticipantBarcode']).astype(int)

# Compute percentage of CDH1 mutants by histological_type
summary = brca_alive.groupby('histological_type').agg(
    n_alive=('ParticipantBarcode', 'nunique'),
    n_mut=('CDH1_mut', 'sum')
).reset_index()
summary['pct_mut'] = (summary['n_mut'] / summary['n_alive'] * 100).round(2)

# Keep histological types with at least, say, 5 alive patients to avoid tiny groups
summary = summary[summary['n_alive'] >= 5]

# Top 3 by percentage
top3 = summary.sort_values(['pct_mut','n_alive'], ascending=[False, False]).head(3)

result = top3.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result) )"""

env_args = {'var_call_2cOtTkFHVO5XA70gR5z47o24': 'file_storage/call_2cOtTkFHVO5XA70gR5z47o24.json', 'var_call_9PMU0vHrhoqPt2xyvMpSsCXl': ['clinical_info'], 'var_call_8tZVBqXAESM7mnZCn0SPwEti': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_RKdvuurd6q6AUcSJVXAaF63i': 'file_storage/call_RKdvuurd6q6AUcSJVXAaF63i.json'}

exec(code, env_args)
