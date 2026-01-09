code = """import json, re, pandas as pd

# load clinical (large json file)
path_clin = var_call_xUSYM48QsgLV6xeIrxXxWK9T
with open(path_clin, 'r') as f:
    clin = json.load(f)

# load mutation cdh1 carriers (large json file)
path_mut = var_call_ESUlp6PUWFu7ONnCFpewj8uM
with open(path_mut, 'r') as f:
    mut = json.load(f)

clin_df = pd.DataFrame(clin)
mut_df = pd.DataFrame(mut)

# extract TCGA barcode from Patient_description
clin_df['barcode'] = clin_df['participant_barcode'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)
clin_df = clin_df.dropna(subset=['barcode','histological_type']).copy()

# ensure unique patient record
clin_df = clin_df.drop_duplicates(subset=['barcode'])

mut_set = set(mut_df['participant_barcode'].astype(str).tolist())
clin_df['cdh1_mut'] = clin_df['barcode'].isin(mut_set).astype(int)

# build contingency counts by histological type
ct = clin_df.groupby(['histological_type','cdh1_mut']).size().unstack(fill_value=0)
# ensure both columns 0 and 1 exist
for col in [0,1]:
    if col not in ct.columns:
        ct[col]=0
ct = ct[[0,1]]

# exclude categories with marginal totals <=10
ct['row_total'] = ct[0] + ct[1]
ct_filt = ct[ct['row_total']>10].drop(columns=['row_total'])

# if after filtering not enough categories, still compute (but will be limited)
obs = ct_filt.to_numpy(dtype=float)
row_tot = obs.sum(axis=1, keepdims=True)
col_tot = obs.sum(axis=0, keepdims=True)
grand = obs.sum()
exp = row_tot @ (col_tot / grand) if grand>0 else obs*0

chi2 = float(((obs-exp)**2/exp).sum()) if grand>0 else None

df = int((obs.shape[0]-1)*(obs.shape[1]-1)) if obs.size>0 else 0

# also provide table
out_table = []
for idx, row in ct_filt.iterrows():
    out_table.append({'histological_type': idx, 'cdh1_mut_0': int(row[0]), 'cdh1_mut_1': int(row[1]), 'row_total': int(row[0]+row[1])})

out = {
    'n_patients_with_known_histology_female_brca': int(len(clin_df)),
    'n_histology_categories_after_filter_row_total_gt10': int(ct_filt.shape[0]),
    'grand_total_after_filter': int(grand),
    'chi_square_statistic': chi2,
    'degrees_of_freedom': df,
    'contingency_table': out_table
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ESUlp6PUWFu7ONnCFpewj8uM': 'file_storage/call_ESUlp6PUWFu7ONnCFpewj8uM.json', 'var_call_wrdqmFYN3DUPBS1RcLDSYfDI': ['clinical_info'], 'var_call_rcpgEkJRlCO1yzwXEJwjZYU4': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_5i0FypaOOZcsNlCC9iq9I1zI': [{'participant_barcode': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'participant_barcode': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'participant_barcode': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'participant_barcode': 'Clinical entry C07B122E-AC50-4DB2-ADD2-5617A5D0E976 identifies patient TCGA-GM-A2DA, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Dead.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'participant_barcode': 'The individual with barcode TCGA-3C-AAAU and UUID 6E7D5EC6-A469-467C-B748-237353C23416 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}], 'var_call_xUSYM48QsgLV6xeIrxXxWK9T': 'file_storage/call_xUSYM48QsgLV6xeIrxXxWK9T.json'}

exec(code, env_args)
