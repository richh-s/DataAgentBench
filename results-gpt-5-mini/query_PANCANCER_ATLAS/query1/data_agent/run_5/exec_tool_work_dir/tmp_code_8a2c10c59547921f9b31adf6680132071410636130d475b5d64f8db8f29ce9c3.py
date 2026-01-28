code = """import json, math, re
# Load extracted LGG barcodes and mapping
path_map = var_call_zSajL1QTawgei8YA7aQTEoiH
with open(path_map, 'r') as f:
    lgg_data = json.load(f)
barcodes = set(lgg_data.get('barcodes', []))
mapping = lgg_data.get('mapping', {})
# Load IGF2 expression records
path_igf2 = var_call_wX6Fr73bir3643XGUNN3senk
with open(path_igf2, 'r') as f:
    igf2_records = json.load(f)
# Prepare per-histology lists
hist_vals = {}
br_total = 0
for rec in igf2_records:
    pb = rec.get('ParticipantBarcode')
    if not pb:
        continue
    if pb not in barcodes:
        continue
    ht = mapping.get(pb)
    # Exclude missing histology
    if not ht:
        continue
    ht_str = ht.strip()
    # Exclude annotations enclosed in square brackets entirely
    if re.match(r'^\[.*\]$', ht_str):
        continue
    # normalized_count
    nc = rec.get('normalized_count')
    try:
        val = float(nc)
    except Exception:
        continue
    # Exclude NA or invalid
    if math.isnan(val):
        continue
    # compute log10(val+1)
    logv = math.log10(val + 1.0)
    hist_vals.setdefault(ht_str, []).append(logv)
    nbr_total += 1
# Compute means with at least four decimal places
result = {}
for ht, vals in hist_vals.items():
    if len(vals) == 0:
        continue
    meanv = sum(vals) / len(vals)
    # format to 4+ decimals (keep 6 for safety)
    result[ht] = float(f"{meanv:.6f}")
# If no data found, result will be empty
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pEURVJBeXBnMZnsMYBViImWI': ['clinical_info'], 'var_call_KmByRUkSviX94BgWWZdYekhf': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_4Tvje90wJGJKLXqaGP0Sx9YB': [], 'var_call_1lRKT64FDzT1ViCVh3Kzy4uO': [], 'var_call_hKfJXEDB4qr9ZW0SiV71MtJi': [], 'var_call_VGCP9S6kAe29Pr0BZvvhOMdk': [{'Symbol': '?'}, {'Symbol': 'A1BG'}, {'Symbol': 'A1CF'}, {'Symbol': 'A2BP1'}, {'Symbol': 'A2LD1'}, {'Symbol': 'A2M'}, {'Symbol': 'A2ML1'}, {'Symbol': 'A4GALT'}, {'Symbol': 'A4GNT'}, {'Symbol': 'AAA1'}, {'Symbol': 'AAAS'}, {'Symbol': 'AACS'}, {'Symbol': 'AACSL'}, {'Symbol': 'AADAC'}, {'Symbol': 'AADACL2'}, {'Symbol': 'AADACL3'}, {'Symbol': 'AADACL4'}, {'Symbol': 'AADAT'}, {'Symbol': 'AAGAB'}, {'Symbol': 'AAK1'}], 'var_call_U8tDtxjw4F6bzWglXt9TkCDm': [{'cnt': '496'}], 'var_call_bT3ho4iMr5aW1ciFTpxWOeQC': 'file_storage/call_bT3ho4iMr5aW1ciFTpxWOeQC.json', 'var_call_49MpdV0zeoMqVvNr7CH6aEc8': 'file_storage/call_49MpdV0zeoMqVvNr7CH6aEc8.json', 'var_call_m0a3endLR0RvqGrms4ks17SA': 'file_storage/call_m0a3endLR0RvqGrms4ks17SA.json', 'var_call_SxxKq86Y9SUjVHY8oFftaz7E': [{'ParticipantBarcode': 'TCGA-KO-8409'}, {'ParticipantBarcode': 'TCGA-KP-A3W0'}, {'ParticipantBarcode': 'TCGA-LA-A7SW'}, {'ParticipantBarcode': 'TCGA-LB-A8F3'}, {'ParticipantBarcode': 'TCGA-LB-A9Q5'}, {'ParticipantBarcode': 'TCGA-LK-A4O0'}, {'ParticipantBarcode': 'TCGA-LL-A9Q3'}, {'ParticipantBarcode': 'TCGA-LN-A4A4'}, {'ParticipantBarcode': 'TCGA-LP-A7HU'}, {'ParticipantBarcode': 'TCGA-MA-AA3W'}, {'ParticipantBarcode': 'TCGA-MB-A5Y8'}, {'ParticipantBarcode': 'TCGA-MH-A855'}, {'ParticipantBarcode': 'TCGA-MH-A857'}, {'ParticipantBarcode': 'TCGA-N8-A4PO'}, {'ParticipantBarcode': 'TCGA-NA-A4QY'}, {'ParticipantBarcode': 'TCGA-NC-A5HL'}, {'ParticipantBarcode': 'TCGA-NG-A4VU'}, {'ParticipantBarcode': 'TCGA-NH-A6GB'}, {'ParticipantBarcode': 'TCGA-OL-A5RW'}, {'ParticipantBarcode': 'TCGA-OL-A5RY'}], 'var_call_zSajL1QTawgei8YA7aQTEoiH': 'file_storage/call_zSajL1QTawgei8YA7aQTEoiH.json', 'var_call_wX6Fr73bir3643XGUNN3senk': 'file_storage/call_wX6Fr73bir3643XGUNN3senk.json'}

exec(code, env_args)
