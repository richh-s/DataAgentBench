code = """import json
import pandas as pd
import re
import numpy as np

# Load clinical data
clinical_file = locals()['var_function-call-9296875304927786827']
with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)

# Load molecular data
molecular_file = locals()['var_function-call-1978868177385730831']
with open(molecular_file, 'r') as f:
    molecular_data = json.load(f)

# Create DataFrames
df_clinical = pd.DataFrame(clinical_data)
df_molecular = pd.DataFrame(molecular_data)

# Extract ParticipantBarcode from Patient_description
# Pattern: TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}
pattern = r"(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})"

def extract_barcode(desc):
    match = re.search(pattern, desc)
    if match:
        return match.group(1)
    return None

df_clinical['ParticipantBarcode'] = df_clinical['Patient_description'].apply(extract_barcode)

# Filter out rows where barcode extraction failed
df_clinical = df_clinical.dropna(subset=['ParticipantBarcode'])

# Merge
# Note: df_molecular has 'ParticipantBarcode'
merged = pd.merge(df_clinical, df_molecular, on='ParticipantBarcode', how='inner')

# Ensure normalized_count is numeric
merged['normalized_count'] = pd.to_numeric(merged['normalized_count'], errors='coerce')
merged = merged.dropna(subset=['normalized_count'])

# Compute log10(normalized_count + 1)
merged['log10_expression'] = np.log10(merged['normalized_count'] + 1)

# Group by histological_type and compute mean
# Filter out histology annotations enclosed in square brackets - already done in SQL but double check
# "Only include patients... histology annotations that are not enclosed in square brackets"
# My SQL filtered "NOT LIKE '[%'", but maybe some end with brackets or have brackets elsewhere?
# Usually "[Not Available]" is the target.
# Let's just group and average.

result = merged.groupby('histological_type')['log10_expression'].mean().reset_index()

# Format values to at least 4 decimal places
result['average_log10_expression'] = result['log10_expression'].apply(lambda x: round(x, 4))

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-8877479728319447730': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-5538570605525599116': [], 'var_function-call-4501164625612777344': [], 'var_function-call-9686946446059020101': [], 'var_function-call-10820253781719147719': [{'tumor_tissue_site': 'Brain'}], 'var_function-call-741518159192623767': [{'histological_type': 'Untreated primary (de novo) GBM'}, {'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'histological_type': 'Treated primary GBM'}], 'var_function-call-4501684365392095753': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'days_to_birth': '-16911.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '939.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '46.0', 'icd_10': 'C71.0', 'tissue_retrospective_collection_indicator': 'NO', 'icd_o_3_histology': '9450/3', 'tissue_prospective_collection_indicator': 'YES', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C71.0', 'tumor_tissue_site': 'Central nervous system', 'new_tumor_event_after_initial_treatment': 'NO', 'radiation_therapy': 'NO', 'race': 'WHITE', 'prior_dx': 'No', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'TUMOR FREE', 'patient_id': 'A83X', 'year_of_initial_pathologic_diagnosis': '2012.0', 'histological_type': 'Oligodendroglioma', 'tissue_source_site': 'RY', 'form_completion_date': '2015-1-7', 'pathologic_T': 'None', 'pathologic_M': 'None', 'clinical_M': 'None', 'pathologic_N': 'None', 'system_version': 'None', 'pathologic_stage': 'None', 'clinical_stage': 'None', 'clinical_T': 'None', 'clinical_N': 'None', 'extranodal_involvement': 'None', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': '[Not Applicable]', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'None', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '[Not Evaluated]', 'anatomic_neoplasm_subdivision': 'None', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': 'None', 'karnofsky_performance_score': '[Not Evaluated]', 'neoplasm_histologic_grade': 'G2', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': '[Not Evaluated]', 'laterality': 'Right', 'targeted_molecular_therapy': 'NO', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'None', 'lymphatic_invasion': 'None', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'NO', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-9296875304927786827': 'file_storage/function-call-9296875304927786827.json', 'var_function-call-1978868177385730831': 'file_storage/function-call-1978868177385730831.json'}

exec(code, env_args)
