code = """import json
import re
import math

# Load clinical LGG data
clinical_path = locals()['var_functions.query_db:22']
with open(clinical_path, 'r') as f:
    clinical_lgg = json.load(f)

# Load IGF2 expression data
igf2_path = locals()['var_functions.query_db:28']
with open(igf2_path, 'r') as f:
    igf2_expr = json.load(f)

# Build patient -> histology mapping
patient_histology = {}
for record in clinical_lgg:
    desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type')
    
    if hist_type and not hist_type.startswith('['):
        match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
        if match:
            patient_histology[match.group(1)] = hist_type

# Build patient -> IGF2 expression (prefer primary tumor)
patient_igf2 = {}
for record in igf2_expr:
    participant = record.get('ParticipantBarcode')
    if participant:
        try:
            count = float(record.get('normalized_count', 0))
            sample_type = record.get('SampleTypeLetterCode')
            
            if participant not in patient_igf2 or sample_type == 'TP':
                patient_igf2[participant] = count
        except:
            pass

# Find common patients and compute group averages
histology_groups = {}
for patient, hist_type in patient_histology.items():
    if patient in patient_igf2:
        if hist_type not in histology_groups:
            histology_groups[hist_type] = []
        histology_groups[hist_type].append(patient_igf2[patient])

# Compute average log10(expression+1) for each histology type
results = {}
for hist_type, expr_values in sorted(histology_groups.items()):
    log_values = [math.log10(val + 1) for val in expr_values]
    avg_log = sum(log_values) / len(log_values)
    results[hist_type] = {
        'average_log10_expression': round(avg_log, 4),
        'sample_count': len(expr_values)
    }

# Overall stats
all_expr = [patient_igf2[p] for p in patient_histology if p in patient_igf2]
all_log = [math.log10(val + 1) for val in all_expr]
overall_avg = sum(all_log) / len(all_log)

print("__RESULT__:")
print(json.dumps({
    "results": results,
    "overall_stats": {
        "total_matched_patients": len(patient_histology),
        "patients_with_expression": len(all_expr),
        "overall_average_log10": round(overall_avg, 4)
    }
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}], 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_functions.query_db:10': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'None'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'diagnosis': 'None', 'icd_10': 'C76.0', 'icd_o_3_histology': '8693/3', 'tumor_tissue_site': 'Extra-adrenal Site', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'diagnosis': 'None', 'icd_10': 'C71.0', 'icd_o_3_histology': '9450/3', 'tumor_tissue_site': 'Central nervous system', 'histological_type': 'Oligodendroglioma'}, {'diagnosis': 'None', 'icd_10': 'C71.9', 'icd_o_3_histology': '9440/3', 'tumor_tissue_site': 'Brain', 'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'diagnosis': 'None', 'icd_10': 'C71.1', 'icd_o_3_histology': '9440/3', 'tumor_tissue_site': 'Brain', 'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'diagnosis': 'None', 'icd_10': 'C48.0', 'icd_o_3_histology': '8693/3', 'tumor_tissue_site': 'Extra-adrenal Site', 'histological_type': 'Paraganglioma'}, {'diagnosis': 'None', 'icd_10': 'C48.0', 'icd_o_3_histology': '8680/1', 'tumor_tissue_site': 'Extra-adrenal Site', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'diagnosis': 'None', 'icd_10': 'C48.0', 'icd_o_3_histology': '8693/1', 'tumor_tissue_site': 'Extra-adrenal Site', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'diagnosis': 'None', 'icd_10': 'C71.0', 'icd_o_3_histology': '9382/3', 'tumor_tissue_site': 'Central nervous system', 'histological_type': 'Oligodendroglioma'}, {'diagnosis': 'None', 'icd_10': 'C49.5', 'icd_o_3_histology': '8693/1', 'tumor_tissue_site': 'Extra-adrenal Site', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'diagnosis': 'None', 'icd_10': 'C74.9', 'icd_o_3_histology': '8680/3', 'tumor_tissue_site': 'Extra-adrenal Site', 'histological_type': 'Paraganglioma'}, {'diagnosis': 'None', 'icd_10': 'C48.0', 'icd_o_3_histology': '8693/3', 'tumor_tissue_site': 'Extra-adrenal Site', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'diagnosis': 'None', 'icd_10': 'C72.9', 'icd_o_3_histology': '8680/3', 'tumor_tissue_site': 'Extra-adrenal Site', 'histological_type': 'Paraganglioma'}, {'diagnosis': 'None', 'icd_10': 'C49.4', 'icd_o_3_histology': '8693/1', 'tumor_tissue_site': 'Extra-adrenal Site', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'diagnosis': 'None', 'icd_10': 'C49.3', 'icd_o_3_histology': '8680/1', 'tumor_tissue_site': 'Extra-adrenal Site', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'diagnosis': 'None', 'icd_10': 'C71.9', 'icd_o_3_histology': '9382/3', 'tumor_tissue_site': 'Central nervous system', 'histological_type': 'Oligodendroglioma'}, {'diagnosis': 'None', 'icd_10': 'C49.6', 'icd_o_3_histology': '8693/1', 'tumor_tissue_site': 'Extra-adrenal Site', 'histological_type': 'Paraganglioma'}, {'diagnosis': 'None', 'icd_10': 'C71.9', 'icd_o_3_histology': '9440/3', 'tumor_tissue_site': 'Brain', 'histological_type': 'Treated primary GBM'}, {'diagnosis': 'None', 'icd_10': 'C38.3', 'icd_o_3_histology': '8693/3', 'tumor_tissue_site': 'Extra-adrenal Site', 'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}, {'diagnosis': 'None', 'icd_10': 'C71.8', 'icd_o_3_histology': '9440/3', 'tumor_tissue_site': 'Brain', 'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'diagnosis': 'None', 'icd_10': 'C71.9', 'icd_o_3_histology': '9450/3', 'tumor_tissue_site': 'Central nervous system', 'histological_type': 'Oligodendroglioma'}], 'var_functions.query_db:16': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': {'lgg_patient_count': 383, 'sample_histologies': ['Oligoastrocytoma', 'Oligodendroglioma', 'Astrocytoma']}, 'var_functions.execute_python:34': {'Astrocytoma': {'average_log10_expression': 2.6014, 'sample_count': 3}, 'Oligoastrocytoma': {'average_log10_expression': 2.7136, 'sample_count': 5}, 'Oligodendroglioma': {'average_log10_expression': 2.6825, 'sample_count': 8}}, 'var_functions.execute_python:36': {'total_clinical_records': 383, 'unique_clinical_barcodes': 383, 'good_histology_count': 383, 'igf2_patient_count': 496, 'matched_patients': 16, 'sample_matches': ['TCGA-DU-7007', 'TCGA-HT-7478', 'TCGA-CS-6670', 'TCGA-QH-A86X', 'TCGA-TM-A7CA', 'TCGA-F6-A8O3', 'TCGA-DB-A64V', 'TCGA-TM-A84T', 'TCGA-S9-A7QZ', 'TCGA-S9-A7J1']}, 'var_functions.execute_python:38': {'lgg_clinical_records': 383, 'lgg_with_good_histology': 383, 'igf2_patients_total': 496, 'sample_lgg_barcodes': ['TCGA-CS-4938', 'TCGA-CS-4944', 'TCGA-CS-5390', 'TCGA-CS-5395', 'TCGA-CS-5396', 'TCGA-CS-6186', 'TCGA-CS-6667', 'TCGA-CS-6668', 'TCGA-CS-6669', 'TCGA-CS-6670'], 'sample_igf2_barcodes': ['TCGA-06-0152', 'TCGA-06-0158', 'TCGA-06-0190', 'TCGA-06-0878', 'TCGA-06-2561', 'TCGA-09-1667', 'TCGA-09-2044', 'TCGA-13-0897', 'TCGA-13-1410', 'TCGA-14-0787']}, 'var_functions.execute_python:40': {'lgg_patients_found': 383, 'igf2_patients_total': 496, 'common_patients': 16, 'sample_common': ['TCGA-CS-6670', 'TCGA-DB-A64V', 'TCGA-DH-A7US', 'TCGA-DU-7007', 'TCGA-E1-A7Z2', 'TCGA-F6-A8O3', 'TCGA-FG-A713', 'TCGA-HT-7473', 'TCGA-HT-7478', 'TCGA-QH-A86X', 'TCGA-S9-A6WP', 'TCGA-S9-A7J1', 'TCGA-S9-A7QZ', 'TCGA-TM-A7CA', 'TCGA-TM-A84T', 'TCGA-VV-A829']}}

exec(code, env_args)
