code = """import json, pandas as pd, math, os

# Load full LGG clinical data
path = var_call_ZaDNJ1g2ZQK3TRUm3wH6rRy7
with open(path, 'r') as f:
    clinical_lgg = json.load(f)

# Convert to DataFrame and extract patient barcodes from Patient_description
c_df = pd.DataFrame(clinical_lgg)
# Patient_description format: "In the Brain lower grade glioma dataset, patient TCGA-XX-XXXX ..."
patient_ids = c_df['Patient_description'].str.extract(r'patient (TCGA-[A-Z0-9-]+)')[0]
c_df['ParticipantBarcode'] = patient_ids

# Load IGF2 expression data
path_expr = var_call_cU4kIzGjLiVsG9FpkqYOWWzI
with open(path_expr, 'r') as f:
    expr_data = json.load(f)

e_df = pd.DataFrame(expr_data)
# ensure correct types
e_df['normalized_count'] = pd.to_numeric(e_df['normalized_count'], errors='coerce')

# Merge LGG clinical with expression on ParticipantBarcode
merged = pd.merge(c_df[['ParticipantBarcode', 'histological_type']], e_df, on='ParticipantBarcode', how='inner')

# Filter: valid IGF2 values and histology annotations not enclosed in square brackets
valid = merged[merged['normalized_count'].notna()].copy()
valid = valid[~valid['histological_type'].str.match(r'^\[.*\]$')]

# Compute log10(normalized_count + 1)
valid['log10_expr'] = (valid['normalized_count'] + 1).apply(lambda x: math.log10(x))

# Group by histological_type and compute mean with at least 4 decimal places
result_series = valid.groupby('histological_type')['log10_expr'].mean()

# Prepare result dict
result = {hist: round(val, 4) for hist, val in result_series.items()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cU4kIzGjLiVsG9FpkqYOWWzI': 'file_storage/call_cU4kIzGjLiVsG9FpkqYOWWzI.json', 'var_call_m48bVjcl1z4Ntaj4wB6MuaH8': ['clinical_info'], 'var_call_alqXs0HNvFOwqLL9tVqxRS90': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_ZaDNJ1g2ZQK3TRUm3wH6rRy7': 'file_storage/call_ZaDNJ1g2ZQK3TRUm3wH6rRy7.json'}

exec(code, env_args)
