code = """import json
import pandas as pd
import re

# Load clinical data from storage
varname_clin = 'var_call_9K8Y1sCS3nJeKbRf7tReLJhY'
varname_mut = 'var_call_D2UonokL4VCxWg8mpS5DPTq2'

# Helper to load variable which may be a file path (string) or list
def load_var(var):
    if isinstance(var, str):
        # it's a file path to json
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

clinical = load_var(var_call_9K8Y1sCS3nJeKbRf7tReLJhY)
mutations = load_var(var_call_D2UonokL4VCxWg8mpS5DPTq2)

# Build DataFrame
clin_df = pd.DataFrame(clinical)
mut_df = pd.DataFrame(mutations)

# Filter clinical records for alive patients (case-insensitive 'alive' in Patient_description)
clin_df['Patient_description'] = clin_df['Patient_description'].astype(str)
clin_df_alive = clin_df[clin_df['Patient_description'].str.lower().str.contains('alive')]

# Further ensure these are breast invasive carcinoma records by checking 'Breast' in Patient_description
clin_df_alive = clin_df_alive[clin_df_alive['Patient_description'].str.contains('Breast', case=False, na=False)]

# Extract patient barcode from Patient_description using regex
def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', text, re.IGNORECASE)
    if m:
        return m.group(1).upper()
    return None

clin_df_alive['patient_barcode'] = clin_df_alive['Patient_description'].apply(extract_barcode)
clin_df_alive = clin_df_alive[clin_df_alive['patient_barcode'].notna()]

# Use unique patients; keep first histological_type if duplicates
clin_unique = clin_df_alive.drop_duplicates(subset=['patient_barcode']).copy()

# Prepare mutation participant set for CDH1
mut_df['ParticipantBarcode'] = mut_df['ParticipantBarcode'].astype(str)
cdh1_participants = set(mut_df['ParticipantBarcode'].str.upper().unique())

# For each clinical patient, mark if mutated in CDH1
clin_unique['has_CDH1_mut'] = clin_unique['patient_barcode'].apply(lambda x: x in cdh1_participants)

# Group by histological_type
group = clin_unique.groupby('histological_type').agg(
    total_patients=('patient_barcode', 'count'),
    mutated_patients=('has_CDH1_mut', 'sum')
).reset_index()

# Compute percentage
group['percent_mutated'] = group.apply(lambda row: (row['mutated_patients']/row['total_patients']*100) if row['total_patients']>0 else 0, axis=1)

# Sort by percent descending, then by mutated count desc, then total_patients desc
group_sorted = group.sort_values(by=['percent_mutated', 'mutated_patients', 'total_patients'], ascending=[False, False, False])

# Take top 3
top3 = group_sorted.head(3)

# Prepare result list of dicts
result = []
for _, r in top3.iterrows():
    result.append({
        'histological_type': None if pd.isna(r['histological_type']) else str(r['histological_type']),
        'total_patients': int(r['total_patients']),
        'mutated_patients': int(r['mutated_patients']),
        'percent_mutated': round(float(r['percent_mutated']), 2)
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uBnMLbrmjsDEN4Y701ytQkfZ': ['clinical_info'], 'var_call_alNYUEYi7pH4OA8hed4DmDPc': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_bn9UOC4wbbQ8BLWxy9VQs5vW': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_QdwcQKnEKe2K8lE4D98J90O6': 'file_storage/call_QdwcQKnEKe2K8lE4D98J90O6.json', 'var_call_ZiHFASkDljKdpVIu0Padi3lr': 'file_storage/call_ZiHFASkDljKdpVIu0Padi3lr.json', 'var_call_9K8Y1sCS3nJeKbRf7tReLJhY': 'file_storage/call_9K8Y1sCS3nJeKbRf7tReLJhY.json', 'var_call_D2UonokL4VCxWg8mpS5DPTq2': 'file_storage/call_D2UonokL4VCxWg8mpS5DPTq2.json'}

exec(code, env_args)
