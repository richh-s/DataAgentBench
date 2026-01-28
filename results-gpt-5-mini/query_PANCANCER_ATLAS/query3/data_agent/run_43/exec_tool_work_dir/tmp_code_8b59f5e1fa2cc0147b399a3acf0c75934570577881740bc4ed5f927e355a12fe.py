code = """import json
import pandas as pd
import numpy as np

# Load data from storage-provided file paths
clinical_path = var_call_KjCUekhiMFJqxCy1fE4kgEGL
mut_path = var_call_J6FJbgdvx1FcYy5ciFfyl2nS

with open(clinical_path, 'r') as f:
    clinical = json.load(f)
with open(mut_path, 'r') as f:
    muts = json.load(f)

# Build clinical DataFrame
df_clin = pd.DataFrame(clinical)
# Keep relevant columns and drop rows without histological_type or patient_id
df_clin = df_clin[['patient_id', 'histological_type']].dropna()
# Normalize patient_id strings
df_clin['patient_id'] = df_clin['patient_id'].astype(str).str.strip()
# Drop duplicates (one record per patient)
df_clin = df_clin.drop_duplicates(subset=['patient_id'])

# Build mutation set for CDH1 PASS participants
# muts is list of dicts with ParticipantBarcode
participant_barcodes = [m['ParticipantBarcode'] for m in muts if m.get('ParticipantBarcode')]
# Extract patient portion (last group after last '-')
mut_patients = set([pb.rsplit('-', 1)[-1] for pb in participant_barcodes])

# Map mutation presence onto clinical df
df_clin['CDH1_mutated'] = df_clin['patient_id'].apply(lambda x: x in mut_patients)

# Filter to only female BRCA patients: clinical query already filtered by 'Breast' and 'FEMALE'
# But ensure histological_type known (non-empty)
df_clin = df_clin[df_clin['histological_type'].astype(str).str.strip() != '']

# Create contingency table: rows = histological_type, columns = mutated (True/False)
ct = pd.crosstab(df_clin['histological_type'], df_clin['CDH1_mutated'])
# Ensure both True and False columns exist
for col in [False, True]:
    if col not in ct.columns:
        ct[col] = 0
ct = ct[[True, False]] if True in ct.columns else ct[[False, True]]

# Exclude categories (histological types) with marginal totals <= 10
row_totals = ct.sum(axis=1)
ct_filtered = ct[row_totals > 10].copy()

# If after filtering there are less than 2 rows or columns, chi-square cannot be computed
result = {}
if ct_filtered.shape[0] < 2 or ct_filtered.sum().min() == 0:
    result = {
        'error': 'Not enough data after filtering to compute chi-square (need at least 2 histological categories with totals > 10 and non-zero margins).',
        'n_histological_categories_before_filter': int(ct.shape[0]),
        'n_histological_categories_after_filter': int(ct_filtered.shape[0])
    }
else:
    # Observed matrix with columns [True (mutated), False (not mutated)]
    obs = ct_filtered.values.astype(float)
    N = obs.sum()
    row_sums = obs.sum(axis=1, keepdims=True)
    col_sums = obs.sum(axis=0, keepdims=True)
    expected = row_sums.dot(col_sums) / N
    # Avoid division by zero; only sum where expected>0
    mask = expected > 0
    chi2 = float(((obs - expected) ** 2 / expected)[mask].sum())
    dof = (obs.shape[0] - 1) * (obs.shape[1] - 1)

    # Build contingency dict
    cont_dict = {}
    for i, idx in enumerate(ct_filtered.index.tolist()):
        cont_dict[idx] = {
            'mutated': int(ct_filtered.iloc[i][True]) if True in ct_filtered.columns else 0,
            'not_mutated': int(ct_filtered.iloc[i][False]) if False in ct_filtered.columns else 0,
            'row_total': int(ct_filtered.iloc[i].sum())
        }

    result = {
        'chi2': chi2,
        'degrees_of_freedom': int(dof),
        'grand_total': int(N),
        'n_histological_categories_before_filter': int(ct.shape[0]),
        'n_histological_categories_after_filter': int(ct_filtered.shape[0]),
        'contingency_table': cont_dict
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DoRJOr1yjGy5vR1w2N7lDYRN': ['clinical_info'], 'var_call_RsK0kspAyb9xPADrrGy2oLbC': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_15Xklp0CoPoht4pM5I5NHAly': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_bzcmXAMGAvKtEyd0PSJTWD0x': 'file_storage/call_bzcmXAMGAvKtEyd0PSJTWD0x.json', 'var_call_SV0N6eNxjV00fEAKIRR9UWRD': 'file_storage/call_SV0N6eNxjV00fEAKIRR9UWRD.json', 'var_call_J6FJbgdvx1FcYy5ciFfyl2nS': 'file_storage/call_J6FJbgdvx1FcYy5ciFfyl2nS.json', 'var_call_KjCUekhiMFJqxCy1fE4kgEGL': 'file_storage/call_KjCUekhiMFJqxCy1fE4kgEGL.json'}

exec(code, env_args)
