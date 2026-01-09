code = """import json, pandas as pd

# Alive BRCA (ICD-10 C50*) from clinical
alive_brca = pd.DataFrame(var_call_jBsr048mHjUtnirVzh0TAmj6)

def extract_tcga_barcode(desc):
    if pd.isna(desc):
        return None
    s = str(desc)
    import re
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', s)
    return m.group(1) if m else None

alive_brca['ParticipantBarcode'] = alive_brca['participantbarcode'].apply(extract_tcga_barcode)

# CDH1 mutation carriers list from molecular (participant-level)
# Load full mutation counts file if path provided
mut_path_or_list = var_call_TqNu7bdkX69nVyhbXaonuSxw
if isinstance(mut_path_or_list, str):
    with open(mut_path_or_list, 'r') as f:
        mut_list = json.load(f)
else:
    mut_list = mut_path_or_list
mut_df = pd.DataFrame(mut_list)
mut_df['mut_count'] = pd.to_numeric(mut_df['mut_count'])
mut_df['has_cdh1_mut'] = mut_df['mut_count'] > 0

# Join
df = alive_brca.merge(mut_df[['ParticipantBarcode','has_cdh1_mut']], on='ParticipantBarcode', how='left')
df['has_cdh1_mut'] = df['has_cdh1_mut'].fillna(False)

# compute per histological_type
agg = df.groupby('histological_type', dropna=False).agg(n_alive=('ParticipantBarcode','nunique'), n_mut=('has_cdh1_mut','sum')).reset_index()
agg['pct_mut'] = (agg['n_mut'] / agg['n_alive'] * 100).round(2)
agg = agg.sort_values(['pct_mut','n_alive'], ascending=[False,False]).head(3)

result = agg.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_6cQy7Ji11KKrxI7lsxJyoKPe': ['clinical_info'], 'var_call_uidvOCtRUEFdCatLf4HdxsMl': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_ccOKD4I8IHMBJS1Q9kHDxa8X': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_TqNu7bdkX69nVyhbXaonuSxw': 'file_storage/call_TqNu7bdkX69nVyhbXaonuSxw.json', 'var_call_udTOdn3qwFbSK8vADhdOUrZY': [], 'var_call_bo5D5NuAgAdVFwgKYDMiCuqV': [{'icd_10': 'C54.9'}, {'icd_10': 'C25.9'}, {'icd_10': 'C69.80'}, {'icd_10': 'C13.9'}, {'icd_10': 'C77.4'}, {'icd_10': 'C34.8'}, {'icd_10': 'C77.2'}, {'icd_10': 'C49.20'}, {'icd_10': 'C83.3'}, {'icd_10': 'C67.6'}, {'icd_10': 'C55'}, {'icd_10': 'C03.9'}, {'icd_10': 'C34.0'}, {'icd_10': 'C24.0'}, {'icd_10': 'C16.2'}, {'icd_10': 'C77.0'}, {'icd_10': 'C62.9'}, {'icd_10': 'C40.3'}, {'icd_10': 'C50.8'}, {'icd_10': 'C01'}], 'var_call_XiSCLHl0DVpzzEVDIfxuzVgL': [{'n_brca_alive': '0'}], 'var_call_PGpixpvT4E0fI1NXmNcbG0z3': [{'person_neoplasm_cancer_status': '[Unknown]'}, {'person_neoplasm_cancer_status': '[Discrepancy]'}, {'person_neoplasm_cancer_status': 'TUMOR FREE'}, {'person_neoplasm_cancer_status': 'WITH TUMOR'}], 'var_call_1bETgTu1tf1S4lGJI0LUU8PR': [{'n_dead': '10761', 'n_no_death_date': '12'}], 'var_call_uqizMQHuFk4yz4SmNeYAwKMM': [{'n_alive': '12'}], 'var_call_jBsr048mHjUtnirVzh0TAmj6': [{'participantbarcode': 'Case 57a1604c-60b7-4b30-a75e-f70939532c5c, linked to barcode TCGA-BH-A0B2, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.', 'icd_10': 'C50.9', 'histological_type': 'Infiltrating Ductal Carcinoma', 'days_to_death': 'None'}]}

exec(code, env_args)
