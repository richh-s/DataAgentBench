code = """import json
import re
import pandas as pd

# Load query results from storage files
with open(var_call_rplNGBrP6x9OoeETctcM3Wjy, 'r') as f:
    clinical_records = json.load(f)
with open(var_call_HBWqvt84xbNHfZC9ppdzIMMT, 'r') as f:
    mutation_records = json.load(f)

# Build clinical DataFrame: extract ParticipantBarcode from Patient_description
rows = []
pattern = re.compile(r"(TCGA-[A-Za-z0-9-]+)")
for rec in clinical_records:
    pd_desc = rec.get('Patient_description') or ''
    hist = rec.get('histological_type')
    if not hist:
        continue
    m = pattern.search(pd_desc)
    if not m:
        continue
    barcode = m.group(1)
    rows.append({'ParticipantBarcode': barcode, 'histological_type': hist})

clin_df = pd.DataFrame(rows).drop_duplicates(subset=['ParticipantBarcode'])

# Build mutation set for CDH1 PASS
mut_barcodes = set(rec['ParticipantBarcode'] for rec in mutation_records if rec.get('ParticipantBarcode'))

# Filter clinical to BRCA cohort: ensure Patient_description mentions Breast or histological_type contains 'Breast' or 'Breast' in any part
# The original clinical query filtered by ILIKE '%Breast%' so assume these are breast patients; but double-check by histological_type or Patient_description
clin_df = clin_df[clin_df['histological_type'].notna()]

# Determine mutation presence
clin_df['CDH1_mutated'] = clin_df['ParticipantBarcode'].apply(lambda x: 1 if x in mut_barcodes else 0)

# Build contingency table: rows = histological_type, columns = mutated (1) and not mutated (0)
ct = clin_df.groupby(['histological_type', 'CDH1_mutated']).size().unstack(fill_value=0)
# Ensure both columns 0 and 1 exist
if 0 not in ct.columns:
    ct[0] = 0
if 1 not in ct.columns:
    ct[1] = 0
ct = ct[[1,0]]  # order as mutated, not_mutated
ct.columns = ['mutated', 'not_mutated']
ct['total'] = ct['mutated'] + ct['not_mutated']

# Exclude histological types with marginal totals <= 10
ct_filtered = ct[ct['total'] > 10].copy()

# If no categories left, return message
if ct_filtered.empty:
    result = {'error': 'No histological categories with total > 10 after filtering.'}
    print("__RESULT__:")
    print(json.dumps(result))
else:
    # Compute chi-square statistic
    grand_total = int(ct_filtered['total'].sum())
    # Column totals
    col_total_mut = int(ct_filtered['mutated'].sum())
    col_total_not = int(ct_filtered['not_mutated'].sum())

    chi2 = 0.0
    # For each cell
    table_dict = {}
    for idx, row in ct_filtered.iterrows():
        r_total = int(row['total'])
        o_mut = int(row['mutated'])
        o_not = int(row['not_mutated'])
        e_mut = r_total * col_total_mut / grand_total if grand_total>0 else 0
        e_not = r_total * col_total_not / grand_total if grand_total>0 else 0
        # avoid division by zero
        if e_mut>0:
            chi2 += (o_mut - e_mut)**2 / e_mut
        if e_not>0:
            chi2 += (o_not - e_not)**2 / e_not
        table_dict[idx] = {'mutated': o_mut, 'not_mutated': o_not, 'total': r_total, 'expected_mutated': e_mut, 'expected_not_mutated': e_not}

    out = {'chi2': chi2, 'grand_total': grand_total, 'contingency_table': table_dict}
    print("__RESULT__:")
    print(json.dumps(out))"""

env_args = {'var_call_cLg2bVKIICIpXvPHFW3BZpn8': ['clinical_info'], 'var_call_2vFWqhs0mCsyw157b6G7Be29': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_kE2byo10XEhr67Kgxu96D8Mo': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_7gjk8aDn9EIlS0eIEaZT6Y6m': 'file_storage/call_7gjk8aDn9EIlS0eIEaZT6Y6m.json', 'var_call_rplNGBrP6x9OoeETctcM3Wjy': 'file_storage/call_rplNGBrP6x9OoeETctcM3Wjy.json', 'var_call_HBWqvt84xbNHfZC9ppdzIMMT': 'file_storage/call_HBWqvt84xbNHfZC9ppdzIMMT.json'}

exec(code, env_args)
