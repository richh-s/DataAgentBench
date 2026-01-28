code = """import json
import re

# Load comprehensive BRCA clinical data from file
clinical_data_file = var_functions.query_db:48
with open(clinical_data_file, 'r') as f:
    brca_patients = json.load(f)

print('Loaded', len(brca_patients), 'BRCA patients')

# Parse patient information
alive_brca_barcodes = []
all_brca_data = []
for patient in brca_patients:
    desc = patient['Patient_description']
    hist_type = patient['histological_type']
    # Extract barcode
    match = re.search(r'(TCGA-\w{2}-\w{4})', desc)
    if match:
        barcode = match.group(1)
        is_alive = 'vital status is Alive' in desc or 'vital status: Alive' in desc or 'vital status = Alive' in desc
        all_brca_data.append({'barcode': barcode, 'alive': is_alive, 'hist_type': hist_type})
        if is_alive:
            alive_brca_barcodes.append(barcode)

print('Total BRCA patients:', len(all_brca_data))
print('Alive BRCA patients:', len(alive_brca_barcodes))

# Load CDH1 mutation data
cdh1_records = var_functions.query_db:34
cdh1_barcodes = list(set([record['ParticipantBarcode'] for record in cdh1_records]))
print('Patients with CDH1 mutations:', cdh1_barcodes)

# Count histological types among alive patients and CDH1 mutated patients
from collections import Counter
hist_alive_total = Counter()
hist_with_cdh1 = Counter()

for patient in all_brca_data:
    if patient['alive']:
        hist_type = patient['hist_type']
        hist_alive_total[hist_type] += 1
        if patient['barcode'] in cdh1_barcodes:
            hist_with_cdh1[hist_type] += 1

print('\nAlive BRCA patients by histological type:')
for hist, count in sorted(hist_alive_total.items(), key=lambda x: x[1], reverse=True):
    print(' ', hist, ':', count)

print('\nCDH1 mutations by histological type:')
for hist, count in hist_with_cdh1.items():
    print(' ', hist, ':', count)

# Calculate percentages and sort
results = []
for hist_type, cdh1_count in hist_with_cdh1.items():
    total = hist_alive_total[hist_type]
    pct = (cdh1_count / total * 100) if total > 0 else 0
    results.append({'hist_type': hist_type, 'cdh1_count': cdh1_count, 'total_alive': total, 'percentage': round(pct, 2)})

results.sort(key=lambda x: x['percentage'], reverse=True)

print('\nTop histological types by CDH1 mutation percentage:')
for i, r in enumerate(results[:5], 1):
    print(f"{i}. {r['hist_type']}: {r['percentage']}% ({r['cdh1_count']}/{r['total_alive']})")

output = {'top_3': results[:3], 'all_results': results}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_functions.query_db:8': [{'Patient_description': "Patient TCGA-DK-A6AW, registered under UUID 01C815BA-7BDA-4F7E-865C-0C5776FEBF2C, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-GD-A3OQ (UUID 2E85C30C-C4C4-4096-9EEF-4EB2C7D991A3) is recorded as a MALE with vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'The individual with barcode TCGA-CF-A47W and UUID 122FC134-8915-47DB-96C9-AB1853C3CD18 is a MALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Patient TCGA-CF-A3MF (MALE, UUID 1E308B12-0590-4DAE-94D0-A539FCF25DF7) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Case DE810AF0-4C18-4E8F-9836-F8ABC425E3EB, linked to barcode TCGA-DK-A2I6, corresponds to a MALE patient diagnosed with Bladder urothelial carcinoma, with vital status Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Patient TCGA-BT-A20V (FEMALE, UUID 24f21425-b001-4986-aedf-5b4dd851c6ad) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Record 35C7BB8A-7B5C-488D-9D3A-725B24D14478 refers to patient TCGA-4Z-AA81, a MALE diagnosed with Bladder urothelial carcinoma. Vital status recorded as Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Case A648D9BF-CF37-41FC-9515-E8F5AC85FCD4, linked to barcode TCGA-XF-A9SX, corresponds to a FEMALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Patient TCGA-XF-A8HE (MALE, UUID 841B4582-A268-4A55-A9A2-47C7E5C3B69F) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Case 679a6869-2ce9-4472-8db1-8869e2c1a440, linked to barcode TCGA-CU-A0YN, corresponds to a MALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:26': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-EO-A22U', 'Tumor_SampleBarcode': 'TCGA-EO-A22U-01A', 'Tumor_AliquotBarcode': 'TCGA-EO-A22U-01A-11D-A17W-09', 'Normal_SampleBarcode': 'TCGA-EO-A22U-10B', 'Normal_AliquotBarcode': 'TCGA-EO-A22U-10B-01D-A17W-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'MUM1L1', 'HGVSp_Short': 'p.Y134Ifs*5', 'Variant_Classification': 'Frame_Shift_Ins', 'HGVSc': 'c.399dupA', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}, {'ParticipantBarcode': 'TCGA-02-2466', 'Tumor_SampleBarcode': 'TCGA-02-2466-01A', 'Tumor_AliquotBarcode': 'TCGA-02-2466-01A-01W-0837-08', 'Normal_SampleBarcode': 'TCGA-02-2466-10A', 'Normal_AliquotBarcode': 'TCGA-02-2466-10A-01W-0837-08', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'CSF2RA', 'HGVSp_Short': 'p.S351P', 'Variant_Classification': 'Missense_Mutation', 'HGVSc': 'c.1051T>C', 'CENTERS': 'MUTECT|MUSE', 'FILTER': 'wga'}], 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json', 'var_functions.query_db:34': [{'ParticipantBarcode': 'TCGA-DK-A6AW', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-HQ-A2OF', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-XF-A9T3', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-KQ-A41S', 'Hugo_Symbol': 'CDH1'}, {'ParticipantBarcode': 'TCGA-KQ-A41S', 'Hugo_Symbol': 'CDH1'}], 'var_functions.execute_python:40': {'alive_count': 145, 'cdh1_count': 5}, 'var_functions.query_db:46': [{'Patient_description': "Patient TCGA-DK-A6AW, registered under UUID 01C815BA-7BDA-4F7E-865C-0C5776FEBF2C, belongs to the Bladder urothelial carcinoma cohort. This MALE patient's vital status is Alive.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Patient TCGA-KQ-A41S (UUID CC8602BB-78E2-4732-9784-83C3388B999E) is a FEMALE diagnosed with Bladder urothelial carcinoma. Current vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': "Patient TCGA-HQ-A2OF, registered under UUID 691ADAA9-196A-4B62-9437-640C4AE6E2B2, belongs to the Bladder urothelial carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-XF-A9T3 (UUID 5F7C3B2D-9A5B-470F-BD12-9C7787A543F0) is recorded as a FEMALE with vital status: Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
