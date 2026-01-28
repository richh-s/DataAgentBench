code = """import json
import re
import math

# Load raw data
with open(var_call_6n8cFRXID0ZaC8CR9ehacfdZ, 'r') as f:
    clinical_records = json.load(f)
with open(var_call_Wdf1boG23o9uHBgef9nZbqm8, 'r') as f:
    mutation_records = json.load(f)

# Clean and normalize clinical records into flat list
clean_clin = []
for rec in clinical_records:
    # rec may have various keys; extract needed safely
    pd_desc = rec.get('Patient_description') if isinstance(rec.get('Patient_description'), str) else ''
    hist = rec.get('histological_type')
    # if hist is list or dict, convert to string
    if isinstance(hist, list):
        hist = ' '.join([str(x) for x in hist])
    if isinstance(hist, dict):
        hist = str(hist)
    # attempt to find barcode
    barcode = rec.get('barcode')
    if not barcode:
        if isinstance(pd_desc, str):
            m = re.search(r'(TCGA-[A-Za-z0-9-]+)', pd_desc)
            if m:
                barcode = m.group(1)
    clean_clin.append({'histological_type': hist, 'Patient_description': pd_desc, 'barcode': barcode})

# Build mutated set
mutated_set = set()
for m in mutation_records:
    pb = m.get('ParticipantBarcode')
    if isinstance(pb, str):
        mutated_set.add(pb)

# Filter clinical for female BRCA: Patient_description contains 'Breast' and 'FEMALE'
filtered = []
for r in clean_clin:
    pd_desc = (r.get('Patient_description') or '')
    hist = r.get('histological_type')
    barcode = r.get('barcode')
    if not pd_desc or not hist or not barcode:
        continue
    if 'breast' not in pd_desc.lower():
        continue
    if 'female' not in pd_desc.lower():
        continue
    # normalize hist
    hist_s = str(hist).strip()
    if hist_s.lower() in ('none',''):
        continue
    filtered.append({'histological_type': hist_s, 'barcode': barcode})

# Deduplicate by barcode: keep first
seen = set()
dedup = []
for r in filtered:
    if r['barcode'] in seen:
        continue
    seen.add(r['barcode'])
    dedup.append(r)

# Build contingency counts per histological_type
from collections import defaultdict
counts = defaultdict(lambda: {'mutated':0, 'not_mutated':0})
for r in dedup:
    hist = r['histological_type']
    is_mut = r['barcode'] in mutated_set
    if is_mut:
        counts[hist]['mutated'] += 1
    else:
        counts[hist]['not_mutated'] += 1

# Compute totals and separate included/excluded
included = {}
excluded = []
for hist, c in counts.items():
    total = c['mutated'] + c['not_mutated']
    if total > 10:
        included[hist] = {'mutated': c['mutated'], 'not_mutated': c['not_mutated'], 'total': total}
    else:
        excluded.append({'histological_type': hist, 'count': total})

# Compute chi-square on included categories
chi2 = None
grand_total = sum(v['mutated'] + v['not_mutated'] for v in included.values())
if grand_total > 0 and len(included) > 0:
    # Build observed matrix rows hist, cols mutated, not_mutated
    hist_list = list(included.keys())
    obs = []
    for h in hist_list:
        obs.append([included[h]['mutated'], included[h]['not_mutated']])
    # compute expected and chi2
    chi2_val = 0.0
    # compute row and col totals
    row_totals = [sum(r) for r in obs]
    col_totals = [sum(obs[i][j] for i in range(len(obs))) for j in range(2)]
    for i in range(len(obs)):
        for j in range(2):
            expected = row_totals[i] * col_totals[j] / grand_total if grand_total>0 else 0
            if expected>0:
                chi2_val += (obs[i][j] - expected)**2 / expected
    chi2 = float(chi2_val)

result = {
    'grand_total_included': grand_total,
    'num_histological_types_included': len(included),
    'histological_types_included': list(included.keys()),
    'excluded_histological_types_marginal_le_10': excluded,
    'contingency_table_included': included,
    'chi2_statistic': chi2
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_s9wC2ntinBw0upr3tf0q4sJC': ['clinical_info'], 'var_call_Vz4gQCjzS0LU588kx22nykpM': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_BojVfzEgn1m1TrDIYKqsxKw1': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_7E2xMhgXQ9cyFAS7u4FVipbp': [], 'var_call_Az627EUCkiX4ZQoHJncsHvK3': 'file_storage/call_Az627EUCkiX4ZQoHJncsHvK3.json', 'var_call_CUSR7OoFmOI05A7C9xpFh4aq': 'file_storage/call_CUSR7OoFmOI05A7C9xpFh4aq.json', 'var_call_ES3caRinNPdx1ICW2wmOFxFQ': 'file_storage/call_ES3caRinNPdx1ICW2wmOFxFQ.json', 'var_call_6n8cFRXID0ZaC8CR9ehacfdZ': 'file_storage/call_6n8cFRXID0ZaC8CR9ehacfdZ.json', 'var_call_Wdf1boG23o9uHBgef9nZbqm8': 'file_storage/call_Wdf1boG23o9uHBgef9nZbqm8.json', 'var_call_0OiPHxD7mfr67GXjt0cbI4bS': {'clinical_len': 1075, 'mutation_len': 261, 'clinical_sample_5': [{'patient_id': 'A5EH', 'histological_type': 'Infiltrating Ductal Carcinoma', 'Patient_description': 'Clinical entry D13FB44B-291B-4EA4-920C-142DAA8D1989 identifies patient TCGA-AC-A5EH, a FEMALE subject with Breast invasive carcinoma. Their current vital status is Alive.', 'barcode': 'TCGA-AC-A5EH'}, {'patient_id': 'A7SZ', 'histological_type': 'Infiltrating Ductal Carcinoma', 'Patient_description': 'Record 09A5E9FD-D816-4F8C-BAA9-0E40BA607B16 refers to patient TCGA-LL-A7SZ, a FEMALE diagnosed with Breast invasive carcinoma. Vital status recorded as Alive.', 'barcode': 'TCGA-LL-A7SZ'}, {'patient_id': 'A0FY', 'histological_type': 'Infiltrating Ductal Carcinoma', 'Patient_description': "Patient TCGA-AN-A0FY, registered under UUID de75d0b9-0f47-4732-8df5-05c350cfcd32, belongs to the Breast invasive carcinoma cohort. This FEMALE patient's vital status is Alive.", 'barcode': 'TCGA-AN-A0FY'}, {'patient_id': 'A2FB', 'histological_type': 'Infiltrating Lobular Carcinoma', 'Patient_description': 'Patient TCGA-AC-A2FB (UUID 02BBB632-0F7F-439D-B8F0-C86A06237424) is a FEMALE diagnosed with Breast invasive carcinoma. Current vital status: Alive.', 'barcode': 'TCGA-AC-A2FB'}, {'patient_id': 'A1KR', 'histological_type': 'Infiltrating Ductal Carcinoma', 'Patient_description': 'The individual with barcode TCGA-AO-A1KR and UUID b7f74ae1-6f58-447c-be50-a7666eb19d9a is a FEMALE case of Breast invasive carcinoma, documented with vital status = Alive.', 'barcode': 'TCGA-AO-A1KR'}], 'mutation_sample_5': [{'ParticipantBarcode': 'TCGA-A2-A0YL', 'HGVSp_Short': 'p.T364Hfs*4', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-AR-A1AT', 'HGVSp_Short': 'p.N315Ifs*41', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-BS-A0U8', 'HGVSp_Short': 'p.A824V', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-D8-A27G', 'HGVSp_Short': 'p.G169Rfs*5', 'FILTER': 'PASS'}, {'ParticipantBarcode': 'TCGA-E6-A1LX', 'HGVSp_Short': 'p.R598Q', 'FILTER': 'PASS'}]}}

exec(code, env_args)
