code = """import json, pandas as pd, math, re

# Load full IGF2 expression data
with open(var_call_d0YG1kGdQ7OxXQMEe1uQJJNy, 'r') as f:
    igf2_records = json.load(f)

# Convert to DataFrame and coerce normalized_count to float
igf2_df = pd.DataFrame(igf2_records)
igf2_df['normalized_count'] = pd.to_numeric(igf2_df['normalized_count'], errors='coerce')
igf2_df = igf2_df.dropna(subset=['normalized_count'])

# Extract patient barcode from Patient_description in clinical data and keep LGG only.
with open(var_call_9NEptX7B3aMB3N1TmhcIOIdh, 'r') as f:
    clin_records = json.load(f)

clin_df = pd.DataFrame(clin_records)

# Filter for LGG based on text containing 'lower grade glioma' or 'LGG'
clin_df = clin_df[clin_df['Patient_description'].str.contains('lower grade glioma', case=False, na=False)]

# Extract TCGA barcode (e.g., TCGA-XX-XXXX) from Patient_description
barcode_pattern = re.compile(r'TCGA-\w\w-\w\w\w\w')
clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(lambda s: barcode_pattern.search(s).group(0) if pd.notna(s) and barcode_pattern.search(s) else None)
clin_df = clin_df.dropna(subset=['ParticipantBarcode'])

# Rename histology column
clin_df = clin_df.rename(columns={'histological_type': 'histology'})

# Exclude histology annotations entirely enclosed in square brackets
clin_df['histology'] = clin_df['histology'].astype(str)
mask_valid_hist = ~clin_df['histology'].str.match(r"^\[[^\]]*\]$")
clin_df = clin_df[mask_valid_hist]

# Merge IGF2 with clinical on ParticipantBarcode
merged = pd.merge(igf2_df, clin_df[['ParticipantBarcode','histology']], on='ParticipantBarcode', how='inner')

# Compute log10(normalized_count + 1)
merged['log10_expr'] = (merged['normalized_count'] + 1).apply(lambda x: math.log10(x) if x > 0 else None)
merged = merged.dropna(subset=['log10_expr', 'histology'])

# Group by histology and compute mean
result_series = merged.groupby('histology')['log10_expr'].mean().sort_index()

# Format with at least 4 decimal places
result = {hist: float(f"{val:.4f}") for hist, val in result_series.items()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_d0YG1kGdQ7OxXQMEe1uQJJNy': 'file_storage/call_d0YG1kGdQ7OxXQMEe1uQJJNy.json', 'var_call_g8Kl6VF0ucmYSyBqtFXp0NcZ': ['clinical_info'], 'var_call_b6sPt67zCFEhFLo1lrGdrBY4': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_9NEptX7B3aMB3N1TmhcIOIdh': 'file_storage/call_9NEptX7B3aMB3N1TmhcIOIdh.json'}

exec(code, env_args)
