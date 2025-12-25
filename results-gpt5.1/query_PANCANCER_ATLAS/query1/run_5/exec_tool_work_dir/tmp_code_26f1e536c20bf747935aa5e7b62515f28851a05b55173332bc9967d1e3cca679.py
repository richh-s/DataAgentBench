code = """import json, math, pandas as pd

# Load full LGG clinical result
path = var_call_deXabAjtbmgBFFwKQYBYGfZu
with open(path, 'r') as f:
    lgg_clin = json.load(f)

clin_df = pd.DataFrame(lgg_clin)

# Extract TCGA barcode from Patient_description (pattern 'TCGA-....')
clin_df['ParticipantBarcode'] = clin_df['Patient_description'].str.extract(r'(TCGA-..-....)')

# Drop rows without barcode or histology, and histology enclosed in square brackets
mask_valid_hist = clin_df['histological_type'].notna() & ~clin_df['histological_type'].str.match(r'^\[.*\]$')
clin_df = clin_df[mask_valid_hist & clin_df['ParticipantBarcode'].notna()]

# Load IGF2 expression data
path_expr = var_call_4WunRTkaawr8Q3EeYkqhBJBY
with open(path_expr, 'r') as f:
    igf2_expr = json.load(f)
expr_df = pd.DataFrame(igf2_expr)

# Coerce normalized_count to numeric and drop invalid
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])

# Merge on ParticipantBarcode
merged = pd.merge(clin_df[['ParticipantBarcode','histological_type']], expr_df, on='ParticipantBarcode', how='inner')

# Compute log10(normalized_count + 1)
merged['log10_expr'] = (merged['normalized_count'] + 1).map(lambda x: math.log10(x))

# Group by histology and compute mean
result = merged.groupby('histological_type')['log10_expr'].mean().round(4).sort_index()

out = result.reset_index().to_dict(orient='records')

j = json.dumps(out)
print("__RESULT__:")
print(j)"""

env_args = {'var_call_4WunRTkaawr8Q3EeYkqhBJBY': 'file_storage/call_4WunRTkaawr8Q3EeYkqhBJBY.json', 'var_call_1TElkGUWRk57WXAH4V4BrT5G': ['clinical_info'], 'var_call_mE6jfx4QvazKT12wPDatZ1fT': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_PBCHyQ4mPbUkZkP6XgZg2P2J': [], 'var_call_jk5ShDst2koW7iKWaDZrRoEy': [], 'var_call_Bbf2EwiOswC1Mz2ayfEN6zZq': [{'histological_type': 'Thyroid Papillary Carcinoma - Classical/usual'}, {'histological_type': 'Pancreas-Colloid (mucinous non-cystic) Carcinoma'}, {'histological_type': 'None'}, {'histological_type': 'Stomach  Adenocarcinoma  Diffuse Type'}, {'histological_type': 'Prostate Adenocarcinoma  Other Subtype'}, {'histological_type': 'Fibrolamellar Carcinoma'}, {'histological_type': 'Infiltrating Ductal Carcinoma'}, {'histological_type': 'Untreated primary (de novo) GBM'}, {'histological_type': 'Synovial Sarcoma - Biphasic'}, {'histological_type': 'Mucinous Adenocarcinoma of Endocervical Type'}, {'histological_type': 'Pancreas-Adenocarcinoma-Other Subtype'}, {'histological_type': 'Thymoma; Type B1|Thymoma; Type B2'}, {'histological_type': 'Seminoma; NOS|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor'}, {'histological_type': 'Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)'}, {'histological_type': 'Non-Seminoma; Choriocarcinoma|Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Mature)|Non-Seminoma; Teratoma (Immature)'}, {'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Non-Seminoma; Embryonal Carcinoma|Non-Seminoma; Yolk Sac Tumor|Non-Seminoma; Teratoma (Immature)'}, {'histological_type': 'Lung Clear Cell Adenocarcinoma'}, {'histological_type': 'Seminoma; NOS|Non-Seminoma; Embryonal Carcinoma'}, {'histological_type': 'Pheochromocytoma'}], 'var_call_deXabAjtbmgBFFwKQYBYGfZu': 'file_storage/call_deXabAjtbmgBFFwKQYBYGfZu.json'}

exec(code, env_args)
