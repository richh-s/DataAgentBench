code = """import json
# Load clinical mapping and mutation data from storage paths
clin_path = var_call_aEeegfuhOPkGiJimuBvYflRR
mut_path = var_call_x4jAhvfkw2QwnuF8jGVcVZHQ

# load files
if isinstance(clin_path, str) and clin_path.endswith('.json'):
    clin = json.load(open(clin_path,'r'))
else:
    clin = clin_path

if isinstance(mut_path, str) and mut_path.endswith('.json'):
    mut = json.load(open(mut_path,'r'))
else:
    mut = mut_path

mapping = clin.get('mapping', {})
# Normalize histological types
for k,v in list(mapping.items()):
    if v is None:
        mapping[k] = ''
    else:
        mapping[k] = str(v).strip()

# Get set of participant barcodes with CDH1 PASS
mut_bcs = set()
for r in mut:
    if r.get('Hugo_Symbol')=='CDH1' and r.get('FILTER')=='PASS' and r.get('ParticipantBarcode'):
        mut_bcs.add(r['ParticipantBarcode'].strip())

# Build counts per histology among mapped breast female patients
from collections import defaultdict
hist_total = defaultdict(int)
hist_mut = defaultdict(int)

for bc, hist in mapping.items():
    if not hist:
        continue
    hist_total[hist] += 1
    if bc in mut_bcs:
        hist_mut[hist] += 1

# Exclude categories with marginal totals <= 10
included_hists = [h for h,t in hist_total.items() if t>10]
included_hists.sort()

contingency = []
mut_total = 0
for h in included_hists:
    total = hist_total[h]
    mutated = hist_mut.get(h,0)
    non_mut = total - mutated
    contingency.append({'histological_type': h, 'mutated': mutated, 'non_mutated': non_mut, 'row_total': total})
    mut_total += mutated

grand_total = sum([c['row_total'] for c in contingency])
non_mut_total = grand_total - mut_total

# Compute chi-square
chi2 = 0.0
expected_issues = False
for c in contingency:
    row = c['row_total']
    for col_name, obs in [('mutated', c['mutated']), ('non_mutated', c['non_mutated'])]:
        col_total = mut_total if col_name=='mutated' else non_mut_total
        E = (row * col_total) / grand_total if grand_total>0 else 0
        if E<=0:
            expected_issues = True
            contrib = 0.0
        else:
            contrib = (obs - E)**2 / E
        chi2 += contrib

output = {
    'included_hist_types_count': len(included_hists),
    'grand_total_included_patients': grand_total,
    'mutation_positive_total': mut_total,
    'mutation_negative_total': non_mut_total,
    'contingency_table': contingency,
    'chi_square_statistic': chi2,
    'expected_issues': expected_issues
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_gnkk8fpHmSlDHx10i0O1Iqsd': ['clinical_info'], 'var_call_RIv0D6uaGgToAR3GNVwIRusK': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_b7DquHDLKdwWsHEpxoW8FUAc': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_6WomJxnRwOxPXfaD3FeMmmQr': [], 'var_call_P0xnvuTDZQzT0r9YKChsst0T': 'file_storage/call_P0xnvuTDZQzT0r9YKChsst0T.json', 'var_call_SNALiDeCXeNh9QGULdYLxEMc': [], 'var_call_v8jOJ11XkfHIQGDbAeu6jvmc': 'file_storage/call_v8jOJ11XkfHIQGDbAeu6jvmc.json', 'var_call_aEeegfuhOPkGiJimuBvYflRR': 'file_storage/call_aEeegfuhOPkGiJimuBvYflRR.json', 'var_call_x4jAhvfkw2QwnuF8jGVcVZHQ': 'file_storage/call_x4jAhvfkw2QwnuF8jGVcVZHQ.json', 'var_call_70J7VjXJFxxgac1v4beM9hhE': {'total_CDH1_PASS': 247, 'CDH1_in_breast_barcodes_count': 92, 'CDH1_in_breast_barcodes_sample': ['TCGA-4H-AAAK', 'TCGA-5L-AAT0', 'TCGA-A1-A0SE', 'TCGA-A2-A0CK', 'TCGA-A2-A0CR', 'TCGA-A2-A0EW', 'TCGA-A2-A0SY', 'TCGA-A2-A0T4', 'TCGA-A2-A0T6', 'TCGA-A2-A0YD', 'TCGA-A2-A0YK', 'TCGA-A2-A0YL', 'TCGA-A2-A1FV', 'TCGA-A2-A1G0', 'TCGA-A2-A25A', 'TCGA-A2-A4S2', 'TCGA-A7-A425', 'TCGA-A7-A4SC', 'TCGA-A7-A5ZX', 'TCGA-AC-A2B8', 'TCGA-AC-A2FB', 'TCGA-AC-A2FF', 'TCGA-AC-A2FG', 'TCGA-AC-A2FO', 'TCGA-AC-A3OD', 'TCGA-AC-A3QQ', 'TCGA-AC-A3YI', 'TCGA-AC-A4ZE', 'TCGA-AC-A5XS', 'TCGA-AC-A6IV', 'TCGA-AC-A6IX', 'TCGA-AC-A8OS', 'TCGA-AO-A128', 'TCGA-AR-A1AL', 'TCGA-AR-A1AT', 'TCGA-AR-A24X', 'TCGA-AR-A2LE', 'TCGA-AR-A2LK', 'TCGA-AR-A2LN', 'TCGA-AR-A5QM', 'TCGA-B6-A0IH', 'TCGA-B6-A0RQ', 'TCGA-B6-A0X7', 'TCGA-B6-A2IU', 'TCGA-B6-A40B', 'TCGA-B6-A40C', 'TCGA-BH-A0C1', 'TCGA-BH-A0E9', 'TCGA-BH-A0HP', 'TCGA-BH-A18F', 'TCGA-BH-A18P', 'TCGA-BH-A209', 'TCGA-BH-A28Q', 'TCGA-BH-A8FY', 'TCGA-BH-AB28', 'TCGA-C8-A1HO', 'TCGA-C8-A274', 'TCGA-C8-A3M7', 'TCGA-D8-A1XO', 'TCGA-D8-A1Y1', 'TCGA-D8-A27G', 'TCGA-D8-A27I', 'TCGA-D8-A27V', 'TCGA-D8-A3Z6', 'TCGA-E2-A576', 'TCGA-EW-A1IZ', 'TCGA-EW-A1J5', 'TCGA-EW-A423', 'TCGA-EW-A6SC', 'TCGA-GI-A2C8', 'TCGA-GM-A2DD', 'TCGA-GM-A2DO', 'TCGA-GM-A4E0', 'TCGA-GM-A5PV', 'TCGA-GM-A5PX', 'TCGA-LD-A66U', 'TCGA-LD-A74U', 'TCGA-LD-A7W6', 'TCGA-LL-A50Y', 'TCGA-LL-A6FP', 'TCGA-LL-A9Q3', 'TCGA-OL-A66K', 'TCGA-OL-A66N', 'TCGA-OL-A6VQ', 'TCGA-PE-A5DD', 'TCGA-PE-A5DE', 'TCGA-S3-A6ZG', 'TCGA-W8-A86G', 'TCGA-WT-AB44', 'TCGA-XX-A899', 'TCGA-XX-A89A', 'TCGA-Z7-A8R5'], 'example_mapping_count': 988}}

exec(code, env_args)
