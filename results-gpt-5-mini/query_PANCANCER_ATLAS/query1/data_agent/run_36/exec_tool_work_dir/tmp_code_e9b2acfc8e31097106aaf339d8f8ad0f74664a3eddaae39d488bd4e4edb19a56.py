code = """import pandas as pd
import json
import re
import math

# Load tool results from storage variables
clinical_var = var_call_cOknPDQNsR54hVWp2LL5wys2
rna_var = var_call_E6VBncy1MwWhFC1nEesngaA2

# Helper to load if variable is a filepath
def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        return pd.read_json(v)
    elif isinstance(v, list):
        return pd.DataFrame(v)
    else:
        # try to convert to DataFrame
        return pd.DataFrame(v)

clin_df = load_var(clinical_var)
rna_df = load_var(rna_var)

# Normalize column names
clin_df.columns = [c for c in clin_df.columns]
rna_df.columns = [c for c in rna_df.columns]

# Extract TCGA barcode from Patient_description
def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if m:
        return m.group(1)
    # sometimes barcode appears as TCGA-XX-XXXX with lowercase letters/numbers
    m2 = re.search(r'(TCGA-[A-Za-z0-9-]+)', desc)
    if m2:
        return m2.group(1)
    return None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Clean histological_type and filter out those enclosed in square brackets
clin_df['histological_type'] = clin_df['histological_type'].astype(str)
# Exclude entries where histological_type contains '[' or ']'
clin_df = clin_df[~clin_df['histological_type'].str.contains('\[|\]', regex=True, na=False)]

# Drop rows without ParticipantBarcode
clin_df = clin_df[clin_df['ParticipantBarcode'].notna()].copy()

# Prepare RNA df: ensure ParticipantBarcode column and numeric normalized_count
rna_df = rna_df[rna_df['Symbol'].astype(str)=='IGF2'].copy()
# Convert normalized_count to numeric, coerce errors to NaN
rna_df['normalized_count'] = pd.to_numeric(rna_df['normalized_count'], errors='coerce')
# Drop invalid expression values
rna_df = rna_df[rna_df['normalized_count'].notna()].copy()

# Merge clinical LGG patients with RNA expression on ParticipantBarcode
merged = pd.merge(clin_df, rna_df, on='ParticipantBarcode', how='inner')

# If no merges, return empty result
if merged.shape[0] == 0:
    result = {}
else:
    # Compute log10(normalized_count + 1)
    merged['log10_expr'] = merged['normalized_count'].apply(lambda x: math.log10(x+1))
    # Group by histological_type and compute mean
    grouped = merged.groupby('histological_type', dropna=True)['log10_expr'].mean()
    # Format results with at least four decimal places
    result = {ht: format(v, '.4f') for ht, v in grouped.items()}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qEqg9tozeQyVWdpVMUYPBIxT': ['clinical_info'], 'var_call_Ce3jW6l7WUqlKM0CKXvoPuE8': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_j2sdpyUtVDn70As4894TRXAu': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_qcsqymuajBEHrOwunhdr1ffY': 'file_storage/call_qcsqymuajBEHrOwunhdr1ffY.json', 'var_call_6TfqSidUJnTDF1PEEEMNjEm9': [], 'var_call_ajMwwlrOYqUzdc9bz8aEKDkO': [], 'var_call_c1nQFZ3zUMJz6il1xIbfbdop': [{'diagnosis': 'None', 'histological_type': 'Untreated primary (de novo) GBM', 'n': '539'}, {'diagnosis': 'None', 'histological_type': 'Glioblastoma Multiforme (GBM)', 'n': '31'}, {'diagnosis': 'None', 'histological_type': 'Treated primary GBM', 'n': '20'}], 'var_call_cOknPDQNsR54hVWp2LL5wys2': 'file_storage/call_cOknPDQNsR54hVWp2LL5wys2.json', 'var_call_E6VBncy1MwWhFC1nEesngaA2': 'file_storage/call_E6VBncy1MwWhFC1nEesngaA2.json'}

exec(code, env_args)
