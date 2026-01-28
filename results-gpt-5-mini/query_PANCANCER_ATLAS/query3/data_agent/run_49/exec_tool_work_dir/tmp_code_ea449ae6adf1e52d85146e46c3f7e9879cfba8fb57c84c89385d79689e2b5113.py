code = """import json
import pandas as pd

# Load clinical BRCA female data from storage file
with open(var_call_wOXlK7X1LpVRD27DXGZgtmv6, 'r') as f:
    clinical_records = json.load(f)

# Load mutation CDH1 PASS records
with open(var_call_cR3n6R7U9OgiyLtA9wIoxWyb, 'r') as f:
    mut_records = json.load(f)

# Create DataFrames
clin_df = pd.DataFrame(clinical_records)
mut_df = pd.DataFrame(mut_records)

# Filter clinical entries to those that mention Breast and FEMALE in Patient_description (case-insensitive)
clin_df = clin_df[clin_df['Patient_description'].str.lower().str.contains('breast', na=False) &
                  clin_df['Patient_description'].str.lower().str.contains('female', na=False)]

# Keep only rows with known histological_type
clin_df = clin_df[clin_df['histological_type'].notna()]
clin_df['histological_type'] = clin_df['histological_type'].astype(str).str.strip()
clin_df = clin_df[clin_df['histological_type'] != '']
clin_df = clin_df[~clin_df['histological_type'].str.lower().isin(['unknown','not available','na','not applicable'])]

# Deduplicate by patient_id (keep first occurrence)
clin_df = clin_df.drop_duplicates(subset=['patient_id'])

# Extract patient_id from mutation ParticipantBarcode (last segment after '-')
mut_df['patient_id'] = mut_df['ParticipantBarcode'].astype(str).apply(lambda x: x.split('-')[-1])

# Create set of mutated patient_ids
mutated_ids = set(mut_df['patient_id'].unique())

# Map mutation status to clinical patients
clin_df['mutated'] = clin_df['patient_id'].apply(lambda x: x in mutated_ids)

# Build contingency table: histological_type vs mutated
contingency = pd.crosstab(clin_df['histological_type'], clin_df['mutated'])
# Ensure both columns exist
if True not in contingency.columns:
    contingency[True] = 0
if False not in contingency.columns:
    contingency[False] = 0

# Rename columns for clarity
contingency = contingency.rename(columns={False: 'Not_Mutated', True: 'Mutated'})

# Exclude histological categories with marginal totals <= 10 (row totals)
contingency['RowTotal'] = contingency['Mutated'] + contingency['Not_Mutated']
filtered = contingency[contingency['RowTotal'] > 10].copy()
filtered = filtered[['Mutated','Not_Mutated']]

# If after filtering no rows left, return None
if filtered.shape[0] == 0:
    result = {'chi2': None, 'message': 'No histological categories with total > 10 after filtering.'}
else:
    # Compute chi-square statistic
    obs = filtered.values.astype(float)
    row_totals = obs.sum(axis=1).reshape(-1,1)
    col_totals = obs.sum(axis=0).reshape(1,-1)
    grand_total = obs.sum()
    expected = row_totals.dot(col_totals) / grand_total
    # Avoid division by zero
    mask = expected > 0
    chi2 = ((obs - expected)**2 / expected)[mask].sum()
    # Degrees of freedom: (r-1)*(c-1)
    df = (obs.shape[0]-1) * (obs.shape[1]-1)
    result = {'chi2': float(chi2), 'degrees_of_freedom': int(df), 'included_histological_types_count': int(obs.shape[0]), 'grand_total': int(grand_total)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4lA1HzAho0G5DZsa4iRpezE2': ['clinical_info'], 'var_call_8TZW5OoNUUm9DG50X4vAyxft': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_49aseKVj2rTyctRf6UFfmIPC': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_CQXeA9hMfyA1npDlor3xcOdG': [], 'var_call_Qqcl68dXHluJ8uLEWrbZiIhv': 'file_storage/call_Qqcl68dXHluJ8uLEWrbZiIhv.json', 'var_call_wOXlK7X1LpVRD27DXGZgtmv6': 'file_storage/call_wOXlK7X1LpVRD27DXGZgtmv6.json', 'var_call_H6sEtMrlXzR95gzJ7UXEI2nD': 'file_storage/call_H6sEtMrlXzR95gzJ7UXEI2nD.json', 'var_call_cR3n6R7U9OgiyLtA9wIoxWyb': 'file_storage/call_cR3n6R7U9OgiyLtA9wIoxWyb.json'}

exec(code, env_args)
