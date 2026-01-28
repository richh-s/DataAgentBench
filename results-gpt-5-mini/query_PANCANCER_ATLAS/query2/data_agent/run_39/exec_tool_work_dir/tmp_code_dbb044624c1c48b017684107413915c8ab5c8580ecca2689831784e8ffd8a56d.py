code = """import json, re, pandas as pd

# Load clinical data (alive BRCA patients) and mutation participant barcodes from storage files
with open(var_call_jW9c281oFItWtateg7CYJ8v6, 'r') as f:
    clinical = json.load(f)
with open(var_call_B2tbV0oD8IejgNJqazs7ZjeK, 'r') as f:
    cdhs = json.load(f)

# Extract patient barcode from Patient_description
barcode_pattern = re.compile(r'(TCGA[-][A-Za-z0-9-]+?)\b', re.IGNORECASE)

records = []
for rec in clinical:
    pd_desc = rec.get('Patient_description','')
    hist = rec.get('histological_type')
    m = barcode_pattern.search(pd_desc)
    if m and hist:
        barcode = m.group(1).upper()
        records.append({'barcode': barcode, 'histological_type': hist})

# Create dataframe
df = pd.DataFrame(records)
if df.empty:
    result = []
else:
    # Normalize histological_type
    df['histological_type'] = df['histological_type'].str.strip()

    # Build set of participant barcodes with CDH1 mutations
    cdh_set = set([d['ParticipantBarcode'].upper() for d in cdhs if d.get('ParticipantBarcode')])

    # Some ParticipantBarcode entries might be longer or shorter; to be safe, consider matching by prefix
    # Define function to check if patient barcode matches any ParticipantBarcode by exact or prefix up to two hyphens
    def has_mut(barcode):
        if barcode in cdh_set:
            return True
        # try matching first 3 segments (TCGA-XX-YYYY) by splitting
        parts = barcode.split('-')
        if len(parts) >= 3:
            short = '-'.join(parts[:3])
            if short in cdh_set:
                return True
        # also check if any cdh_set member startswith barcode or barcode startswith member
        for p in (barcode, short if len(parts)>=3 else barcode):
            for q in cdh_set:
                if q.startswith(p) or p.startswith(q):
                    return True
        return False

    # Aggregate counts per histological_type
    agg = []
    for hist, group in df.groupby('histological_type'):
        total = group['barcode'].nunique()
        # count mutated among unique barcodes
        mutated = sum(group['barcode'].apply(has_mut).astype(int))
        pct = (mutated / total * 100) if total>0 else 0.0
        agg.append({'histological_type': hist, 'total_alive_patients': int(total), 'mutated_patients': int(mutated), 'percent_mutated': round(pct,2)})

    # Sort by percent desc, then mutated_patients desc, then total desc
    agg_sorted = sorted(agg, key=lambda x: (-x['percent_mutated'], -x['mutated_patients'], -x['total_alive_patients']))
    result = agg_sorted[:3]

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Rpcp0xB7n7YmXOWMpetNfMNd': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_pIdN2BxAeTwCpfyvPXumfvRf': [], 'var_call_dOUG1fLBdlHlQkAJQoMwlCaN': 'file_storage/call_dOUG1fLBdlHlQkAJQoMwlCaN.json', 'var_call_w6dmyPqPMeCUrCkVW3cSlvSr': 'file_storage/call_w6dmyPqPMeCUrCkVW3cSlvSr.json', 'var_call_jW9c281oFItWtateg7CYJ8v6': 'file_storage/call_jW9c281oFItWtateg7CYJ8v6.json', 'var_call_B2tbV0oD8IejgNJqazs7ZjeK': 'file_storage/call_B2tbV0oD8IejgNJqazs7ZjeK.json'}

exec(code, env_args)
