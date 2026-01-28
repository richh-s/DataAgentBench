code = """import json
import re
import math

# Load LGG patient data from clinical database
clinical_file = locals()['var_functions.query_db:20']
with open(clinical_file, 'r') as f:
    lgg_patients = json.load(f)

# Load IGF2 expression data from molecular database
expression_file = locals()['var_functions.query_db:26']
with open(expression_file, 'r') as f:
    igf2_expression = json.load(f)

print('LGG patients found:', len(lgg_patients))
print('IGF2 expression records found:', len(igf2_expression))

# Extract patient barcodes from Patient_description using regex
barcode_pattern = r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})'

# Create dictionary of LGG patients with their histology
lgg_patient_data = {}
for patient in lgg_patients:
    desc = patient['Patient_description']
    match = re.search(barcode_pattern, desc)
    if match:
        barcode = match.group(1)
        hist_type = patient['histological_type']
        # Filter out histology types in square brackets
        if hist_type and not (hist_type.startswith('[') and hist_type.endswith(']')):
            lgg_patient_data[barcode] = hist_type

print('LGG patients with valid histology:', len(lgg_patient_data))

# Create dictionary of IGF2 expression values
igf2_values = {}
for record in igf2_expression:
    barcode = record['ParticipantBarcode']
    norm_count = record['normalized_count']
    if norm_count and norm_count != '':
        try:
            # Convert to float and check if valid
            count_val = float(norm_count)
            if count_val >= 0:  # expression should be non-negative
                igf2_values[barcode] = count_val
        except (ValueError, TypeError):
            continue

print('IGF2 expression values for patients:', len(igf2_values))

# Combine data: find intersection of LGG patients with IGF2 expression
combined_data = []
for barcode in lgg_patient_data:
    if barcode in igf2_values:
        hist_type = lgg_patient_data[barcode]
        norm_count = igf2_values[barcode]
        # Compute log10(normalized_count + 1)
        log10_expr = math.log10(norm_count + 1)
        combined_data.append({
            'barcode': barcode,
            'histological_type': hist_type,
            'normalized_count': norm_count,
            'log10_expression': log10_expr
        })

print('Patients with both LGG and IGF2 data:', len(combined_data))

# Group by histological type and compute average log10 expression
histology_groups = {}
for record in combined_data:
    hist_type = record['histological_type']
    log10_val = record['log10_expression']
    if hist_type not in histology_groups:
        histology_groups[hist_type] = []
    histology_groups[hist_type].append(log10_val)

# Compute averages with 4+ decimal places
results = {}
for hist_type, values in histology_groups.items():
    avg_log10 = sum(values) / len(values)
    results[hist_type] = {
        'average_log10_expression': round(avg_log10, 4),
        'patient_count': len(values)
    }

print('Histology types found:', len(results))
print('Results:')
for hist_type, data in sorted(results.items()):
    print(f"  {hist_type}: {data['average_log10_expression']} (n={data['patient_count']})")

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.execute_python:16': {'status': 'checking variables'}, 'var_functions.query_db:18': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-P5-A5F0 (MALE, UUID 7EB5D055-E1C8-4B93-9205-A49A6E79DFD4) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-S9-A6U1 (UUID A5E10E2E-5157-487B-88DC-6C70AD5E244A) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-TM-A7C3 and UUID D13AC936-87A9-4164-BDAB-02CCF3908CFE is a FEMALE case of Brain lower grade glioma, documented with vital status = Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Case 8E44FB97-C649-4056-80AC-257CEF61D226, linked to barcode TCGA-S9-A7R2, corresponds to a MALE patient diagnosed with Brain lower grade glioma, with vital status Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record 21BBE030-8DBB-47EB-A670-13EB57C12159 refers to patient TCGA-TM-A84R, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': "Patient TCGA-S9-A6TU, registered under UUID 688FC346-A14D-4859-8727-057CD0A0B880, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record c3c41fd2-f0d7-4f46-9e18-cce4626538c2 refers to patient TCGA-HW-7490, a MALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Record D81B9957-8C82-4006-B111-449FA9FB95ED refers to patient TCGA-P5-A733, a FEMALE diagnosed with Brain lower grade glioma. Vital status recorded as Alive.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Patient TCGA-DH-A7US (MALE, UUID 82FD02AB-D628-469F-8853-4C603CF04964) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Clinical entry bc3b4816-df1d-44ed-a8c6-f32c8e011a1f identifies patient TCGA-HW-8319, a FEMALE subject with Brain lower grade glioma. Their current vital status is Dead.', 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Patient TCGA-P5-A5F4 (FEMALE, UUID 0557B788-5AED-4919-85EB-A503AD893D75) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'Patient TCGA-FG-7637 (MALE, UUID c40ab957-fe46-43b1-992d-b4e2040a3f57) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': "Patient TCGA-FG-A4MW, registered under UUID DCE168B1-D2A9-4409-8437-AB382F6D7D31, belongs to the Brain lower grade glioma cohort. This MALE patient's vital status is Dead.", 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': "Patient TCGA-E1-A7Z3, registered under UUID 3AC41CC6-5DFB-40A1-BD13-5DC7CA2BB6F3, belongs to the Brain lower grade glioma cohort. This FEMALE patient's vital status is Dead.", 'histological_type': 'Astrocytoma'}, {'Patient_description': 'Patient TCGA-S9-A7R4 (MALE, UUID 58650D08-7685-41DE-9AE0-21665F8F449F) is enrolled in the study of Brain lower grade glioma. Vital status: Alive.', 'histological_type': 'Astrocytoma'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:24': {'status': 'success', 'patient_count': 513}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
