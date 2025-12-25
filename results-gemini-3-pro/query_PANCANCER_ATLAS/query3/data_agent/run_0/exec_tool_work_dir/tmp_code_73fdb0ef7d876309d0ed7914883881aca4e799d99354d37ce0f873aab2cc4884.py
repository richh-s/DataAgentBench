code = """import json
import re

# Load Clinical Data
clinical_file = locals()['var_function-call-8916468336537709102']
with open(clinical_file, 'r') as f:
    clinical_data = json.load(f)

# Load Mutation Data
mutation_file = locals()['var_function-call-16499183128350860883']
with open(mutation_file, 'r') as f:
    mutation_data = json.load(f)
    
mutated_barcodes = set(item['ParticipantBarcode'] for item in mutation_data)

patients = []
cancer_names_set = set()

for entry in clinical_data:
    desc = entry.get('Patient_description', '')
    hist_type = entry.get('histological_type', 'None')
    
    # Barcode
    m_bc = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if not m_bc:
        continue
    barcode = m_bc.group(1)
    
    # Gender (Removed \b based on debugging)
    m_gen = re.search(r'(FEMALE|MALE)', desc)
    gender = m_gen.group(1) if m_gen else 'Unknown'
    
    # Cancer Name
    cancer_name = None
    patterns = [
        r"In the (.+?) dataset",
        r"study of (.+?)\.",
        r"diagnosed with (.+?)\.",
        r"belongs to the (.+?) cohort",
        r"case of (.+?), documented",
        r"subject with (.+?)\. Their"
    ]
    for pat in patterns:
        m = re.search(pat, desc)
        if m:
            raw_name = m.group(1)
            raw_name = raw_name.split(', with vital status')[0]
            cancer_name = raw_name.strip()
            break
            
    if cancer_name:
        cancer_names_set.add(cancer_name)
        
    patients.append({
        'Barcode': barcode,
        'Gender': gender,
        'CancerName': cancer_name,
        'HistologicalType': hist_type
    })

# Select Target Cancer
target_cancer = "Breast invasive carcinoma"
if target_cancer not in cancer_names_set:
    # Fallback or check
    if "Bladder urothelial carcinoma" in cancer_names_set:
        target_cancer = "Bladder urothelial carcinoma"

# Filter and Count
counts = {}
cohort_size = 0

for p in patients:
    if p['CancerName'] == target_cancer and p['Gender'] == 'FEMALE':
        cohort_size += 1
        h_type = p['HistologicalType']
        if h_type in ['None', '[Not Applicable]', 'Unknown', None]:
            continue
            
        is_mutated = p['Barcode'] in mutated_barcodes
        
        if h_type not in counts:
            counts[h_type] = {'Mutated': 0, 'WildType': 0}
        
        if is_mutated:
            counts[h_type]['Mutated'] += 1
        else:
            counts[h_type]['WildType'] += 1

# Filter marginal totals <= 10
valid_counts = {}
for h_type, vals in counts.items():
    total = vals['Mutated'] + vals['WildType']
    if total > 10:
        valid_counts[h_type] = vals

# Calculate Chi-Square
grand_total = 0
row_totals = []
col_totals = [0, 0] # [Mutated, WildType]
observed_matrix = []
sorted_hist_types = sorted(valid_counts.keys())

for h_type in sorted_hist_types:
    mut = valid_counts[h_type]['Mutated']
    wt = valid_counts[h_type]['WildType']
    
    row_sum = mut + wt
    row_totals.append(row_sum)
    
    col_totals[0] += mut
    col_totals[1] += wt
    
    grand_total += row_sum
    observed_matrix.append([mut, wt])

chi2_stat = 0
if grand_total > 0:
    for i in range(len(row_totals)):
        for j in range(len(col_totals)):
            e = (row_totals[i] * col_totals[j]) / grand_total
            if e > 0:
                o = observed_matrix[i][j]
                chi2_stat += ((o - e) ** 2) / e

result = {
    "target_cancer": target_cancer,
    "cohort_size": cohort_size,
    "chi_square_statistic": chi2_stat,
    "degrees_of_freedom": (len(row_totals) - 1) * (len(col_totals) - 1) if len(row_totals) > 0 else 0,
    "valid_histological_types": sorted_hist_types,
    "counts": valid_counts
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16885241436338951520': ['clinical_info'], 'var_function-call-11810306831500174421': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-3126046614530830882': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_function-call-8590567274006828467': [{'count': '10761'}], 'var_function-call-8916468336537709102': 'file_storage/function-call-8916468336537709102.json', 'var_function-call-16499183128350860883': 'file_storage/function-call-16499183128350860883.json', 'var_function-call-11259357700728850213': {'target_cancer': 'Breast invasive carcinoma', 'available_cancers': ['Head and Neck squamous cell carcinoma, with vital status Dead', 'Cholangiocarcinoma, with vital status Alive', 'Thyroid carcinoma, with vital status Alive', 'Ovarian serous cystadenocarcinoma, with vital status Dead', 'Prostate adenocarcinoma', 'Adrenocortical carcinoma, with vital status Alive', 'Brain lower grade glioma, with vital status Alive', 'Lymphoid Neoplasm Diffuse Large B-cell Lymphoma, with vital status Alive', 'Head and Neck squamous cell carcinoma', 'Adrenocortical carcinoma', 'Pheochromocytoma and Paraganglioma', 'Lung adenocarcinoma, with vital status Dead', 'Rectum adenocarcinoma, with vital status Dead', 'Bladder urothelial carcinoma', 'Breast invasive carcinoma, with vital status Dead', 'Uterine Carcinosarcoma, with vital status Alive', 'Uterine Carcinosarcoma', 'Liver hepatocellular carcinoma', 'Prostate adenocarcinoma, with vital status Alive', 'Bladder urothelial carcinoma, with vital status Alive', 'Glioblastoma multiforme, with vital status Dead', 'Glioblastoma multiforme', 'Mesothelioma', 'Lung adenocarcinoma', 'Bladder urothelial carcinoma, with vital status Dead', 'Thyroid carcinoma, with vital status Dead', 'Lung squamous cell carcinoma, with vital status Dead', 'Rectum adenocarcinoma', 'Sarcoma, with vital status Dead', 'Adrenocortical carcinoma, with vital status Dead', 'Pheochromocytoma and Paraganglioma, with vital status Alive', 'Cholangiocarcinoma', 'Pancreatic adenocarcinoma', 'Kidney renal clear cell carcinoma, with vital status Alive', 'Colon adenocarcinoma, with vital status Alive', 'Thymoma, with vital status Alive', 'Esophageal carcinoma, with vital status Alive', 'Brain lower grade glioma, with vital status Dead', 'Skin Cutaneous Melanoma', 'Stomach adenocarcinoma, with vital status Alive', 'Lymphoid Neoplasm Diffuse Large B-cell Lymphoma', 'Pancreatic adenocarcinoma, with vital status Alive', 'Breast invasive carcinoma', 'Kidney Chromophobe, with vital status Alive', 'Glioblastoma multiforme, with vital status Alive', 'Liver hepatocellular carcinoma, with vital status Alive', 'Skin Cutaneous Melanoma, with vital status Dead', 'Cervical squamous cell carcinoma and endocervical adenocarcinoma, with vital status Dead', 'Brain lower grade glioma', 'Uveal Melanoma', 'Prostate adenocarcinoma, with vital status Dead', 'Skin Cutaneous Melanoma, with vital status Alive', 'Sarcoma', 'Kidney Chromophobe', 'Mesothelioma, with vital status Dead', 'Kidney renal papillary cell carcinoma', 'Kidney renal clear cell carcinoma, with vital status Dead', 'Pancreatic adenocarcinoma, with vital status Dead', 'Uveal Melanoma, with vital status Dead', 'Lung squamous cell carcinoma, with vital status Alive', 'Uterine Corpus Endometrial Carcinoma, with vital status Alive', 'Uterine Corpus Endometrial Carcinoma', 'Breast invasive carcinoma, with vital status Alive', 'Esophageal carcinoma', 'Cholangiocarcinoma, with vital status Dead', 'Cervical squamous cell carcinoma and endocervical adenocarcinoma', 'Lung squamous cell carcinoma', 'Kidney renal clear cell carcinoma', 'Uveal Melanoma, with vital status Alive', 'Lung adenocarcinoma, with vital status Alive', 'Colon adenocarcinoma, with vital status Dead', 'Ovarian serous cystadenocarcinoma', 'Stomach adenocarcinoma', 'Kidney renal papillary cell carcinoma, with vital status Dead', 'Sarcoma, with vital status Alive', 'Testicular Germ Cell Tumors, with vital status Dead', 'Kidney renal papillary cell carcinoma, with vital status Alive', 'Rectum adenocarcinoma, with vital status Alive', 'Cervical squamous cell carcinoma and endocervical adenocarcinoma, with vital status Alive', 'Stomach adenocarcinoma, with vital status Dead', 'Ovarian serous cystadenocarcinoma, with vital status Alive', 'Testicular Germ Cell Tumors, with vital status Alive', 'Uterine Corpus Endometrial Carcinoma, with vital status Dead', 'Testicular Germ Cell Tumors', 'Thymoma', 'Uterine Carcinosarcoma, with vital status Dead', 'Thyroid carcinoma', 'Esophageal carcinoma, with vital status Dead', 'Head and Neck squamous cell carcinoma, with vital status Alive', 'Colon adenocarcinoma', 'Liver hepatocellular carcinoma, with vital status Dead'], 'chi_square_statistic': 0, 'valid_histological_types': [], 'observed_counts': {}}, 'var_function-call-591096022168053694': {'target_cancer': 'Breast invasive carcinoma', 'chi_square_statistic': 0, 'valid_histological_types': [], 'counts': {}}, 'var_function-call-9861487407748466410': {'cohort_size': 0, 'histological_dist': {}}, 'var_function-call-12881639829241540721': ['Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.'], 'var_function-call-3638234194744859943': [{'desc': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'parsed_gender': 'Unknown', 'parsed_cancer': 'Breast invasive carcinoma'}, {'desc': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'parsed_gender': 'Unknown', 'parsed_cancer': 'Breast invasive carcinoma'}, {'desc': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'parsed_gender': 'Unknown', 'parsed_cancer': 'Breast invasive carcinoma'}, {'desc': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'parsed_gender': 'Unknown', 'parsed_cancer': 'Breast invasive carcinoma'}, {'desc': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'parsed_gender': 'Unknown', 'parsed_cancer': 'Breast invasive carcinoma'}], 'var_function-call-16207027024253342628': [{'desc': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'found_genders': ['FEMALE']}, {'desc': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'found_genders': ['FEMALE']}, {'desc': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'found_genders': ['FEMALE']}, {'desc': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'found_genders': ['FEMALE']}, {'desc': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'found_genders': ['FEMALE']}]}

exec(code, env_args)
