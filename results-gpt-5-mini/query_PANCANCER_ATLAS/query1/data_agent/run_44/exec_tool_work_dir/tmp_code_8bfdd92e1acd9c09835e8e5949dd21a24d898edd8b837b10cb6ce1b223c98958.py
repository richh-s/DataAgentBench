code = """import json
import pandas as pd
import math

# Load storage files (large results stored as file paths)
with open(var_call_NfOkPlVA131R2kZAQ44atqPo, 'r') as f:
    clinical_data = json.load(f)
with open(var_call_bDODlN3PLjz3QTGpkyBMCM8c, 'r') as f:
    expr_data = json.load(f)

# Create dataframes
df_clin = pd.DataFrame(clinical_data)
# Normalize column name
if 'participantbarcode' in df_clin.columns:
    df_clin.rename(columns={'participantbarcode': 'ParticipantBarcode'}, inplace=True)

# Drop rows with missing histological_type or ParticipantBarcode
df_clin = df_clin[['ParticipantBarcode', 'histological_type']].dropna()

# Exclude histological_type entries enclosed in square brackets
# Define as any string that starts with '[' and ends with ']' ignoring surrounding whitespace
def is_bracketed(s):
    s = str(s).strip()
    return s.startswith('[') and s.endswith(']')

# Filter out bracketed annotations
df_clin = df_clin[~df_clin['histological_type'].apply(is_bracketed)].copy()

# Deduplicate by ParticipantBarcode keeping first occurrence
df_clin = df_clin.drop_duplicates(subset=['ParticipantBarcode'], keep='first')

# Expression dataframe
df_expr = pd.DataFrame(expr_data)
# Ensure correct column names
if 'ParticipantBarcode' not in df_expr.columns and 'participantbarcode' in df_expr.columns:
    df_expr.rename(columns={'participantbarcode': 'ParticipantBarcode'}, inplace=True)

# Keep only rows with non-null normalized_count
df_expr = df_expr[['ParticipantBarcode', 'normalized_count']].dropna()

# Convert normalized_count to float
def to_float(x):
    try:
        return float(x)
    except:
        return None

df_expr['normalized_count'] = df_expr['normalized_count'].apply(to_float)
df_expr = df_expr.dropna(subset=['normalized_count'])

# Merge clinical LGG participants with IGF2 expression
# Note: clinical ParticipantBarcode values may be complete barcodes (e.g., TCGA-DB-A4XE)
# Ensure casing matches
merged = pd.merge(df_clin, df_expr, on='ParticipantBarcode', how='inner')

# If merge empty, try matching by taking first 12 characters (TCGA-XX-XXXX) from expr
if merged.shape[0] == 0:
    df_expr['ParticipantBarcode_short'] = df_expr['ParticipantBarcode'].str.slice(0,12)
    df_clin['ParticipantBarcode_short'] = df_clin['ParticipantBarcode'].str.slice(0,12)
    merged = pd.merge(df_clin, df_expr, left_on='ParticipantBarcode_short', right_on='ParticipantBarcode_short', how='inner')
    # use histological_type and normalized_count

# Compute log10(normalized_count + 1)
merged['log10_expr'] = merged['normalized_count'].apply(lambda x: math.log10(x + 1.0))

# Group by histological_type and compute mean
grouped = merged.groupby('histological_type')['log10_expr'].mean().reset_index()

# Format results with at least four decimal places
result = {}
for _, row in grouped.iterrows():
    hist = row['histological_type']
    mean_val = row['log10_expr']
    # Format to 4 decimal places
    result[hist] = float(f"{mean_val:.4f}")

# Sort result by histological_type for consistent output
result = dict(sorted(result.items()))

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JIXcft0SldMkXHbKZN2fJy30': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_ARfGnMo5lXgc8tb3J9nxYRIH': 'file_storage/call_ARfGnMo5lXgc8tb3J9nxYRIH.json', 'var_call_KAg4eGGhF2pK5ajtxXMmkHHI': 'file_storage/call_KAg4eGGhF2pK5ajtxXMmkHHI.json', 'var_call_NfOkPlVA131R2kZAQ44atqPo': 'file_storage/call_NfOkPlVA131R2kZAQ44atqPo.json', 'var_call_bDODlN3PLjz3QTGpkyBMCM8c': 'file_storage/call_bDODlN3PLjz3QTGpkyBMCM8c.json'}

exec(code, env_args)
