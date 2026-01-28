code = """import json
import pandas as pd
import math
import re

# Load clinical LGG participants and histology
data_path_clin = var_call_ezAccnCBdXPICWGjQuEeSl1e
if isinstance(data_path_clin, str):
    with open(data_path_clin, 'r') as f:
        clin = json.load(f)
else:
    clin = data_path_clin

# Load IGF2 expression data
data_path_expr = var_call_Z7UyzzcYaWnxVXZtkJkL4MWz
if isinstance(data_path_expr, str):
    with open(data_path_expr, 'r') as f:
        expr = json.load(f)
else:
    expr = data_path_expr

# Create DataFrames
df_clin = pd.DataFrame(clin)
# clinical query returned 'participant_barcode' and 'histological_type'
# Normalize column names
if 'participant_barcode' not in df_clin.columns and 'ParticipantBarcode' in df_clin.columns:
    df_clin = df_clin.rename(columns={'ParticipantBarcode':'participant_barcode'})

# Drop rows with null histological_type or participant_barcode
df_clin = df_clin[df_clin['histological_type'].notna() & df_clin['participant_barcode'].notna()].copy()

# Exclude histological_type enclosed in square brackets: e.g., '[Astrocytoma]'
def enclosed_in_brackets(x):
    x2 = str(x).strip()
    return bool(re.match(r'^\[.*\]$', x2))

mask = df_clin['histological_type'].apply(lambda x: not enclosed_in_brackets(x))
df_clin = df_clin[mask].copy()

# Some participant barcodes might include trailing/leading spaces
df_clin['participant_barcode'] = df_clin['participant_barcode'].str.strip()

# Expression dataframe
df_expr = pd.DataFrame(expr)
# Normalize column name
if 'ParticipantBarcode' in df_expr.columns and 'ParticipantBarcode' not in df_expr.columns:
    pass
# Ensure ParticipantBarcode and normalized_count exist
if 'ParticipantBarcode' not in df_expr.columns or 'normalized_count' not in df_expr.columns:
    raise ValueError('Expected columns not in expression data')

# Clean and convert normalized_count to float; drop invalids
def to_float(x):
    try:
        return float(x)
    except Exception:
        return None

df_expr['normalized_count'] = df_expr['normalized_count'].apply(to_float)
# Drop null normalized_count
df_expr = df_expr[df_expr['normalized_count'].notna()].copy()
# Strip participant barcode
df_expr['ParticipantBarcode'] = df_expr['ParticipantBarcode'].str.strip()

# Join clinical LGG patients with expression on ParticipantBarcode == participant_barcode
# Note: clinical participant_barcode likely in form TCGA-XX-XXXX; molecular ParticipantBarcode same
merged = pd.merge(df_clin, df_expr, left_on='participant_barcode', right_on='ParticipantBarcode', how='inner')

# Only include patients with valid IGF2 expression values already filtered
# Compute log10(normalized_count + 1)
merged['log10_expr'] = merged['normalized_count'].apply(lambda v: math.log10(v + 1.0))

# Group by histological_type and compute mean
grouped = merged.groupby('histological_type')['log10_expr'].mean().reset_index()

# Prepare result dict with at least four decimal places
result = {}
for _, row in grouped.iterrows():
    hist = row['histological_type']
    val = row['log10_expr']
    # Format with 4 decimal places
    result[hist] = format(round(float(val), 4), '.4f')

# Sort result by histology name for consistency
result_sorted = {k: result[k] for k in sorted(result.keys())}

print("__RESULT__:")
print(json.dumps(result_sorted))"""

env_args = {'var_call_Y9j2KgN8WdaxcJDMyS20Q4zF': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_gmbI0JSnIv4rWDnrIjj8hkhP': 'file_storage/call_gmbI0JSnIv4rWDnrIjj8hkhP.json', 'var_call_ezAccnCBdXPICWGjQuEeSl1e': 'file_storage/call_ezAccnCBdXPICWGjQuEeSl1e.json', 'var_call_Z7UyzzcYaWnxVXZtkJkL4MWz': 'file_storage/call_Z7UyzzcYaWnxVXZtkJkL4MWz.json'}

exec(code, env_args)
