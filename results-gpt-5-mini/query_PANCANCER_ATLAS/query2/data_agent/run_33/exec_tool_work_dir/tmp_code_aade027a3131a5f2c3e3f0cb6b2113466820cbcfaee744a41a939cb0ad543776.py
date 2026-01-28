code = """import json
import pandas as pd

# Load clinical alive breast data and mutation data from storage files
with open(var_call_Ie6ctFvF6FrB8wlKAaGwHzcr, 'r') as f:
    clinical = json.load(f)
with open(var_call_E3jbwx5CXtcWsWgVuHgHmpkX, 'r') as f:
    mutations = json.load(f)

cli_df = pd.DataFrame(clinical)
mut_df = pd.DataFrame(mutations)

# Normalize column names
# clinical entries: Patient_description, histological_type, patient_id
# mutation entries: ParticipantBarcode, Hugo_Symbol

# Extract patient_id from ParticipantBarcode
def extract_patient_id(pb):
    if not isinstance(pb, str):
        return ''
    parts = pb.split('-')
    if len(parts) >= 3:
        return parts[2]
    return pb

mut_df['patient_id'] = mut_df['ParticipantBarcode'].apply(extract_patient_id)

# Consider unique mutated patient IDs for CDH1 (mut_df already filtered to CDH1 in the query)
mutated_patient_ids = set(mut_df['patient_id'].unique())

# Filter clinical rows: ensure patient_id present and histological_type not null
cli_df = cli_df[cli_df['patient_id'].notnull()]

# Group by histological_type among alive breast patients
# clinical data already filtered to alive breast patients when queried
grouped = cli_df.groupby('histological_type').agg(
    total_alive_patients=pd.NamedAgg(column='patient_id', aggfunc=lambda x: x.nunique()),
    patient_ids=pd.NamedAgg(column='patient_id', aggfunc=lambda x: list(pd.Series(x).unique()))
).reset_index()

# Compute mutated counts per histological_type
results = []
for _, row in grouped.iterrows():
    htype = row['histological_type']
    total = int(row['total_alive_patients'])
    pids = row['patient_ids']
    mutated = sum(1 for pid in pids if pid in mutated_patient_ids)
    pct = (mutated / total * 100) if total > 0 else 0.0
    results.append({'histological_type': htype, 'total_alive_patients': total, 'mutated_patients': mutated, 'percent_mutated': round(pct, 2)})

# Sort by percent_mutated desc, then by mutated_patients desc
results_sorted = sorted(results, key=lambda x: (-x['percent_mutated'], -x['mutated_patients']))

top3 = results_sorted[:3]

import json as _json
out = _json.dumps(top3)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cY8fR8o5INPoxANpVsLI4Rva': ['clinical_info'], 'var_call_tSKH4a6hPPSgmCY7LCeTLQ6b': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_cb5pzHhGzgqoqK5QVtxc2cag': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_zAqAxz3xUczmdHtQtUv6AeOi': [{'diagnosis': 'None'}, {'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_call_dvTUNqvPld9Bsr4v2ZYE4ARr': [], 'var_call_nePJY3eHTU93RsPjC0CcKwQM': 'file_storage/call_nePJY3eHTU93RsPjC0CcKwQM.json', 'var_call_OjIz9OjGmslVdeSf39YFudFP': 'file_storage/call_OjIz9OjGmslVdeSf39YFudFP.json', 'var_call_Ie6ctFvF6FrB8wlKAaGwHzcr': 'file_storage/call_Ie6ctFvF6FrB8wlKAaGwHzcr.json', 'var_call_E3jbwx5CXtcWsWgVuHgHmpkX': 'file_storage/call_E3jbwx5CXtcWsWgVuHgHmpkX.json'}

exec(code, env_args)
