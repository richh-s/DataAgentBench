code = """import json, re, math

# Load clinical LGG records (from previous query)
clinical_path = var_call_xlnKixTAh6FWCFog8b1MFli7
with open(clinical_path, 'r') as f:
    clinical = json.load(f)

# Load IGF2 expression records
igf2_path = var_call_YngX9o68XKmIoVGv7rFGwaET
with open(igf2_path, 'r') as f:
    igf2 = json.load(f)

# Build mapping from patient barcode to histological_type for LGG patients
barcode_to_hist = {}
pattern = re.compile(r'TCGA-[A-Za-z0-9-]+')
for rec in clinical:
    desc = rec.get('Patient_description','')
    hist = rec.get('histological_type')
    if not hist:
        continue
    # skip histological types enclosed in square brackets
    if '[' in hist or ']' in hist:
        continue
    m = pattern.search(desc)
    if not m:
        # sometimes Patient_description may contain 'barcode TCGA-XX-YYYY' or different format
        # try searching for 'TCGA-' in whole record
        continue
    barcode = m.group(0).strip()
    # Normalize barcode to upper
    barcode = barcode.upper()
    # Some barcodes in clinical may be like TCGA-AB-1234 but participant barcodes match exactly
    barcode_to_hist[barcode] = hist

# Now aggregate IGF2 values for barcodes present in barcode_to_hist
hist_values = {}
for rec in igf2:
    pbar = rec.get('ParticipantBarcode')
    if not pbar:
        continue
    pbar = pbar.upper()
    if pbar not in barcode_to_hist:
        continue
    val = rec.get('normalized_count')
    try:
        num = float(val)
    except Exception:
        continue
    # valid expression required
    # compute log10(normalized_count + 1)
    logv = math.log10(num + 1.0)
    hist = barcode_to_hist[pbar]
    hist_values.setdefault(hist, []).append(logv)

# Compute averages
hist_means = {}
for hist, vals in hist_values.items():
    if len(vals) == 0:
        continue
    meanv = sum(vals)/len(vals)
    # format with at least four decimal places
    hist_means[hist] = format(meanv, '.4f')

# Sort results by histology name for consistency
sorted_result = {k: hist_means[k] for k in sorted(hist_means.keys())}

print('__RESULT__:')
print(json.dumps(sorted_result))"""

env_args = {'var_call_bTwKGiabme4M52iMyBzCtaKD': ['clinical_info'], 'var_call_YZbk31TlRbTB41YiG6LHnLni': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_n1Pw2BCPkFn7G88dobCqQFjw': 'file_storage/call_n1Pw2BCPkFn7G88dobCqQFjw.json', 'var_call_NYHVxdzxVvS080GYpGg49y1P': {'first_record_keys': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'candidate_fields': ['tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'person_neoplasm_cancer_status', 'primary_therapy_outcome_success', 'primary_lymph_node_presentation_assessment', 'eastern_cancer_oncology_group', 'residual_tumor', 'tumor_tissue_site_other', 'days_to_new_tumor_event_after_initial_treatment', 'family_history_of_cancer'], 'sample_field_values': {'tumor_tissue_site': ['Peritoneum ovary', 'Brain', 'Ovary', 'Adrenal', 'Gynecological - Uterus', 'Omentum'], 'diagnosis': ['None'], 'histological_type': ['Glioblastoma Multiforme (GBM)', 'Serous Cystadenocarcinoma', 'Leiomyosarcoma (LMS)', 'Adrenocortical carcinoma- Usual Type', 'Untreated primary (de novo) GBM', 'Treated primary GBM'], 'patient_id': ['1124', '1688', '1694', '1692', '4209', '2081', '1120', '2641', '0933', '2427', '1584', '2425', '1318', '1576', '1955', '2408', '1328', 'A838', '1696', '1953']}}, 'var_call_69BIQxJiroYpVpajQc1CVkvs': [], 'var_call_xlnKixTAh6FWCFog8b1MFli7': 'file_storage/call_xlnKixTAh6FWCFog8b1MFli7.json', 'var_call_L3wgGJZksnUcUJd4ZUIHQXX6': [{'ParticipantBarcode': 'TCGA-AB-2908', 'Symbol': 'IGF2', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'Symbol': 'IGF2', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'Symbol': 'IGF2', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'Symbol': 'IGF2', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'Symbol': 'IGF2', 'normalized_count': '613.474'}, {'ParticipantBarcode': 'TCGA-A8-A082', 'Symbol': 'IGF2', 'normalized_count': '630.54'}, {'ParticipantBarcode': 'TCGA-B5-A3FA', 'Symbol': 'IGF2', 'normalized_count': '423.628'}, {'ParticipantBarcode': 'TCGA-BH-A1EX', 'Symbol': 'IGF2', 'normalized_count': '1151.13'}, {'ParticipantBarcode': 'TCGA-BT-A20O', 'Symbol': 'IGF2', 'normalized_count': '369.106'}, {'ParticipantBarcode': 'TCGA-CD-5799', 'Symbol': 'IGF2', 'normalized_count': '3936.02070028943'}], 'var_call_YngX9o68XKmIoVGv7rFGwaET': 'file_storage/call_YngX9o68XKmIoVGv7rFGwaET.json'}

exec(code, env_args)
