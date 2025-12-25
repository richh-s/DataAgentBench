code = """import json
import pandas as pd
import numpy as np

# Load clinical data
clinical_data_raw = json.load(open(locals()['var_function-call-14786415575251320296']))

# Extract ParticipantBarcode and histological_type from clinical data
clinical_patients = []
for entry in clinical_data_raw:
    description = entry["Patient_description"]
    barcode_start = description.find("TCGA-")
    if barcode_start != -1:
        participant_barcode = description[barcode_start : barcode_start + 12]
        clinical_patients.append({
            "ParticipantBarcode": participant_barcode,
            "histological_type": entry["histological_type"]
        })
clinical_df = pd.DataFrame(clinical_patients)

# Filter for unique patient barcodes (already done, but ensuring here again for clean dataframe)
patient_barcodes_list = json.load(open(locals()['var_function-call-3444562512994196272']))
clinical_df = clinical_df[clinical_df['ParticipantBarcode'].isin(patient_barcodes_list)]

# Load mutation data
mutation_data_raw = json.load(open(locals()['var_function-call-13309788191453516904']))

# Get set of patients with CDH1 mutations
cdh1_mutation_barcodes = set([entry["ParticipantBarcode"] for entry in mutation_data_raw])

# Add 'has_CDH1_mutation' column to clinical_df
clinical_df['has_CDH1_mutation'] = clinical_df['ParticipantBarcode'].apply(lambda x: 'Yes' if x in cdh1_mutation_barcodes else 'No')

# Create contingency table
contingency_table = pd.crosstab(clinical_df['histological_type'], clinical_df['has_CDH1_mutation'])

# Filter out categories with marginal totals <= 10
# Row totals
row_totals = contingency_table.sum(axis=1)
contingency_table_filtered_rows = contingency_table[row_totals > 10]

# Column totals (recalculate after row filtering)
col_totals = contingency_table_filtered_rows.sum(axis=0)
contingency_table_filtered = contingency_table_filtered_rows.loc[:, col_totals > 10]

# Ensure the table is not empty after filtering
if contingency_table_filtered.empty or contingency_table_filtered.shape[0] < 2 or contingency_table_filtered.shape[1] < 2:
    print("__RESULT__:")
    print(json.dumps("Not enough data after filtering to perform chi-square test."))
else:
    # Manual Chi-square calculation
    observed_values = contingency_table_filtered.values
    
    row_sums = observed_values.sum(axis=1)
    col_sums = observed_values.sum(axis=0)
    grand_total = observed_values.sum()

    expected_values = np.outer(row_sums, col_sums) / grand_total

    # Calculate chi-square statistic
    chi_square_statistic = np.sum((observed_values - expected_values)**2 / expected_values)

    print("__RESULT__:")
    print(json.dumps(chi_square_statistic))"""

env_args = {'var_function-call-13129883693595191659': ['clinical_info'], 'var_function-call-150481197693506109': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-14786415575251320296': 'file_storage/function-call-14786415575251320296.json', 'var_function-call-3444562512994196272': 'file_storage/function-call-3444562512994196272.json', 'var_function-call-13309788191453516904': 'file_storage/function-call-13309788191453516904.json'}

exec(code, env_args)
