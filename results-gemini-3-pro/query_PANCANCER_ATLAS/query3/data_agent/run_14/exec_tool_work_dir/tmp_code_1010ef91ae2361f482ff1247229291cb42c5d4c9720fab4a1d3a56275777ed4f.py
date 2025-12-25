code = """import json
import pandas as pd
import re
import traceback

try:
    with open(locals()['var_function-call-3480703303480285917'], 'r') as f:
        clinical_data = json.load(f)

    with open(locals()['var_function-call-6096349508840927938'], 'r') as f:
        mutation_data = json.load(f)

    clinical_list = []
    for entry in clinical_data:
        desc = entry.get('Patient_description', '')
        hist_type = entry.get('histological_type')
        match = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
        if match:
            barcode = match.group(1)
            if hist_type and hist_type != 'None':
                clinical_list.append({'Barcode': barcode, 'Histological_Type': hist_type})

    df_clinical = pd.DataFrame(clinical_list)
    
    if df_clinical.empty:
        raise ValueError("df_clinical is empty")

    mutation_barcodes = set()
    for entry in mutation_data:
        b = entry.get('ParticipantBarcode')
        if b:
            mutation_barcodes.add(b[:12])

    df_clinical['Has_Mutation'] = df_clinical['Barcode'].apply(lambda x: x in mutation_barcodes)

    ct = pd.crosstab(df_clinical['Histological_Type'], df_clinical['Has_Mutation'])

    for col in [False, True]:
        if col not in ct.columns:
            ct[col] = 0
    ct = ct[[False, True]]

    row_sums = ct.sum(axis=1)
    filtered_table = ct[row_sums > 10]
    
    # Check if we have enough data
    if filtered_table.shape[0] < 2:
        # Not enough categories for association?
        # Chi-square usually implies >=2 rows.
        # But if the formula is generic goodness of fit or independence?
        # Independence: (r-1)(c-1) df. If r=1, df=0.
        # We'll calculate the value anyway using the formula provided.
        pass

    grand_total = filtered_table.values.sum()
    col_totals = filtered_table.sum(axis=0)
    row_totals = filtered_table.sum(axis=1)
    
    chi2_stat = 0.0
    if grand_total > 0:
        for row_idx in filtered_table.index:
            r_total = row_totals[row_idx]
            for col_label in filtered_table.columns:
                c_total = col_totals[col_label]
                observed = filtered_table.at[row_idx, col_label]
                expected = (r_total * c_total) / grand_total
                if expected > 0:
                    chi2_stat += ((observed - expected) ** 2) / expected
    
    print("__RESULT__:")
    print(json.dumps(chi2_stat))

except Exception as e:
    print("__RESULT__:")
    print(json.dumps(f"Error: {str(e)}"))"""

env_args = {'var_function-call-7854171642018935874': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_function-call-18180327115781918543': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_function-call-8086918354594162213': [{'Patient_description': 'Patient TCGA-BT-A20V (FEMALE, UUID 24f21425-b001-4986-aedf-5b4dd851c6ad) is enrolled in the study of Bladder urothelial carcinoma. Vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Case A648D9BF-CF37-41FC-9515-E8F5AC85FCD4, linked to barcode TCGA-XF-A9SX, corresponds to a FEMALE patient diagnosed with Bladder urothelial carcinoma, with vital status Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'Record 234086DD-5A74-4FF1-94AB-BAD43EE69D5C refers to patient TCGA-DK-A2I2, a FEMALE diagnosed with Bladder urothelial carcinoma. Vital status recorded as Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'In the Bladder urothelial carcinoma dataset, patient TCGA-XF-A8HH (UUID 02964D82-CC94-4286-A66F-03567101950C) is recorded as a FEMALE with vital status: Dead.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}, {'Patient_description': 'The individual with barcode TCGA-ZF-A9R7 and UUID CE4E4549-BEFC-447F-9B79-ED46E302E6D7 is a FEMALE case of Bladder urothelial carcinoma, documented with vital status = Alive.', 'histological_type': 'Muscle invasive urothelial carcinoma (pT2 or above)'}], 'var_function-call-333261346705978443': 'file_storage/function-call-333261346705978443.json', 'var_function-call-6096349508840927938': 'file_storage/function-call-6096349508840927938.json', 'var_function-call-13160247121529640866': 'Done', 'var_function-call-710630576433707748': {'columns': ['False', 'True'], 'index': ['Muscle invasive urothelial carcinoma (pT2 or above)'], 'data': [[102, 6]], 'row_sums': [108]}, 'var_function-call-17121255186119575466': {'Muscle invasive urothelial carcinoma (pT2 or above)': 108}, 'var_function-call-14708463453089447761': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma'}, {'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'histological_type': 'Infiltrating Lobular Carcinoma'}, {'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}], 'var_function-call-3720035615667625394': {'None': 108}, 'var_function-call-3480703303480285917': 'file_storage/function-call-3480703303480285917.json'}

exec(code, env_args)
