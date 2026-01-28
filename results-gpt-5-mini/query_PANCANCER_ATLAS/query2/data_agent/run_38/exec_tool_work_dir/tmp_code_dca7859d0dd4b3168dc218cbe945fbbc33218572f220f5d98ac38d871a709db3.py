code = """import json
import pandas as pd

# Load the clinical and mutation data files from storage paths
clinical_path = var_call_QMxtiZmkCL7eiFdmonFXNnra
mutation_path = var_call_WKei9pCMg8Z1ZFtPO2ovzEWN

with open(clinical_path, 'r') as f:
    clinical_data = json.load(f)
with open(mutation_path, 'r') as f:
    mutation_data = json.load(f)

# Create DataFrames
df_clin = pd.DataFrame(clinical_data)
# Ensure barcode and histological_type columns exist
if 'barcode' not in df_clin.columns:
    df_clin['barcode'] = None
if 'histological_type' not in df_clin.columns:
    df_clin['histological_type'] = None

# Clean clinical dataframe: drop rows without barcode
df_clin = df_clin.dropna(subset=['barcode'])
# Normalize barcode strings
df_clin['barcode'] = df_clin['barcode'].str.strip().str.upper()
# Keep unique patients (by barcode) and their histological type (first occurrence)
df_clin = df_clin.drop_duplicates(subset=['barcode']).reset_index(drop=True)

# Load mutation barcodes
df_mut = pd.DataFrame(mutation_data)
if 'ParticipantBarcode' not in df_mut.columns:
    df_mut['ParticipantBarcode'] = None

# Normalize mutation barcodes
df_mut['ParticipantBarcode'] = df_mut['ParticipantBarcode'].astype(str).str.strip().str.upper()
mutated_set = set(df_mut['ParticipantBarcode'].dropna().unique())

# Filter clinical to BRCA patients - the clinical query already filtered for Breast invasive carcinoma and Alive
# So use df_clin as-is

# Compute per-histological type totals and mutated counts
summary = []
for hist, group in df_clin.groupby('histological_type'):
    total = group['barcode'].nunique()
    # count how many of these barcodes are in mutated_set
    mutated = group['barcode'].apply(lambda x: x in mutated_set).sum()
    perc = (mutated / total * 100) if total > 0 else 0.0
    summary.append({'histological_type': hist if hist is not None else 'Unknown',
                    'total_patients': int(total),
                    'mutated_patients': int(mutated),
                    'percentage': round(float(perc), 2)})

# Sort by percentage desc, then by mutated_patients desc, then by total_patients desc
summary_sorted = sorted(summary, key=lambda x: (-x['percentage'], -x['mutated_patients'], -x['total_patients']))

# Take top 3
top3 = summary_sorted[:3]

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_zAPlYbRE6Sc604Xg76MfBHgy': ['clinical_info'], 'var_call_o9UL7mlDJjaICZB2JiHLAkKe': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_SBHscYGGjF5cuh1pjCQqD4dD': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_wrtcvM3RlgEdm1CygcHc3SUH': 'file_storage/call_wrtcvM3RlgEdm1CygcHc3SUH.json', 'var_call_nXWuXWvjRFJO3sxjbG1KLW15': 'file_storage/call_nXWuXWvjRFJO3sxjbG1KLW15.json', 'var_call_QMxtiZmkCL7eiFdmonFXNnra': 'file_storage/call_QMxtiZmkCL7eiFdmonFXNnra.json', 'var_call_WKei9pCMg8Z1ZFtPO2ovzEWN': 'file_storage/call_WKei9pCMg8Z1ZFtPO2ovzEWN.json'}

exec(code, env_args)
