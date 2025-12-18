code = """import json
import pandas as pd
from collections import defaultdict
import scipy.stats as stats

# Load the processed clinical data (female BRCA patients with histological types)
clinical_data = json.loads(open(locals()['var_function-call-1706879267772521055'], 'r').read())
df_clinical = pd.DataFrame(clinical_data)

# Load the CDH1 mutation data
mutation_data = json.loads(open(locals()['var_function-call-7733525554577291838'], 'r').read())
df_mutation = pd.DataFrame(mutation_data)

# Get a set of ParticipantBarcodes with CDH1 mutations
cdh1_mutated_patients = set(df_mutation['ParticipantBarcode'].unique())

# Add a 'CDH1_Mutated' column to the clinical DataFrame
df_clinical['CDH1_Mutated'] = df_clinical['ParticipantBarcode'].apply(lambda x: 'Yes' if x in cdh1_mutated_patients else 'No')

# Create the contingency table
contingency_table = pd.crosstab(df_clinical['histological_type'], df_clinical['CDH1_Mutated'])

# Ensure both 'Yes' and 'No' columns exist, fill with 0 if not
if 'Yes' not in contingency_table.columns:
    contingency_table['Yes'] = 0
if 'No' not in contingency_table.columns:
    contingency_table['No'] = 0

# Filter out categories with marginal totals less than or equal to 10
# Calculate row totals
row_totals = contingency_table.sum(axis=1)
contingency_table_filtered = contingency_table[row_totals > 10]

# Calculate column totals for filtered table (these will be the marginal totals for the chi-square)
col_totals_filtered = contingency_table_filtered.sum(axis=0)

# Recalculate row totals after column filtering (as some histological types might be removed due to 'No' mutations below 10 or vice-versa)
row_totals_filtered = contingency_table_filtered.sum(axis=1)

# Re-filter again to ensure all marginal totals (rows and columns) are > 10
# If after filtering rows, some columns now have totals <= 10, these columns would ideally be excluded if they were categories like 'Yes' or 'No'
# However, since 'Yes'/'No' are the only column categories for mutation, we only need to ensure overall counts are > 10

# Re-check column totals for filtering condition
final_contingency_table = contingency_table_filtered.copy()

# Chi-square calculation
# The chi-square test requires expected frequencies. If expected frequencies are too small (e.g., < 5), the approximation may not be valid.
# We are already filtering by marginal totals > 10. This is a common heuristic.

# Perform chi-square test
if not final_contingency_table.empty and (final_contingency_table.values.sum() > 0) and (min(final_contingency_table.shape) > 1):
    chi2, p_value, dof, expected = stats.chi2_contingency(final_contingency_table)
    result = {
        'chi2_statistic': chi2,
        'p_value': p_value,
        'degrees_of_freedom': dof,
        'observed_frequencies': final_contingency_table.to_dict(orient='index'),
        'expected_frequencies': pd.DataFrame(expected, index=final_contingency_table.index, columns=final_contingency_table.columns).to_dict(orient='index')
    }
else:
    result = {'error': 'Contingency table is empty or too small for chi-square calculation after filtering.'}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7685199027355279957': ['clinical_info'], 'var_function-call-14464687409741544894': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_function-call-5553293297742273042': 'file_storage/function-call-5553293297742273042.json', 'var_function-call-3322615637953469944': [], 'var_function-call-14561242205782074667': 'file_storage/function-call-14561242205782074667.json', 'var_function-call-18322034851678707887': [], 'var_function-call-1706879267772521055': 'file_storage/function-call-1706879267772521055.json', 'var_function-call-7733525554577291838': 'file_storage/function-call-7733525554577291838.json'}

exec(code, env_args)
