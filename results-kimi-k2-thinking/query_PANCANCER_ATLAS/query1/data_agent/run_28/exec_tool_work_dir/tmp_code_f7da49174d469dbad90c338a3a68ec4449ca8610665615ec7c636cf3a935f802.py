code = """import json
import math
from collections import defaultdict

# Load IGF2 expression data
igf2_file = locals()['var_functions.query_db:72']
with open(igf2_file, 'r') as f:
    igf2_data = json.load(f)

print('Total IGF2 records:', len(igf2_data))

# Load barcode to histology mapping
mapping_file = locals()['var_functions.execute_python:48']
with open(mapping_file, 'r') as f:
    mapping_data = json.load(f)

barcode_to_histology = mapping_data['barcode_to_histology']
print('Total LGG patients:', len(barcode_to_histology))

# Find matching records
lgg_barcodes = set(barcode_to_histology.keys())
igf2_barcodes = set(r['ParticipantBarcode'] for r in igf2_data)
matching_barcodes = lgg_barcodes.intersection(igf2_barcodes)
print('Matching LGG+IGF2 barcodes:', len(matching_barcodes))

# Group by histology and compute log10 values
histology_groups = defaultdict(list)

for record in igf2_data:
    barcode = record['ParticipantBarcode']
    if barcode in lgg_barcodes:
        try:
            count = float(record['normalized_count'])
            log_val = math.log10(count + 1)
            hist_type = barcode_to_histology[barcode]
            histology_groups[hist_type].append(log_val)
        except:
            continue

total_valid = sum(len(v) for v in histology_groups.values())
print('Total valid patients:', total_valid)

# Calculate averages
results = {}
for hist_type, values in histology_groups.items():
    if values:
        avg = sum(values) / len(values)
        results[hist_type] = {
            'average_log10_expression': round(avg, 4),
            'patient_count': len(values)
        }

output = {
    'total_lgg_patients_analyzed': total_valid,
    'results_by_histology': results
}

print('Results:')
for hist, data in results.items():
    print(hist + ':', data['average_log10_expression'])

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'columns': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'samples': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'histological_type': 'Serous Cystadenocarcinoma'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.', 'histological_type': 'Serous Cystadenocarcinoma'}]}, 'var_functions.list_db:16': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:20': [], 'var_functions.execute_python:24': {'lgg_patients_found': 0, 'lgg_patients': [], 'unique_cancer_types': ['serous cystadenocarcinoma']}, 'var_functions.query_db:26': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:28': [{'total_records': '10761'}], 'var_functions.query_db:30': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Paraganglioma'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'total_clinical_records': 220, 'extracted_barcodes': 220, 'unique_histology_types': ['Oligodendroglioma', 'Paraganglioma', 'Paraganglioma; Extra-adrenal Pheochromocytoma'], 'sample_patients': [{'ParticipantBarcode': 'TCGA-RY-A83X', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-P5-A5F0', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-TM-A84R', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-DH-A7US', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-P5-A5F4', 'histological_type': 'Oligodendroglioma'}]}, 'var_functions.query_db:40': [{'ParticipantBarcode': 'TCGA-CS-6670', 'normalized_count': '381.503', 'Symbol': 'IGF2'}, {'ParticipantBarcode': 'TCGA-DB-A64V', 'normalized_count': '1509.87', 'Symbol': 'IGF2'}, {'ParticipantBarcode': 'TCGA-DH-A7US', 'normalized_count': '418.886', 'Symbol': 'IGF2'}, {'ParticipantBarcode': 'TCGA-E1-A7YE', 'normalized_count': '353.243', 'Symbol': 'IGF2'}, {'ParticipantBarcode': 'TCGA-E1-A7Z2', 'normalized_count': '173.521', 'Symbol': 'IGF2'}, {'ParticipantBarcode': 'TCGA-QH-A86X', 'normalized_count': '427.57', 'Symbol': 'IGF2'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:44': {'total_patients': 189, 'histology_types': ['Oligodendroglioma'], 'patient_counts': {'Oligodendroglioma': 189}}, 'var_functions.execute_python:46': {'total_barcodes': 189, 'batches_count': 4, 'first_batch_sample': ['TCGA-RY-A83X', 'TCGA-P5-A5F0', 'TCGA-TM-A84R', 'TCGA-DH-A7US', 'TCGA-P5-A5F4'], 'last_batch_sample': ['TCGA-HT-7677', 'TCGA-HT-7687', 'TCGA-HT-7856', 'TCGA-HT-7695', 'TCGA-HT-7874']}, 'var_functions.execute_python:48': 'file_storage/functions.execute_python:48.json', 'var_functions.execute_python:50': {'total_barcodes': 189, 'batches_count': 4, 'sample_barcodes': ['TCGA-RY-A83X', 'TCGA-P5-A5F0', 'TCGA-TM-A84R', 'TCGA-DH-A7US', 'TCGA-P5-A5F4', 'TCGA-IK-7675', 'TCGA-HW-A5KJ', 'TCGA-S9-A7J3', 'TCGA-DB-A4XG', 'TCGA-VM-A8CA']}, 'var_functions.query_db:52': [{'ParticipantBarcode': 'TCGA-DB-A64V', 'normalized_count': '1509.87'}, {'ParticipantBarcode': 'TCGA-DH-A7US', 'normalized_count': '418.886'}, {'ParticipantBarcode': 'TCGA-QH-A86X', 'normalized_count': '427.57'}, {'ParticipantBarcode': 'TCGA-CS-6670', 'normalized_count': '381.503'}, {'ParticipantBarcode': 'TCGA-E1-A7Z2', 'normalized_count': '173.521'}], 'var_functions.query_db:56': [{'ParticipantBarcode': 'TCGA-F6-A8O3', 'normalized_count': '650.505'}, {'ParticipantBarcode': 'TCGA-S9-A7QZ', 'normalized_count': '596.332'}, {'ParticipantBarcode': 'TCGA-S9-A7J1', 'normalized_count': '407.007'}], 'var_functions.query_db:58': [], 'var_functions.query_db:64': [], 'var_functions.execute_python:66': {'total_lgg_patients_analyzed': 0, 'average_log10_expression_by_histology': {}}, 'var_functions.execute_python:70': {'total_patients': 0, 'averages': {}}, 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
