code = """import json, re, pandas as pd

# Load alive BRCA clinical rows (Breast invasive carcinoma dataset) from file
path = var_call_7A5hossamsT2PyTZ660aEl2p
with open(path, 'r') as f:
    clin = json.load(f)
clin_df = pd.DataFrame(clin)

# Extract TCGA barcode from Patient_description
clin_df['ParticipantBarcode'] = clin_df['Patient_description'].str.extract(r'patient\s+(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', expand=False)
# Keep only explicitly Alive in description to satisfy query
clin_df['is_alive'] = clin_df['Patient_description'].str.contains('vital status: Alive', regex=False)
clin_df = clin_df[clin_df['is_alive'] & clin_df['ParticipantBarcode'].notna()].copy()

# Load CDH1 mutation participants from file
mpath = var_call_FxwULpdY6CSNO4QnhHIO6JSN
with open(mpath, 'r') as f:
    muts = json.load(f)
mut_df = pd.DataFrame(muts)
# distinct participants with CDH1 mutation
mut_set = set(mut_df['ParticipantBarcode'].dropna().unique().tolist())

clin_df['has_CDH1_mut'] = clin_df['ParticipantBarcode'].isin(mut_set)

# Group by histological_type
agg = clin_df.groupby('histological_type', dropna=False).agg(
    alive_n=('ParticipantBarcode','nunique'),
    cdh1_mut_n=('has_CDH1_mut','sum')
).reset_index()
agg['pct_CDH1_mut'] = (agg['cdh1_mut_n'] / agg['alive_n'] * 100).round(2)

# Filter to histology types with at least 5 alive patients to avoid tiny denominators? Not specified, so keep all.
# Rank by percentage then by cdh1_mut_n then alive_n
agg_sorted = agg.sort_values(['pct_CDH1_mut','cdh1_mut_n','alive_n'], ascending=[False, False, False])

top3 = agg_sorted.head(3)
result = top3.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_FxwULpdY6CSNO4QnhHIO6JSN': 'file_storage/call_FxwULpdY6CSNO4QnhHIO6JSN.json', 'var_call_LNpPtVvzhcM5HN2zIWeP6W8o': ['clinical_info'], 'var_call_tvlh88nJxX8YkkSPqon6Yo2m': [{'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'histological_type_other'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'diagnosis'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'history_of_neoadjuvant_treatment'}], 'var_call_NHCRY8gkDNV9LWdPK0pjsN54': [{'column_name': 'days_to_death'}, {'column_name': 'status'}, {'column_name': 'wal_status'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'patient_death_reason'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}], 'var_call_r94yn63MCloZXt9nRpX6YIVw': [{'column_name': 'Patient_description'}], 'var_call_KIfqCxEbikgzl20lfdS14FYI': [], 'var_call_j0PFVvsdHlDKSkxj9nE8NVYF': [], 'var_call_RngatJJtiyjRGrWFB40Eja0G': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_7A5hossamsT2PyTZ660aEl2p': 'file_storage/call_7A5hossamsT2PyTZ660aEl2p.json'}

exec(code, env_args)
