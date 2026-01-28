code = """import json
import re
from collections import defaultdict
import math

# Access clinical data
clinical_file = locals()['var_functions.query_db:16']
with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)

# Access CDH1 mutation data
cdh1_file = locals()['var_functions.query_db:26']
with open(cdh1_file, 'r') as f:
    cdh1_mutations = json.load(f)

# Get set of patients with CDH1 mutations
cdh1_barcodes = set(record['ParticipantBarcode'] for record in cdh1_mutations)

# Filter for BRCA female patients and match with CDH1 status
brca_female_data = []
for record in clinical_data:
    patient_desc = record.get('Patient_description', '').lower()
    hist_type = record.get('histological_type', 'None')
    
    # Check for BRCA female patients with known histological type
    if ('breast' in patient_desc or 'brca' in patient_desc) and 'female' in patient_desc:
        if hist_type and hist_type != 'None' and hist_type != 'Not Available':
            barcode_match = re.search(r'(TCGA-\S+)', record.get('Patient_description', ''))
            if barcode_match:
                barcode = barcode_match.group(1)
                has_cdh1 = barcode in cdh1_barcodes
                brca_female_data.append({
                    'barcode': barcode,
                    'histological_type': hist_type,
                    'cdh1_mutation': has_cdh1
                })

# Group by histological type and CDH1 status
contingency_table = defaultdict(lambda: {'cdh1_mutated': 0, 'cdh1_wildtype': 0})
for patient in brca_female_data:
    hist_type = patient['histological_type']
    if patient['cdh1_mutation']:
        contingency_table[hist_type]['cdh1_mutated'] += 1
    else:
        contingency_table[hist_type]['cdh1_wildtype'] += 1

# Filter out categories with row totals <= 10
filtered_table = {}
for hist_type, counts in contingency_table.items():
    row_total = counts['cdh1_mutated'] + counts['cdh1_wildtype']
    if row_total > 10:
        filtered_table[hist_type] = counts

# Calculate chi-square statistic
cdh1_mutated_total = sum(counts['cdh1_mutated'] for counts in filtered_table.values())
cdh1_wildtype_total = sum(counts['cdh1_wildtype'] for counts in filtered_table.values())
grand_total = cdh1_mutated_total + cdh1_wildtype_total

chi_square = 0
chi_square_components = []

for hist_type, counts in filtered_table.items():
    row_total = counts['cdh1_mutated'] + counts['cdh1_wildtype']
    
    # Expected values for CDH1 mutated
    expected_mutated = (row_total * cdh1_mutated_total) / grand_total
    
    # Expected values for CDH1 wildtype
    expected_wildtype = (row_total * cdh1_wildtype_total) / grand_total
    
    # Calculate components
    observed_mutated = counts['cdh1_mutated']
    observed_wildtype = counts['cdh1_wildtype']
    
    component_mutated = ((observed_mutated - expected_mutated) ** 2) / expected_mutated
    component_wildtype = ((observed_wildtype - expected_wildtype) ** 2) / expected_wildtype
    
    chi_square += component_mutated + component_wildtype
    
    chi_square_components.append({
        'histological_type': hist_type,
        'observed_mutated': observed_mutated,
        'observed_wildtype': observed_wildtype,
        'expected_mutated': round(expected_mutated, 2),
        'expected_wildtype': round(expected_wildtype, 2),
        'component_mutated': round(component_mutated, 4),
        'component_wildtype': round(component_wildtype, 4)
    })

results = {
    'filtered_contingency_table': filtered_table,
    'chi_square_statistic': round(chi_square, 4),
    'degrees_of_freedom': len(filtered_table) - 1,
    'cdh1_mutated_total': cdh1_mutated_total,
    'cdh1_wildtype_total': cdh1_wildtype_total,
    'grand_total': grand_total,
    'chi_square_components': chi_square_components
}

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.execute_python:8': {'total_records': 5, 'genders': ['FEMALE'], 'histological_types_sample': ['Serous Cystadenocarcinoma'], 'histological_types_count': 1, 'patient_barcodes_count': 5}, 'var_functions.query_db:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'found_brca': False, 'brca_count': 0, 'brca_barcodes': []}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_records': 10000, 'sample_record_0': {'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'nan', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'nan', 'weight': 'nan', 'number_of_lymphnodes_positive_by_ihc': 'nan', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'nan', 'stopped_smoking_year': 'nan', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'nan', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'nan', 'total_aor_lnr': 'nan', 'prior_glioma': 'None'}}, 'var_functions.execute_python:20': {'brca_patient_count': 1075, 'brca_barcodes_count': 1075, 'sample_patients': [{'barcode': 'TCGA-AC-A5EH,', 'description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'barcode': 'TCGA-LL-A7SZ,', 'description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'barcode': 'TCGA-AN-A0FY,', 'description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'barcode': 'TCGA-AC-A2FB', 'description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'barcode': 'TCGA-AO-A1KR', 'description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}]}, 'var_functions.execute_python:22': {'total_brca_female_patients': 1074, 'histological_type_counts': {'Infiltrating Ductal Carcinoma': 766, 'Infiltrating Lobular Carcinoma': 201, 'Other  specify': 45, 'Metaplastic Carcinoma': 8, 'Infiltrating Carcinoma NOS': 1, 'Mucinous Carcinoma': 17, 'Medullary Carcinoma': 6, 'Mixed Histology (please specify)': 30}}, 'var_functions.query_db:24': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CMC4', 'HGVSp_Short': '.', 'Variant_Classification': 'Splice_Site', 'HGVSc': 'c.-10-2A>T', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'THADA', 'HGVSp_Short': 'p.I1462T', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.4385T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_cdh1_mutations': 261, 'unique_cdh1_barcodes': 247}, 'var_functions.execute_python:30': {'total_analysis_patients': 1074, 'contingency_table': {'Infiltrating Ductal Carcinoma': {'cdh1_mutated': 5, 'cdh1_wildtype': 761}, 'Infiltrating Lobular Carcinoma': {'cdh1_mutated': 43, 'cdh1_wildtype': 158}, 'Other  specify': {'cdh1_mutated': 1, 'cdh1_wildtype': 44}, 'Metaplastic Carcinoma': {'cdh1_mutated': 0, 'cdh1_wildtype': 8}, 'Infiltrating Carcinoma NOS': {'cdh1_mutated': 0, 'cdh1_wildtype': 1}, 'Mucinous Carcinoma': {'cdh1_mutated': 0, 'cdh1_wildtype': 17}, 'Medullary Carcinoma': {'cdh1_mutated': 0, 'cdh1_wildtype': 6}, 'Mixed Histology (please specify)': {'cdh1_mutated': 2, 'cdh1_wildtype': 28}}}}

exec(code, env_args)
