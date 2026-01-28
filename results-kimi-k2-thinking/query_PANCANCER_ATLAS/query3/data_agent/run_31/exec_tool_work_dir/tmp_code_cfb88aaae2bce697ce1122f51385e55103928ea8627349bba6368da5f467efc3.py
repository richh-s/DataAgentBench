code = """import json, re
from collections import Counter

# Find available data variables
data_vars = {}
for name, value in list(locals().items()):
    if isinstance(value, list) and len(value) > 0:
        if isinstance(value[0], dict):
            if 'Patient_description' in value[0]:
                data_vars['clinical'] = value
            elif 'ParticipantBarcode' in value[0]:
                data_vars['mutation'] = value

if 'clinical' not in data_vars or 'mutation' not in data_vars:
    print("Data not found in variables")
    # List all variables that might contain data
    for name, value in list(locals().items()):
        if isinstance(value, list) and len(value) > 0:
            if isinstance(value[0], dict):
                print(f"Variable {name}: {list(value[0].keys())}")
    result = {'error': 'Data not found'}
else:
    clinical_data = data_vars['clinical']
    mutation_data = data_vars['mutation']
    
    print(f"Clinical: {len(clinical_data)}, Mutation: {len(mutation_data)}")
    
    # Process data
    female_brca_patients = {}
    for record in clinical_data:
        desc = record.get('Patient_description', '')
        hist_type = record.get('histological_type')
        
        match = re.search(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', desc)
        if match:
            barcode = match.group()
            if hist_type and hist_type != 'None' and hist_type.strip():
                female_brca_patients[barcode] = hist_type.strip()
    
    cdh1_mutation_patients = set()
    for record in mutation_data:
        if 'ParticipantBarcode' in record:
            cdh1_mutation_patients.add(record['ParticipantBarcode'])
    
    # Build contingency table
    contingency = {}
    hist_counts = Counter(female_brca_patients.values())
    
    for hist_type in hist_counts:
        contingency[hist_type] = {'mutation': 0, 'no_mutation': 0, 'total': 0}
    
    for patient, hist_type in female_brca_patients.items():
        if patient in cdh1_mutation_patients:
            contingency[hist_type]['mutation'] += 1
        else:
            contingency[hist_type]['no_mutation'] += 1
        contingency[hist_type]['total'] += 1
    
    # Filter categories with marginal totals > 10
    filtered_contingency = {}
    for hist_type, counts in contingency.items():
        if counts['total'] > 10:
            filtered_contingency[hist_type] = counts
    
    # Calculate chi-square
    chi_square = 0.0
    total_mutation = sum(c['mutation'] for c in filtered_contingency.values())
    total_no_mutation = sum(c['no_mutation'] for c in filtered_contingency.values())
    grand_total = total_mutation + total_no_mutation
    
    for hist_type, counts in filtered_contingency.items():
        expected_mutation = (counts['total'] * total_mutation) / grand_total
        expected_no_mutation = (counts['total'] * total_no_mutation) / grand_total
        
        chi_square += ((counts['mutation'] - expected_mutation) ** 2) / expected_mutation
        chi_square += ((counts['no_mutation'] - expected_no_mutation) ** 2) / expected_no_mutation
    
    result = {
        'chi_square_statistic': round(chi_square, 4),
        'total_patients': grand_total,
        'categories': len(filtered_contingency),
        'table': filtered_contingency
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_functions.query_db:10': [], 'var_functions.query_db:14': [{'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-FI-A2D5', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-G4-6628', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-GI-A2C8', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-VQ-A8PX', 'Hugo_Symbol': 'CDH1', 'FILTER': 'PASS'}], 'var_functions.query_db:16': [], 'var_functions.query_db:18': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive."}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.'}, {'Patient_description': 'Clinical entry C07B122E-AC50-4DB2-ADD2-5617A5D0E976 identifies patient TCGA-GM-A2DA, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Dead.'}, {'Patient_description': 'The individual with barcode TCGA-3C-AAAU and UUID 6E7D5EC6-A469-467C-B748-237353C23416 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.'}, {'Patient_description': "Patient TCGA-A7-A26I, registered under UUID b2ecbc0f-2c30-4200-8d5e-7b95424bcadb, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive."}, {'Patient_description': 'Record 523E24A2-51B9-4658-BE2F-42E5FCCEBB17 refers to patient TCGA-A7-A5ZW, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'The individual with barcode TCGA-C8-A26Z and UUID dc11b1c7-1f00-4813-b4b5-ecf776b2eb37 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.'}, {'Patient_description': 'The individual with barcode TCGA-EW-A6SA and UUID ABA5F46A-E67A-4CD2-9C52-C0686968FF04 is a MALE case of Breast invasive carcinoma, documented with vital status = Alive.'}, {'Patient_description': 'The individual with barcode TCGA-C8-A273 and UUID 5a5f0f48-2b13-4e78-b130-901b85d9a7f3 is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.'}, {'Patient_description': 'Record c2a742fe-3e8b-4210-85a6-7191a1123609 refers to patient TCGA-AN-A0FN, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.'}, {'Patient_description': "Patient TCGA-AN-A0FD, registered under UUID c6086936-7544-4da0-8c0c-114166848483, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive."}, {'Patient_description': 'Clinical entry 10c9be1e-2cc0-45e4-8d2c-c013ea63ef05 identifies patient TCGA-AN-A0FS, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.'}, {'Patient_description': 'Record b5b99291-507e-4b68-a039-9a0f571f55df refers to patient TCGA-AO-A12H, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Record 3e9f93c0-aa79-4b4c-bd6c-b3325912362a refers to patient TCGA-AN-A0AL, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Patient TCGA-AC-A3YI (UUID A45D296E-EFC0-479E-B2F6-BAD834668CDF) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.'}, {'Patient_description': "Patient TCGA-C8-A137, registered under UUID 03ab1e9f-4918-404d-b178-3a4fd929c5e8, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive."}, {'Patient_description': 'Clinical entry 0DD8DBC1-C48B-4E7C-B401-57101F724967 identifies patient TCGA-S3-AA11, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:52': {'clinical': None, 'mutation': None}, 'var_functions.execute_python:54': {'found_files': [], 'tmp_files': []}, 'var_functions.query_db:56': [{'total_records': '1075'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.execute_python:76': {'error': 'Data not found in storage'}, 'var_functions.execute_python:94': {'error': 'Data not available', 'files': []}, 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json'}

exec(code, env_args)
