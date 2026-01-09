code = """import json, re, pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r') as f:
            return json.load(f)
    return x

clin = load_records(var_call_k7mIJEgioOETlXWHb20Z3bHl)
mut = load_records(var_call_ZNC8T1CutPoqxgHHSPLZW5bI)

cdf = pd.DataFrame(clin)
# extract TCGA barcode
cdf['participant_barcode'] = cdf['patient_description'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')[0]
# extract sex using robust pattern
pattern = r'(?<![A-Z])(?:FEMALE|MALE)(?![A-Z])'
cdf['sex'] = cdf['patient_description'].str.extract(f'({pattern})')[0]

cdf = cdf[cdf['sex']=='FEMALE']
cdf = cdf[cdf['histological_type'].notna() & (cdf['histological_type'].astype(str).str.strip()!='')]

mdf = pd.DataFrame(mut)
mdf = mdf.dropna(subset=['participant_barcode'])
mdf = mdf.drop_duplicates(subset=['participant_barcode'])
mdf['cdh1_mut'] = 1

merged = cdf.merge(mdf[['participant_barcode','cdh1_mut']], on='participant_barcode', how='left')
merged['cdh1_mut'] = merged['cdh1_mut'].fillna(0).astype(int)

ct = pd.crosstab(merged['histological_type'], merged['cdh1_mut'])
for col in [0,1]:
    if col not in ct.columns:
        ct[col]=0
ct = ct[[0,1]]

ct_filt = ct[ct.sum(axis=1) > 10]
col_tot = ct_filt.sum(axis=0)
ct_filt = ct_filt[[c for c in ct_filt.columns if col_tot[c] > 10]]

import numpy as np
O = ct_filt.to_numpy(dtype=float)
row_tot = O.sum(axis=1, keepdims=True)
col_tot = O.sum(axis=0, keepdims=True)
grand = O.sum()
E = row_tot @ (col_tot / grand) if grand>0 else None
chi2 = float(((O-E)**2 / E).sum()) if grand>0 and E is not None else None

dof = int((ct_filt.shape[0]-1)*(ct_filt.shape[1]-1)) if ct_filt.size>0 else 0

out = {
 'n_female_brca_with_known_histology': int(len(merged)),
 'histology_levels_used': list(ct_filt.index),
 'contingency_table': {idx: {'CDH1_MUT0': int(ct_filt.loc[idx,0]) if 0 in ct_filt.columns else None,
                             'CDH1_MUT1': int(ct_filt.loc[idx,1]) if 1 in ct_filt.columns else None} for idx in ct_filt.index},
 'chi_square_statistic': chi2,
 'degrees_of_freedom': dof,
 'grand_total': float(grand)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ZNC8T1CutPoqxgHHSPLZW5bI': 'file_storage/call_ZNC8T1CutPoqxgHHSPLZW5bI.json', 'var_call_sNh0RPdwNesKXOXyWAJQYGdE': ['clinical_info'], 'var_call_b8ugrNdEkNUBrxMrUrCI88Yp': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_Ko89CpcuQLOSkocD0S0cezMr': [], 'var_call_KRnUAYdRL8dHpJypSjpi7UDn': [], 'var_call_sqlLDkukRis6UIhRLrN8OpNO': [], 'var_call_dcYXP4m5YO3EuzfpyHKvnIF0': [], 'var_call_NAuU6kx6qawLKQzCpcIR0HSM': {'likely_columns': [], 'ncols': 99}, 'var_call_seCkucV6RFf1AysZUBr3H8sG': [{'participant_barcode': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'participant_barcode': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'participant_barcode': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'participant_barcode': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'participant_barcode': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_call_k7mIJEgioOETlXWHb20Z3bHl': 'file_storage/call_k7mIJEgioOETlXWHb20Z3bHl.json', 'var_call_BP9urZXjXDRrmyJYFi2Clnoc': {'n_female_brca_with_known_histology': 0, 'n_histology_categories_before_filter': 0, 'n_histology_categories_after_filter': 0, 'column_totals_after_filter': {}, 'contingency_table_after_filter': {}, 'chi_square_statistic': None, 'degrees_of_freedom': 1}, 'var_call_Yw3AzGPjNi9763066JfiaMUf': {'sample_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'barcode_match': 'TCGA-AC-A5EH', 'sex_match': None, 'n_rows': 1077, 'n_female_token': 1065, 'n_male_token': 1077}, 'var_call_uvWEBIcOMseJji4gp2qhoWZy': {'sex_boundary': None, 'sex_simple_regex': 'FEMALE', 'cnt_boundary_female': 0, 'cnt_simple_female': 1065, 'cnt_boundary_male': 0, 'cnt_simple_male': 1077}, 'var_call_o5WVHs6Wh4DJIBhfjRftzhcE': {'window': 'H, a FEMALE sub', 'codepoints': [72, 44, 32, 97, 32, 70, 69, 77, 65, 76, 69, 32, 115, 117, 98]}, 'var_call_4okAuiWAuKQYVDSAxSECLuQo': {'sex_match': 'FEMALE', 'female_count': 1077}}

exec(code, env_args)
