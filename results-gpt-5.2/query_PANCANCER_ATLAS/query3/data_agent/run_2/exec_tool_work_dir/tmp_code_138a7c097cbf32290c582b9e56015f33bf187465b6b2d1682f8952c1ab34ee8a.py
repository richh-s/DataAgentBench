code = """import json, re, pandas as pd

# load clinical
clin_path = var_call_hyiBSdVuByqrGFbEFZXJd9fe
with open(clin_path,'r') as f:
    clin = json.load(f)
clin_df = pd.DataFrame(clin)
# extract TCGA barcode from Patient_description text
clin_df['participant_barcode_extracted'] = clin_df['participant_barcode'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')[0]
# keep female only
clin_df['is_female'] = clin_df['participant_barcode'].str.contains('FEMALE', case=False, na=False)
clin_df = clin_df[clin_df['is_female'] & clin_df['participant_barcode_extracted'].notna()].copy()
clin_df = clin_df[['participant_barcode_extracted','histological_type']].rename(columns={'participant_barcode_extracted':'participant_barcode'})

# load mutation participants
mut_path = var_call_ikVTvO3uik6r74tqEcDmPnh9
with open(mut_path,'r') as f:
    mut = json.load(f)
mut_set = set([r['participant_barcode'] for r in mut])

# contingency
clin_df['cdh1_mut'] = clin_df['participant_barcode'].isin(mut_set).map({True:'Mut', False:'WT'})
ct = pd.crosstab(clin_df['histological_type'], clin_df['cdh1_mut'])
# ensure both columns
for col in ['Mut','WT']:
    if col not in ct.columns:
        ct[col]=0
ct = ct[['Mut','WT']]
# filter categories with marginal totals <=10
ct_f = ct[ct.sum(axis=1) > 10].copy()
# also ensure column totals >10
col_keep = [c for c in ct_f.columns if ct_f[c].sum() > 10]
ct_f = ct_f[col_keep]

# compute chi-square
import numpy as np
obs = ct_f.values.astype(float)
row_tot = obs.sum(axis=1, keepdims=True)
col_tot = obs.sum(axis=0, keepdims=True)
grand = obs.sum()
exp = row_tot @ col_tot / grand
chi2 = float(((obs-exp)**2/exp).sum())
dof = int((obs.shape[0]-1)*(obs.shape[1]-1))

result = {
  'chi_square': chi2,
  'dof': dof,
  'grand_total': int(grand),
  'table': ct_f.reset_index().to_dict(orient='records'),
  'row_categories_used': ct_f.shape[0],
  'col_totals': {c:int(ct_f[c].sum()) for c in ct_f.columns}
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ikVTvO3uik6r74tqEcDmPnh9': 'file_storage/call_ikVTvO3uik6r74tqEcDmPnh9.json', 'var_call_BnanU3gbsFV974qezLkAQP3t': ['clinical_info'], 'var_call_4Fz15OJodZdp0gjjK3wtZQtG': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_KgNCVYnTt7xXtWrN0v36ikHm': [], 'var_call_lnh3hscAdp17v89VhjH1AMqW': [], 'var_call_2m0p8l8fTYDlX7ba5bhNI4HO': [], 'var_call_03SgtuhICIlWX5TmrEScDf5Q': [], 'var_call_gmcrGitlvIoSmhfk3D3JGigG': [{'diagnosis': 'None', 'n': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'n': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'n': '490'}], 'var_call_UAjnJX6JwicgYs1044vNAEF7': ['tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'person_neoplasm_cancer_status', 'histological_type', 'eastern_cancer_oncology_group', 'residual_tumor', 'histological_type_other', 'tumor_tissue_site_other', 'axillary_lymph_node_stage_method_type', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'days_to_new_tumor_event_after_initial_treatment', 'family_history_of_cancer'], 'var_call_hyiBSdVuByqrGFbEFZXJd9fe': 'file_storage/call_hyiBSdVuByqrGFbEFZXJd9fe.json'}

exec(code, env_args)
