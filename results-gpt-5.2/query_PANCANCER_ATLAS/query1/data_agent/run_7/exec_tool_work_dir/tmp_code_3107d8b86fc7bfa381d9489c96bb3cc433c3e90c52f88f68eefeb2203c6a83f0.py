code = """import json, re, math, pandas as pd

# Load expression (may be file path)
expr_src = var_call_1k2BB01YHfG7GpDhda7WPQDn
if isinstance(expr_src, str):
    with open(expr_src, 'r') as f:
        expr = json.load(f)
else:
    expr = expr_src

clin_src = var_call_B5bSNKeTezr66QfvgFHDM0vs
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

expr_df = pd.DataFrame(expr)
# coerce numeric
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])
expr_df = expr_df[expr_df['normalized_count'] >= 0]
expr_df['log10_expr'] = (expr_df['normalized_count'] + 1).apply(lambda x: math.log10(x))

clin_df = pd.DataFrame(clin)
# extract TCGA barcode from Patient_description text
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
clin_df['ParticipantBarcode_extracted'] = clin_df['participantbarcode'].apply(lambda s: (pat.search(s).group(1) if isinstance(s,str) and pat.search(s) else None))
clin_df = clin_df.dropna(subset=['ParticipantBarcode_extracted','histology'])
# exclude histology enclosed in square brackets
clin_df = clin_df[~clin_df['histology'].astype(str).str.match(r'^\[.*\]$')]

merged = expr_df.merge(clin_df, left_on='ParticipantBarcode', right_on='ParticipantBarcode_extracted', how='inner')

grp = merged.groupby('histology')['log10_expr'].mean().reset_index()
grp = grp.sort_values('histology')
# format to at least 4 decimals
out_lines = []
for _, row in grp.iterrows():
    out_lines.append(f"{row['histology']}: {row['log10_expr']:.4f}")
answer = "\n".join(out_lines) if out_lines else "No matching LGG patients with valid IGF2 expression and histology annotations found."

print('__RESULT__:')
print(json.dumps({'answer': answer}))"""

env_args = {'var_call_1k2BB01YHfG7GpDhda7WPQDn': 'file_storage/call_1k2BB01YHfG7GpDhda7WPQDn.json', 'var_call_JD56sj14WFqJwvDHu2BYNNAY': ['clinical_info'], 'var_call_EZNQS1RGk6GlnsgKFbH5lwgI': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_mAfnaGEw6fnRt2BbYpBVaSlO': [], 'var_call_DUCG6BxPDGwUQlJ41Ya5ls7U': [{'diagnosis': 'None', 'n': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'n': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'n': '490'}], 'var_call_eegbOLTBXYUkfwt7y3frtOyl': [{'icd_o_3_site': 'C50.9', 'icd_o_3_histology': '8500/3', 'n': '764'}, {'icd_o_3_site': 'C71.9', 'icd_o_3_histology': '9440/3', 'n': '581'}, {'icd_o_3_site': 'C56.9', 'icd_o_3_histology': '8441/3', 'n': '571'}, {'icd_o_3_site': 'C64.9', 'icd_o_3_histology': '8310/3', 'n': '505'}, {'icd_o_3_site': 'C54.1', 'icd_o_3_histology': '8380/3', 'n': '391'}, {'icd_o_3_site': 'C22.0', 'icd_o_3_histology': '8170/3', 'n': '357'}, {'icd_o_3_site': 'C73.9', 'icd_o_3_histology': '8260/3', 'n': '351'}, {'icd_o_3_site': 'C61.9', 'icd_o_3_histology': '8140/3', 'n': '289'}, {'icd_o_3_site': 'C64.9', 'icd_o_3_histology': '8260/3', 'n': '286'}, {'icd_o_3_site': 'C34.1', 'icd_o_3_histology': '8070/3', 'n': '232'}, {'icd_o_3_site': 'C50.9', 'icd_o_3_histology': '8520/3', 'n': '199'}, {'icd_o_3_site': 'C61.9', 'icd_o_3_histology': '8550/3', 'n': '192'}, {'icd_o_3_site': 'C34.1', 'icd_o_3_histology': '8140/3', 'n': '191'}, {'icd_o_3_site': 'C67.9', 'icd_o_3_histology': '8120/3', 'n': '187'}, {'icd_o_3_site': 'C53.9', 'icd_o_3_histology': '8070/3', 'n': '168'}, {'icd_o_3_site': 'C34.3', 'icd_o_3_histology': '8070/3', 'n': '158'}, {'icd_o_3_site': 'C54.1', 'icd_o_3_histology': '8441/3', 'n': '119'}, {'icd_o_3_site': 'C25.0', 'icd_o_3_histology': '8500/3', 'n': '117'}, {'icd_o_3_site': 'C71.0', 'icd_o_3_histology': '9382/3', 'n': '111'}, {'icd_o_3_site': 'C71.0', 'icd_o_3_histology': '9401/3', 'n': '107'}], 'var_call_B5bSNKeTezr66QfvgFHDM0vs': 'file_storage/call_B5bSNKeTezr66QfvgFHDM0vs.json'}

exec(code, env_args)
