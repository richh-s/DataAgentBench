code = """import json, re, pandas as pd

def load_tool_result(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

clin = load_tool_result(var_call_umk4yhIDzaSdb0LCnQsp9xg9)
mut = load_tool_result(var_call_Hj7MzlkhXe8xP7v00wXM4TgC)

df_clin = pd.DataFrame(clin)
# Extract TCGA barcode from Patient_description text
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
df_clin['ParticipantBarcode'] = df_clin['participantbarcode'].apply(lambda s: (pat.search(s).group(1) if isinstance(s,str) and pat.search(s) else None))
# Alive: check for 'vital status is Alive' in description (more reliable than person_neoplasm_cancer_status)
df_clin['is_alive'] = df_clin['participantbarcode'].str.contains('vital status is Alive', case=False, na=False)
# BRCA cohort: description contains 'Breast invasive carcinoma'
df_clin['is_brca'] = df_clin['participantbarcode'].str.contains('Breast invasive carcinoma', case=False, na=False)

df_brca_alive = df_clin[df_clin['is_brca'] & df_clin['is_alive']].copy()

# Mutation carriers (unique patients)
df_mut = pd.DataFrame(mut)
cdh1_patients = set(df_mut['ParticipantBarcode'].dropna().unique().tolist())

df_brca_alive['has_CDH1_mut'] = df_brca_alive['ParticipantBarcode'].isin(cdh1_patients)

# group by histological type
grp = df_brca_alive.groupby('histological_type', dropna=False).agg(
    n_patients=('ParticipantBarcode','nunique'),
    n_cdh1=('has_CDH1_mut','sum')
).reset_index()
# avoid tiny groups? keep >=5 patients
grp['pct_cdh1'] = (grp['n_cdh1'] / grp['n_patients'] * 100).round(2)

# filter groups with at least 5 patients to make percentage meaningful
grp_f = grp[grp['n_patients']>=5].copy()
# sort desc pct then n_patients
grp_f = grp_f.sort_values(['pct_cdh1','n_patients'], ascending=[False, False])

top3 = grp_f.head(3)
res = top3.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_9Z6ugyGADGI8HRzSaHS1VZXL': ['clinical_info'], 'var_call_32nsvpi9Ne6UEWKhnnLosInT': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_3Y8UQflzY51Wx7ckY6SqZ5fZ': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_umk4yhIDzaSdb0LCnQsp9xg9': 'file_storage/call_umk4yhIDzaSdb0LCnQsp9xg9.json', 'var_call_Hj7MzlkhXe8xP7v00wXM4TgC': 'file_storage/call_Hj7MzlkhXe8xP7v00wXM4TgC.json'}

exec(code, env_args)
