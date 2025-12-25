code = """import pandas as pd
import re

# Load the full data from the file for clinical_info
with open(locals()['var_function-call-6382127827338163103'], 'r') as f:
    clinical_data = pd.read_json(f)

# Filter for female BRCA patients with known histological types (this filtering was already done in the query)
# Now we just need to extract the ParticipantBarcode from the Patient_description
fem_brca_patients = clinical_data.copy()

fem_brca_patients['ParticipantBarcode'] = fem_brca_patients['Patient_description'].apply(
    lambda x: re.search(r'TCGA-([\w-]+)', x).group(0) if re.search(r'TCGA-([\w-]+)', x) else None
)

# Remove rows where ParticipantBarcode could not be extracted or histological_type is null
fem_brca_patients = fem_brca_patients.dropna(subset=['ParticipantBarcode', 'histological_type'])

# Select relevant columns and remove duplicates based on ParticipantBarcode to ensure unique patient entries
fem_brca_patients = fem_brca_patients[['ParticipantBarcode', 'histological_type']].drop_duplicates(subset=['ParticipantBarcode'])

# Load the mutation data for CDH1 with PASS filter
with open(locals()['var_function-call-15923151208779991952'], 'r') as f:
    mutation_data_raw = pd.read_json(f)

cdh1_mutations = mutation_data_raw.copy()
cdh1_mutations = cdh1_mutations[cdh1_mutations['Hugo_Symbol'] == 'CDH1']
cdh1_mutations = cdh1_mutations[cdh1_mutations['FILTER'] == 'PASS']

# Create a set of ParticipantBarcodes with CDH1 mutations
cdh1_mutated_patients = set(cdh1_mutations['ParticipantBarcode'].unique())

# Add a 'CDH1_Mutated' column to fem_brca_patients dataframe
fem_brca_patients['CDH1_Mutated'] = fem_brca_patients['ParticipantBarcode'].apply(
    lambda x: 'Yes' if x in cdh1_mutated_patients else 'No'
)

# Create a contingency table
contingency_table = pd.crosstab(
    fem_brca_patients['histological_type'],
    fem_brca_patients['CDH1_Mutated']
)

# Ensure both 'Yes' and 'No' columns exist, fill with 0 if not
if 'Yes' not in contingency_table.columns:
    contingency_table['Yes'] = 0
if 'No' not in contingency_table.columns:
    contingency_table['No'] = 0

# Filter out rows with marginal totals <= 10
contingency_table = contingency_table[
    (contingency_table.sum(axis=1) > 10)
].copy()

# Filter out columns with marginal totals <= 10 (this is for 'Yes' and 'No' groups)
# If either 'Yes' or 'No' column total is <= 10, that group is excluded.
# Since we are interested in the association between histological type and CDH1 mutation,
# we should keep both 'Yes' and 'No' columns as long as they contribute to the overall chi-square.
# The filtering condition for column totals should be applied at the same level as row totals.
# For a 2xN table, if a column total is <= 10, it means either 'Yes' or 'No' counts are low.
# We will only remove histological types if their *row total* is <= 10, as specified.
# If after row filtering, a column becomes all zeros, it will be handled by chi-square calculation.

# Calculate expected frequencies
row_totals = contingency_table.sum(axis=1)
col_totals = contingency_table.sum(axis=0)
grand_total = contingency_table.sum().sum()

expected_frequencies = pd.DataFrame(
    [[(
        (row_totals.loc[r] * col_totals.loc[c]) / grand_total
    ) for c in contingency_table.columns] for r in contingency_table.index],
    index=contingency_table.index,
    columns=contingency_table.columns
)

# Calculate chi-square statistic
# Avoid division by zero for expected frequencies that are 0
chi_square_statistic = ((contingency_table - expected_frequencies)**2 / expected_frequencies.replace(0, 1e-9)).sum().sum()

print("__RESULT__:")
print(pd.Series({
    'chi_square_statistic': chi_square_statistic,
    'contingency_table': contingency_table.to_dict(orient='index'),
    'expected_frequencies': expected_frequencies.to_dict(orient='index')
}).to_json())"""

env_args = {'var_function-call-10610325522388191519': ['clinical_info'], 'var_function-call-685300227974147815': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-9704739870392990070': [], 'var_function-call-4824634680027645265': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'var_function-call-16929134511802878209': [], 'var_function-call-4926675373636284248': 'file_storage/function-call-4926675373636284248.json', 'var_function-call-16069711497695978885': [], 'var_function-call-11978866167004671161': [{'tumor_tissue_site': 'Chest - Breast'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal'}, {'tumor_tissue_site': 'Superficial Trunk - Back'}, {'tumor_tissue_site': 'Chest - Chest wall'}, {'tumor_tissue_site': 'Choroid|Ciliary body|Iris'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Rectum'}, {'tumor_tissue_site': 'Chest - Mediastinum'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Other (please specify'}, {'tumor_tissue_site': 'Esophagus'}, {'tumor_tissue_site': 'Extra-adrenal Site'}, {'tumor_tissue_site': 'Omentum'}, {'tumor_tissue_site': 'Endometrial'}, {'tumor_tissue_site': 'Chest - Other (please specify'}, {'tumor_tissue_site': 'Chest - Lung/pleura'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum'}, {'tumor_tissue_site': 'Gynecological - Uterus'}, {'tumor_tissue_site': 'Colon'}, {'tumor_tissue_site': 'None'}, {'tumor_tissue_site': 'Lung'}, {'tumor_tissue_site': 'Choroid|Ciliary body'}, {'tumor_tissue_site': 'Upper Extremity - Upper arm/elbow'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney|Retroperitoneum/Upper abdominal - Liver|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Other  Specify'}, {'tumor_tissue_site': 'Head and Neck - Neck|Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Gynecological - Ovary'}, {'tumor_tissue_site': 'Lower Extremity - Lower leg/calf'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Other (please specify'}, {'tumor_tissue_site': 'Uterus'}, {'tumor_tissue_site': 'Extremities'}, {'tumor_tissue_site': 'Thyroid'}, {'tumor_tissue_site': 'Cervical'}, {'tumor_tissue_site': 'Choroid'}, {'tumor_tissue_site': 'Ovary'}, {'tumor_tissue_site': 'Upper Extremity - Shoulder/axilla'}, {'tumor_tissue_site': 'Peritoneum ovary'}, {'tumor_tissue_site': 'Stomach'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Bladder'}, {'tumor_tissue_site': 'Head and Neck - Head'}, {'tumor_tissue_site': 'Kidney'}, {'tumor_tissue_site': 'Head and Neck'}, {'tumor_tissue_site': 'Lower Extremity - Other (please specify'}, {'tumor_tissue_site': 'Pancreas'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Pelvic|Gynecological - Uterus'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Intraabdominal|Lower abdominal/Pelvic - Pelvic'}, {'tumor_tissue_site': 'Extremities|Extremities'}, {'tumor_tissue_site': 'Pleura'}, {'tumor_tissue_site': 'Brain'}, {'tumor_tissue_site': 'Anterior Mediastinum'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Colon'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Gastric'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Kidney'}, {'tumor_tissue_site': 'Testes'}, {'tumor_tissue_site': 'Trunk'}, {'tumor_tissue_site': 'Breast'}, {'tumor_tissue_site': 'Extremities|Trunk'}, {'tumor_tissue_site': 'Prostate'}, {'tumor_tissue_site': 'Lower abdominal/Pelvic - Spermatic Cord'}, {'tumor_tissue_site': 'Head and Neck - Other (please specify'}, {'tumor_tissue_site': 'Head and Neck - Head|Chest - Chest wall'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Pancreas'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee'}, {'tumor_tissue_site': 'Trunk|[Not Available]'}, {'tumor_tissue_site': 'Central nervous system'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Small Intestines'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Intraabdominal|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Adrenal gland'}, {'tumor_tissue_site': 'Bile duct'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Small Intestines|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum|Retroperitoneum/Upper abdominal - Other (please specify'}, {'tumor_tissue_site': 'Superficial Trunk - Buttock'}, {'tumor_tissue_site': 'Lower Extremity - Groin'}, {'tumor_tissue_site': 'Liver'}, {'tumor_tissue_site': 'Trunk|Extremities'}, {'tumor_tissue_site': 'Adrenal'}, {'tumor_tissue_site': 'Bladder'}, {'tumor_tissue_site': 'Thymus'}, {'tumor_tissue_site': '[Unknown]'}, {'tumor_tissue_site': 'Gynecological - Uterus|Gynecological - Cervix'}, {'tumor_tissue_site': 'Superficial Trunk - Abdominal wall'}, {'tumor_tissue_site': 'Superficial Trunk - Flank'}, {'tumor_tissue_site': 'Lower Extremity - Foot/ankle'}], 'var_function-call-6382127827338163103': 'file_storage/function-call-6382127827338163103.json', 'var_function-call-15923151208779991952': 'file_storage/function-call-15923151208779991952.json'}

exec(code, env_args)
