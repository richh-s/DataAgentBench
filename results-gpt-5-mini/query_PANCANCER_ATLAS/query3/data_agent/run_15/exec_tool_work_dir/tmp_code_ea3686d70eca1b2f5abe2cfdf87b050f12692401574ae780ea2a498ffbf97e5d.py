code = """import json
import re
import numpy as np

clinical_path = var_call_zy4tZsxMKyrZFbbF9YrTfRrD
mut_path = var_call_QCuF3u74lcU4YxB2aoBqvPSM

clin_list = json.load(open(clinical_path))
mut_list = json.load(open(mut_path))

# extract participant short barcode
pat_pattern = re.compile(r'(TCGA-[A-Za-z0-9]+-[A-Za-z0-9]+)')

def get_barcode(desc):
    if not isinstance(desc, str):
        return None
    m = pat_pattern.search(desc)
    return m.group(1) if m else None

# build mapping patient_id -> (participant_barcode_short, histological_type, patient_description)
patients = {}
for rec in clin_list:
    pid = rec.get('patient_id')
    hist = rec.get('histological_type')
    desc = rec.get('Patient_description')
    if hist is None:
        continue
    if not isinstance(desc, str):
        continue
    if 'breast' not in desc.lower():
        continue
    if pid in patients:
        # keep first occurrence
        continue
    barcode = get_barcode(desc)
    p_short = barcode[:12] if barcode else None
    patients[pid] = {'p_short': p_short, 'histological_type': hist, 'Patient_description': desc}

# build set of mutation participant short barcodes for CDH1 with FILTER == 'PASS'
mut_pass_set = set()
for m in mut_list:
    if m.get('Hugo_Symbol') == 'CDH1' and m.get('FILTER') == 'PASS':
        pb = m.get('ParticipantBarcode')
        if pb:
            mut_pass_set.add(pb[:12])

# compute counts per histological_type
counts = {}
for pid, info in patients.items():
    hist = info['histological_type']
    has_mut = False
    pshort = info['p_short']
    if pshort and pshort in mut_pass_set:
        has_mut = True
    if hist not in counts:
        counts[hist] = {'mut':0, 'no_mut':0, 'patients':[]}
    if has_mut:
        counts[hist]['mut'] += 1
    else:
        counts[hist]['no_mut'] += 1
    counts[hist]['patients'].append({'patient_id': pid, 'p_short': pshort, 'has_mut': has_mut})

# prepare contingency table list
ct_all = []
for hist, v in counts.items():
    total = v['mut'] + v['no_mut']
    ct_all.append({'histological_type': hist, 'mut': v['mut'], 'no_mut': v['no_mut'], 'row_total': total})

# filter rows with marginal totals > 10
ct_filtered = [r for r in ct_all if r['row_total'] > 10]

chi2 = None
note = ''
if len(ct_filtered) < 2:
    note = 'Not enough histological categories with >10 patients to compute chi-square.'
else:
    # build obs array
    obs = np.array([[r['no_mut'], r['mut']] for r in ct_filtered], dtype=float)
    grand_total = obs.sum()
    row_totals = obs.sum(axis=1)
    col_totals = obs.sum(axis=0)
    expected = np.outer(row_totals, col_totals) / grand_total
    chi2_val = ((obs - expected)**2 / expected).sum()
    chi2 = float(chi2_val)
    note = 'Chi-square computed across filtered histological types.'

output = {
    'num_brca_patients_with_histology': len(patients),
    'contingency_table_all': sorted(ct_all, key=lambda x: x['row_total'], reverse=True),
    'contingency_table_filtered': sorted(ct_filtered, key=lambda x: x['row_total'], reverse=True),
    'chi2_statistic': chi2,
    'note': note
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_wOj7qrE0JQPF2UVzC1M1YWH1': ['clinical_info'], 'var_call_AUSYNZ1jNLCd9ulFOYd4yy2N': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_i1IGbdodRagTpinL0swZ8hiY': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_nvYXSsjRiEboTuQif7frewKq': 'file_storage/call_nvYXSsjRiEboTuQif7frewKq.json', 'var_call_ELAZEPHz9ApJqfAtkMT3fl1V': [], 'var_call_QFJdkG1LA0XE5F21jrQ8rdte': 'file_storage/call_QFJdkG1LA0XE5F21jrQ8rdte.json', 'var_call_zy4tZsxMKyrZFbbF9YrTfRrD': 'file_storage/call_zy4tZsxMKyrZFbbF9YrTfRrD.json', 'var_call_260oEDAaJqkSZk94cDsRBcgN': [{'cid': '0', 'name': 'ParticipantBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Tumor_SampleBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Tumor_AliquotBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Normal_SampleBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'Normal_AliquotBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'Normal_SampleTypeLetterCode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'Hugo_Symbol', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '7', 'name': 'HGVSp_Short', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '8', 'name': 'Variant_Classification', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '9', 'name': 'HGVSc', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '10', 'name': 'CENTERS', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '11', 'name': 'FILTER', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_call_QCuF3u74lcU4YxB2aoBqvPSM': 'file_storage/call_QCuF3u74lcU4YxB2aoBqvPSM.json', 'var_call_eUJqfKNGOciydDIhzyQJM9yw': {'clinical_len': 1074, 'mutation_len': 200, 'clinical_sample_keys_first': ['patient_id', 'Patient_description', 'histological_type'], 'mutation_sample_keys_first': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], 'clinical_first': {'patient_id': 'A5EH', 'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}, 'mutation_first': {'ParticipantBarcode': 'TCGA-A8-A091', 'Hugo_Symbol': 'CDH1', 'HGVSp_Short': 'p.E243K', 'Variant_Classification': 'Missense_Mutation', 'FILTER': 'wga'}}}

exec(code, env_args)
