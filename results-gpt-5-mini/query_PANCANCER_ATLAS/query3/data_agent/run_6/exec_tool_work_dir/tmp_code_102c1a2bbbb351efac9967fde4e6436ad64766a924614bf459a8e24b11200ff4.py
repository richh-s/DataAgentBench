code = """import json
import re
import numpy as np

clinical_path = var_call_VJG2iCWQfZt8H5NtOLSdoX0W
mut_path = var_call_HFxYtNV89LYasiyD2KdL3Yyg

with open(clinical_path,'r') as f:
    clinical_raw = json.load(f)
with open(mut_path,'r') as f:
    mut_raw = json.load(f)

# Extract barcode robustly
def extract_barcode(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'TCGA[-][A-Za-z0-9-]+', text)
    if m:
        bc = m.group(0)
        # strip trailing punctuation
        return re.sub(r'[.,;:]$','',bc)
    return None

# Build clinical patients list
patients = []
for rec in clinical_raw:
    pd_desc = rec.get('Patient_description')
    hist = rec.get('histological_type')
    bc = extract_barcode(pd_desc)
    if bc and hist:
        patients.append({'barcode': bc.upper(), 'histological_type': hist})

# Deduplicate by barcode, keep first
seen = set()
uniq_patients = []
for p in patients:
    if p['barcode'] not in seen:
        seen.add(p['barcode'])
        uniq_patients.append(p)

# Build mutation barcode set
mut_bcs = [r.get('ParticipantBarcode') for r in mut_raw if r.get('ParticipantBarcode')]
mut_bcs = [m.upper() for m in mut_bcs]
mut_set = set(mut_bcs)

# Helper to check match
def is_mutated(patient_bc):
    if patient_bc in mut_set:
        return True
    # check prefix first 12 chars
    p12 = patient_bc[:12]
    for m in mut_bcs:
        if m.startswith(patient_bc) or patient_bc.startswith(m) or m[:12]==p12:
            return True
    return False

# Build contingency counts
from collections import defaultdict
counts = defaultdict(lambda: {'Mutated':0,'Not_Mutated':0})
for p in uniq_patients:
    mutated = is_mutated(p['barcode'])
    if mutated:
        counts[p['histological_type']]['Mutated'] += 1
    else:
        counts[p['histological_type']]['Not_Mutated'] += 1

# Convert to list and filter row totals > 10
hist_list = []
for hist,vals in counts.items():
    total = vals['Mutated'] + vals['Not_Mutated']
    hist_list.append((hist, vals['Not_Mutated'], vals['Mutated'], total))

hist_list_sorted = sorted(hist_list, key=lambda x: -x[3])

# Filter
filtered = [h for h in hist_list_sorted if h[3] > 10]

if len(filtered) < 2:
    result = {
        'error': 'Not enough histological categories with total > 10 to compute chi-square after filtering.',
        'num_histologies_before_filter': len(hist_list_sorted),
        'num_histologies_after_filter': len(filtered),
        'clinical_patients_used': len(uniq_patients),
        'mutation_records_considered': len(mut_bcs)
    }
else:
    # build observed matrix rows x cols (Not_Mutated, Mutated)
    obs = np.array([[h[1], h[2]] for h in filtered], dtype=float)
    row_totals = obs.sum(axis=1).reshape(-1,1)
    col_totals = obs.sum(axis=0).reshape(1,-1)
    grand_total = obs.sum()
    expected = row_totals.dot(col_totals) / grand_total
    with np.errstate(divide='ignore', invalid='ignore'):
        chi2 = float(np.nansum((obs - expected)**2 / expected))

    observed_by_histology = { h[0]: {'Not_Mutated': int(h[1]), 'Mutated': int(h[2]), 'Row_Total': int(h[3])} for h in filtered }
    column_totals = {'Not_Mutated': int(col_totals[0,0]), 'Mutated': int(col_totals[0,1]), 'Grand_Total': int(grand_total)}
    result = {
        'chi2': chi2,
        'observed_by_histology': observed_by_histology,
        'column_totals': column_totals,
        'num_histologies_before_filter': len(hist_list_sorted),
        'num_histologies_after_filter': len(filtered),
        'clinical_patients_used': len(uniq_patients),
        'mutation_records_considered': len(mut_bcs)
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_66FQ3X8I18ech3D2reUjRPhU': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_ALFwwCUHSRMb52LoVoyfmAe6': [], 'var_call_AfruguUVTMgF3wc4Ch5gcjBG': [], 'var_call_eUsldShlvtnOeezxQrKnkSbu': 'file_storage/call_eUsldShlvtnOeezxQrKnkSbu.json', 'var_call_dMaeD4wkq2kaM19KCWRwr1ql': 'file_storage/call_dMaeD4wkq2kaM19KCWRwr1ql.json', 'var_call_VJG2iCWQfZt8H5NtOLSdoX0W': 'file_storage/call_VJG2iCWQfZt8H5NtOLSdoX0W.json', 'var_call_HFxYtNV89LYasiyD2KdL3Yyg': 'file_storage/call_HFxYtNV89LYasiyD2KdL3Yyg.json', 'var_call_13PJ6ag4wJfjS7k1zy1A2ftb': {'clinical_len': 1075, 'mutation_len': 261, 'clinical_sample_keys_types': [{'index': 0, 'keys': ['Patient_description', 'histological_type'], 'types': {'Patient_description': 'str', 'histological_type': 'str'}}, {'index': 1, 'keys': ['Patient_description', 'histological_type'], 'types': {'Patient_description': 'str', 'histological_type': 'str'}}, {'index': 2, 'keys': ['Patient_description', 'histological_type'], 'types': {'Patient_description': 'str', 'histological_type': 'str'}}, {'index': 3, 'keys': ['Patient_description', 'histological_type'], 'types': {'Patient_description': 'str', 'histological_type': 'str'}}, {'index': 4, 'keys': ['Patient_description', 'histological_type'], 'types': {'Patient_description': 'str', 'histological_type': 'str'}}], 'mutation_sample_keys_types': [{'index': 0, 'keys': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], 'types': {'ParticipantBarcode': 'str', 'Hugo_Symbol': 'str', 'HGVSp_Short': 'str', 'Variant_Classification': 'str', 'FILTER': 'str'}}, {'index': 1, 'keys': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], 'types': {'ParticipantBarcode': 'str', 'Hugo_Symbol': 'str', 'HGVSp_Short': 'str', 'Variant_Classification': 'str', 'FILTER': 'str'}}, {'index': 2, 'keys': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], 'types': {'ParticipantBarcode': 'str', 'Hugo_Symbol': 'str', 'HGVSp_Short': 'str', 'Variant_Classification': 'str', 'FILTER': 'str'}}, {'index': 3, 'keys': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], 'types': {'ParticipantBarcode': 'str', 'Hugo_Symbol': 'str', 'HGVSp_Short': 'str', 'Variant_Classification': 'str', 'FILTER': 'str'}}, {'index': 4, 'keys': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER'], 'types': {'ParticipantBarcode': 'str', 'Hugo_Symbol': 'str', 'HGVSp_Short': 'str', 'Variant_Classification': 'str', 'FILTER': 'str'}}]}}

exec(code, env_args)
