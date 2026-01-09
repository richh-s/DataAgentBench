code = """import json, pandas as pd

path = var_call_zeukG0iFzyIkL2cSBXpDYEei
with open(path, 'r') as f:
    clin = json.load(f)
clin_df = pd.DataFrame(clin)
clin_df['participantbarcode'] = clin_df['patient_description'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)
clin_df = clin_df.dropna(subset=['participantbarcode','histological_type']).drop_duplicates(subset=['participantbarcode'])

mut_path = var_call_ZqmAMDNFc7TiHCr9VQKsgkTz
with open(mut_path, 'r') as f:
    muts = json.load(f)
mut_df = pd.DataFrame(muts).dropna(subset=['participantbarcode'])
mut_set = set(mut_df['participantbarcode'].unique())

clin_df['CDH1_mut'] = clin_df['participantbarcode'].isin(mut_set)

ct = pd.crosstab(clin_df['histological_type'], clin_df['CDH1_mut'])
for col in [False, True]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[[False, True]].copy()

# Rename by position, not by boolean labels
ct.columns = ['CDH1_mut_False','CDH1_mut_True']

ct['row_total'] = ct.sum(axis=1)
ct_filt = ct[ct['row_total'] > 10][['CDH1_mut_False','CDH1_mut_True']].copy()

O = ct_filt.to_numpy(dtype=float)
row_tot = O.sum(axis=1, keepdims=True)
col_tot = O.sum(axis=0, keepdims=True)
grand = float(O.sum())
E = row_tot @ (col_tot / grand)
chi2 = float(((O - E)**2 / E).sum())
dof = int((O.shape[0]-1) * (O.shape[1]-1))

result = {
    'chi_square': chi2,
    'degrees_of_freedom': dof,
    'grand_total_n': int(grand),
    'n_histological_types_included': int(O.shape[0]),
    'column_totals': {
        'CDH1_mut_False': int(col_tot[0,0]),
        'CDH1_mut_True': int(col_tot[0,1])
    },
    'contingency_table': ct_filt.reset_index().to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ZqmAMDNFc7TiHCr9VQKsgkTz': 'file_storage/call_ZqmAMDNFc7TiHCr9VQKsgkTz.json', 'var_call_MrvmAMvEyDGj5H1kcM4xE6Cj': 'file_storage/call_MrvmAMvEyDGj5H1kcM4xE6Cj.json', 'var_call_3p9AwO5QpvBef0NMcN98QUIK': ['clinical_info'], 'var_call_ZiyBucrsvxeUFqMk33VPQsYD': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_5lbGWu1HzvADopgCk5xwaX9W': [{'column_name': 'icd_o_3_histology'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}], 'var_call_51CCEUcr6CvOraUxkY93wLUL': [{'column_name': 'Patient_description'}, {'column_name': 'patient_death_reason'}, {'column_name': 'patient_id'}], 'var_call_SEDS64OPAl7rfWpk8OASWQra': [], 'var_call_FYOIdWnK8fHxZtxSql7fOhq7': [{'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_l7xToR5Zzm225jjHzGnpybgy': [{'histological_type': 'Infiltrating Ductal Carcinoma', 'n': '777'}, {'histological_type': 'Serous Cystadenocarcinoma', 'n': '584'}, {'histological_type': 'Untreated primary (de novo) GBM', 'n': '539'}, {'histological_type': 'Kidney Clear Cell Renal Carcinoma', 'n': '518'}, {'histological_type': 'Head and Neck Squamous Cell Carcinoma', 'n': '512'}, {'histological_type': 'Prostate Adenocarcinoma Acinar Type', 'n': '480'}, {'histological_type': 'Lung Squamous Cell Carcinoma- Not Otherwise Specified (NOS)', 'n': '470'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'n': '409'}, {'histological_type': 'Endometrioid endometrial adenocarcinoma', 'n': '401'}, {'histological_type': 'Colon Adenocarcinoma', 'n': '378'}, {'histological_type': 'Hepatocellular Carcinoma', 'n': '364'}, {'histological_type': 'Thyroid Papillary Carcinoma - Classical/usual', 'n': '356'}, {'histological_type': 'Lung Adenocarcinoma- Not Otherwise Specified (NOS)', 'n': '320'}, {'histological_type': 'Kidney Papillary Renal Cell Carcinoma', 'n': '286'}, {'histological_type': 'Cervical Squamous Cell Carcinoma', 'n': '254'}, {'histological_type': 'Infiltrating Lobular Carcinoma', 'n': '201'}, {'histological_type': 'Astrocytoma', 'n': '194'}, {'histological_type': 'Oligodendroglioma', 'n': '189'}, {'histological_type': 'Stomach  Adenocarcinoma  Not Otherwise Specified (NOS)', 'n': '162'}, {'histological_type': 'Pancreas-Adenocarcinoma Ductal Type', 'n': '153'}], 'var_call_8fx2yIxaukF0Hrd4wY3SdxJ0': [], 'var_call_Ymuy84astVEqOk7A6vXRCLJw': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_zeukG0iFzyIkL2cSBXpDYEei': 'file_storage/call_zeukG0iFzyIkL2cSBXpDYEei.json'}

exec(code, env_args)
