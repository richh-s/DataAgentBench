code = """import json
import re
from collections import defaultdict
# Load mutation participant barcodes (file path stored in var_call_lLJsBwzhTCgMM2CQeHsfdT5F)
path_mut = var_call_lLJsBwzhTCgMM2CQeHsfdT5F
with open(path_mut, 'r') as f:
    mut_data = json.load(f)
# Load clinical BRCA alive records (file path stored in var_call_52e6UDbGq7dZ6hfFKgT6Aw7Y)
path_clin = var_call_52e6UDbGq7dZ6hfFKgT6Aw7Y
with open(path_clin, 'r') as f:
    clin_data = json.load(f)
# Extract mutated participant barcodes for BRCA
mut_barcodes = set()
for r in mut_data:
    pb = r.get('ParticipantBarcode')
    if pb and pb.upper().startswith('TCGA-BR-'):
        mut_barcodes.add(pb.upper())
# Build histological type -> set of patient barcodes from clinical data
hist_to_barcodes = defaultdict(set)
barcode_pattern = re.compile(r'TCGA-BR-[A-Z0-9-]+', re.IGNORECASE)
for r in clin_data:
    desc = r.get('Patient_description','')
    hist = r.get('histological_type')
    if not hist or hist in ['None', '[Not Applicable]', '']:
        hist = 'Unknown'
    m = barcode_pattern.search(desc)
    if m:
        barcode = m.group(0).upper()
        hist_to_barcodes[hist].add(barcode)
# Compute percentages
results = []
for hist, bset in hist_to_barcodes.items():
    total = len(bset)
    if total == 0:
        continue
    mutated = len(bset & mut_barcodes)
    percent = (mutated / total) * 100
    results.append({'histological_type': hist, 'total_alive_patients': total, 'cdh1_mutated_patients': mutated, 'percentage_mutated': round(percent,2)})
# Sort by percentage desc, then mutated count desc
results_sorted = sorted(results, key=lambda x: (-x['percentage_mutated'], -x['cdh1_mutated_patients'], x['histological_type']))
top3 = results_sorted[:3]
print('__RESULT__:')
print(json.dumps(top3))"""

env_args = {'var_call_7VPsp2nmm0BFOeMooG8FVxj7': ['clinical_info'], 'var_call_jwp5Ztyo54VKQSLLNASnS5Mq': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_EJDnqfTdPKQTvUTBa42yj7YA': 'file_storage/call_EJDnqfTdPKQTvUTBa42yj7YA.json', 'var_call_Qp0YKK65hQDTdDdvG5uHZcAJ': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'var_call_lLJsBwzhTCgMM2CQeHsfdT5F': 'file_storage/call_lLJsBwzhTCgMM2CQeHsfdT5F.json', 'var_call_OaOdXI0BlRKkhde1bVhOqEqy': [], 'var_call_52e6UDbGq7dZ6hfFKgT6Aw7Y': 'file_storage/call_52e6UDbGq7dZ6hfFKgT6Aw7Y.json', 'var_call_7C3ebSYKwsO84nwfk85JisjI': 'file_storage/call_7C3ebSYKwsO84nwfk85JisjI.json'}

exec(code, env_args)
