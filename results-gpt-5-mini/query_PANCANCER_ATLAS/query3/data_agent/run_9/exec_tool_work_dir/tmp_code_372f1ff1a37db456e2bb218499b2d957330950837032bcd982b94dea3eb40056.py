code = """import json
import pandas as pd
import math

# Load data from storage file paths
with open(var_call_17Gybx9xV7ztk6k2Zb3YDcYT, 'r') as f:
    clinical = json.load(f)
with open(var_call_qgX7HsqmqZ01KH68it25uYKR, 'r') as f:
    mutations = json.load(f)

# Create DataFrames
cli_df = pd.DataFrame(clinical)
mut_df = pd.DataFrame(mutations)

# Standardize column names in clinical df
if 'participantbarcode' in cli_df.columns:
    cli_df['ParticipantBarcode'] = cli_df['participantbarcode']

# Keep only patients with known histological_type
cli_df = cli_df[cli_df['histological_type'].notnull() & (cli_df['histological_type'] != '')].copy()

# Unique patients (in case of duplicates)
cli_df = cli_df.drop_duplicates(subset=['ParticipantBarcode'])

# Determine mutated participants (CDH1 PASS already filtered in query)
mut_participants = set(mut_df['ParticipantBarcode'].dropna().unique())

# Keep only clinical patients that are female BRCA as queried
cli_df['Mutated'] = cli_df['ParticipantBarcode'].apply(lambda x: x in mut_participants)

# Build contingency table: rows histological_type, columns Mutated True/False
cont = pd.crosstab(cli_df['histological_type'], cli_df['Mutated'])
cont = cont.rename(columns={False: 'Not_Mutated', True: 'Mutated'})

# Compute marginal totals
cont['RowTotal'] = cont.sum(axis=1)
col_totals = cont[['Not_Mutated','Mutated']].sum()

# Exclude categories with marginal totals <= 10 (rows or columns)
# Drop rows with RowTotal <= 10
cont_filtered = cont[cont['RowTotal'] > 10].copy()
# Drop columns with col_total <= 10
cols_to_keep = [c for c in ['Not_Mutated','Mutated'] if col_totals.get(c,0) > 10]
cont_final = cont_filtered[cols_to_keep].copy()

# Recompute totals
row_totals = cont_final.sum(axis=1)
col_totals_final = cont_final.sum(axis=0)
grand_total = col_totals_final.sum()

result = {}
if cont_final.empty or grand_total == 0 or len(col_totals_final) < 2:
    result['error'] = 'Not enough data after applying marginal total > 10 filter to compute chi-square.'
    result['rows_remaining'] = cont_filtered.shape[0]
    result['columns_remaining'] = len(cols_to_keep)
else:
    # Observed matrix
    observed = cont_final.values.astype(float)
    # Expected matrix
    expected = (row_totals.values.reshape(-1,1) * col_totals_final.values.reshape(1,-1)) / grand_total
    # Chi-square statistic
    chi2 = float(((observed - expected)**2 / expected).sum())
    df = (observed.shape[0]-1) * (observed.shape[1]-1)

    # Prepare contingency table dict
    contingency_dict = {}
    for i, row in enumerate(cont_final.index.tolist()):
        row_dict = {}
        for j, col in enumerate(cont_final.columns.tolist()):
            row_dict[col] = int(observed[i,j])
        contingency_dict[row] = row_dict

    # Expected values dict
    expected_dict = {}
    for i, row in enumerate(cont_final.index.tolist()):
        row_dict = {}
        for j, col in enumerate(cont_final.columns.tolist()):
            row_dict[col] = float(expected[i,j])
        expected_dict[row] = row_dict

    result['chi2'] = chi2
    result['degrees_of_freedom'] = int(df)
    result['grand_total'] = int(grand_total)
    result['contingency_table'] = contingency_dict
    result['expected_table'] = expected_dict
    result['rows_included'] = cont_final.shape[0]
    result['columns_included'] = cont_final.shape[1]

# Output as JSON string
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_I7yg1EcfdcCclKBj9ZMq0pXT': ['clinical_info'], 'var_call_c7hvApErh5A3JcizjsAykeby': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_GX2rSWN3BAaSmJQEgl5PutgT': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_dWP0DCtcd2rX2xfKX5rpkxHT': [], 'var_call_54zICc9bR5OJF3r4Qcngk5rP': 'file_storage/call_54zICc9bR5OJF3r4Qcngk5rP.json', 'var_call_qgX7HsqmqZ01KH68it25uYKR': 'file_storage/call_qgX7HsqmqZ01KH68it25uYKR.json', 'var_call_17Gybx9xV7ztk6k2Zb3YDcYT': 'file_storage/call_17Gybx9xV7ztk6k2Zb3YDcYT.json'}

exec(code, env_args)
