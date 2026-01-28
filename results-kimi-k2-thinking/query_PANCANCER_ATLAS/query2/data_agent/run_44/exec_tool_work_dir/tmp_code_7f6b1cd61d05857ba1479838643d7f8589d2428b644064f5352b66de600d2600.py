code = """import json
import pandas as pd

# Load CDH1 mutation data
cdh1_file = locals()['var_functions.query_db:20']
with open(cdh1_file, 'r') as f:
    cdh1_mutations = json.load(f)

# Load alive BRCA patients data
brca_file = locals()['var_functions.query_db:8']
with open(brca_file, 'r') as f:
    brca_patients = json.load(f)

# Process BRCA patients - extract IDs and filter alive ones
import re
alive_brca_patients = []
for patient in brca_patients:
    if patient.get('days_to_death') == '[Not Applicable]':
        desc = patient.get('Patient_description', '')
        match = re.search(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', desc)
        if match:
            alive_brca_patients.append({
                'patient_id': match.group(1),
                'histological_type': patient.get('histological_type')
            })

# Create DataFrames
df_alive = pd.DataFrame(alive_brca_patients)
df_cdh1 = pd.DataFrame(cdh1_mutations)

# Group alive patients by histological type to get counts
histology_counts = df_alive['histological_type'].value_counts()

# Find CDH1 mutations in alive BRCA patients
alive_with_cdh1 = df_cdh1[df_cdh1['ParticipantBarcode'].isin(df_alive['patient_id'])]

# Count CDH1 mutations by histological type
cdh1_by_histology = {}
for _, row in alive_with_cdh1.iterrows():
    patient_id = row['ParticipantBarcode']
    hist_type = df_alive[df_alive['patient_id'] == patient_id]['histological_type'].iloc[0] if len(df_alive[df_alive['patient_id'] == patient_id]) > 0 else None
    if hist_type:
        cdh1_by_histology[hist_type] = cdh1_by_histology.get(hist_type, 0) + 1

# Calculate percentages
cdh1_percentages = {}
for hist_type, cdh1_count in cdh1_by_histology.items():
    total_count = histology_counts.get(hist_type, 0)
    if total_count > 0:
        cdh1_percentages[hist_type] = float(cdh1_count / total_count) * 100

# Get top 3 histological types
sorted_histology = sorted(cdh1_percentages.items(), key=lambda x: x[1], reverse=True)[:3]

# Convert histology_counts to regular dict for JSON serialization
histology_counts_dict = {k: int(v) for k, v in histology_counts.items()}
cdh1_counts_dict = {k: int(v) for k, v in cdh1_by_histology.items()}

print('__RESULT__:')
print(json.dumps({
    'total_alive_brca': len(df_alive),
    'alive_with_cdh1_mutations': len(alive_with_cdh1),
    'unique_histological_types': len(histology_counts),
    'top_3_histology': sorted_histology,
    'cdh1_by_histology': cdh1_counts_dict,
    'histology_counts': histology_counts_dict
}))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'total_patients': 1087, 'columns': ['Patient_description', 'histological_type', 'days_to_death'], 'alive_count': 936, 'unique_histological_types': 9, 'sample_records': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma', 'days_to_death': '[Not Applicable]'}]}, 'var_functions.execute_python:18': {'alive_brca_count': 936, 'sample_patients': [{'patient_id': 'TCGA-AC-A5EH', 'histological_type': 'Infiltrating Ductal Carcinoma', 'description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.'}, {'patient_id': 'TCGA-LL-A7SZ', 'histological_type': 'Infiltrating Ductal Carcinoma', 'description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.'}, {'patient_id': 'TCGA-AN-A0FY', 'histological_type': 'Infiltrating Ductal Carcinoma', 'description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive."}, {'patient_id': 'TCGA-AC-A2FB', 'histological_type': 'Infiltrating Lobular Carcinoma', 'description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.'}, {'patient_id': 'TCGA-AO-A1KR', 'histological_type': 'Infiltrating Ductal Carcinoma', 'description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.'}], 'unique_histological_types': 9}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
