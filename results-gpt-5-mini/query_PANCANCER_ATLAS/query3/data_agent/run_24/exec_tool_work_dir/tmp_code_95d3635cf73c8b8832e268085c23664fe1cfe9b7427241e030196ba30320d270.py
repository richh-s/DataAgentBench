code = """import json
import re
import pandas as pd

# Load data from storage variables (they may be file paths if large)
clinical_key = var_call_spCEGh9pTe256nADB4blw3NY
mutation_key = var_call_v2YtiC8nH4O8JzVZ0zGWt9NA

def load_var(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

clinical = load_var(clinical_key)
mutations = load_var(mutation_key)

# Convert to DataFrame
clin_df = pd.DataFrame(clinical)
mut_df = pd.DataFrame(mutations)

# Extract TCGA barcode from Patient_description
barcode_re = re.compile(r'(TCGA[-A-Za-z0-9]+)', re.IGNORECASE)

def extract_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = barcode_re.search(desc)
    return m.group(1).upper() if m else None

clin_df['barcode'] = clin_df['Patient_description'].apply(extract_barcode)

# Filter female patients only and with a barcode
clin_df = clin_df[clin_df['Patient_description'].str.contains('FEMALE', case=False, na=False)]
clin_df = clin_df[clin_df['barcode'].notnull()].copy()

# Deduplicate by barcode keeping first
clin_df = clin_df.drop_duplicates(subset=['barcode'])

# Build set of mutated barcodes from mutation data (PASS only already)
mut_df['ParticipantBarcode'] = mut_df['ParticipantBarcode'].str.upper()
mutated_set = set(mut_df['ParticipantBarcode'].dropna().unique())

# For each clinical patient determine mutation presence
clin_df['mutated'] = clin_df['barcode'].apply(lambda b: b in mutated_set)

# Build contingency table: histological_type x mutated(True/False)
cont_table = clin_df.pivot_table(index='histological_type', columns='mutated', values='barcode', aggfunc='count', fill_value=0)
# Ensure both True and False columns exist
for col in [False, True]:
    if col not in cont_table.columns:
        cont_table[col] = 0
cont_table = cont_table[[True, False]]  # order: mutated, not mutated
cont_table.columns = ['mutated', 'not_mutated']

# Exclude histological categories with marginal totals <= 10 (row totals)
cont_table['row_total'] = cont_table['mutated'] + cont_table['not_mutated']
filtered_table = cont_table[cont_table['row_total'] > 10].drop(columns=['row_total'])

# If after filtering there are fewer than 2 rows or one of the columns has zero total, chi-square not defined
result = {}
if filtered_table.shape[0] < 1 or filtered_table[['mutated','not_mutated']].sum().min() == 0:
    result['error'] = 'Not enough data after filtering to compute chi-square.'
    result['included_histological_types'] = int(filtered_table.shape[0])
    out = json.dumps(result)
    print("__RESULT__:")
    print(out)
else:
    # Compute chi-square statistic
    obs = filtered_table[['mutated','not_mutated']].astype(float)
    row_totals = obs.sum(axis=1)
    col_totals = obs.sum(axis=0)
    grand_total = col_totals.sum()
    expected = pd.DataFrame(index=obs.index, columns=obs.columns, dtype=float)
    chi2 = 0.0
    for r in obs.index:
        for c in obs.columns:
            E = (row_totals.loc[r] * col_totals.loc[c]) / grand_total
            O = obs.loc[r, c]
            if E > 0:
                chi2 += (O - E) ** 2 / E
    # Prepare output
    table_out = {r: {'mutated': int(obs.loc[r,'mutated']), 'not_mutated': int(obs.loc[r,'not_mutated'])} for r in obs.index}
    result['chi2'] = chi2
    result['included_histological_types'] = int(obs.shape[0])
    result['contingency_table'] = table_out
    out = json.dumps(result)
    print("__RESULT__:")
    print(out)"""

env_args = {'var_call_LezJA4Cs5rCxfZn1WQgXC95R': ['clinical_info'], 'var_call_jCAiuLhbXp01mWuX97bgS9Vc': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_iHcUbCsEwYHCtmDCBTMclLH7': 'file_storage/call_iHcUbCsEwYHCtmDCBTMclLH7.json', 'var_call_Jh8hgpdCCtTFIlO2bR3YApjB': [{'tumor_tissue_site': 'Breast'}], 'var_call_spCEGh9pTe256nADB4blw3NY': 'file_storage/call_spCEGh9pTe256nADB4blw3NY.json', 'var_call_v2YtiC8nH4O8JzVZ0zGWt9NA': 'file_storage/call_v2YtiC8nH4O8JzVZ0zGWt9NA.json'}

exec(code, env_args)
