code = """import json
res = var_call_CsubguT2mL6An6p2MuT1MhGb
# build observed for rows_included
rows = res['rows_included']
observed = {}
for r in rows:
    observed[r['histological_type']] = [r['mut'], r['nomut']]
# totals
row_totals = {r['histological_type']: r['row_total'] for r in rows}
col_total_mut = sum([v[0] for v in observed.values()])
col_total_nomut = sum([v[1] for v in observed.values()])
grand_total = col_total_mut + col_total_nomut
# expected
expected = {}
chi2 = 0.0
for ht, (o_mut, o_nomut) in observed.items():
    row_total = row_totals[ht]
    e_mut = row_total * col_total_mut / grand_total
    e_nomut = row_total * col_total_nomut / grand_total
    expected[ht] = [e_mut, e_nomut]
    # components
    if e_mut>0:
        chi2 += (o_mut - e_mut)**2 / e_mut
    if e_nomut>0:
        chi2 += (o_nomut - e_nomut)**2 / e_nomut

df = (len(observed)-1)*(2-1)
output = {
    'chi2': chi2,
    'df': df,
    'grand_total': grand_total,
    'col_totals': {'mut': col_total_mut, 'nomut': col_total_nomut},
    'observed': observed,
    'expected': expected
}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_HDhJHt3AQ9Kiakg4pYZbagtT': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_h1ayRX9fxnFASddQJcUnEdhj': 'file_storage/call_h1ayRX9fxnFASddQJcUnEdhj.json', 'var_call_qfgbJzWHGoSSxsLNCWz2XduQ': 'file_storage/call_qfgbJzWHGoSSxsLNCWz2XduQ.json', 'var_call_CHHmXIY6m0FElj93VtBbtWwO': 'file_storage/call_CHHmXIY6m0FElj93VtBbtWwO.json', 'var_call_CsubguT2mL6An6p2MuT1MhGb': {'counts_all': {'Infiltrating Ductal Carcinoma': {'mut': 9, 'nomut': 700}, 'Infiltrating Lobular Carcinoma': {'mut': 75, 'nomut': 111}, 'Other  specify': {'mut': 3, 'nomut': 41}, 'Metaplastic Carcinoma': {'mut': 0, 'nomut': 7}, 'Infiltrating Carcinoma NOS': {'mut': 0, 'nomut': 1}, 'Mucinous Carcinoma': {'mut': 0, 'nomut': 15}, 'Medullary Carcinoma': {'mut': 1, 'nomut': 4}, 'Mixed Histology (please specify)': {'mut': 4, 'nomut': 15}, 'Leiomyosarcoma (LMS)': {'mut': 0, 'nomut': 1}}, 'rows_included': [{'histological_type': 'Infiltrating Ductal Carcinoma', 'mut': 9, 'nomut': 700, 'row_total': 709}, {'histological_type': 'Infiltrating Lobular Carcinoma', 'mut': 75, 'nomut': 111, 'row_total': 186}, {'histological_type': 'Other  specify', 'mut': 3, 'nomut': 41, 'row_total': 44}, {'histological_type': 'Mucinous Carcinoma', 'mut': 0, 'nomut': 15, 'row_total': 15}, {'histological_type': 'Mixed Histology (please specify)', 'mut': 4, 'nomut': 15, 'row_total': 19}], 'num_participants_considered': 987}}

exec(code, env_args)
