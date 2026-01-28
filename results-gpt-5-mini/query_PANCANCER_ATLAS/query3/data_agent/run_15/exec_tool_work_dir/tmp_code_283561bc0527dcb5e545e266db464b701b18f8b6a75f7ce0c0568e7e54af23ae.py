code = """import pandas as pd
import json
import re
import numpy as np

clinical_path = var_call_zy4tZsxMKyrZFbbF9YrTfRrD
mut_path = var_call_QCuF3u74lcU4YxB2aoBqvPSM

clin = pd.read_json(clinical_path)
mut = pd.read_json(mut_path)

# Ensure columns
clin = clin[clin['histological_type'].notna()].copy()

def extract_barcode(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4}', s)
    if m:
        return m.group(0)
    m2 = re.search(r'TCGA-[^\s,;()]+', s)
    if m2:
        return m2.group(0)
    return None

clin['ParticipantBarcode'] = clin['Patient_description'].apply(extract_barcode)
clin['p_short'] = clin['ParticipantBarcode'].str[:12]
mut['p_short'] = mut['ParticipantBarcode'].str[:12]

# reliable mutations
mut_pass = mut[mut['FILTER'] == 'PASS'].copy()
mut_pass_set = set(mut_pass['p_short'].dropna().unique())

# focus BRCA: Patient_description contains 'Breast' (case-insensitive)
clin_brca = clin[clin['Patient_description'].str.contains('Breast', case=False, na=False)].copy()

# mark mutation presence per patient
clin_brca['CDH1_mut_present'] = clin_brca['p_short'].apply(lambda x: x in mut_pass_set)

# create summary per patient (one row per patient)
summary = clin_brca.drop_duplicates(subset=['patient_id']).loc[:, ['patient_id','histological_type','CDH1_mut_present']].copy()

# contingency table
pivot = pd.pivot_table(summary, index='histological_type', columns='CDH1_mut_present', values='patient_id', aggfunc='count', fill_value=0)
# Ensure both columns exist
if True not in pivot.columns:
    pivot[True] = 0
if False not in pivot.columns:
    pivot[False] = 0
pivot = pivot[[False, True]]

ct = pivot.reset_index()
ct['row_total'] = ct[False] + ct[True]
ct_filtered = ct[ct['row_total'] > 10].copy()

if ct_filtered.shape[0] < 2:
    chi2 = None
    msg = 'Not enough histological categories with >10 patients to compute chi-square.'
else:
    obs = ct_filtered[[False, True]].values
    grand_total = obs.sum()
    row_totals = obs.sum(axis=1)
    col_totals = obs.sum(axis=0)
    expected = np.outer(row_totals, col_totals) / grand_total
    chi2 = float(((obs - expected)**2 / expected).sum())
    msg = 'Chi-square computed across filtered histological types.'

output = {
    'num_brca_patients_with_histology': int(summary.shape[0]),
    'contingency_table_all': ct.rename(columns={False:'no_mut', True:'mut'}).to_dict(orient='records'),
    'contingency_table_filtered': ct_filtered.rename(columns={False:'no_mut', True:'mut'}).to_dict(orient='records'),
    'chi2_statistic': chi2,
    'note': msg
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_wOj7qrE0JQPF2UVzC1M1YWH1': ['clinical_info'], 'var_call_AUSYNZ1jNLCd9ulFOYd4yy2N': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_i1IGbdodRagTpinL0swZ8hiY': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_nvYXSsjRiEboTuQif7frewKq': 'file_storage/call_nvYXSsjRiEboTuQif7frewKq.json', 'var_call_ELAZEPHz9ApJqfAtkMT3fl1V': [], 'var_call_QFJdkG1LA0XE5F21jrQ8rdte': 'file_storage/call_QFJdkG1LA0XE5F21jrQ8rdte.json', 'var_call_zy4tZsxMKyrZFbbF9YrTfRrD': 'file_storage/call_zy4tZsxMKyrZFbbF9YrTfRrD.json', 'var_call_260oEDAaJqkSZk94cDsRBcgN': [{'cid': '0', 'name': 'ParticipantBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Tumor_SampleBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Tumor_AliquotBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Normal_SampleBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'Normal_AliquotBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'Normal_SampleTypeLetterCode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'Hugo_Symbol', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '7', 'name': 'HGVSp_Short', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '8', 'name': 'Variant_Classification', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '9', 'name': 'HGVSc', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '10', 'name': 'CENTERS', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '11', 'name': 'FILTER', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_call_QCuF3u74lcU4YxB2aoBqvPSM': 'file_storage/call_QCuF3u74lcU4YxB2aoBqvPSM.json'}

exec(code, env_args)
