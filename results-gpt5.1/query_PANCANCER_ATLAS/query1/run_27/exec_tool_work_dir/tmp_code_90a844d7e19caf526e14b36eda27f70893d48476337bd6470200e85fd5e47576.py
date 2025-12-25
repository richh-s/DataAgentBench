code = """import json, pandas as pd, math

# Load IGF2 expression file
with open(var_call_L66SxSNNd2f7hCakXH3NikxR, 'r') as f:
    igf2_data = json.load(f)
expr_df = pd.DataFrame(igf2_data)

# Load brain tumor (C71) clinical subset
with open(var_call_FuYBKgzYguFiCsuLqOxYEKCv, 'r') as f:
    clin_data = json.load(f)
clin_df = pd.DataFrame(clin_data)

# Extract PatientBarcode from Patient_description (pattern like TCGA-..-....)
import re

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].str.extract(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')

# Filter for LGG versus GBM by histologic_type codes in icd_o_3_histology
# LGG ICD-O-3 histology codes often include 9382/3 (oligoastrocytoma), 9400/3 (astrocytoma), 9410/3, 9420/3, etc.
# But the problem statement directly says LGG means Brain lower grade glioma; however our C71 query returns mainly GBM (9440/3).
# We will identify records whose histological_type or icd_o_3_histology string contains 'Astrocytoma', 'Oligodendroglioma', 'Oligoastrocytoma', or codes starting with 9382, 9400, 9410, 9420, 9450, 9451.

lgg_mask = (
    clin_df['histological_type'].str.contains('astrocytoma', case=False, na=False) |
    clin_df['histological_type'].str.contains('oligodendroglioma', case=False, na=False) |
    clin_df['histological_type'].str.contains('oligoastrocytoma', case=False, na=False) |
    clin_df['icd_o_3_histology'].str.startswith(('9382', '9400', '9410', '9420', '9450', '9451'), na=False)
)

lgg_clin = clin_df[lgg_mask].copy()

# Merge LGG clinical with IGF2 expression on ParticipantBarcode
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])

merged = pd.merge(lgg_clin[['ParticipantBarcode','histological_type']], expr_df[['ParticipantBarcode','normalized_count']], on='ParticipantBarcode', how='inner')

# Exclude histology annotations enclosed entirely in square brackets
valid_hist_mask = ~merged['histological_type'].str.match(r'\[[^\]]*\]$', na=False)
merged = merged[valid_hist_mask].copy()

# Compute log10(normalized_count + 1)
merged['log10_expr'] = merged['normalized_count'].apply(lambda x: math.log10(x + 1))

# Group by histological_type and compute mean
result_series = merged.groupby('histological_type')['log10_expr'].mean().sort_index()

result = {hist: round(val, 4) for hist, val in result_series.items()}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_L66SxSNNd2f7hCakXH3NikxR': 'file_storage/call_L66SxSNNd2f7hCakXH3NikxR.json', 'var_call_ySwYbVDPfWZ8MRH5L5aCVaS4': ['clinical_info'], 'var_call_CWvM41SR8Fvg7Kwu3DLbB4RP': 'file_storage/call_CWvM41SR8Fvg7Kwu3DLbB4RP.json', 'var_call_ShQclJlgrEotge6SnHxcS8eV': {'columns_sample': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight']}, 'var_call_FuYBKgzYguFiCsuLqOxYEKCv': 'file_storage/call_FuYBKgzYguFiCsuLqOxYEKCv.json'}

exec(code, env_args)
