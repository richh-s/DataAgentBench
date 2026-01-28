code = """import json, re
import pandas as pd

# Load clinical BRCA alive data
clin_var = var_call_y3B3hO536l1naZ9F3f81NxFw
mut_var = var_call_kTvgpsu0eS1tgwTlhmQfMuBP

# If variables are file paths (strings), load JSON
def load_var(v):
    if isinstance(v, str):
        # assume it's a file path
        with open(v, 'r') as f:
            return json.load(f)
    return v

clin = load_var(clin_var)
mut = load_var(mut_var)

# Create DataFrames
df_clin = pd.DataFrame(clin)
# Ensure relevant columns
if 'Patient_description' in df_clin.columns:
    df_clin['barcode'] = df_clin['Patient_description'].apply(lambda x: (re.search(r"TCGA-[A-Za-z0-9-]+", x) .group(0)) if isinstance(x, str) and re.search(r"TCGA-[A-Za-z0-9-]+", x) else None)
else:
    df_clin['barcode'] = None

# Use histological_type
if 'histological_type' not in df_clin.columns:
    df_clin['histological_type'] = None

# Drop entries without barcode
df_clin = df_clin[df_clin['barcode'].notnull()].copy()
# Normalize barcode (strip whitespace)
df_clin['barcode'] = df_clin['barcode'].str.strip()

# Mutations dataframe
df_mut = pd.DataFrame(mut)
# Ensure ParticipantBarcode column
if 'ParticipantBarcode' in df_mut.columns:
    df_mut['ParticipantBarcode'] = df_mut['ParticipantBarcode'].astype(str).str.strip()
else:
    df_mut['ParticipantBarcode'] = None

# For safety, deduplicate clinical by barcode, keep first histotype
df_clin_unique = df_clin.drop_duplicates(subset=['barcode']).copy()

# Compute counts per histological_type
summary = []
for ht, group in df_clin_unique.groupby('histological_type'):
    total = len(group)
    # mutated if barcode in df_mut ParticipantBarcode
    mutated = df_mut[df_mut['ParticipantBarcode'].isin(group['barcode'])]['ParticipantBarcode'].nunique()
    pct = (mutated / total * 100) if total>0 else 0.0
    summary.append({'histological_type': ht if pd.notnull(ht) else 'Unknown', 'total_patients': int(total), 'mutated_patients': int(mutated), 'percentage_mutated': round(pct,2)})

# Sort by percentage desc, then by mutated count desc
summary_sorted = sorted(summary, key=lambda x: (-x['percentage_mutated'], -x['mutated_patients']))

# Take top 3
top3 = summary_sorted[:3]

# Prepare result
result = top3

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_N0W42BbdNjHckPGDY3NaxUUy': ['clinical_info'], 'var_call_3QgwZP5fHmoK5uGojeSRfVrN': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_uHTrJ5bPn2YJNXgrCJdx2Taj': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_1ScvKaLb2iOp14HJ9Jk04ACV': [], 'var_call_Cf3tncp2c9gxmqjbiF9yqO7W': 'file_storage/call_Cf3tncp2c9gxmqjbiF9yqO7W.json', 'var_call_tm2W6Q0JD5OKQZZcCvDWoXMG': [], 'var_call_qJ2jwtnxNdUsJd6Gw1Llm0Hb': 'file_storage/call_qJ2jwtnxNdUsJd6Gw1Llm0Hb.json', 'var_call_y3B3hO536l1naZ9F3f81NxFw': 'file_storage/call_y3B3hO536l1naZ9F3f81NxFw.json', 'var_call_kTvgpsu0eS1tgwTlhmQfMuBP': 'file_storage/call_kTvgpsu0eS1tgwTlhmQfMuBP.json'}

exec(code, env_args)
