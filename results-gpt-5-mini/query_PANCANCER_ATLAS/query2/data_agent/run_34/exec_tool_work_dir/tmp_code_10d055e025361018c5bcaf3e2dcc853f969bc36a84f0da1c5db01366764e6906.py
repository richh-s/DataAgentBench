code = """import pandas as pd
import json

def load_var(v):
    # v may be a list of records or a filepath to a .json
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

clin = load_var(var_call_wM0CppujH8gFAdYAhXpfEfBV)
mut = load_var(var_call_QJj8JTdwUkJVdxjJliEfZbkW)

# Create DataFrames
df_clin = pd.DataFrame(clin)
# Ensure patient_id and histological_type present
if 'patient_id' not in df_clin.columns or 'histological_type' not in df_clin.columns:
    # try alternative keys
    df_clin = df_clin.rename(columns={c:c.strip() for c in df_clin.columns})

# Drop rows without patient_id
df_clin = df_clin[df_clin['patient_id'].notnull()].copy()
# Normalize patient_id
df_clin['patient_id'] = df_clin['patient_id'].astype(str).str.strip()
# Keep unique patients per histology
hist_patient_groups = df_clin.groupby('histological_type')['patient_id'].apply(lambda s: set(s)).to_dict()

# Load mutation data
df_mut = pd.DataFrame(mut)
# ParticipantBarcode column
if 'ParticipantBarcode' not in df_mut.columns:
    # try variations
    pass
# Extract patient id as last segment after '-'
df_mut['mut_patient_id'] = df_mut['ParticipantBarcode'].astype(str).apply(lambda x: x.split('-')[-1].strip())
mutated_ids = set(df_mut['mut_patient_id'].unique())

results = []
for hist, pset in hist_patient_groups.items():
    total = len(pset)
    if total == 0:
        continue
    mutated = sum(1 for pid in pset if pid in mutated_ids)
    pct = (mutated / total) * 100
    results.append({'histological_type': hist, 'total_alive_patients': total, 'mutated_patients': mutated, 'mutation_percentage': round(pct,2)})

# Sort by mutation_percentage desc, then by mutated_patients desc
results_sorted = sorted(results, key=lambda x: (x['mutation_percentage'], x['mutated_patients']), reverse=True)
# Top 3
top3 = results_sorted[:3]

print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_U3oBMtwi9VVJ8A97pdLFLkcO': ['clinical_info'], 'var_call_gGVy0eQSb82aVdBvMAZZc4hJ': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_w8Cq8gvTluncKwNHfwFod32q': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_42k1CPg7XBV6xvdiZwz8W3CI': [{'diagnosis': 'None', 'cnt': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'cnt': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'cnt': '490'}], 'var_call_nHpYVrVBd8jA6GgZ6kAFek01': [], 'var_call_XFrOHTbE8h4zJydCXaNR1hAo': [], 'var_call_x0u0yee4FjCXCI0wdPGgdz33': 'file_storage/call_x0u0yee4FjCXCI0wdPGgdz33.json', 'var_call_hh4yYdWSpq4cImO92dJTJP4R': 'file_storage/call_hh4yYdWSpq4cImO92dJTJP4R.json', 'var_call_wM0CppujH8gFAdYAhXpfEfBV': 'file_storage/call_wM0CppujH8gFAdYAhXpfEfBV.json', 'var_call_QJj8JTdwUkJVdxjJliEfZbkW': 'file_storage/call_QJj8JTdwUkJVdxjJliEfZbkW.json'}

exec(code, env_args)
