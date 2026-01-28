code = """import json
import pandas as pd

# Load data from previous tool results (file paths)
with open(var_call_1M3edAIjxXhzDzeUuxoMY6Vr, 'r') as f:
    clinical = json.load(f)
with open(var_call_IZwFqeTop5tSEABBglGCS1IZ, 'r') as f:
    cdh1 = json.load(f)

df_clin = pd.DataFrame(clinical)
df_cdh1 = pd.DataFrame(cdh1)

# Normalize participant barcode fields
if 'participantbarcode' in df_clin.columns:
    df_clin['participantbarcode'] = df_clin['participantbarcode'].astype(str).str.upper()
else:
    # try other possible column names
    df_clin['participantbarcode'] = df_clin.get('ParticipantBarcode', '').astype(str).str.upper()

if 'ParticipantBarcode' in df_cdh1.columns:
    df_cdh1['ParticipantBarcode'] = df_cdh1['ParticipantBarcode'].astype(str).str.upper()
else:
    df_cdh1['ParticipantBarcode'] = df_cdh1.get('participantbarcode', '').astype(str).str.upper()

# Determine alive status from Patient_description
df_clin['Patient_description'] = df_clin['Patient_description'].astype(str)
df_clin['is_alive'] = df_clin['Patient_description'].str.contains('Alive', case=False, na=False)

# Filter to alive BRCA patients (these clinical rows were already selected for Breast invasive carcinoma)
df_alive = df_clin[df_clin['is_alive']].copy()

# Build set of participants with CDH1 mutations
cdh1_set = set(df_cdh1['ParticipantBarcode'].unique())

# Group by histological_type and compute totals and mutated counts
grouped = df_alive.groupby('histological_type')['participantbarcode'].nunique().reset_index(name='total_alive_patients')

def mutated_count_for_hist(hist):
    subset = df_alive[df_alive['histological_type'] == hist]
    uniq = set(subset['participantbarcode'].unique())
    return len(uniq & cdh1_set)

grouped['mutated_count'] = grouped['histological_type'].apply(mutated_count_for_hist)
# Avoid division by zero
grouped = grouped[grouped['total_alive_patients'] > 0].copy()
grouped['percent_mutated'] = grouped['mutated_count'] / grouped['total_alive_patients'] * 100

# Select top 3 by percent_mutated then mutated_count
grouped_sorted = grouped.sort_values(['percent_mutated', 'mutated_count'], ascending=[False, False]).head(3)

result = []
for _, r in grouped_sorted.iterrows():
    result.append({
        'histological_type': None if pd.isna(r['histological_type']) else str(r['histological_type']),
        'total_alive_patients': int(r['total_alive_patients']),
        'mutated_count': int(r['mutated_count']),
        'percent_mutated': round(float(r['percent_mutated']), 2)
    })

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_6fzPNYSgdPpIZCR1Ji4tLA4Y': ['clinical_info'], 'var_call_NQBt9vtUgAQvurS9WLfJA1Gj': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_Us2kSVe3pN9w0FzFBfjsS6RL': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_sKViZS9VeOGkTIc0052zm85d': [], 'var_call_FfNXu7iCjjgJmdCNkHRPTBMt': 'file_storage/call_FfNXu7iCjjgJmdCNkHRPTBMt.json', 'var_call_nWMdqRcQ6H87uxJBAckwgGUo': 'file_storage/call_nWMdqRcQ6H87uxJBAckwgGUo.json', 'var_call_IZwFqeTop5tSEABBglGCS1IZ': 'file_storage/call_IZwFqeTop5tSEABBglGCS1IZ.json', 'var_call_1M3edAIjxXhzDzeUuxoMY6Vr': 'file_storage/call_1M3edAIjxXhzDzeUuxoMY6Vr.json'}

exec(code, env_args)
