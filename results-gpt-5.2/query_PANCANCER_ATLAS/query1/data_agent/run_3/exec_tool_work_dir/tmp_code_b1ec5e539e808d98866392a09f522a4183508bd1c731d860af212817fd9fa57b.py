code = """import json, re, math, pandas as pd

clin_src = var_call_jWTWt0bC0uwSvj3yYRtF8CJB
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

expr_src = var_call_8unUpTa4OoObPlS1eVMLt2Y1
if isinstance(expr_src, str):
    with open(expr_src, 'r') as f:
        expr = json.load(f)
else:
    expr = expr_src

clin_df = pd.DataFrame(clin)
expr_df = pd.DataFrame(expr)

pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
clin_df['ParticipantBarcode_extracted'] = clin_df['participantbarcode'].astype(str).str.extract(pat, expand=False)
clin_df = clin_df.dropna(subset=['ParticipantBarcode_extracted','histology']).copy()
clin_df['ParticipantBarcode_extracted'] = clin_df['ParticipantBarcode_extracted'].str.strip()
clin_df = clin_df[~clin_df['histology'].astype(str).str.match(r'^\[.*\]$')]

expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['ParticipantBarcode','normalized_count']).copy()
expr_df['log10_expr'] = (expr_df['normalized_count'] + 1.0).map(lambda x: math.log10(x) if x > -1 else float('nan'))
expr_df = expr_df.dropna(subset=['log10_expr'])

pat_mean = expr_df.groupby('ParticipantBarcode', as_index=False)['log10_expr'].mean()
merged = clin_df.merge(pat_mean, left_on='ParticipantBarcode_extracted', right_on='ParticipantBarcode', how='inner')
res = merged.groupby('histology', as_index=False).agg(
    avg_log10_igf2=('log10_expr','mean'),
    n_patients=('ParticipantBarcode','nunique')
).sort_values('histology')

out_lines = [f"{row['histology']}: {row['avg_log10_igf2']:.4f} (n={int(row['n_patients'])})" for _, row in res.iterrows()]
answer = "\\n".join(out_lines)

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_eIq2SNf5etbnJ6BAoi6m6gqX': ['clinical_info'], 'var_call_dBUmFKlxUBAMKZtRifZY1f8j': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_8unUpTa4OoObPlS1eVMLt2Y1': 'file_storage/call_8unUpTa4OoObPlS1eVMLt2Y1.json', 'var_call_ZCf3lfpHViNywtOtu1RxF3JW': [{'column_name': 'Patient_description'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'city_of_procurement'}, {'column_name': 'clinical_M'}, {'column_name': 'clinical_N'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_stage'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'diagnosis'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'ethnicity'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'form_completion_date'}, {'column_name': 'height'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'histological_type'}, {'column_name': 'histological_type_other'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_10'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'laterality'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'margin_status'}, {'column_name': 'menopause_status'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'pathologic_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_stage'}, {'column_name': 'patient_death_reason'}, {'column_name': 'patient_id'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'prior_dx'}, {'column_name': 'prior_glioma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'race'}, {'column_name': 'radiation_therapy'}, {'column_name': 'residual_tumor'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'surgical_approach'}, {'column_name': 'system_version'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'tissue_source_site'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'venous_invasion'}, {'column_name': 'weight'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}], 'var_call_bHgLENTY6bDmR5TzLMTLIJsn': [], 'var_call_iwaVAB2wLUDWVXuz3XCl8WQV': [{'diagnosis': 'None', 'n': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'n': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'n': '490'}], 'var_call_RgTaRGySd7z1GYsTJipwyMY3': [{'n_null': '10761', 'n_sql_null': '9757'}], 'var_call_0h4r7hDHIn1JxhjXgHrmkuyR': [], 'var_call_FmzS1NYV78w3OaoP0MzV0eC5': [{'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'person_neoplasm_cancer_status'}], 'var_call_fn8FVTEFvXt5w7lDTIZbi4PO': [], 'var_call_kciWxevGgq7iiNPU3rqbhPSW': [{'n_hist_notnull': '10198'}], 'var_call_3Hx9Qs3W9WNIfKjsthZPeqyv': [{'histological_type': 'Infiltrating Ductal Carcinoma', 'n': '777'}, {'histological_type': 'Serous Cystadenocarcinoma', 'n': '584'}, {'histological_type': 'Untreated primary (de novo) GBM', 'n': '539'}, {'histological_type': 'Kidney Clear Cell Renal Carcinoma', 'n': '518'}, {'histological_type': 'Head and Neck Squamous Cell Carcinoma', 'n': '512'}, {'histological_type': 'Prostate Adenocarcinoma Acinar Type', 'n': '480'}, {'histological_type': 'Lung Squamous Cell Carcinoma- Not Otherwise Specified (NOS)', 'n': '470'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'n': '409'}, {'histological_type': 'Endometrioid endometrial adenocarcinoma', 'n': '401'}, {'histological_type': 'Colon Adenocarcinoma', 'n': '378'}, {'histological_type': 'Hepatocellular Carcinoma', 'n': '364'}, {'histological_type': 'Thyroid Papillary Carcinoma - Classical/usual', 'n': '356'}, {'histological_type': 'Lung Adenocarcinoma- Not Otherwise Specified (NOS)', 'n': '320'}, {'histological_type': 'Kidney Papillary Renal Cell Carcinoma', 'n': '286'}, {'histological_type': 'Cervical Squamous Cell Carcinoma', 'n': '254'}, {'histological_type': 'Infiltrating Lobular Carcinoma', 'n': '201'}, {'histological_type': 'Astrocytoma', 'n': '194'}, {'histological_type': 'Oligodendroglioma', 'n': '189'}, {'histological_type': 'Stomach  Adenocarcinoma  Not Otherwise Specified (NOS)', 'n': '162'}, {'histological_type': 'Pancreas-Adenocarcinoma Ductal Type', 'n': '153'}], 'var_call_MmqLdye1fSHTvW6M3uZB84FP': [{'n': '513'}], 'var_call_jWTWt0bC0uwSvj3yYRtF8CJB': 'file_storage/call_jWTWt0bC0uwSvj3yYRtF8CJB.json'}

exec(code, env_args)
