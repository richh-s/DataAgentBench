code = """import json
import re
import math

# Load clinical data (LGG patients with histology)
clinical_data_path = locals()['var_functions.query_db:16']
if isinstance(clinical_data_path, str):
    with open(clinical_data_path, 'r') as f:
        clinical_data = json.load(f)
else:
    clinical_data = clinical_data_path

# Extract patient barcodes and histology types
lgg_barcode_histology = {}
for record in clinical_data:
    patient_desc = record.get("Patient_description", "")
    hist_type = record.get("histological_type", "")
    
    # Skip records with histology in square brackets
    if not hist_type or hist_type.startswith('['):
        continue
    
    # Extract full TCGA barcode
    barcode_matches = re.findall(r'TCGA-[A-Z0-9]{2}-[A-Z0-9]{4}', patient_desc)
    if barcode_matches:
        barcode = barcode_matches[0]
        lgg_barcode_histology[barcode] = hist_type

# Load IGF2 expression data
expression_data_path = locals()['var_functions.query_db:34']
if isinstance(expression_data_path, str):
    with open(expression_data_path, 'r') as f:
        expression_data = json.load(f)
else:
    expression_data = expression_data_path

# Filter IGF2 expression for LGG patients and primary tumor samples
lgg_expression = []
for record in expression_data:
    barcode = record.get("ParticipantBarcode")
    if barcode in lgg_barcode_histology:
        # Convert normalized_count to float
        try:
            count = float(record.get("normalized_count", 0))
            if count > 0:  # Valid expression value
                lgg_expression.append({
                    'barcode': barcode,
                    'histology': lgg_barcode_histology[barcode],
                    'expression': count
                })
        except (ValueError, TypeError):
            continue

# Group by histology and compute average log10(expression + 1)
from collections import defaultdict

histology_groups = defaultdict(list)
for item in lgg_expression:
    histology_groups[item['histology']].append(item['expression'])

# Compute statistics
results = {}
for histology, expressions in histology_groups.items():
    if len(expressions) > 0:
        log10_vals = [math.log10(expr + 1) for expr in expressions]
        avg_log10 = sum(log10_vals) / len(log10_vals)
        results[histology] = {
            'count': len(expressions),
            'avg_log10_expression': round(avg_log10, 4)
        }

# Format final answer
final_results = {}
for histology, stats in sorted(results.items(), key=lambda x: -x[1]['count']):
    final_results[histology] = f"{stats['avg_log10_expression']:.4f}"

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_functions.query_db:5': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Paraganglioma'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}], 'var_functions.list_db:6': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.list_db:8': ['clinical_info'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['clinical_info'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'ParticipantBarcode': 'TCGA-AB-2908', 'SampleBarcode': 'TCGA-AB-2908-03A', 'AliquotBarcode': 'TCGA-AB-2908-03A-01T-0740-13', 'SampleTypeLetterCode': 'TB', 'SampleType': 'Primary Blood Derived Cancer - Peripheral Blood', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'SampleBarcode': 'TCGA-19-5960-01A', 'AliquotBarcode': 'TCGA-19-5960-01A-11R-1850-01', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'SampleBarcode': 'TCGA-21-1071-01A', 'AliquotBarcode': 'TCGA-21-1071-01A-01R-0692-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'SampleBarcode': 'TCGA-30-1862-01A', 'AliquotBarcode': 'TCGA-30-1862-01A-02R-1568-13', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'SampleBarcode': 'TCGA-66-2795-01A', 'AliquotBarcode': 'TCGA-66-2795-01A-02R-0980-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '613.474'}], 'var_functions.execute_python:20': {'patient_count': 220, 'histology_types': [['Oligodendroglioma', 189], ['Paraganglioma', 18], ['Paraganglioma; Extra-adrenal Pheochromocytoma', 13]], 'first_five_patients': [{'barcode': 'TCGA-DB', 'histological_type': 'Oligodendroglioma'}, {'barcode': 'TCGA-P5', 'histological_type': 'Oligodendroglioma'}, {'barcode': 'TCGA-TM', 'histological_type': 'Oligodendroglioma'}, {'barcode': 'TCGA-DH', 'histological_type': 'Oligodendroglioma'}, {'barcode': 'TCGA-P5', 'histological_type': 'Oligodendroglioma'}]}, 'var_functions.execute_python:22': {'unique_patient_count': 220, 'total_records': 220, 'first_10_barcode': ['TCGA-DB-A64P', 'TCGA-P5-A5F0', 'TCGA-TM-A84R', 'TCGA-DH-A7US', 'TCGA-P5-A5F4', 'TCGA-IK-7675', 'TCGA-HW-A5KJ', 'TCGA-S9-A7J3', 'TCGA-DB-A4XG', 'TCGA-VM-A8CA'], 'first_10_histologies': ['Oligodendroglioma', 'Oligodendroglioma', 'Oligodendroglioma', 'Oligodendroglioma', 'Oligodendroglioma', 'Oligodendroglioma', 'Oligodendroglioma', 'Oligodendroglioma', 'Oligodendroglioma', 'Oligodendroglioma'], 'histology_distribution': [['Oligodendroglioma', 189], ['Paraganglioma', 18], ['Paraganglioma; Extra-adrenal Pheochromocytoma', 13]]}, 'var_functions.query_db:24': [{'ParticipantBarcode': 'TCGA-E1-A7Z2', 'SampleBarcode': 'TCGA-E1-A7Z2-01A', 'AliquotBarcode': 'TCGA-E1-A7Z2-01A-21R-A34R-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '173.521'}, {'ParticipantBarcode': 'TCGA-QH-A86X', 'SampleBarcode': 'TCGA-QH-A86X-01A', 'AliquotBarcode': 'TCGA-QH-A86X-01A-11R-A36H-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '427.57'}, {'ParticipantBarcode': 'TCGA-DB-A64V', 'SampleBarcode': 'TCGA-DB-A64V-01A', 'AliquotBarcode': 'TCGA-DB-A64V-01A-11R-A29R-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '1509.87'}, {'ParticipantBarcode': 'TCGA-DH-A7US', 'SampleBarcode': 'TCGA-DH-A7US-01A', 'AliquotBarcode': 'TCGA-DH-A7US-01A-11R-A33Z-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '418.886'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'barcode_count': 220, 'first_10_barcodes': ['TCGA-DB-A64P', 'TCGA-P5-A5F0', 'TCGA-TM-A84R', 'TCGA-DH-A7US', 'TCGA-P5-A5F4', 'TCGA-IK-7675', 'TCGA-HW-A5KJ', 'TCGA-S9-A7J3', 'TCGA-DB-A4XG', 'TCGA-VM-A8CA'], 'sql_query_preview': "SELECT * FROM RNASeq_Expression WHERE Symbol = 'IGF2' AND ParticipantBarcode IN ('TCGA-DB-A64P','TCGA-P5-A5F0','TCGA-TM-A84R','TCGA-DH-A7US','TCGA-P5-A5F4','TCGA-IK-7675','TCGA-HW-A..."}, 'var_functions.query_db:30': [{'ParticipantBarcode': 'TCGA-CS-6670', 'SampleBarcode': 'TCGA-CS-6670-01A', 'AliquotBarcode': 'TCGA-CS-6670-01A-11R-1896-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '381.503'}, {'ParticipantBarcode': 'TCGA-DB-A64V', 'SampleBarcode': 'TCGA-DB-A64V-01A', 'AliquotBarcode': 'TCGA-DB-A64V-01A-11R-A29R-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '1509.87'}, {'ParticipantBarcode': 'TCGA-DH-A7US', 'SampleBarcode': 'TCGA-DH-A7US-01A', 'AliquotBarcode': 'TCGA-DH-A7US-01A-11R-A33Z-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '418.886'}, {'ParticipantBarcode': 'TCGA-QH-A86X', 'SampleBarcode': 'TCGA-QH-A86X-01A', 'AliquotBarcode': 'TCGA-QH-A86X-01A-11R-A36H-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '427.57'}, {'ParticipantBarcode': 'TCGA-E1-A7Z2', 'SampleBarcode': 'TCGA-E1-A7Z2-01A', 'AliquotBarcode': 'TCGA-E1-A7Z2-01A-21R-A34R-07', 'SampleTypeLetterCode': 'TP', 'SampleType': 'Primary solid Tumor', 'Symbol': 'IGF2', 'Entrez': '3481', 'normalized_count': '173.521'}], 'var_functions.query_db:32': [{'ParticipantBarcode': 'TCGA-CS-6670', 'Symbol': 'IGF2', 'normalized_count': '381.503'}, {'ParticipantBarcode': 'TCGA-DB-A64V', 'Symbol': 'IGF2', 'normalized_count': '1509.87'}, {'ParticipantBarcode': 'TCGA-DH-A7US', 'Symbol': 'IGF2', 'normalized_count': '418.886'}, {'ParticipantBarcode': 'TCGA-E1-A7Z2', 'Symbol': 'IGF2', 'normalized_count': '173.521'}, {'ParticipantBarcode': 'TCGA-QH-A86X', 'Symbol': 'IGF2', 'normalized_count': '427.57'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
