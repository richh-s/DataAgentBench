code = """import pandas as pd
import json

# Load clinical data for female BRCA patients with known histological types
with open(locals()['var_function-call-1818329998380457615'], 'r') as f:
    df_brca_female = pd.DataFrame(json.load(f))

# Load CDH1 mutation data
with open(locals()['var_function-call-602958096687681950'], 'r') as f:
    df_cdh1_mutation = pd.DataFrame(json.load(f))

# Extract ParticipantBarcode from the clinical data if it's not in the correct format
df_brca_female['ParticipantBarcode'] = df_brca_female['ParticipantBarcode'].apply(lambda x: x if x.startswith('TCGA-') else 'TCGA-' + x)

# Create a set of ParticipantBarcodes with CDH1 mutations
cdh1_mutated_patients = set(df_cdh1_mutation['ParticipantBarcode'].unique())

# Add a 'CDH1_Mutated' column to the clinical data
df_brca_female['CDH1_Mutated'] = df_brca_female['ParticipantBarcode'].apply(lambda x: 'Yes' if x in cdh1_mutated_patients else 'No')

# Create a contingency table
contingency_table = pd.crosstab(df_brca_female['histological_type'], df_brca_female['CDH1_Mutated'])

# Exclude categories with marginal totals less than or equal to 10
original_contingency_table = contingency_table.copy()
row_totals = original_contingency_table.sum(axis=1)
col_totals = original_contingency_table.sum(axis=0)

# Filter rows where row_total <= 10
contingency_table = contingency_table[row_totals > 10]
# Filter columns where col_total <= 10, considering the updated column totals after row filtering
col_totals_after_row_filter = contingency_table.sum(axis=0)
contingency_table = contingency_table.loc[:, col_totals_after_row_filter > 10]

# Calculate chi-square statistic manually
chi2_statistic = 0
if not contingency_table.empty and (contingency_table.shape[0] > 1 or contingency_table.shape[1] > 1):
    grand_total = contingency_table.sum().sum()
    if grand_total > 0:
        for i in range(contingency_table.shape[0]):
            for j in range(contingency_table.shape[1]):
                observed_value = contingency_table.iloc[i, j]
                row_total = contingency_table.iloc[i, :].sum()
                col_total = contingency_table.iloc[:, j].sum()
                
                if row_total > 0 and col_total > 0 and grand_total > 0: # Ensure no division by zero
                    expected_value = (row_total * col_total) / grand_total
                    if expected_value > 0: # Avoid division by zero in the chi-square formula
                        chi2_statistic += ((observed_value - expected_value) ** 2) / expected_value

result = {
    'chi2_statistic': chi2_statistic,
    'p_value': 'Cannot be calculated without scipy',
    'degrees_of_freedom': 'Cannot be calculated without scipy',
    'contingency_table_filtered': contingency_table.to_dict(orient='index')
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7609636765276631308': ['clinical_info'], 'var_function-call-6954646914502994805': ['clinical_info'], 'var_function-call-9308148816593779667': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-18154499326552069552': [], 'var_function-call-2176793223485392742': [], 'var_function-call-12993911544105620596': 'file_storage/function-call-12993911544105620596.json', 'var_function-call-1818329998380457615': 'file_storage/function-call-1818329998380457615.json', 'var_function-call-602958096687681950': 'file_storage/function-call-602958096687681950.json'}

exec(code, env_args)
