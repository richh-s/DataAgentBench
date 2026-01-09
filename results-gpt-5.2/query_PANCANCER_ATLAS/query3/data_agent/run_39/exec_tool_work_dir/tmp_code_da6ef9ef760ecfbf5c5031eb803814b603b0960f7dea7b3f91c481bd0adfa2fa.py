code = """import pandas as pd, json, re

def load_res(var):
    if isinstance(var, str):
        import os, json
        with open(var, 'r') as f:
            return json.load(f)
    return var

clin = load_res(var_call_EPf3n07FvgDS2m7JXMXZeYmg)
mut = load_res(var_call_cB25AfS4pgww9Dr0VtqFSHcg)

df_clin = pd.DataFrame(clin)
# parse TCGA barcode from participant description
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
df_clin['barcode'] = df_clin['participant'].str.extract(pat, expand=False)
# keep only valid barcodes
df_clin = df_clin.dropna(subset=['barcode','histology'])
# mutation set
mut_df = pd.DataFrame(mut)
mut_set = set(mut_df['participant'])

df_clin['cdh1_mut'] = df_clin['barcode'].isin(mut_set).astype(int)

# contingency
ct = pd.crosstab(df_clin['histology'], df_clin['cdh1_mut'])
# ensure both columns 0 and 1 exist
for col in [0,1]:
    if col not in ct.columns:
        ct[col]=0
ct = ct[[0,1]]

# filter categories with marginal totals <=10 (row totals)
row_tot = ct.sum(axis=1)
ct_f = ct.loc[row_tot>10].copy()

# recompute after filtering
obs = ct_f.values.astype(float)
row_sums = obs.sum(axis=1, keepdims=True)
col_sums = obs.sum(axis=0, keepdims=True)
grand = obs.sum()
exp = row_sums @ (col_sums/grand)
chi2 = float(((obs-exp)**2/exp).sum())

dof = int((obs.shape[0]-1)*(obs.shape[1]-1))

out = {
    'n_patients_with_known_histology_female_brca': int(df_clin.shape[0]),
    'n_histology_categories_after_filter_rowtotal_gt10': int(ct_f.shape[0]),
    'grand_total_after_filter': int(grand),
    'chi_square': chi2,
    'dof': dof,
    'contingency_table': ct_f.reset_index().rename(columns={'histology':'histology',0:'cdh1_wt_or_no_pass',1:'cdh1_mut_pass'}).to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1aDYuH3ddhp84Btt09o4thBD': ['clinical_info'], 'var_call_7S2PFEcX1ptjMnMDIcPaWyTx': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_Pu4WTsA744p0XSl5k1mPjR2A': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_IHYiIdju7eQ6QsAn8NncgYjv': [{'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_a0t1PPBwHmfkBi74NiDJVH5N': {'example_patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'parsed_dataset': 'Ovarian serous cystadenocarcinoma', 'parsed_barcode': 'TCGA-31-1953', 'example_acronym_guess': 'OV'}, 'var_call_mOGDy4S0VCJInN29CRzKoUV1': [], 'var_call_EPf3n07FvgDS2m7JXMXZeYmg': 'file_storage/call_EPf3n07FvgDS2m7JXMXZeYmg.json', 'var_call_cB25AfS4pgww9Dr0VtqFSHcg': 'file_storage/call_cB25AfS4pgww9Dr0VtqFSHcg.json'}

exec(code, env_args)
