code = """import pandas as pd
import json
import re
from scipy.stats import chi2_contingency

# Load data
# keys:
# bladder: var_function-call-7680100113290464292
# breast: var_function-call-17554851907966980650
# mutations: var_function-call-3690300690266598589

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

bladder_data = load_json(locals()['var_function-call-7680100113290464292'])
breast_data = load_json(locals()['var_function-call-17554851907966980650'])
mutation_data = load_json(locals()['var_function-call-3690300690266598589'])

# Helper to extract barcode and create DF
def process_clinical(data):
    rows = []
    for entry in data:
        desc = entry.get('Patient_description', '')
        hist = entry.get('histological_type', '')
        # Extract TCGA barcode
        match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
        if match:
            barcode = match.group(0)
            rows.append({'ParticipantBarcode': barcode, 'histological_type': hist})
    return pd.DataFrame(rows)

df_bladder = process_clinical(bladder_data)
df_breast = process_clinical(breast_data)

# Check histological types in Bladder
bladder_types = df_bladder['histological_type'].nunique()
print(f"Bladder unique types: {bladder_types}")
print(f"Bladder types: {df_bladder['histological_type'].unique()}")

# Check histological types in Breast
breast_types = df_breast['histological_type'].nunique()
print(f"Breast unique types: {breast_types}")
print(f"Breast types: {df_breast['histological_type'].unique()}")

# Decide cohort
# If Bladder has > 1 type and reasonable distribution, use it (per hint).
# Else use Breast.
if bladder_types > 1:
    df_clinical = df_bladder
    cohort = "Bladder"
else:
    df_clinical = df_breast
    cohort = "Breast"

print(f"Selected Cohort: {cohort}")

# Process mutations
# Mutation data contains CDH1 mutations with FILTER=PASS
mut_df = pd.DataFrame(mutation_data)
# Get set of mutated barcodes
mutated_barcodes = set(mut_df['ParticipantBarcode'].unique())

# Assign status
df_clinical['CDH1_Status'] = df_clinical['ParticipantBarcode'].apply(lambda x: 'Mutated' if x in mutated_barcodes else 'WT')

# Create Contingency Table
crosstab = pd.crosstab(df_clinical['histological_type'], df_clinical['CDH1_Status'])

# Filter marginals <= 10
# We need to remove rows/cols where sum <= 10? 
# "excluding categories with marginal totals less than or equal to 10"
# Usually means excluding Histological Types (rows) with <= 10 patients total, 
# or Mutation Status (cols) with <= 10 patients (unlikely for WT).
# Let's filter rows (hist types) with total count <= 10.
# And also columns if any (though Mutation status has 2 cols).

# Filter rows
row_sums = crosstab.sum(axis=1)
crosstab_filtered = crosstab.loc[row_sums > 10]

# Filter cols (just in case, e.g. no mutations found)
col_sums = crosstab_filtered.sum(axis=0)
crosstab_filtered = crosstab_filtered.loc[:, col_sums > 10]

print("Contingency Table:")
print(crosstab_filtered)

# Calculate Chi-square
if crosstab_filtered.shape[0] < 2 or crosstab_filtered.shape[1] < 2:
    result = "Not enough data for Chi-square"
else:
    chi2, p, dof, ex = chi2_contingency(crosstab_filtered)
    result = chi2

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5810139052163137877': ['clinical_info'], 'var_function-call-18314453340741473054': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-5882646802725146008': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_function-call-3196614121774816647': 'file_storage/function-call-3196614121774816647.json', 'var_function-call-8773118855581621867': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_function-call-10947642004532660868': [{'Patient_description': 'Patient TCGA-BT-A20V (FEMALE, UUID 24f21425-b001-4986-aedf-5b4dd851c6ad) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Case A648D9BF-CF37-41FC-9515-E8F5AC85FCD4, linked to barcode TCGA-XF-A9SX, corresponds to a FEMALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Record 234086DD-5A74-4FF1-94AB-BAD43EE69D5C refers to patient TCGA-DK-A2I2, a FEMALE diagnosed with Bladder urothelial carcinoma. Vital status recorded as Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-XF-A8HH (UUID 02964D82-CC94-4286-A66F-03567101950C) is recorded as a FEMALE with vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'The individual with barcode TCGA-ZF-A9R7 and UUID CE4E4549-BEFC-447F-9B79-ED46E302E6D7 is a FEMALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}], 'var_function-call-18090152291096884407': [], 'var_function-call-7680100113290464292': 'file_storage/function-call-7680100113290464292.json', 'var_function-call-3690300690266598589': 'file_storage/function-call-3690300690266598589.json', 'var_function-call-17554851907966980650': 'file_storage/function-call-17554851907966980650.json'}

exec(code, env_args)
