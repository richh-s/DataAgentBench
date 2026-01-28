code = """import json, re, traceback

try:
    clinical_path = var_call_kPrfeGwjv27evuhf8zWlxOMt
    mut_path = var_call_nXCvAMkLLW60oJJ9Zt0HntiR
    with open(clinical_path, 'r') as f:
        clinical = json.load(f)
    with open(mut_path, 'r') as f:
        mutations = json.load(f)

    # Filter clinical entries for FEMALE and non-null histological_type and have Patient_description
    clin_filtered = []
    for rec in clinical:
        pd_desc = rec.get('Patient_description')
        hist = rec.get('histological_type')
        if not pd_desc or not hist:
            continue
        if 'FEMALE' in pd_desc.upper():
            clin_filtered.append(rec)

    # Extract barcode function
    def extract_barcode(desc):
        if not desc:
            return None
        m = re.search(r'TCGA-[A-Za-z0-9-]+', desc)
        return m.group(0) if m else None

    # Build unique patient mapping: ParticipantBarcode -> histological_type (first occurrence)
    patient_hist = {}
    for rec in clin_filtered:
        desc = rec.get('Patient_description','')
        hist = rec.get('histological_type')
        barcode = extract_barcode(desc)
        if not barcode:
            continue
        if barcode not in patient_hist:
            patient_hist[barcode] = hist

    # Build mutation set
    mut_set = set()
    for m in mutations:
        pb = m.get('ParticipantBarcode')
        if pb:
            mut_set.add(pb)

    # Function to match clinical barcode to mutation barcodes
    def match_barcode(clin_barcode):
        if clin_barcode in mut_set:
            return clin_barcode
        parts = clin_barcode.split('-')
        if len(parts) >= 3:
            prefix = '-'.join(parts[:2])
            # find any mutation barcode that startswith prefix
            for ms in mut_set:
                if ms.startswith(prefix + '-'):
                    return ms
        return None

    # Tally counts per histology
    tally = {}
    for clin_barcode, hist in patient_hist.items():
        matched = match_barcode(clin_barcode)
        mutated = bool(matched)
        if hist not in tally:
            tally[hist] = {'Mutated': 0, 'Not_Mutated': 0}
        if mutated:
            tally[hist]['Mutated'] += 1
        else:
            tally[hist]['Not_Mutated'] += 1

    # Build included histologies (row total > 10)
    included = {}
    excluded_count = 0
    for hist, counts in tally.items():
        row_total = counts['Mutated'] + counts['Not_Mutated']
        if row_total > 10:
            included[hist] = {'Mutated': counts['Mutated'], 'Not_Mutated': counts['Not_Mutated'], 'Row_Total': row_total}
        else:
            excluded_count += 1

    # Compute chi-square
    grand_total = sum(v['Row_Total'] for v in included.values())
    col_mut = sum(v['Mutated'] for v in included.values())
    col_not = sum(v['Not_Mutated'] for v in included.values())
    chi2 = 0.0
    for hist, counts in included.items():
        row_total = counts['Row_Total']
        for col, col_total in [('Mutated', col_mut), ('Not_Mutated', col_not)]:
            O = counts[col]
            E = (row_total * col_total) / grand_total if grand_total>0 else 0
            if E>0:
                chi2 += (O - E)**2 / E

    r = len(included)
    df = (r - 1) * (2 - 1) if r>0 else 0

    result = {
        'chi2': chi2,
        'degrees_of_freedom': df,
        'grand_total': grand_total,
        'column_totals': {'Mutated': col_mut, 'Not_Mutated': col_not},
        'included_histologies': [{'histological_type': h, 'Mutated': v['Mutated'], 'Not_Mutated': v['Not_Mutated'], 'Row_Total': v['Row_Total']} for h,v in included.items()],
        'excluded_histology_count': excluded_count,
        'total_unique_female_clinical_patients': len(patient_hist)
    }

    print('__RESULT__:')
    print(json.dumps(result))

except Exception as e:
    tb = traceback.format_exc()
    out = {'error': str(e), 'traceback': tb}
    print('__RESULT__:')
    print(json.dumps(out))"""

env_args = {'var_call_EZConpLNNtTMuMHqwpFGCPmZ': ['clinical_info'], 'var_call_4Bo1zPhpt8F051RJTIEiJptH': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_eZ2gRyyrwAfUjcUJlM6Vbk5s': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_adNAHTxP5f0V2biww0rq8Qci': 'file_storage/call_adNAHTxP5f0V2biww0rq8Qci.json', 'var_call_ZCOG8WZGyXMcorybiEOoCO4m': [], 'var_call_U1Fil0FI5kei2c3BCsbICuQd': 'file_storage/call_U1Fil0FI5kei2c3BCsbICuQd.json', 'var_call_kPrfeGwjv27evuhf8zWlxOMt': 'file_storage/call_kPrfeGwjv27evuhf8zWlxOMt.json', 'var_call_nXCvAMkLLW60oJJ9Zt0HntiR': 'file_storage/call_nXCvAMkLLW60oJJ9Zt0HntiR.json', 'var_call_j97ieRM1DWC8xoBVwH4olaNl': {'clinical_len': 1074, 'mutation_len': 261, 'clinical_first3': [{'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma', 'patient_id': 'A5EH'}, {'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma', 'patient_id': 'A7SZ'}, {'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'histological_type': 'Infiltrating Ductal Carcinoma', 'patient_id': 'A0FY'}], 'mutation_first3': [{'ParticipantBarcode': 'TCGA-A2-A0YL', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.T364Hfs*4', 'Variant_Classification': 'Frame_Shift_Del', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.N315Ifs*41', 'Variant_Classification': 'Frame_Shift_Del', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.A824V', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'PASS'}], 'clinical_columns_sample': ['Patient_description', 'histological_type', 'patient_id'], 'mutation_columns_sample': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER']}}

exec(code, env_args)
