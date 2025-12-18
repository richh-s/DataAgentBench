code = """import pandas as pd
import json

clinical_data = json.load(open(locals()['var_function-call-5332461788665001929'], 'r'))
df_clinical = pd.DataFrame(clinical_data)

# Extract ParticipantBarcode and Vital Status from Patient_description
def extract_patient_info(description):
    participant_barcode = None
    vital_status = None
    cancer_type_acronym = None

    # Extract ParticipantBarcode
    barcode_match = re.search(r'TCGA-\w{2}-\w{4}', description)
    if barcode_match:
        participant_barcode = barcode_match.group(0)

    # Extract Vital Status
    if "vital status: Alive" in description:
        vital_status = "Alive"
    elif "vital status: Dead" in description:
        vital_status = "Dead"

    # Extract cancer type acronym (e.g., BRCA, LGG) - this is a heuristic
    # Looking for a 3-4 letter uppercase word often followed by 'dataset' or 'cohort'
    cancer_type_match = re.search(r'\b([A-Z]{3,4}) (dataset|cohort)', description)
    if cancer_type_match:
        cancer_type_acronym = cancer_type_match.group(1)
    else:
        # Try another pattern if the first one fails (e.g. Bladder urothelial carcinoma)
        if 'Bladder urothelial carcinoma' in description:
            cancer_type_acronym = 'BRCA'

    return participant_barcode, vital_status, cancer_type_acronym

import re
df_clinical[['ParticipantBarcode', 'VitalStatus', 'CancerTypeAcronym']] = df_clinical['Patient_description'].apply(lambda x: pd.Series(extract_patient_info(x)))

# Filter for BRCA patients (Bladder urothelial carcinoma) and vital status "Alive"
brca_alive_patients = df_clinical[(df_clinical['CancerTypeAcronym'] == 'BRCA') & (df_clinical['VitalStatus'] == 'Alive')]

# Select relevant columns and drop duplicates to get unique patients
brca_alive_patients = brca_alive_patients[['ParticipantBarcode', 'histological_type']].drop_duplicates()

print("__RESULT__:")
print(brca_alive_patients.to_json(orient='records'))"""

env_args = {'var_function-call-717839249057813350': ['clinical_info'], 'var_function-call-6964507516600495946': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-5332461788665001929': 'file_storage/function-call-5332461788665001929.json', 'var_function-call-15191325560090571334': [], 'var_function-call-10672615406131513126': 'file_storage/function-call-10672615406131513126.json'}

exec(code, env_args)
