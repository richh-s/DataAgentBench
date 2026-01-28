code = """import json
import pandas as pd
import re

# Load previous tool results from storage (file paths)
with open(var_call_pdZrRgz1vAX96qWuFXg8OrkR, 'r') as f:
    clinical = json.load(f)
with open(var_call_s3RcIl25SeiTzFSdKIu6T4Zm, 'r') as f:
    mutations = json.load(f)

# Create dataframes
clin_df = pd.DataFrame(clinical)
mut_df = pd.DataFrame(mutations)

# Filter clinical to female breast patients
clin_df['Patient_description'] = clin_df['Patient_description'].astype(str)
clin_df['tumor_tissue_site'] = clin_df['tumor_tissue_site'].astype(str)
clin_df_female = clin_df[clin_df['Patient_description'].str.contains('FEMALE', case=False, na=False) & clin_df['tumor_tissue_site'].str.contains('breast', case=False, na=False)].copy()

# Extract ParticipantBarcode from Patient_description
def extract_barcode(text):
    m = re.search(r'(TCGA[-A-Z0-9]+)', text)
    return m.group(1) if m else None

clin_df_female['ParticipantBarcode'] = clin_df_female['Patient_description'].apply(extract_barcode)

# Keep only entries with known histological_type
clin_df_female['histological_type'] = clin_df_female['histological_type'].astype(str).str.strip()
known_mask = clin_df_female['histological_type'].notna() & (clin_df_female['histological_type'] != '') & (~clin_df_female['histological_type'].str.lower().isin(['none','not reported','unknown','nan']))
clin_df_female = clin_df_female[known_mask].copy()

# Prepare mutation presence: only reliable entries (FILTER == 'PASS')
mut_df_pass = mut_df[mut_df['FILTER'] == 'PASS'].copy()
# Ensure ParticipantBarcode column exists as string
mut_df_pass['ParticipantBarcode'] = mut_df_pass['ParticipantBarcode'].astype(str)
mutated_set = set(mut_df_pass['ParticipantBarcode'].unique())

# Mark mutation presence in clinical data
clin_df_female['CDH1_mutated'] = clin_df_female['ParticipantBarcode'].apply(lambda x: x in mutated_set)

# Build contingency table
ct = pd.crosstab(clin_df_female['histological_type'], clin_df_female['CDH1_mutated']).rename(columns={False: 'No', True: 'Yes'})

# Drop histological categories with marginal totals <= 10 (row totals)
row_totals = ct.sum(axis=1)
keep_rows = row_totals > 10
ct2 = ct.loc[keep_rows].copy()
rows_dropped = int((~keep_rows).sum())

# Drop columns with marginal totals <= 10 (column totals)
col_totals = ct2.sum(axis=0)
keep_cols = col_totals > 10
ct3 = ct2.loc[:, keep_cols].copy()
cols_dropped = int((~keep_cols).sum())

# If after dropping we have insufficient table, return message
if ct3.shape[0] < 2 or ct3.shape[1] < 2:
    result = {
        'message': 'Insufficient data after excluding categories with marginal totals <= 10 to compute chi-square.',
        'initial_total_patients': int(len(clin_df_female)),
        'rows_dropped': rows_dropped,
        'cols_dropped': cols_dropped,
        'contingency_table_after_filtering': ct3.to_dict()
    }
else:
    obs = ct3.values.astype(float)
    grand_total = obs.sum()
    row_sums = obs.sum(axis=1).reshape(-1,1)
    col_sums = obs.sum(axis=0).reshape(1,-1)
    expected = (row_sums @ col_sums) / grand_total
    # Compute chi2, handling zeros in expected by ignoring those terms
    mask = expected > 0
    chi2 = float(((obs - expected)**2 / expected)[mask].sum())
    result = {
        'chi2': chi2,
        'grand_total': int(grand_total),
        'contingency_table': ct3.to_dict(),
        'expected_table': pd.DataFrame(expected, index=ct3.index, columns=ct3.columns).to_dict(),
        'rows_dropped': rows_dropped,
        'cols_dropped': cols_dropped,
        'included_histological_types': list(ct3.index.astype(str))
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_aaS4vUjQL7a5hLecfWRnlJGp': ['clinical_info'], 'var_call_6GXo3WbD5mjQIMdb1UvZXs2C': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_z3EUu6x1DAXTUEk1JjK8jpvv': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_UR4g05dlP8k96vvdOqOu8xH9': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'None'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_call_okLPOxiEAoaUTiZBX9kxFYjE': [], 'var_call_s3RcIl25SeiTzFSdKIu6T4Zm': 'file_storage/call_s3RcIl25SeiTzFSdKIu6T4Zm.json', 'var_call_pdZrRgz1vAX96qWuFXg8OrkR': 'file_storage/call_pdZrRgz1vAX96qWuFXg8OrkR.json'}

exec(code, env_args)
