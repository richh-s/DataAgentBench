code = """import json, math, pandas as pd

# Load full RNA expression data
rna_path = var_call_3xlUlyNcIniWTMgJ0JWKTFWY
with open(rna_path, 'r') as f:
    rna_data = json.load(f)

# Load full clinical data for brain site C71.9 (LGG/GBM etc.)
clin_path = var_call_PHPXw4NDgv4tsA2FJfuDoZ8e
with open(clin_path, 'r') as f:
    clin_data = json.load(f)

rna_df = pd.DataFrame(rna_data)
clin_df = pd.DataFrame(clin_data)

# Extract patient barcode from Patient_description: token after 'TCGA-' pattern (first 3 segments)
import re

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r'TCGA-[0-9A-Z]{2}-[0-9A-Z]{4}', desc)
    return m.group(0) if m else None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Filter to LGG patients: diagnosis of Brain lower grade glioma or similar in text
# More robust: look for 'lower grade glioma' or 'LGG' in description
clin_lgg = clin_df[clin_df['Patient_description'].str.contains('lower grade glioma', case=False, na=False)]

# Merge with RNA by ParticipantBarcode
merged = pd.merge(rna_df, clin_lgg[['ParticipantBarcode', 'histological_type']], on='ParticipantBarcode', how='inner')

# Keep valid normalized_count and histological_type not enclosed in []
merged['normalized_count'] = pd.to_numeric(merged['normalized_count'], errors='coerce')
merged = merged.dropna(subset=['normalized_count', 'histological_type'])

# Exclude histology values that are fully enclosed in square brackets, like "[Not Available]"
mask_bracket = merged['histological_type'].str.match(r'^\s*\[.*\]\s*$')
merged = merged[~mask_bracket]

# Compute log10(normalized_count + 1)
merged['log10_expr'] = (merged['normalized_count'] + 1).apply(lambda x: math.log10(x) if x > 0 else None)

# Group by histological_type and compute mean
result_series = merged.groupby('histological_type')['log10_expr'].mean().sort_index()

# Format with at least 4 decimal places
result = {k: float(f"{v:.6f}") for k, v in result_series.to_dict().items()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_3xlUlyNcIniWTMgJ0JWKTFWY': 'file_storage/call_3xlUlyNcIniWTMgJ0JWKTFWY.json', 'var_call_Obx5XgwLYImIrd1G4mMloEvZ': ['clinical_info'], 'var_call_gDfw3CuO4uzpRkvtjK754jOl': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_PHPXw4NDgv4tsA2FJfuDoZ8e': 'file_storage/call_PHPXw4NDgv4tsA2FJfuDoZ8e.json'}

exec(code, env_args)
