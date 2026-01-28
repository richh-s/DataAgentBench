code = """import json
import pandas as pd

# Load previous query results from files
with open(var_call_6n8cFRXID0ZaC8CR9ehacfdZ, 'r') as f:
    clinical_records = json.load(f)
with open(var_call_Wdf1boG23o9uHBgef9nZbqm8, 'r') as f:
    mutation_records = json.load(f)

# Create DataFrames
clin_df = pd.DataFrame(clinical_records)
mut_df = pd.DataFrame(mutation_records)

# Normalize column names
# clinical records have 'barcode' and 'histological_type'
clin_df = clin_df[[c for c in clin_df.columns if c in ['barcode','histological_type'] or True]]
# Ensure we pick the expected columns
if 'barcode' not in clin_df.columns:
    # try to find the barcode-like column
    if 'barcode' in clin_df.columns:
        pass

# Keep only rows with barcode and known histological_type
clin_df = clin_df[clin_df.get('barcode').notna()]
clin_df = clin_df[clin_df.get('histological_type').notna()]
clin_df = clin_df[~clin_df['histological_type'].str.strip().str.lower().isin(['none',''])]

# Deduplicate by barcode, keep first occurrence
clin_df = clin_df.drop_duplicates(subset=['barcode'])

# Prepare mutation set: only PASS entries were queried, so consider unique ParticipantBarcode
mut_df = mut_df[mut_df.get('ParticipantBarcode').notna()]
mutated_set = set(mut_df['ParticipantBarcode'].unique())

# Create mutated flag for clinical patients
clin_df['mutated'] = clin_df['barcode'].apply(lambda x: x in mutated_set)

# Build contingency table: rows=histological_type, columns mutated True/False
ct = pd.crosstab(clin_df['histological_type'], clin_df['mutated'])
# Ensure columns for True/False exist
for col in [False, True]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[[True, False]] if True in ct.columns and False in ct.columns else ct
ct = ct.rename(columns={True: 'mutated', False: 'not_mutated'})

# Exclude histological types with marginal totals <= 10
ct['total'] = ct.sum(axis=1)
included_ct = ct[ct['total'] > 10].drop(columns=['total'])
excluded = ct[ct['total'] <= 10].drop(columns=['total'])

# If no included categories, return empty
grand_total = int(included_ct.values.sum())

# Compute chi-square statistic manually
chi2 = None
if grand_total > 0 and included_ct.shape[0] > 0:
    # Observed
    obs = included_ct.values.astype(float)
    row_totals = obs.sum(axis=1, keepdims=True)
    col_totals = obs.sum(axis=0, keepdims=True)
    expected = row_totals.dot(col_totals) / grand_total
    # Avoid division by zero
    with pd.option_context('mode.use_inf_as_na', True):
        chi2_val = ((obs - expected) ** 2 / expected)
        # replace nan/inf with 0
        chi2_val = pd.DataFrame(chi2_val).fillna(0).values
    chi2 = float(chi2_val.sum())

# Prepare contingency dict
contingency = {}
for idx, row in included_ct.iterrows():
    contingency[idx] = {'mutated': int(row['mutated']), 'not_mutated': int(row['not_mutated']), 'total': int(row['mutated']+row['not_mutated'])}

excluded_list = []
for idx, row in excluded.iterrows():
    excluded_list.append({'histological_type': idx, 'count': int(row['mutated']+row['not_mutated'])})

result = {
    'grand_total_included': grand_total,
    'num_histological_types_included': included_ct.shape[0],
    'histological_types_included': list(included_ct.index),
    'excluded_histological_types_marginal_le_10': excluded_list,
    'contingency_table_included': contingency,
    'chi2_statistic': chi2
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_s9wC2ntinBw0upr3tf0q4sJC': ['clinical_info'], 'var_call_Vz4gQCjzS0LU588kx22nykpM': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_BojVfzEgn1m1TrDIYKqsxKw1': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_7E2xMhgXQ9cyFAS7u4FVipbp': [], 'var_call_Az627EUCkiX4ZQoHJncsHvK3': 'file_storage/call_Az627EUCkiX4ZQoHJncsHvK3.json', 'var_call_CUSR7OoFmOI05A7C9xpFh4aq': 'file_storage/call_CUSR7OoFmOI05A7C9xpFh4aq.json', 'var_call_ES3caRinNPdx1ICW2wmOFxFQ': 'file_storage/call_ES3caRinNPdx1ICW2wmOFxFQ.json', 'var_call_6n8cFRXID0ZaC8CR9ehacfdZ': 'file_storage/call_6n8cFRXID0ZaC8CR9ehacfdZ.json', 'var_call_Wdf1boG23o9uHBgef9nZbqm8': 'file_storage/call_Wdf1boG23o9uHBgef9nZbqm8.json'}

exec(code, env_args)
