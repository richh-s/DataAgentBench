code = """import json, re, math
# load clinical LGG query result and IGF2 RNA rows
clin_fp = var_call_qADwp5shUiOxBVXoaCycl8MY
rna_fp = var_call_loCJAqxLBALs6DTiKWGu4kBo
with open(clin_fp, 'r') as f:
    clin = json.load(f)
with open(rna_fp, 'r') as f:
    rna = json.load(f)
# build mapping participant barcode -> histology
pat_hist = {}
pattern = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', re.IGNORECASE)
for row in clin:
    desc = row.get('Patient_description','') or ''
    hist = row.get('histological_type') or row.get('histology') or ''
    # skip histologies with square brackets
    if '[' in hist or ']' in hist or hist.strip() == '' or hist.strip().upper() == 'NONE':
        continue
    m = pattern.search(desc)
    if m:
        barcode = m.group(1).upper()
        # normalize barcode format to uppercase
        if barcode not in pat_hist:
            pat_hist[barcode] = hist
# Now collect log10(normalized_count+1) values for IGF2 rows where ParticipantBarcode in pat_hist
hist_values = {}
for row in rna:
    p = (row.get('ParticipantBarcode') or '').upper()
    if p in pat_hist:
        nc = row.get('normalized_count')
        if nc is None:
            continue
        try:
            val = float(nc)
        except Exception:
            # skip non-numeric
            continue
        # valid value
        logval = math.log10(val + 1.0)
        hist = pat_hist[p]
        hist_values.setdefault(hist, []).append(logval)
# compute means with at least four decimals
result = {}
for hist, vals in hist_values.items():
    if len(vals) == 0:
        continue
    meanv = sum(vals)/len(vals)
    # round to 6 decimals for safety, but ensure at least 4 decimals
    result[hist] = float(f"{meanv:.6f}")
# sort keys for deterministic output
sorted_result = {k: result[k] for k in sorted(result.keys())}
print('__RESULT__:')
print(json.dumps(sorted_result))"""

env_args = {'var_call_HxopMXjEYprqo2Rsgs2APlEL': ['clinical_info'], 'var_call_thEdX7eq3idUjPazPmrd9Qcg': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_p3DB1WnJMNwHq8XbVSD57niU': 'file_storage/call_p3DB1WnJMNwHq8XbVSD57niU.json', 'var_call_g6d3z0Vi0JW1X3MpjtF5J2Nd': {'num_records_sampled': 200, 'keys_count': 99, 'keys_sample': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight'], 'inspect_candidates': {'tumor_tissue_site': ['Brain', 'Gynecological - Uterus', 'Omentum', 'Ovary', 'Peritoneum ovary'], 'diagnosis': ['None'], 'icd_10': ['C56.9', 'C71.9', 'C55', 'C48.1', 'C48.2']}, 'sample_vals': {'tumor_tissue_site': ['Brain', 'Gynecological - Uterus', 'Omentum', 'Ovary', 'Peritoneum ovary'], 'histological_type': ['Untreated primary (de novo) GBM', 'Treated primary GBM', 'Leiomyosarcoma (LMS)', 'Serous Cystadenocarcinoma'], 'Patient_description': ['Patient TCGA-29-2429 (UUID 4309ca23-1cf9-40a2-a01c-ccee90f958b2) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Dead.', 'Case 8628F1B2-3763-4BA9-A375-083874BB18F2, linked to barcode TCGA-VG-A8LO, corresponds to a FEMALE patient diagnosed with Ovarian serous cystadenocarcinoma, with vital status Dead.', "Patient TCGA-23-1026, registered under UUID c6ede8ae-881c-47a0-a0ef-745ed4b7764a, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Alive.", 'Patient TCGA-23-1032 (FEMALE, UUID d1976840-35f7-4423-8458-12fb32a52b33) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Dead.', 'Patient TCGA-36-1569 (FEMALE, UUID 7d82ce56-32eb-4107-aa5c-c568764805c9) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.', 'Patient TCGA-04-1351 (FEMALE, UUID 12b032ed-ff92-4bfe-b980-eb273ae8ae17) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Alive.', 'Patient TCGA-04-1331 (FEMALE, UUID 6d10d4ee-6331-4bba-93bc-a7b64cc0b22a) is enrolled in the study of Ovarian serous cystadenocarcinoma. Vital status: Dead.', "Patient TCGA-04-1365, registered under UUID 0484a929-7a7f-4926-8d25-470ddab082ec, belongs to the Ovarian serous cystadenocarcinoma cohort. This FEMALE patient's vital status is Alive.", 'Patient TCGA-23-2077 (UUID ef57bc45-858f-4d4e-8407-b7eadfa43be5) is a FEMALE diagnosed with Ovarian serous cystadenocarcinoma. Current vital status: Alive.', 'The individual with barcode TCGA-57-1584 and UUID ed21615c-0de3-421c-9e8d-8996026c4431 is a FEMALE case of Ovarian serous cystadenocarcinoma, documented with vital status = Alive.']}}, 'var_call_UFGGcjph0IqmXDwlpY4eaqQm': 'file_storage/call_UFGGcjph0IqmXDwlpY4eaqQm.json', 'var_call_qADwp5shUiOxBVXoaCycl8MY': 'file_storage/call_qADwp5shUiOxBVXoaCycl8MY.json', 'var_call_jz5VNNpcn3MbWHCBhJ6lFuMd': {'all_keys': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'len_keys': 99, 'barcode_like_keys': [], 'possible_keys': []}, 'var_call_loCJAqxLBALs6DTiKWGu4kBo': 'file_storage/call_loCJAqxLBALs6DTiKWGu4kBo.json'}

exec(code, env_args)
