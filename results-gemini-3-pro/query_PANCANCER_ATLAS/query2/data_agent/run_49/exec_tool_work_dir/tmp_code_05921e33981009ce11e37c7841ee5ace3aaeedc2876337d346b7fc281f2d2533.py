code = """import json
import pandas as pd
import re

# Get file paths
clinical_file_path = locals()['var_function-call-16725730694038778780']
mutation_file_path = locals()['var_function-call-3891555800941188895']

# Load clinical data
with open(clinical_file_path, 'r') as f:
    clinical_data = json.load(f)

# Load mutation data
with open(mutation_file_path, 'r') as f:
    mutation_data = json.load(f)

# Extract barcodes with CDH1 mutation
cdh1_mutated_barcodes = set(item['ParticipantBarcode'] for item in mutation_data)

# Process clinical data
processed_clinical = []
for entry in clinical_data:
    desc = entry.get('Patient_description', '')
    icd_code = entry.get('icd_o_3_histology', 'Unknown')
    
    # Extract barcode: TCGA-XX-XXXX
    match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if match:
        barcode = match.group(1)
        has_mutation = barcode in cdh1_mutated_barcodes
        processed_clinical.append({
            'barcode': barcode,
            'icd_code': icd_code,
            'has_mutation': has_mutation
        })

df = pd.DataFrame(processed_clinical)

# Mapping codes to names
code_map = {
    '8120/3': 'Transitional Cell Carcinoma',
    '8130/3': 'Papillary Transitional Cell Carcinoma',
    '8260/3': 'Papillary Adenocarcinoma',
    '8070/3': 'Squamous Cell Carcinoma'
}

df['histological_type_name'] = df['icd_code'].map(code_map).fillna(df['icd_code'])

# Group by histological_type_name
stats = df.groupby('histological_type_name').agg(
    total_patients=('barcode', 'count'),
    mutated_patients=('has_mutation', 'sum')
).reset_index()

stats['percentage'] = (stats['mutated_patients'] / stats['total_patients']) * 100

# Sort by percentage descending
top_3 = stats.sort_values(by=['percentage', 'total_patients'], ascending=[False, False]).head(3)

print("__RESULT__:")
print(top_3.to_json(orient='records'))"""

env_args = {'var_function-call-14271955825820705516': [], 'var_function-call-13377566559293195381': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-13950027014280360429': 'file_storage/function-call-13950027014280360429.json', 'var_function-call-3891555800941188895': 'file_storage/function-call-3891555800941188895.json', 'var_function-call-1457586144274176432': [{'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'total_patients': 228, 'mutated_patients': 7, 'percentage': 3.0701754386}, {'histological_type': 'None', 'total_patients': 2, 'mutated_patients': 0, 'percentage': 0.0}], 'var_function-call-17069608712397688295': [{'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'histological_type_other': 'None'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'histological_type_other': 'None'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'histological_type_other': 'None'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'histological_type_other': 'None'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'histological_type_other': 'None'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'histological_type_other': 'None'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'histological_type_other': 'None'}, {'histological_type': 'None', 'histological_type_other': 'None'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'histological_type_other': 'None'}, {'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'histological_type_other': 'None'}], 'var_function-call-885026181756242692': [{'icd_o_3_histology': '8070/3', 'count': '1'}, {'icd_o_3_histology': '8260/3', 'count': '1'}, {'icd_o_3_histology': '8130/3', 'count': '44'}, {'icd_o_3_histology': '8120/3', 'count': '184'}], 'var_function-call-9700471374738425297': [{'count': '1087'}], 'var_function-call-16725730694038778780': 'file_storage/function-call-16725730694038778780.json'}

exec(code, env_args)
