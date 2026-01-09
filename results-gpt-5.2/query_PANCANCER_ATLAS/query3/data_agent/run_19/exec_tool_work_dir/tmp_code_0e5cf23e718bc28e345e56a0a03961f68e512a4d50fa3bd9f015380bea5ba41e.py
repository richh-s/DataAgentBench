code = """import json, re, pandas as pd

def load_records(x):
    if isinstance(x, str):
        with open(x,'r') as f:
            return json.load(f)
    return x

def extract_tcga_barcode(s):
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', str(s))
    return m.group(1) if m else None

clin = pd.DataFrame(load_records(var_call_XijJtk44Y7M14YJfCRmV3s2l))
clin['participant_barcode'] = clin['patient_description'].map(extract_tcga_barcode)
clin = clin.dropna(subset=['participant_barcode','histological_type'])
clin['histological_type'] = clin['histological_type'].astype(str).str.strip()

mut = pd.DataFrame(load_records(var_call_hS7RQQhihNNXgn69YqMqzj5s))
mut_set = set(mut['participant_barcode'].dropna().astype(str))

clin['cdh1_mut'] = clin['participant_barcode'].isin(mut_set)

ct = pd.crosstab(clin['histological_type'], clin['cdh1_mut'])
for col in [False, True]:
    if col not in ct.columns:
        ct[col]=0
ct = ct.loc[:, [False, True]]
ct.columns = ['CDH1_WT','CDH1_MUT']

row_total = ct.sum(axis=1)
ct_f = ct.loc[row_total > 10].copy()

obs = ct_f.astype(float)
row_totals = obs.sum(axis=1)
col_totals = obs.sum(axis=0)
grand_total = float(obs.values.sum())

expected = pd.DataFrame(index=obs.index, columns=obs.columns, dtype=float)
for r in obs.index:
    expected.loc[r,:] = row_totals.loc[r] * col_totals / grand_total

chi2 = float((((obs-expected)**2)/expected).values.sum())

out = {
  'chi_square': chi2,
  'grand_total': int(grand_total),
  'histology_levels_included': int(obs.shape[0]),
  'observed_table': ct_f.reset_index().rename(columns={'histological_type':'histological_type'}).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_hS7RQQhihNNXgn69YqMqzj5s': 'file_storage/call_hS7RQQhihNNXgn69YqMqzj5s.json', 'var_call_FQ6eVtVWxmVUTEzAes3f22qQ': [{'column_name': 'Patient_description'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'neoplasm_histologic_grade'}], 'var_call_7VYpEEJysJI0apgAWrSGznZT': [], 'var_call_XCFjJRishAaCm9yvbQ4w2KoL': [{'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'residual_tumor'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'tumor_tissue_site_other'}], 'var_call_kqlNXKPhoH5lOcx2B36Lnh5i': [], 'var_call_leBBtQevwm4akvbtGaeoHrdo': [], 'var_call_xsdWPAjiyPLWKXSgyuFo6DyQ': [], 'var_call_NpNDVol2J0ULNHloSG5Ium2L': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}], 'var_call_i7onwqT1iJmzF5W6yjzO4PYj': [{'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'margin_status'}, {'column_name': 'menopause_status'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_CojyxWypGox4LOi2wrAO44e8': [{'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}], 'var_call_kiYbmnq3GzJv0fPgzt6IZiiE': [{'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'residual_tumor'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'tumor_tissue_site_other'}], 'var_call_AlFoGmstoPSUO5QhbRxzIOV8': [], 'var_call_hMxsQOlebItm8BQZy26LF2qn': [], 'var_call_hBUbRKbipsa3SFjC57WT0iLT': [{'participant_barcode': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'participant_barcode': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'participant_barcode': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'participant_barcode': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'participant_barcode': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}], 'var_call_oKvCQg6ycJyctjSz82NrjnyA': [], 'var_call_KFSogK75nHuOomAqETsXOnuG': [{'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'diagnosis'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}], 'var_call_FJhGcKC4uXTqsZNWONhjOWKj': [{'diagnosis': 'None', 'n': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'n': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'n': '490'}], 'var_call_BNNNiGGPKw2H4vgkrjufjqMc': [], 'var_call_ARoeh9hi2wPAGyG65pM5CoSk': [], 'var_call_yuahWqF5hlAw9KmBoFXZ1lA7': {'status': 'need_clinical_query'}, 'var_call_XijJtk44Y7M14YJfCRmV3s2l': 'file_storage/call_XijJtk44Y7M14YJfCRmV3s2l.json'}

exec(code, env_args)
