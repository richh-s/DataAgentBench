code = """import json, re, os

# Find the correct clinical data file
for f in os.listdir('/tmp'):
    if f.endswith('.json') and 'tmp' in f:
        try:
            with open('/tmp/' + f, 'r') as file:
                data = json.load(file)
                if len(data) > 1000 and 'Patient_description' in data[0]:
                    clinical_file = '/tmp/' + f
                    break
        except:
            pass

print('Using clinical file:', clinical_file.split('/')[-1])

# Read BRCA clinical data
with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)

# Identify alive BRCA patients and extract their barcodes
alive_patients = []
alive_barcodes = set()

for rec in clinical_data:
    days_to_death = str(rec.get('days_to_death', ''))
    if days_to_death == '[Not Applicable]':
        alive_patients.append(rec)
        desc = str(rec.get('Patient_description', ''))
        match = re.search(r'(TCGA-\w{2}-\w{4})', desc)
        if match:
            alive_barcodes.add(match.group(1))

print('Total BRCA patients:', len(clinical_data))
print('Alive BRCA patients:', len(alive_patients))
print('Alive barcodes:', len(alive_barcodes))

# Get histological type counts for alive patients
hist_counts = {}
for rec in alive_patients:
    hist_type = str(rec.get('histological_type', 'Unknown'))
    hist_counts[hist_type] = hist_counts.get(hist_type, 0) + 1

print('\nTop histological types among alive BRCA patients:')
sorted_hists = sorted(hist_counts.items(), key=lambda x: x[1], reverse=True)
for hist_type, count in sorted_hists[:15]:
    print(hist_type + ': ' + str(count))

# Save result to a dictionary
result = {
    'total_brca': len(clinical_data),
    'alive_brca': len(alive_patients),
    'alive_barcodes': list(alive_barcodes),
    'hist_type_counts': hist_counts
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_functions.query_db:10': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'patient_id': '1953', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'patient_id': '1576', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'patient_id': '2408', 'days_to_death': '943.0'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'patient_id': '2427', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'patient_id': '0933', 'days_to_death': '446.0'}, {'Patient_description': "Patient TCGA-23-1124, registered under UUID 8a6d2ce3-cc57-451b-9b07-8263782aa23f, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Dead.", 'histological_type': 'Serous Cystadenocarcinoma', 'patient_id': '1124', 'days_to_death': '1768.0'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-2641 (UUID 49e5ee61-a1c9-4038-84ac-92683e573a65) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'patient_id': '2641', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'Patient TCGA-23-1118 (FEMALE, UUID 700e91bb-d675-41b2-bbbd-935767c7b447) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'patient_id': '1118', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-23-1120 (UUID fdf83fdf-dfbb-4306-9a1b-b4487d18b402) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma', 'patient_id': '1120', 'days_to_death': '[Not Applicable]'}, {'Patient_description': 'The individual with barcode TCGA-23-2081 and UUID 41178cbc-db73-4007-b5d8-febebf7f578d is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Dead.', 'histological_type': 'Serous Cystadenocarcinoma', 'patient_id': '2081', 'days_to_death': '2342.0'}], 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:24': {'total': 1087, 'alive': 0, 'dead': 0, 'top_hist_types': {}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:40': 'file_storage/functions.execute_python:40.json', 'var_functions.list_db:44': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:46': [{'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A8-A0A1', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-A8-A0A9', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Nonsense_Mutation'}, {'ParticipantBarcode': 'TCGA-AA-3821', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Del'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Frame_Shift_Ins'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}, {'ParticipantBarcode': 'TCGA-EJ-7782', 'Hugo_Symbol': 'CDH1', 'Variant_Classification': 'Missense_Mutation'}]}

exec(code, env_args)
