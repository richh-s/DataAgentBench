code = """import json
import pandas as pd
import re
import scipy.stats as stats

# Load data
with open(locals()['var_function-call-8274837993436129523'], 'r') as f:
    clinical_data = json.load(f)

with open(locals()['var_function-call-12632565715066766670'], 'r') as f:
    mutation_data = json.load(f)

# Extract mutated barcodes
mutated_barcodes = set(item['ParticipantBarcode'] for item in mutation_data)

# Process clinical data
parsed_patients = []
for entry in clinical_data:
    desc = entry['Patient_description']
    hist_type = entry['histological_type']
    
    # Extract Barcode
    barcode_match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    barcode = barcode_match.group(1) if barcode_match else None
    
    # Extract Gender
    gender_match = re.search(r'\\b(FEMALE|MALE)\\b', desc)
    gender = gender_match.group(1) if gender_match else None
    
    # Identify Cancer Type
    cancer_type = None
    if "Bladder Urothelial Carcinoma" in desc or "Bladder urothelial carcinoma" in desc:
        cancer_type = "Bladder Urothelial Carcinoma"
    elif "Breast Invasive Carcinoma" in desc or "Breast invasive carcinoma" in desc:
        cancer_type = "Breast Invasive Carcinoma"
    else:
        cancer_type = "Other"
        
    if barcode and gender:
        parsed_patients.append({
            'barcode': barcode,
            'gender': gender,
            'cancer_type': cancer_type,
            'histological_type': hist_type
        })

df = pd.DataFrame(parsed_patients)
df_female = df[df['gender'] == 'FEMALE']

print('Counts by cancer type (Female):')
print(df_female['cancer_type'].value_counts())

# Decision based on hint: BRCA = Bladder Urothelial Carcinoma
# But verify if data exists.
count_bladder = df_female[df_female['cancer_type'] == 'Bladder Urothelial Carcinoma'].shape[0]
count_breast = df_female[df_female['cancer_type'] == 'Breast Invasive Carcinoma'].shape[0]

if count_bladder > 0:
    target_cancer = 'Bladder Urothelial Carcinoma'
    print('Selected Bladder Urothelial Carcinoma based on hint.')
elif count_breast > 0:
    target_cancer = 'Breast Invasive Carcinoma'
    print('Selected Breast Invasive Carcinoma (fallback).')
else:
    target_cancer = None
    print('No matching cancer type found.')

if target_cancer:
    target_df = df_female[df_female['cancer_type'] == target_cancer].copy()
    
    # Filter valid histological type
    target_df = target_df[target_df['histological_type'].notna()]
    target_df = target_df[target_df['histological_type'] != 'None']

    # Mutation status
    target_df['has_CDH1_mutation'] = target_df['barcode'].apply(lambda x: 1 if x in mutated_barcodes else 0)
    
    # Filter marginal totals <= 10
    hist_counts = target_df['histological_type'].value_counts()
    print('Hist counts:')
    print(hist_counts)
    
    valid_hist_types = hist_counts[hist_counts > 10].index.tolist()
    final_df = target_df[target_df['histological_type'].isin(valid_hist_types)]
    
    print('Final DF shape:', final_df.shape)
    
    contingency_table = pd.crosstab(final_df['histological_type'], final_df['has_CDH1_mutation'])
    print('Contingency Table:')
    print(contingency_table)
    
    if contingency_table.empty or contingency_table.shape[0] < 2:
        # If less than 2 rows, Chi-square test isn't suitable for association between types.
        # But if 2+ rows, we proceed.
        # Check dimensions. 
        # If only 1 column (all mutated or all not), can't compute?
        # stats.chi2_contingency handles it but returns 0 or nan?
        # We need at least 2x2 ideally, or RxC.
        result = "Insufficient data"
    else:
        # Check if we have variation in mutation column
        if contingency_table.shape[1] < 2:
             # Only 0s or Only 1s
             result = "No variation in mutation status"
        else:
             chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
             result = chi2
else:
    result = "No target cancer found"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-16424533104229354194': ['clinical_info'], 'var_function-call-9655096740930957648': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-9508474626360991202': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_function-call-15156480802812079322': [{'count': '10761'}], 'var_function-call-8274837993436129523': 'file_storage/function-call-8274837993436129523.json', 'var_function-call-12632565715066766670': 'file_storage/function-call-12632565715066766670.json'}

exec(code, env_args)
