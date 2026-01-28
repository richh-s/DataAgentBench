code = """import json
import pandas as pd

# Load clinical data (var_call_fw3i3zXLu20yzVWfGbgQqU4R) and mutation data (var_call_TInIMkx6lAggMaJOGaxae2UJ)

def load_storage(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

clin = load_storage(var_call_fw3i3zXLu20yzVWfGbgQqU4R)
mut = load_storage(var_call_TInIMkx6lAggMaJOGaxae2UJ)

df_clin = pd.DataFrame(clin)
# Ensure expected columns
if 'barcode' not in df_clin.columns or 'histological_type' not in df_clin.columns:
    raise ValueError('Clinical data missing expected columns')

# Normalize and drop NA
df_clin = df_clin[['barcode','histological_type']].dropna()
# Keep unique patients
df_clin = df_clin.drop_duplicates(subset=['barcode'])

# Mutation data
df_mut = pd.DataFrame(mut)
if 'ParticipantBarcode' not in df_mut.columns:
    raise ValueError('Mutation data missing ParticipantBarcode')
mut_set = set(df_mut['ParticipantBarcode'].dropna().unique())

# Compute per-histology totals and mutated counts
summary = df_clin.groupby('histological_type').agg(
    total_patients=('barcode', 'nunique'),
    mutated_patients=('barcode', lambda x: sum(1 for b in x if b in mut_set))
).reset_index()
summary['percent_mutated'] = summary.apply(lambda r: (r['mutated_patients']/r['total_patients']*100) if r['total_patients']>0 else 0, axis=1)

# Sort by percent desc, then mutated desc, then total desc
summary = summary.sort_values(by=['percent_mutated','mutated_patients','total_patients'], ascending=[False,False,False])

# Select top 3
top3 = summary.head(3)
# Prepare result list
result = []
for _, row in top3.iterrows():
    result.append({
        'histological_type': row['histological_type'],
        'total_patients': int(row['total_patients']),
        'mutated_patients': int(row['mutated_patients']),
        'percent_mutated': round(float(row['percent_mutated']), 2)
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_XWDH8CVWHKeCRk72B1vVlCxj': ['clinical_info'], 'var_call_68UkpTHjuMfvI4bwCV8tzpss': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_0AGdXT3A8GU1jM4SE1Z7yWTo': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_vRu840GgnZhNEQ8eP679D0Kx': [], 'var_call_5nnlmNzNLuPzKCglH6kmaEw1': 'file_storage/call_5nnlmNzNLuPzKCglH6kmaEw1.json', 'var_call_BjAdCgOuDM7GXlK3tWAKVkTi': [{'count': '1087'}], 'var_call_9q7zvi24LRl68W9JXW3wvAnU': 'file_storage/call_9q7zvi24LRl68W9JXW3wvAnU.json', 'var_call_NbmY9fWZ8i0zzcz6v3iqZZo3': 'file_storage/call_NbmY9fWZ8i0zzcz6v3iqZZo3.json', 'var_call_fw3i3zXLu20yzVWfGbgQqU4R': 'file_storage/call_fw3i3zXLu20yzVWfGbgQqU4R.json', 'var_call_TInIMkx6lAggMaJOGaxae2UJ': 'file_storage/call_TInIMkx6lAggMaJOGaxae2UJ.json'}

exec(code, env_args)
