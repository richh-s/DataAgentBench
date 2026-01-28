code = """import json
import re

# Load LGG patients data
lgg_file = var_functions.query_db_28
if isinstance(lgg_file, str):
    with open(lgg_file, 'r') as f:
        lgg_patients = json.load(f)
else:
    lgg_patients = lgg_file

print(f"Total LGG patients in clinical data: {len(lgg_patients)}")

# Extract barcode and histological type, filtering out those in square brackets
patient_data = []
for record in lgg_patients:
    desc = record.get('Patient_description', '')
    hist_type = record.get('histological_type', '')
    
    # Skip if histological type is in square brackets
    if hist_type.startswith('[') and hist_type.endswith(']'):
        continue
    
    # Extract TCGA barcode
    barcode_match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if barcode_match:
        barcode = barcode_match.group(1)
        patient_data.append({
            'ParticipantBarcode': barcode,
            'histological_type': hist_type
        })

print(f"LGG patients with valid histology: {len(patient_data)}")
print(f"Sample: {patient_data[:3]}")

# Count histological types
hist_counts = {}
for p in patient_data:
    ht = p['histological_type']
    hist_counts[ht] = hist_counts.get(ht, 0) + 1

print("\nHistological type distribution:")
for ht, count in sorted(hist_counts.items()):
    print(f"  {ht}: {count}")

# Save for next step
print('__RESULT__:')
print(json.dumps(patient_data))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:5': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_functions.query_db:6': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Paraganglioma'}, {'histological_type': 'Paraganglioma; Extra-adrenal Pheochromocytoma'}], 'var_functions.list_db:8': ['clinical_info'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:16': {'patients': [{'ParticipantBarcode': 'TCGA-RY-A83X', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-FG-A60K', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XH', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XE', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-DB-A4XC', 'histological_type': 'Oligoastrocytoma'}, {'ParticipantBarcode': 'TCGA-P5-A5F0', 'histological_type': 'Oligodendroglioma'}, {'ParticipantBarcode': 'TCGA-S9-A6U1', 'histological_type': 'Astrocytoma'}, {'ParticipantBarcode': 'TCGA-TM-A7C3', 'histological_type': 'Astrocytoma'}, {'ParticipantBarcode': 'TCGA-S9-A7R2', 'histological_type': 'Astrocytoma'}, {'ParticipantBarcode': 'TCGA-TM-A84R', 'histological_type': 'Oligodendroglioma'}], 'hist_types': {'Oligodendroglioma': 3, 'Oligoastrocytoma': 4, 'Astrocytoma': 3}}, 'var_functions.query_db:18': [], 'var_functions.list_db:20': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:22': [{'ParticipantBarcode': 'TCGA-FS-A1ZC'}, {'ParticipantBarcode': 'TCGA-P4-AAVM'}, {'ParticipantBarcode': 'TCGA-55-8092'}, {'ParticipantBarcode': 'TCGA-C5-A2M2'}, {'ParticipantBarcode': 'TCGA-HC-A9TH'}, {'ParticipantBarcode': 'TCGA-AG-4021'}, {'ParticipantBarcode': 'TCGA-A2-A259'}, {'ParticipantBarcode': 'TCGA-XU-A931'}, {'ParticipantBarcode': 'TCGA-BH-A0BP'}, {'ParticipantBarcode': 'TCGA-FE-A235'}, {'ParticipantBarcode': 'TCGA-OR-A5LS'}, {'ParticipantBarcode': 'TCGA-EE-A2M5'}, {'ParticipantBarcode': 'TCGA-22-A5C4'}, {'ParticipantBarcode': 'TCGA-AC-A2FO'}, {'ParticipantBarcode': 'TCGA-E9-A1N8'}, {'ParticipantBarcode': 'TCGA-HT-7478'}, {'ParticipantBarcode': 'TCGA-CR-6472'}, {'ParticipantBarcode': 'TCGA-CV-5436'}, {'ParticipantBarcode': 'TCGA-21-1071'}, {'ParticipantBarcode': 'TCGA-30-1862'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
