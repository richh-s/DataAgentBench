code = """import json, math
# Load clinical LGG results
clinical_path = var_call_acqnX62PAxMUgImCmfcMdoG7
rna_path = var_call_4CFo6DeE9o6ghdMNjiSlAzpo
with open(clinical_path, 'r') as f:
    clinical = json.load(f)
with open(rna_path, 'r') as f:
    rna = json.load(f)
# Build patient_id -> histology mapping, excluding histologies enclosed in square brackets
pat_hist = {}
for rec in clinical:
    pid = rec.get('patient_id')
    hist = rec.get('histological_type')
    if pid is None or hist is None:
        continue
    # Exclude histologies that are enclosed in square brackets (contain '[' or ']')
    if ('[' in hist) or (']' in hist):
        continue
    # strip whitespace
    hist = hist.strip()
    if hist == '' or hist.lower() == 'none':
        continue
    pat_hist[pid] = hist
# Now iterate RNA rows for IGF2, join by participant patient segment
hist_values = {}
for rec in rna:
    pbar = rec.get('ParticipantBarcode')
    cnt = rec.get('normalized_count')
    if pbar is None or cnt is None:
        continue
    # extract patient id segment after second '-'
    parts = pbar.split('-')
    if len(parts) < 3:
        continue
    pid = parts[2]
    # Only consider if pid in pat_hist
    if pid not in pat_hist:
        continue
    # parse normalized_count to float
    try:
        val = float(cnt)
    except:
        continue
    # consider only valid values (non-negative)
    if math.isnan(val):
        continue
    # compute log10(val + 1)
    logv = math.log10(val + 1)
    hist = pat_hist[pid]
    hist_values.setdefault(hist, []).append(logv)
# compute means
hist_means = {}
for hist, vals in hist_values.items():
    if len(vals) == 0:
        continue
    meanv = sum(vals) / len(vals)
    # format to at least 4 decimal places, use 6
    meanv_rounded = round(meanv, 6)
    hist_means[hist] = meanv_rounded
# Sort keys for consistency
hist_means_sorted = {k: hist_means[k] for k in sorted(hist_means.keys())}
print('__RESULT__:')
print(json.dumps(hist_means_sorted))"""

env_args = {'var_call_l9BxyW69nXvgBIVU8MpUiO8K': ['clinical_info'], 'var_call_N6Qbzpu3ynJhE5mwzyHMaRsU': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_cvLxnMZPwIiMPdWajwObQTUM': 'file_storage/call_cvLxnMZPwIiMPdWajwObQTUM.json', 'var_call_4RKyADyPqqzYoGzvAqTGatAH': {'first_record_keys': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'candidates': ['days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_o_3_histology', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'person_neoplasm_cancer_status', 'year_of_initial_pathologic_diagnosis', 'tissue_source_site', 'initial_pathologic_diagnosis_method', 'eastern_cancer_oncology_group', 'residual_tumor', 'tumor_tissue_site_other', 'diagnosis', 'days_to_new_tumor_event_after_initial_treatment', 'family_history_of_cancer'], 'sample_patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.'}, 'var_call_acqnX62PAxMUgImCmfcMdoG7': 'file_storage/call_acqnX62PAxMUgImCmfcMdoG7.json', 'var_call_4CFo6DeE9o6ghdMNjiSlAzpo': 'file_storage/call_4CFo6DeE9o6ghdMNjiSlAzpo.json'}

exec(code, env_args)
