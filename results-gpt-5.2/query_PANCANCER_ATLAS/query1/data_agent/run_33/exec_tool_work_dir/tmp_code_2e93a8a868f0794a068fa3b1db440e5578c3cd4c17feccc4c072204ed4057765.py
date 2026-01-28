code = """import json, re, pandas as pd, numpy as np

expr_src = var_call_kHsRWtqwcFGVz7qLmeG92Y5i
if isinstance(expr_src, str):
    with open(expr_src, 'r') as f:
        expr = json.load(f)
else:
    expr = expr_src
expr_df = pd.DataFrame(expr)
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])

clin_src = var_call_t39fxkWFwxZnsd57elWXkDtk
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src
clin_df = pd.DataFrame(clin)

pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
clin_df['ParticipantBarcode'] = clin_df['participantbarcode'].astype(str).str.extract(pat, expand=False)
clin_df = clin_df.dropna(subset=['ParticipantBarcode'])

mask_lgg = (~clin_df['participantbarcode'].str.contains('Glioblastoma', case=False, na=False) &
            ~clin_df['histology'].astype(str).str.contains('GBM|Glioblastoma', case=False, na=False))
lgg_clin = clin_df.loc[mask_lgg, ['ParticipantBarcode','histology']].copy()

lgg_clin['histology'] = lgg_clin['histology'].astype(str)
valid_hist = ~lgg_clin['histology'].str.match(r'^\s*\[.*\]\s*$')
lgg_clin = lgg_clin.loc[valid_hist]

m = pd.merge(lgg_clin, expr_df[['ParticipantBarcode','normalized_count']], on='ParticipantBarcode', how='inner')
m['log10_expr'] = np.log10(m['normalized_count'] + 1.0)

res = (m.groupby('histology', dropna=False)['log10_expr']
         .mean()
         .reset_index()
         .sort_values('histology'))

out_lines = []
for _, row in res.iterrows():
    out_lines.append(f"{row['histology']}\t{row['log10_expr']:.4f}")

answer = "Histology\tAvg_log10(IGF2_norm_count+1)\n" + "\n".join(out_lines)

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_SvcYZeNPfhvP7VhLSWAtqpA6': ['clinical_info'], 'var_call_zTa8unawXxyyDEEXXsbTQ90E': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_se3JRAiJcMLhzgOpWRRl3HHK': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_UKJwvv7LRWeIKTjI1bjtKR21': [], 'var_call_Cr1XLiqu731voNHsQS0FbMNu': [{'diagnosis': 'None', 'n': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'n': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'n': '490'}], 'var_call_yCg8FFBUipAUja5zE2TaOuit': [{'n': '1111'}], 'var_call_1QQtMXCfKjGXpRBgensYIYC8': [{'icd_10': 'C50.9', 'n': '1078'}, {'icd_10': 'C71.9', 'n': '646'}, {'icd_10': 'C64.9', 'n': '585'}, {'icd_10': 'C56.9', 'n': '579'}, {'icd_10': 'C34.1', 'n': '560'}, {'icd_10': 'C54.1', 'n': '551'}, {'icd_10': 'C73', 'n': '503'}, {'icd_10': 'C61', 'n': '494'}, {'icd_10': 'C71.0', 'n': '438'}, {'icd_10': 'C22.0', 'n': '376'}, {'icd_10': 'C34.3', 'n': '342'}, {'icd_10': 'C53.9', 'n': '300'}, {'icd_10': 'C64.1', 'n': '286'}, {'icd_10': 'C67.9', 'n': '237'}, {'icd_10': 'C16.3', 'n': '156'}], 'var_call_vRrvkmng6NLkOYWTjBG0Q4lc': [{'n': '496'}], 'var_call_kHsRWtqwcFGVz7qLmeG92Y5i': 'file_storage/call_kHsRWtqwcFGVz7qLmeG92Y5i.json', 'var_call_t39fxkWFwxZnsd57elWXkDtk': 'file_storage/call_t39fxkWFwxZnsd57elWXkDtk.json'}

exec(code, env_args)
