code = """import json, re, pandas as pd, numpy as np

# load clinical
clin_src = var_call_23yrFK3sqSEb82jn63uY7X1z
if isinstance(clin_src, str):
    with open(clin_src,'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

df_clin = pd.DataFrame(clin)
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
df_clin['tcga_barcode'] = df_clin['participant_barcode'].astype(str).str.extract(pat, expand=False)
hist_df = df_clin.dropna(subset=['tcga_barcode','histological_type'])[['tcga_barcode','histological_type']].copy()

# load mutation
mut_src = var_call_oCqtYZ0Nq8fQfx7haNoGuds9
if isinstance(mut_src, str):
    with open(mut_src,'r') as f:
        mut = json.load(f)
else:
    mut = mut_src
mut_df = pd.DataFrame(mut)
mut_set = set(mut_df['participant_barcode'].dropna().unique().tolist())

hist_df['CDH1_mut'] = hist_df['tcga_barcode'].isin(mut_set)

ct = pd.crosstab(hist_df['histological_type'], hist_df['CDH1_mut'])
for col in [False, True]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[[False, True]]

# filter row categories with row total > 10
ct = ct.loc[ct.sum(axis=1) > 10]
# filter columns with col total > 10
ct = ct.loc[:, ct.sum(axis=0) > 10]

result = {
    'grand_total': int(ct.to_numpy().sum()),
    'row_categories': ct.index.tolist(),
    'col_categories': [str(c) for c in ct.columns.tolist()],
}

obs = ct.to_numpy(dtype=float)
grand = obs.sum()
if grand == 0 or obs.shape[0] == 0 or obs.shape[1] < 2:
    chi2 = None
    dof = None
    expected = None
else:
    expected_mat = (obs.sum(axis=1, keepdims=True) @ obs.sum(axis=0, keepdims=True)) / grand
    chi2 = float(np.sum((obs-expected_mat)**2/expected_mat))
    dof = int((obs.shape[0]-1)*(obs.shape[1]-1))
    expected = expected_mat.tolist()

result['chi_square'] = chi2
result['dof'] = dof

# observed table to records
obs_df = ct.copy()
# rename columns for clarity
rename_map = {}
if False in obs_df.columns: rename_map[False] = 'CDH1_wt'
if True in obs_df.columns: rename_map[True] = 'CDH1_mut'
obs_df = obs_df.rename(columns=rename_map).reset_index().rename(columns={'histological_type':'histological_type'})
result['observed'] = obs_df.to_dict(orient='records')
result['expected'] = expected

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_oCqtYZ0Nq8fQfx7haNoGuds9': 'file_storage/call_oCqtYZ0Nq8fQfx7haNoGuds9.json', 'var_call_8mkQX0YDOCOP6wdqoR8Pju1T': ['clinical_info'], 'var_call_iQo0Vu6qzBKhGdMU2o1b3FBZ': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_EbQtH9JCgce3ES2V6LonTt6E': [], 'var_call_23yrFK3sqSEb82jn63uY7X1z': 'file_storage/call_23yrFK3sqSEb82jn63uY7X1z.json'}

exec(code, env_args)
