code = """import json, re, math, pandas as pd

# Load expression records
expr_src = var_call_PiXRPqkwTTt3H3m5PPkNOikU
if isinstance(expr_src, str):
    with open(expr_src, 'r') as f:
        expr_records = json.load(f)
else:
    expr_records = expr_src

clin_src = var_call_D9ij0HAwQ1InybKruaMWPN3k
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin_records = json.load(f)
else:
    clin_records = clin_src

expr_df = pd.DataFrame(expr_records)
clin_df = pd.DataFrame(clin_records)

# Clean / parse participant barcode from clinical Patient_description-like field
# clinical query returned key lowercased 'participantbarcode'
clin_df = clin_df.rename(columns={c: c.lower() for c in clin_df.columns})

pattern = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
clin_df['ParticipantBarcode'] = clin_df['participantbarcode'].astype(str).str.extract(pattern, expand=False)

# Filter histology not enclosed in square brackets
clin_df['histology'] = clin_df['histology'].astype(str)
mask_brackets = clin_df['histology'].str.match(r'^\s*\[.*\]\s*$', na=False)
clin_df = clin_df[~mask_brackets]

# Expression df types
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['ParticipantBarcode','normalized_count'])
expr_df = expr_df[expr_df['normalized_count'] >= 0]

# log10 transform
expr_df['log10_expr'] = (expr_df['normalized_count'] + 1.0).apply(lambda x: math.log10(x))

# If multiple samples per participant exist, average within participant first
expr_pt = expr_df.groupby('ParticipantBarcode', as_index=False)['log10_expr'].mean()

# Join to clinical (some participants may have multiple entries; take first histology per participant)
clin_pt = clin_df.dropna(subset=['ParticipantBarcode'])[['ParticipantBarcode','histology']].drop_duplicates('ParticipantBarcode')
merged = expr_pt.merge(clin_pt, on='ParticipantBarcode', how='inner')

# Group by histology
out = merged.groupby('histology').agg(n_patients=('ParticipantBarcode','nunique'), avg_log10_igf2=('log10_expr','mean')).reset_index()
out = out.sort_values('histology')

# format to 4 decimals
out['avg_log10_igf2'] = out['avg_log10_igf2'].map(lambda v: float(f"{v:.4f}"))

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_PiXRPqkwTTt3H3m5PPkNOikU': 'file_storage/call_PiXRPqkwTTt3H3m5PPkNOikU.json', 'var_call_wxgP0kEbr27mLnQm9PhiQdZu': ['clinical_info'], 'var_call_rTOprgY43YyF1Humw7hP6nNj': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_i0C1OM5c8CRgGt6FeaihNLMn': [], 'var_call_N70u0AjBFQoqmhytG3aGJu7e': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}, {'diagnosis': 'None'}], 'var_call_85QXU3izdbvP8fgeSNDt5Aru': [{'site': 'C50.9', 'n': '1079'}, {'site': 'C64.9', 'n': '871'}, {'site': 'C71.9', 'n': '646'}, {'site': 'C56.9', 'n': '579'}, {'site': 'C34.1', 'n': '553'}, {'site': 'C54.1', 'n': '551'}, {'site': 'C73.9', 'n': '505'}, {'site': 'C61.9', 'n': '495'}, {'site': 'C71.0', 'n': '437'}, {'site': 'C22.0', 'n': '376'}, {'site': 'C34.3', 'n': '351'}, {'site': 'C53.9', 'n': '300'}, {'site': 'C67.9', 'n': '237'}, {'site': 'C16.3', 'n': '156'}, {'site': 'C74.9', 'n': '145'}, {'site': 'C25.0', 'n': '140'}, {'site': 'C62.9', 'n': '134'}, {'site': 'C02.9', 'n': '129'}, {'site': 'C15.5', 'n': '122'}, {'site': 'C32.9', 'n': '118'}], 'var_call_iiPJa4yFXvrfaWfdWMqDfvIl': 'file_storage/call_iiPJa4yFXvrfaWfdWMqDfvIl.json', 'var_call_D9ij0HAwQ1InybKruaMWPN3k': 'file_storage/call_D9ij0HAwQ1InybKruaMWPN3k.json'}

exec(code, env_args)
