code = """import json, math
# Load barcode to histology mapping
p_map = var_call_QVoF2qnMkf2rM21iQy1wbP4h
with open(p_map, 'r') as f:
    map_data = json.load(f)
barcode_to_hist = {k.upper(): v for k, v in map_data.get('barcode_to_histology', {}).items()}

# Load IGF2 expression records
p_expr = var_call_HunKwSYjTZBiW1NcKue3vXYx
with open(p_expr, 'r') as f:
    expr_records = json.load(f)

# Aggregate log10(normalized_count + 1) by histology
vals_by_hist = {}
for rec in expr_records:
    part = rec.get('ParticipantBarcode')
    if not part:
        continue
    part_up = part.upper()
    if part_up not in barcode_to_hist:
        continue
    hist = barcode_to_hist[part_up]
    if not isinstance(hist, str):
        continue
    hs = hist.strip()
    # exclude histologies enclosed in square brackets
    if hs.startswith('[') and hs.endswith(']'):
        continue
    nc = rec.get('normalized_count')
    if nc is None or nc == '':
        continue
    try:
        val = float(nc)
    except:
        continue
    if math.isnan(val):
        continue
    lg = math.log10(val + 1.0)
    vals_by_hist.setdefault(hs, []).append(lg)

# Compute means with at least 4 decimal places
means = {}
for hist, lst in vals_by_hist.items():
    if len(lst) == 0:
        continue
    m = sum(lst) / len(lst)
    # keep 6 decimal places for safety
    means[hist] = round(m, 6)

# Sort keys for consistent output
out = {k: means[k] for k in sorted(means.keys())}

result_str = json.dumps(out)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_call_OV22WEad6UfwHraf6wlGs5r7': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_Sd59Be0wqycr5ZqZw0hhX3l5': [], 'var_call_nnoDenIU6HdLB88szf5dZu7i': [], 'var_call_iMfXuyGnfixPiA8F3gjtybET': 'file_storage/call_iMfXuyGnfixPiA8F3gjtybET.json', 'var_call_rRChSbxkObaP56e8cUR8KWxu': 'file_storage/call_rRChSbxkObaP56e8cUR8KWxu.json', 'var_call_wcJAzIKt1Dvnsge0rxRQKmrz': 'file_storage/call_wcJAzIKt1Dvnsge0rxRQKmrz.json', 'var_call_QVoF2qnMkf2rM21iQy1wbP4h': 'file_storage/call_QVoF2qnMkf2rM21iQy1wbP4h.json', 'var_call_HunKwSYjTZBiW1NcKue3vXYx': 'file_storage/call_HunKwSYjTZBiW1NcKue3vXYx.json'}

exec(code, env_args)
