code = """import json
import pandas as pd
import re

# Load clinical data (alive breast patients)
data_clinical = None
if isinstance(var_call_BuXG9JpUCFnwVI99VzGvswu0, str):
    with open(var_call_BuXG9JpUCFnwVI99VzGvswu0, 'r') as f:
        data_clinical = json.load(f)
else:
    data_clinical = var_call_BuXG9JpUCFnwVI99VzGvswu0

# Load mutation data (CDH1 participant counts)
data_mut = None
if isinstance(var_call_EFmQZMhmVrqiji99KQwIw01E, str):
    with open(var_call_EFmQZMhmVrqiji99KQwIw01E, 'r') as f:
        data_mut = json.load(f)
else:
    data_mut = var_call_EFmQZMhmVrqiji99KQwIw01E

# Convert to DataFrames
df_clin = pd.DataFrame(data_clinical)
# Ensure columns exist
if 'Patient_description' not in df_clin.columns:
    df_clin['Patient_description'] = df_clin.get('patient_description', '')

# Extract participant barcode from Patient_description using regex
def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'(TCGA[-A-Za-z0-9]+)', text)
    return m.group(1) if m else None

df_clin['ParticipantBarcode'] = df_clin['Patient_description'].apply(extract_barcode)
# Keep rows that have a barcode and histological_type
df_clin = df_clin[df_clin['ParticipantBarcode'].notna()]
# Normalize histological_type
if 'histological_type' not in df_clin.columns:
    df_clin['histological_type'] = df_clin.get('histology', None)

# Deduplicate by ParticipantBarcode (keep first)
df_clin = df_clin.drop_duplicates(subset=['ParticipantBarcode'])

# Mutation dataframe
df_mut = pd.DataFrame(data_mut)
# Ensure column name ParticipantBarcode
if 'ParticipantBarcode' not in df_mut.columns and 'participantbarcode' in df_mut.columns:
    df_mut.rename(columns={'participantbarcode':'ParticipantBarcode'}, inplace=True)

# Mark mutated participants
mut_participants = set(df_mut['ParticipantBarcode'].dropna().astype(str).tolist())

# Filter clinical to BRCA (breast) - we already queried by Patient_description ILIKE '%Breast%'
# Compute totals per histological_type

# Some histological_type may be null
df_clin['histological_type'] = df_clin['histological_type'].fillna('Unknown')

# Total counts
totals = df_clin.groupby('histological_type').size().reset_index(name='total_patients')

# Mutated counts
# For each clinical participant, check if in mut_participants
df_clin['has_CDH1_mut'] = df_clin['ParticipantBarcode'].astype(str).isin(mut_participants)
mut_counts = df_clin.groupby('histological_type')['has_CDH1_mut'].sum().reset_index(name='mutated_patients')

# Merge
summary = pd.merge(totals, mut_counts, on='histological_type')
summary['percent_mutated'] = (summary['mutated_patients'] / summary['total_patients']) * 100

# Sort by percent desc, then by mutated_patients desc
summary_sorted = summary.sort_values(by=['percent_mutated','mutated_patients'], ascending=[False, False])

# Select top 3
top3 = summary_sorted.head(3)

# Prepare output list of dicts
output = []
for _, row in top3.iterrows():
    output.append({
        'histological_type': row['histological_type'],
        'total_patients': int(row['total_patients']),
        'mutated_patients': int(row['mutated_patients']),
        'percent_mutated': round(float(row['percent_mutated']), 2)
    })

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_XiGkn6iJ0KoxjFe25aH6gnLs': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_Ot2MojocABImKiW8RmDYEJ1x': [], 'var_call_OOS1Y2EQTKEz8r9XF4Eu3hzf': 'file_storage/call_OOS1Y2EQTKEz8r9XF4Eu3hzf.json', 'var_call_hQIIJ3JH6JwzDg5AMGP8pPke': 'file_storage/call_hQIIJ3JH6JwzDg5AMGP8pPke.json', 'var_call_BuXG9JpUCFnwVI99VzGvswu0': 'file_storage/call_BuXG9JpUCFnwVI99VzGvswu0.json', 'var_call_EFmQZMhmVrqiji99KQwIw01E': 'file_storage/call_EFmQZMhmVrqiji99KQwIw01E.json'}

exec(code, env_args)
