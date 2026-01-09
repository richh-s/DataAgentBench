code = """import json, re, math, pandas as pd

# Load IGF2 expression (all cancers) from molecular result file
path_expr = var_call_SDGyfaAFgezeOtuRGQTgmPnS
with open(path_expr, 'r') as f:
    expr = json.load(f)
df_expr = pd.DataFrame(expr)
# normalized_count may come as string
df_expr['normalized_count'] = pd.to_numeric(df_expr['normalized_count'], errors='coerce')
df_expr = df_expr.dropna(subset=['normalized_count'])

# Load clinical brain (C71*) with histological_type
path_clin = var_call_lj6Ij95qd3bC4z6wGJByPzOb
with open(path_clin, 'r') as f:
    clin = json.load(f)
df_clin = pd.DataFrame(clin)
# column name came lowercased in result preview
# normalize expected names
if 'participantbarcode' in df_clin.columns and 'ParticipantBarcode' not in df_clin.columns:
    df_clin = df_clin.rename(columns={'participantbarcode':'ParticipantBarcode'})

# Extract TCGA barcode from Patient_description text
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
df_clin['TCGA_barcode'] = df_clin['ParticipantBarcode'].astype(str).str.extract(pat, expand=False)

df_clin = df_clin.dropna(subset=['TCGA_barcode','histological_type'])
# Keep LGG patients by excluding glioblastoma; approximate using histological_type not containing 'GBM' or 'Glioblastoma'
mask_lgg = ~df_clin['histological_type'].str.contains(r'GBM|Glioblastoma', case=False, na=False)
df_lgg = df_clin[mask_lgg].copy()

# Exclude histology enclosed in square brackets
mask_valid_hist = ~df_lgg['histological_type'].str.match(r'^\s*\[.*\]\s*$', na=False)
df_lgg = df_lgg[mask_valid_hist]

# Join with expression on barcode
merged = df_lgg.merge(df_expr, left_on='TCGA_barcode', right_on='ParticipantBarcode', how='inner', suffixes=('_clin','_expr'))
merged = merged.dropna(subset=['normalized_count'])
merged['log10_expr'] = (merged['normalized_count'] + 1.0).apply(lambda x: math.log10(x) if x> -1 else float('nan'))
merged = merged.dropna(subset=['log10_expr'])

res = (merged.groupby('histological_type')['log10_expr']
       .mean()
       .reset_index()
       .sort_values('histological_type'))
res['avg_log10_IGF2'] = res['log10_expr'].map(lambda v: f"{v:.4f}")
res_out = res[['histological_type','avg_log10_IGF2']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res_out))"""

env_args = {'var_call_SDGyfaAFgezeOtuRGQTgmPnS': 'file_storage/call_SDGyfaAFgezeOtuRGQTgmPnS.json', 'var_call_QreK0fUr4ErJfX9BRQyLpRWi': ['clinical_info'], 'var_call_weyJ8JH3ShKjj0HIULhEa1WF': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_3UaVgOZRoZxU5HrHeJ3ZlOJS': [], 'var_call_0pJmLICzzmVCdrAv6UreCGE0': [{'diagnosis': 'None', 'n': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'n': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'n': '490'}], 'var_call_QBdVEmkTINGdTecu0BWG27dq': [{'icd_o_3_site': 'C50.9', 'n': '1079'}, {'icd_o_3_site': 'C64.9', 'n': '871'}, {'icd_o_3_site': 'C71.9', 'n': '646'}, {'icd_o_3_site': 'C56.9', 'n': '579'}, {'icd_o_3_site': 'C34.1', 'n': '553'}, {'icd_o_3_site': 'C54.1', 'n': '551'}, {'icd_o_3_site': 'C73.9', 'n': '505'}, {'icd_o_3_site': 'C61.9', 'n': '495'}, {'icd_o_3_site': 'C71.0', 'n': '437'}, {'icd_o_3_site': 'C22.0', 'n': '376'}, {'icd_o_3_site': 'C34.3', 'n': '351'}, {'icd_o_3_site': 'C53.9', 'n': '300'}, {'icd_o_3_site': 'C67.9', 'n': '237'}, {'icd_o_3_site': 'C16.3', 'n': '156'}, {'icd_o_3_site': 'C74.9', 'n': '145'}, {'icd_o_3_site': 'C25.0', 'n': '140'}, {'icd_o_3_site': 'C62.9', 'n': '134'}, {'icd_o_3_site': 'C02.9', 'n': '129'}, {'icd_o_3_site': 'C15.5', 'n': '122'}, {'icd_o_3_site': 'C32.9', 'n': '118'}], 'var_call_lj6Ij95qd3bC4z6wGJByPzOb': 'file_storage/call_lj6Ij95qd3bC4z6wGJByPzOb.json'}

exec(code, env_args)
