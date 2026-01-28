code = """import json
import pandas as pd
import re
import math

# Load the clinical and RNASeq JSON results from storage file paths
with open(var_call_gZdL3ygepf8ykHnX2ULSmHuS, 'r') as f:
    clinical_records = json.load(f)
with open(var_call_nzq49ZxWmzmM0uYoPCNGSSgo, 'r') as f:
    rna_records = json.load(f)

# Create DataFrames
df_clin = pd.DataFrame(clinical_records)
df_rna = pd.DataFrame(rna_records)

# Extract TCGA barcode from Patient_description
def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,6})', text)
    return m.group(1) if m else None

if 'Patient_description' not in df_clin.columns:
    df_clin['Patient_description'] = None

df_clin['barcode'] = df_clin['Patient_description'].apply(extract_barcode)

# Filter out records without barcode or without histological_type
df_clin = df_clin[df_clin['barcode'].notna() & df_clin['histological_type'].notna()]

# Exclude histological_type annotations enclosed in square brackets
def is_enclosed_in_brackets(s):
    if not isinstance(s, str):
        return False
    s2 = s.strip()
    return s2.startswith('[') and s2.endswith(']')

df_clin = df_clin[~df_clin['histological_type'].apply(is_enclosed_in_brackets)]

# Keep first histological_type per barcode (if multiple entries exist)
df_clin = df_clin.drop_duplicates(subset=['barcode'], keep='first')

# Prepare RNA dataframe: ensure ParticipantBarcode and numeric normalized_count
if 'ParticipantBarcode' not in df_rna.columns:
    df_rna['ParticipantBarcode'] = None
if 'normalized_count' not in df_rna.columns:
    df_rna['normalized_count'] = None

# Convert normalized_count to numeric
df_rna['normalized_count_num'] = pd.to_numeric(df_rna['normalized_count'], errors='coerce')
# Drop invalid expression values
df_rna = df_rna[df_rna['normalized_count_num'].notna()]

# Merge on barcode
merged = pd.merge(df_rna, df_clin, left_on='ParticipantBarcode', right_on='barcode', how='inner')

# If no matches, return empty result
results = {}
if merged.empty:
    results = {}
else:
    # Compute log10(normalized_count + 1)
    merged['log10_expr'] = merged['normalized_count_num'].apply(lambda x: math.log10(x + 1))
    # Group by histological_type and compute mean
    grp = merged.groupby('histological_type', dropna=True)['log10_expr'].mean()
    # Format results with at least 4 decimal places
    for idx, val in grp.items():
        # Ensure Python float
        results[str(idx)] = float(f"{val:.4f}")

# Print according to required format
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_F23xmEoZZKOKtIv5b447A0GQ': ['clinical_info'], 'var_call_P86JQ6Y1n09QThKVpAI1qQSE': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_MeNTcQbPHuegcMd4YSUjOBzl': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_8aBmwrr6pxsF0mtm5ogmhgWC': [], 'var_call_3tBXDtzXOue9hWefsTIAOhff': 'file_storage/call_3tBXDtzXOue9hWefsTIAOhff.json', 'var_call_gZdL3ygepf8ykHnX2ULSmHuS': 'file_storage/call_gZdL3ygepf8ykHnX2ULSmHuS.json', 'var_call_nzq49ZxWmzmM0uYoPCNGSSgo': 'file_storage/call_nzq49ZxWmzmM0uYoPCNGSSgo.json'}

exec(code, env_args)
