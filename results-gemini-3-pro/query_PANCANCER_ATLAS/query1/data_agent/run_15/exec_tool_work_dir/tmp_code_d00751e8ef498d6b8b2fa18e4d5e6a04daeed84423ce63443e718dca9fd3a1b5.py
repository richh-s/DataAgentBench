code = """import json
import pandas as pd
import numpy as np
import re

# Load clinical data
with open(locals()['var_function-call-306403426989290109'], 'r') as f:
    clinical_data = json.load(f)

# Load expression data
with open(locals()['var_function-call-15421238206356016169'], 'r') as f:
    expression_data = json.load(f)

# Regex for barcode
barcode_pattern = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')

# Process clinical data
clinical_dict = {}
for entry in clinical_data:
    desc = entry.get('Patient_description', '')
    hist = entry.get('histological_type', '')
    
    # Filter invalid histology
    if not hist or hist.startswith('[') or hist.endswith(']'):
        continue
        
    # Extract barcode
    match = barcode_pattern.search(desc)
    if match:
        barcode = match.group(1)
        clinical_dict[barcode] = hist

# Process expression data
results = {} # {histology: [values]}

for entry in expression_data:
    p_barcode = entry.get('ParticipantBarcode', '')
    count_str = entry.get('normalized_count', '0')
    
    try:
        count = float(count_str)
    except:
        continue
        
    # Extract 12-char barcode just in case, though it seems to be 12 chars already
    # If p_barcode is like TCGA-AB-2908-01...
    # match = barcode_pattern.search(p_barcode)
    # if match:
    #    p_barcode_clean = match.group(1)
    # else:
    #    p_barcode_clean = p_barcode[:12]
    
    # Actually, let's just take the first 12 chars if it starts with TCGA
    if p_barcode.startswith('TCGA'):
        p_barcode_clean = p_barcode[:12]
    else:
        p_barcode_clean = p_barcode
        
    if p_barcode_clean in clinical_dict:
        hist = clinical_dict[p_barcode_clean]
        
        # Log10 transform
        val = np.log10(count + 1)
        
        if hist not in results:
            results[hist] = []
        results[hist].append(val)

# Compute averages
final_averages = {}
for hist, vals in results.items():
    avg = np.mean(vals)
    final_averages[hist] = round(avg, 4)

print("__RESULT__:")
print(json.dumps(final_averages))"""

env_args = {'var_function-call-851189100024032710': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-17822574276987267104': [{'Patient_description': 'Case 739CC9F1-71BE-4F81-A5D1-EDA673903E45, linked to barcode TCGA-RY-A83X, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligodendroglioma'}, {'Patient_description': 'The individual with barcode TCGA-FG-A60K and UUID A85AEBDA-B182-41BA-815A-3FF055E22829 is a FEMALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Patient TCGA-DB-A4XH (UUID 5CCD86AB-2587-4F35-B96A-4F4320B10FB9) is a FEMALE diagnosed with Brain lower grade glioma. Current vital status: Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'Case 1701F4AD-58C5-40D8-90C4-99E3ACAC0104, linked to barcode TCGA-DB-A4XE, corresponds to a FEMALE patient diagnosed with Brain lower grade glioma, with vital status Alive.', 'histological_type': 'Oligoastrocytoma'}, {'Patient_description': 'The individual with barcode TCGA-DB-A4XC and UUID 33615113-791B-4286-A23A-AD3D1F8D4B09 is a MALE case of Brain lower grade glioma, documented with vital status = Alive.', 'histological_type': 'Oligoastrocytoma'}], 'var_function-call-6918755380265797397': [{'ParticipantBarcode': 'TCGA-AB-2908', 'Symbol': 'IGF2', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'Symbol': 'IGF2', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'Symbol': 'IGF2', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'Symbol': 'IGF2', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'Symbol': 'IGF2', 'normalized_count': '613.474'}], 'var_function-call-306403426989290109': 'file_storage/function-call-306403426989290109.json', 'var_function-call-15421238206356016169': 'file_storage/function-call-15421238206356016169.json'}

exec(code, env_args)
