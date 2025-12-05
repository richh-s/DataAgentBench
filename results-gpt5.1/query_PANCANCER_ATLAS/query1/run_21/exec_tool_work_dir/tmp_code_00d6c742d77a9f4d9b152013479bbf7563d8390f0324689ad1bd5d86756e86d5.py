code = """import json, math, pandas as pd

# Load full RNASeq IGF2 data
with open(var_call_iMWVXZSmbM8zkPyjh5tinHwK, 'r') as f:
    igf2_records = json.load(f)

# Convert to DataFrame
rna_df = pd.DataFrame(igf2_records)

# Ensure numeric
rna_df['normalized_count'] = pd.to_numeric(rna_df['normalized_count'], errors='coerce')

# Extract patient barcode from Patient_description in LGG clinical subset
with open(var_call_t4BW4J0YLnMofZ76XYCpKSH6, 'r') as f:
    lgg_records = json.load(f)

clin_df = pd.DataFrame(lgg_records)

# Parse barcode like 'patient TCGA-XX-YYYY' or 'barcode TCGA-XX-YYYY'
import re

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
    return m.group(0) if m else None

clin_df['ParticipantBarcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Drop rows without barcode
clin_df = clin_df.dropna(subset=['ParticipantBarcode'])

# For this task, treat icd_o_3_histology as histology type
clin_df = clin_df.rename(columns={'icd_o_3_histology': 'histology'})

# Exclude histology annotations enclosed in square brackets (exactly like "[xxx]")
mask_valid_hist = ~clin_df['histology'].astype(str).str.match(r'^\[.*\]$')
clin_df = clin_df[mask_valid_hist]

# Join RNA with clinical on ParticipantBarcode
merged = pd.merge(rna_df, clin_df[['ParticipantBarcode', 'histology']], on='ParticipantBarcode', how='inner')

# Keep valid expression values
merged = merged.dropna(subset=['normalized_count'])

# Compute log10(normalized_count + 1)
merged['log10_expr'] = (merged['normalized_count'] + 1).apply(lambda x: math.log10(x) if x > 0 else None)
merged = merged.dropna(subset=['log10_expr'])

# Group by histology and compute mean
result_series = merged.groupby('histology')['log10_expr'].mean()

# Prepare result with at least four decimal places
result = [
    {
        'histology': hist,
        'average_log10_IGF2_expression': float(f"{val:.4f}")
    }
    for hist, val in result_series.items()
]

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_iMWVXZSmbM8zkPyjh5tinHwK': 'file_storage/call_iMWVXZSmbM8zkPyjh5tinHwK.json', 'var_call_iFMcWSm4jKgA5O8o3yU2sXXb': ['clinical_info'], 'var_call_hoIauEKLn6RRvWaIMNmcVvxx': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_tbWkpwx4L0U2O49i1nrfFVPA': [], 'var_call_HNxdJnPgVCwupqZYN27XJAMu': 'file_storage/call_HNxdJnPgVCwupqZYN27XJAMu.json', 'var_call_t4BW4J0YLnMofZ76XYCpKSH6': 'file_storage/call_t4BW4J0YLnMofZ76XYCpKSH6.json'}

exec(code, env_args)
