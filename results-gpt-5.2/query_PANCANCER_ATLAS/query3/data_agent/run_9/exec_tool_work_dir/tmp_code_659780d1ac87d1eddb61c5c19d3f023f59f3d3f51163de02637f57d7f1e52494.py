code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

clin = load_records(var_call_yB6zEBhX2VdiUMbMdASg32Fo)
mut = load_records(var_call_qcI9HU0UpkhMoIBOfUiJOFiO)

df_clin = pd.DataFrame(clin)
df_mut = pd.DataFrame(mut)

# extract TCGA barcode from Patient_description text
df_clin['participant_barcode_extracted'] = df_clin['participant_barcode'].astype(str).str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)

df_clin = df_clin.dropna(subset=['participant_barcode_extracted','histological_type']).copy()
# normalize histological types
df_clin['histological_type_norm'] = df_clin['histological_type'].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)

mut_set = set(df_mut['participant_barcode'].dropna().astype(str))

df_clin['CDH1_mut'] = df_clin['participant_barcode_extracted'].isin(mut_set)

# contingency table
ct = pd.crosstab(df_clin['histological_type_norm'], df_clin['CDH1_mut'])
# ensure both columns exist
for col in [False, True]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[[False, True]]

# filter categories with row totals <=10
ct_f = ct.loc[ct.sum(axis=1) > 10].copy()

# compute chi-square
obs = ct_f.values.astype(float)
row_tot = obs.sum(axis=1, keepdims=True)
col_tot = obs.sum(axis=0, keepdims=True)
grand = obs.sum()
exp = row_tot @ (col_tot / grand)
chi2 = float(((obs - exp)**2 / exp).sum())

dof = int((ct_f.shape[0]-1)*(ct_f.shape[1]-1))

out = {
    'chi_square': chi2,
    'degrees_of_freedom': dof,
    'n_patients_used': int(grand),
    'n_histological_types_used': int(ct_f.shape[0]),
    'contingency_table': ct_f.reset_index().rename(columns={'histological_type_norm':'histological_type', False:'CDH1_mut_false', True:'CDH1_mut_true'}).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_qcI9HU0UpkhMoIBOfUiJOFiO': 'file_storage/call_qcI9HU0UpkhMoIBOfUiJOFiO.json', 'var_call_DtOOYIq2VQTI0DwT8i38q1qg': ['clinical_info'], 'var_call_9p3TwdV4yiqjXGkHq72Y3tIF': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_I38Q6Q9TJAXBt9GJD19BafHZ': [], 'var_call_iak6tMZgZbJTpmg0DfD2OTU7': [{'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_QCTaLHgIXRxhpNVzS3XOUXI5': [{'diagnosis': 'None', 'n': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'n': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'n': '490'}], 'var_call_NJJB6D6mC2N9besBtRR7jScL': [{'icd_o_3_site': 'C50.9', 'n': '1079'}, {'icd_o_3_site': 'C64.9', 'n': '871'}, {'icd_o_3_site': 'C71.9', 'n': '646'}, {'icd_o_3_site': 'C56.9', 'n': '579'}, {'icd_o_3_site': 'C34.1', 'n': '553'}, {'icd_o_3_site': 'C54.1', 'n': '551'}, {'icd_o_3_site': 'C73.9', 'n': '505'}, {'icd_o_3_site': 'C61.9', 'n': '495'}, {'icd_o_3_site': 'C71.0', 'n': '437'}, {'icd_o_3_site': 'C22.0', 'n': '376'}, {'icd_o_3_site': 'C34.3', 'n': '351'}, {'icd_o_3_site': 'C53.9', 'n': '300'}, {'icd_o_3_site': 'C67.9', 'n': '237'}, {'icd_o_3_site': 'C16.3', 'n': '156'}, {'icd_o_3_site': 'C74.9', 'n': '145'}, {'icd_o_3_site': 'C25.0', 'n': '140'}, {'icd_o_3_site': 'C62.9', 'n': '134'}, {'icd_o_3_site': 'C02.9', 'n': '129'}, {'icd_o_3_site': 'C15.5', 'n': '122'}, {'icd_o_3_site': 'C32.9', 'n': '118'}], 'var_call_yB6zEBhX2VdiUMbMdASg32Fo': 'file_storage/call_yB6zEBhX2VdiUMbMdASg32Fo.json'}

exec(code, env_args)
