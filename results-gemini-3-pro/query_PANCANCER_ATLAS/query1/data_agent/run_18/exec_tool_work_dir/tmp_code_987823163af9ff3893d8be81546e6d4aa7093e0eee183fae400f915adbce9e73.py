code = """import pandas as pd
import json
import re
import numpy as np

# Load data
clinical_data = json.load(open('var_function-call-15280271133414053003.json'))
molecular_data = json.load(open('var_function-call-16563805635535746873.json'))

df_clinical = pd.DataFrame(clinical_data)
df_molecular = pd.DataFrame(molecular_data)

# Extract barcode from Patient_description
def extract_barcode(text):
    if not text: return None
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', str(text))
    if match:
        return match.group(1)
    return None

df_clinical['Barcode'] = df_clinical['Patient_description'].apply(extract_barcode)

# Filter out rows where barcode could not be extracted
df_clinical = df_clinical.dropna(subset=['Barcode'])

# Molecular data: ParticipantBarcode should be the key.
# Ensure it is treated as string and truncated to 12 chars (Participant ID)
df_molecular['Barcode'] = df_molecular['ParticipantBarcode'].apply(lambda x: str(x)[:12] if x else None)

# Merge
merged = pd.merge(df_clinical, df_molecular, on='Barcode', how='inner')

# Filter histology
def is_valid_histology(h):
    if not h: return False
    h = str(h).strip()
    if h.startswith('[') and h.endswith(']'):
        return False
    return True

merged = merged[merged['histological_type'].apply(is_valid_histology)]

# Filter valid expression
merged['normalized_count'] = pd.to_numeric(merged['normalized_count'], errors='coerce')
merged = merged.dropna(subset=['normalized_count'])

# Calculate log10(count + 1)
merged['log_expression'] = np.log10(merged['normalized_count'] + 1)

# Group and mean
result_df = merged.groupby('histological_type')['log_expression'].mean().reset_index()

# Format
result_dict = result_df.set_index('histological_type')['log_expression'].to_dict()
# Format values to 4 decimal places
final_result = {k: round(v, 4) for k, v in result_dict.items()}

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-16289054157185713684': [], 'var_function-call-7755090668036211384': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-15026113604796674186': [], 'var_function-call-9123079210909633698': [], 'var_function-call-17659558473062265843': [], 'var_function-call-3931523983616324428': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}, {'Patient_description': "Patient TCGA-23-1124, registered under UUID 8a6d2ce3-cc57-451b-9b07-8263782aa23f, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Dead."}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-2641 (UUID 49e5ee61-a1c9-4038-84ac-92683e573a65) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-23-1118 (FEMALE, UUID 700e91bb-d675-41b2-bbbd-935767c7b447) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-1120 (UUID fdf83fdf-dfbb-4306-9a1b-b4487d18b402) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-23-2081 and UUID 41178cbc-db73-4007-b5d8-febebf7f578d is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Dead.'}], 'var_function-call-7215902109184091988': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}], 'var_function-call-15280271133414053003': 'file_storage/function-call-15280271133414053003.json', 'var_function-call-16563805635535746873': 'file_storage/function-call-16563805635535746873.json'}

exec(code, env_args)
