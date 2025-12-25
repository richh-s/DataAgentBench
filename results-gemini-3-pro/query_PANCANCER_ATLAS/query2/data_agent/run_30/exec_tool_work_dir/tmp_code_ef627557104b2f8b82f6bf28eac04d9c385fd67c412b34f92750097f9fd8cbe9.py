code = """import json
import re

file_path = locals()['var_function-call-3578721670386679657']
with open(file_path, 'r') as f:
    clinical_data = json.load(f)

# Regex patterns
barcode_pattern = re.compile(r"(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})")
vital_status_pattern = re.compile(r"vital status.*?(Alive|Dead)", re.IGNORECASE)

target_patients = []

for entry in clinical_data:
    desc = entry.get('Patient_description', '')
    hist_type = entry.get('histological_type', '')
    
    # Check for Breast Invasive Carcinoma
    if "Breast invasive carcinoma" not in desc and "Breast Invasive Carcinoma" not in desc:
        continue
        
    # Extract Barcode
    barcode_match = barcode_pattern.search(desc)
    if not barcode_match:
        continue
    barcode = barcode_match.group(1)
    
    # Extract Vital Status
    vital_match = vital_status_pattern.search(desc)
    if not vital_match:
        continue
    status = vital_match.group(1).capitalize()
    
    if status == "Alive":
        target_patients.append({'barcode': barcode, 'histological_type': hist_type})

# Load Mutation Data
mutation_file = locals()['var_function-call-3762801184127302826']
with open(mutation_file, 'r') as f:
    mutation_records = json.load(f)

mutated_patients = set(r['ParticipantBarcode'] for r in mutation_records)

# Stats
stats = {}
for p in target_patients:
    h_type = p['histological_type']
    pid = p['barcode']
    
    if h_type not in stats:
        stats[h_type] = {'total': 0, 'mutated': 0}
    
    stats[h_type]['total'] += 1
    if pid in mutated_patients:
        stats[h_type]['mutated'] += 1

results = []
for h_type, counts in stats.items():
    if h_type == 'None' or h_type is None:
        continue
    percentage = (counts['mutated'] / counts['total']) * 100
    results.append({
        'histological_type': h_type,
        'percentage': percentage,
        'count': counts['mutated'],
        'total': counts['total']
    })

results.sort(key=lambda x: x['percentage'], reverse=True)

print("__RESULT__:")
print(json.dumps(results[:5]))"""

env_args = {'var_function-call-13055555728011235960': ['clinical_info'], 'var_function-call-16643262182886110087': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-9457281706804386901': [{'count': '10761'}], 'var_function-call-12953876657794964614': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}, {'Patient_description': 'Patient TCGA-36-1576 (UUID 3445c524-5a37-40b6-8614-956d76eed939) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.'}, {'Patient_description': 'Record fdd4adb8-9295-480a-9352-305b5eb51187 refers to patient TCGA-25-2408, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Dead.'}, {'Patient_description': 'Record 6f25001a-f890-4fd0-a994-e62a9ea5c6f3 refers to patient TCGA-29-2427, a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Vital status recorded as Alive.'}, {'Patient_description': 'Case 9446e349-71e6-455a-aa8f-53ec96597146, linked to barcode TCGA-10-0933, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.'}], 'var_function-call-12547535175407997554': [{'ParticipantBarcode': 'TCGA-AX-A3G8', 'Tumor_SampleBarcode': 'TCGA-AX-A3G8-01A', 'Tumor_AliquotBarcode': 'TCGA-AX-A3G8-01A-11D-A228-09', 'Normal_SampleBarcode': 'TCGA-AX-A3G8-10A', 'Normal_AliquotBarcode': 'TCGA-AX-A3G8-10A-01D-A22A-09', 'Normal_SampleTypeLetterCode': 'NB', 'Hugo_Symbol': 'GLI3', 'HGVSp_Short': 'p.P1033Rfs*46', 'Variant_Classification': 'Frame_Shift_Del', 'HGVSc': 'c.3098delC', 'CENTERS': 'INDELOCATOR|VARSCANI', 'FILTER': 'ndp'}], 'var_function-call-3578721670386679657': 'file_storage/function-call-3578721670386679657.json', 'var_function-call-11577334636562803': {'count_bladder': 412, 'count_breast': 1087, 'sample_parsed': [{'barcode': 'TCGA-31-1953', 'histological_type': 'Serous Cystadenocarcinoma', 'vital_status': 'Alive', 'cancer_type': 'Ovarian Serous Cystadenocarcinoma'}, {'barcode': 'TCGA-36-1576', 'histological_type': 'Serous Cystadenocarcinoma', 'vital_status': 'Alive', 'cancer_type': 'Ovarian Serous Cystadenocarcinoma'}, {'barcode': 'TCGA-25-2408', 'histological_type': 'Serous Cystadenocarcinoma', 'vital_status': 'Recorded', 'cancer_type': 'Ovarian Serous Cystadenocarcinoma'}, {'barcode': 'TCGA-29-2427', 'histological_type': 'Serous Cystadenocarcinoma', 'vital_status': 'Recorded', 'cancer_type': 'Ovarian Serous Cystadenocarcinoma'}, {'barcode': 'TCGA-10-0933', 'histological_type': 'Serous Cystadenocarcinoma', 'vital_status': 'Dead', 'cancer_type': 'Ovarian Serous Cystadenocarcinoma'}]}, 'var_function-call-10185568822916147757': 'file_storage/function-call-10185568822916147757.json', 'var_function-call-3762801184127302826': 'file_storage/function-call-3762801184127302826.json', 'var_function-call-4127817848711562213': [{'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'percentage': 3.070175438596491, 'count': 7, 'total': 228}]}

exec(code, env_args)
