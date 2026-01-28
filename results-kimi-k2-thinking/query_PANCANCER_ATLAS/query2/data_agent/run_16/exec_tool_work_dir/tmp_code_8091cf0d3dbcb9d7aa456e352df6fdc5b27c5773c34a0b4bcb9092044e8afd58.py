code = """import json
import re
from collections import defaultdict

# Access the data from storage
brca_alive_patients = locals()['var_functions.query_db:28']

# Process patients - extract barcode and histological type
patients_with_histology = []

for patient in brca_alive_patients:
    description = patient.get('Patient_description', '')
    hist_type = patient.get('histological_type', 'Unknown')
    
    # Extract TCGA barcode
    barcode_match = re.search(r'(TCGA-[A-Z0-9]+-[A-Z0-9]+)', description)
    if barcode_match:
        barcode = barcode_match.group(1)
        patients_with_histology.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type
        })

# Get CDH1 mutation barcodes
cdh1_mutations = locals()['var_functions.query_db:26']
cdh1_barcodes = set(m['ParticipantBarcode'] for m in cdh1_mutations)

# For each histological type, calculate percentage of patients with CDH1 mutation
hist_type_stats = defaultdict(lambda: {'total': 0, 'mutated': 0})

for patient in patients_with_histology:
    hist_type = patient['histological_type']
    barcode = patient['ParticipantBarcode']
    
    hist_type_stats[hist_type]['total'] += 1
    if barcode in cdh1_barcodes:
        hist_type_stats[hist_type]['mutated'] += 1

# Calculate percentages
results = []
for hist_type, stats in hist_type_stats.items():
    if stats['total'] >= 3:  # Include types with at least 3 patients
        percentage = (stats['mutated'] / stats['total']) * 100
        results.append({
            'histological_type': hist_type,
            'total_patients': stats['total'],
            'mutated_patients': stats['mutated'],
            'mutation_percentage': round(percentage, 2)
        })

# Sort by percentage and get top 3
top_3 = sorted(results, key=lambda x: x['mutation_percentage'], reverse=True)[:3]

# Also get overall statistics
total_patients = len(patients_with_histology)
total_mutated = sum(1 for p in patients_with_histology if p['ParticipantBarcode'] in cdh1_barcodes)
overall_percentage = round((total_mutated / total_patients) * 100, 2)

output = {
    'total_brca_alive_patients': total_patients,
    'overall_cdh1_mutation_rate': overall_percentage,
    'unique_histological_types': len(hist_type_stats),
    'top_3_histological_types': top_3
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:9': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:11': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.execute_python:24': {'total_patients_extracted': 500, 'unique_patients': 500, 'hist_type_distribution': {'Infiltrating Ductal Carcinoma': 341, 'Infiltrating Lobular Carcinoma': 111, 'Other  specify': 25, 'Metaplastic Carcinoma': 5, 'Infiltrating Carcinoma NOS': 1, 'Mucinous Carcinoma': 10, 'Medullary Carcinoma': 2, 'Mixed Histology (please specify)': 4, 'Leiomyosarcoma (LMS)': 1}, 'sample_patients': [{'ParticipantBarcode': 'TCGA-AC-A5EH', 'histological_type': 'Infiltrating Ductal Carcinoma', 'patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.'}, {'ParticipantBarcode': 'TCGA-LL-A7SZ', 'histological_type': 'Infiltrating Ductal Carcinoma', 'patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.'}, {'ParticipantBarcode': 'TCGA-AN-A0FY', 'histological_type': 'Infiltrating Ductal Carcinoma', 'patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive."}]}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
