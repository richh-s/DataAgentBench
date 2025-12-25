code = """import json
import pandas as pd
import numpy as np
import re

# Load data
with open(locals()['var_function-call-13896710250551149987'], 'r') as f:
    clinical_data = json.load(f)

with open(locals()['var_function-call-15727249239212036806'], 'r') as f:
    expression_data = json.load(f)

df_clinical = pd.DataFrame(clinical_data)
df_expression = pd.DataFrame(expression_data)

# Extract barcode from Patient_description
# Patterns observed: 
# "linked to barcode TCGA-RY-A83X"
# "barcode TCGA-FG-A60K"
# "Patient TCGA-DB-A4XH"
# "patient TCGA-31-1953"
# Regex to find 'TCGA-XX-XXXX'
barcode_pattern = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')

def extract_barcode(text):
    if not isinstance(text, str):
        return None
    match = barcode_pattern.search(text)
    if match:
        return match.group(1)
    return None

df_clinical['barcode'] = df_clinical['Patient_description'].apply(extract_barcode)

# Filter valid histology
# "histology annotations that are not enclosed in square brackets"
# This usually means values like "[Not Available]" should be excluded.
# We will exclude if the string starts with '[' and ends with ']'
def is_valid_histology(hist):
    if not isinstance(hist, str):
        return False
    hist = hist.strip()
    if hist.startswith('[') and hist.endswith(']'):
        return False
    return True

df_clinical = df_clinical[df_clinical['histological_type'].apply(is_valid_histology)]

# Clean expression data
df_expression['normalized_count'] = pd.to_numeric(df_expression['normalized_count'], errors='coerce')
df_expression = df_expression.dropna(subset=['normalized_count'])

# Merge
# Molecular data ParticipantBarcode might be longer or same.
# Clinical barcode is 12 chars.
# Let's standardize to 12 chars for join just in case, though molecular preview showed 12 chars.
df_expression['barcode_join'] = df_expression['ParticipantBarcode'].str.slice(0, 12)
df_clinical['barcode_join'] = df_clinical['barcode']

merged = pd.merge(df_clinical, df_expression, on='barcode_join', how='inner')

# Calculate log10(count + 1)
merged['log_expression'] = np.log10(merged['normalized_count'] + 1)

# Group by histology and compute mean
result_df = merged.groupby('histological_type')['log_expression'].mean().reset_index()

# Format output
output = {}
for _, row in result_df.iterrows():
    output[row['histological_type']] = round(row['log_expression'], 4)

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-12045710671379752357': ['clinical_info'], 'var_function-call-14699453513018016664': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-17370598896042896957': [{'ParticipantBarcode': 'TCGA-06-0675', 'Symbol': 'LXN', 'normalized_count': '69.7259'}], 'var_function-call-92189842307908399': [], 'var_function-call-13333180193972140474': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}], 'var_function-call-13896710250551149987': 'file_storage/function-call-13896710250551149987.json', 'var_function-call-15727249239212036806': 'file_storage/function-call-15727249239212036806.json'}

exec(code, env_args)
