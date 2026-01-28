code = """import json
import re
import pandas as pd

# Load clinical data
clinical_var = var_call_N049iS6y1sxs1ADpsSYurYON
if isinstance(clinical_var, str):
    with open(clinical_var, 'r') as f:
        clinical = json.load(f)
else:
    clinical = clinical_var

# Load mutation data for CDH1
mut_var = var_call_70jFNmBs2ua7Z4rEe7SPUbYc
if isinstance(mut_var, str):
    with open(mut_var, 'r') as f:
        mutations = json.load(f)
else:
    mutations = mut_var

# Extract patient barcode from Patient_description
barcode_pattern = re.compile(r'(TCGA[^,;\)\s]+)')

barcode_to_hist = {}
for rec in clinical:
    desc = rec.get('Patient_description', '') or ''
    hist = rec.get('histological_type') or None
    m = barcode_pattern.search(desc)
    if m:
        barcode = m.group(1).strip()
        # Normalize barcode to uppercase
        barcode = barcode.upper()
        # If hist is empty or null, keep as None
        if isinstance(hist, str):
            hist = hist.strip()
            if hist == '':
                hist = None
        # Prefer existing non-null hist, otherwise set
        if barcode in barcode_to_hist:
            if not barcode_to_hist[barcode] and hist:
                barcode_to_hist[barcode] = hist
        else:
            barcode_to_hist[barcode] = hist

# Build set of mutated participant barcodes
mutated_barcodes = set()
for rec in mutations:
    pb = rec.get('ParticipantBarcode') or ''
    if pb:
        mutated_barcodes.add(pb.strip().upper())

# Build histology totals
from collections import defaultdict
hist_total = defaultdict(int)
hist_mutated = defaultdict(int)

for barcode, hist in barcode_to_hist.items():
    if not hist:
        continue
    hist_total[hist] += 1
    if barcode in mutated_barcodes:
        hist_mutated[hist] += 1

# Compute percentages
results = []
for hist, total in hist_total.items():
    mutated = hist_mutated.get(hist, 0)
    pct = (mutated / total) * 100 if total>0 else 0.0
    results.append({'histological_type': hist, 'num_patients': total, 'num_mutated': mutated, 'percentage': round(pct, 2)})

# Sort by percentage desc, then by num_patients desc
results_sorted = sorted(results, key=lambda x: (-x['percentage'], -x['num_patients']))

top3 = results_sorted[:3]

print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_VYvXeVPjOCVbu3y63iwPwL4X': ['clinical_info'], 'var_call_69615ybwI9V6VhPL2hBc9b0L': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_OX84Ot47Wejy51oYGG5LCJi8': [{'column_name': 'stopped_smoking_year', 'data_type': 'double precision'}, {'column_name': 'days_to_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_he', 'data_type': 'double precision'}, {'column_name': 'age_at_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'year_of_tobacco_smoking_onset', 'data_type': 'double precision'}, {'column_name': 'year_of_initial_pathologic_diagnosis', 'data_type': 'double precision'}, {'column_name': 'height', 'data_type': 'double precision'}, {'column_name': 'weight', 'data_type': 'double precision'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc', 'data_type': 'double precision'}, {'column_name': 'days_to_birth', 'data_type': 'double precision'}, {'column_name': 'total_pelv_lnr', 'data_type': 'double precision'}, {'column_name': 'total_aor_lnr', 'data_type': 'double precision'}, {'column_name': 'number_pack_years_smoked', 'data_type': 'double precision'}, {'column_name': 'prior_dx', 'data_type': 'text'}, {'column_name': 'ethnicity', 'data_type': 'text'}, {'column_name': 'informed_consent_verified', 'data_type': 'text'}, {'column_name': 'person_neoplasm_cancer_status', 'data_type': 'text'}, {'column_name': 'patient_id', 'data_type': 'text'}, {'column_name': 'histological_type', 'data_type': 'text'}, {'column_name': 'tissue_source_site', 'data_type': 'text'}, {'column_name': 'form_completion_date', 'data_type': 'text'}, {'column_name': 'pathologic_T', 'data_type': 'text'}, {'column_name': 'pathologic_M', 'data_type': 'text'}, {'column_name': 'clinical_M', 'data_type': 'text'}, {'column_name': 'pathologic_N', 'data_type': 'text'}, {'column_name': 'system_version', 'data_type': 'text'}, {'column_name': 'pathologic_stage', 'data_type': 'text'}, {'column_name': 'clinical_stage', 'data_type': 'text'}, {'column_name': 'clinical_T', 'data_type': 'text'}, {'column_name': 'clinical_N', 'data_type': 'text'}, {'column_name': 'extranodal_involvement', 'data_type': 'text'}, {'column_name': 'postoperative_rx_tx', 'data_type': 'text'}, {'column_name': 'primary_therapy_outcome_success', 'data_type': 'text'}, {'column_name': 'lymph_node_examined_count', 'data_type': 'text'}, {'column_name': 'primary_lymph_node_presentation_assessment', 'data_type': 'text'}, {'column_name': 'initial_pathologic_diagnosis_method', 'data_type': 'text'}, {'column_name': 'eastern_cancer_oncology_group', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision', 'data_type': 'text'}, {'column_name': 'residual_tumor', 'data_type': 'text'}, {'column_name': 'histological_type_other', 'data_type': 'text'}, {'column_name': 'init_pathology_dx_method_other', 'data_type': 'text'}, {'column_name': 'karnofsky_performance_score', 'data_type': 'text'}, {'column_name': 'neoplasm_histologic_grade', 'data_type': 'text'}, {'column_name': 'tobacco_smoking_history', 'data_type': 'text'}, {'column_name': 'performance_status_scale_timing', 'data_type': 'text'}, {'column_name': 'laterality', 'data_type': 'text'}, {'column_name': 'targeted_molecular_therapy', 'data_type': 'text'}, {'column_name': 'anatomic_neoplasm_subdivision_other', 'data_type': 'text'}, {'column_name': 'patient_death_reason', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site_other', 'data_type': 'text'}, {'column_name': 'menopause_status', 'data_type': 'text'}, {'column_name': 'margin_status', 'data_type': 'text'}, {'column_name': 'kras_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'venous_invasion', 'data_type': 'text'}, {'column_name': 'lymphatic_invasion', 'data_type': 'text'}, {'column_name': 'perineural_invasion_present', 'data_type': 'text'}, {'column_name': 'her2_immunohistochemistry_level_result', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_surgical_procedure_name', 'data_type': 'text'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'data_type': 'text'}, {'column_name': 'axillary_lymph_node_stage_method_type', 'data_type': 'text'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status', 'data_type': 'text'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'data_type': 'text'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'data_type': 'text'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'data_type': 'text'}, {'column_name': 'additional_pharmaceutical_therapy', 'data_type': 'text'}, {'column_name': 'additional_radiation_therapy', 'data_type': 'text'}, {'column_name': 'lymphovascular_invasion_present', 'data_type': 'text'}, {'column_name': 'location_in_lung_parenchyma', 'data_type': 'text'}, {'column_name': 'pulmonary_function_test_performed', 'data_type': 'text'}, {'column_name': 'egfr_mutation_performed', 'data_type': 'text'}, {'column_name': 'diagnosis', 'data_type': 'text'}, {'column_name': 'eml4_alk_translocation_performed', 'data_type': 'text'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'hemoglobin_result', 'data_type': 'text'}, {'column_name': 'serum_calcium_result', 'data_type': 'text'}, {'column_name': 'platelet_qualitative_result', 'data_type': 'text'}, {'column_name': 'number_of_lymphnodes_positive', 'data_type': 'text'}, {'column_name': 'white_cell_count_result', 'data_type': 'text'}, {'column_name': 'alcohol_history_documented', 'data_type': 'text'}, {'column_name': 'family_history_of_cancer', 'data_type': 'text'}, {'column_name': 'braf_gene_analysis_performed', 'data_type': 'text'}, {'column_name': 'city_of_procurement', 'data_type': 'text'}, {'column_name': 'surgical_approach', 'data_type': 'text'}, {'column_name': 'peritoneal_wash', 'data_type': 'text'}, {'column_name': 'Patient_description', 'data_type': 'text'}, {'column_name': 'prior_glioma', 'data_type': 'text'}, {'column_name': 'days_to_death', 'data_type': 'text'}, {'column_name': 'days_to_last_followup', 'data_type': 'text'}, {'column_name': 'icd_10', 'data_type': 'text'}, {'column_name': 'tissue_retrospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'icd_o_3_histology', 'data_type': 'text'}, {'column_name': 'tissue_prospective_collection_indicator', 'data_type': 'text'}, {'column_name': 'history_of_neoadjuvant_treatment', 'data_type': 'text'}, {'column_name': 'icd_o_3_site', 'data_type': 'text'}, {'column_name': 'tumor_tissue_site', 'data_type': 'text'}, {'column_name': 'new_tumor_event_after_initial_treatment', 'data_type': 'text'}, {'column_name': 'radiation_therapy', 'data_type': 'text'}, {'column_name': 'race', 'data_type': 'text'}], 'var_call_LkgYEE6KBAjAdVcWKDO9qWTI': [], 'var_call_4RWFq2M1yrRRJV82x3egiNaS': 'file_storage/call_4RWFq2M1yrRRJV82x3egiNaS.json', 'var_call_N049iS6y1sxs1ADpsSYurYON': 'file_storage/call_N049iS6y1sxs1ADpsSYurYON.json', 'var_call_70jFNmBs2ua7Z4rEe7SPUbYc': 'file_storage/call_70jFNmBs2ua7Z4rEe7SPUbYc.json'}

exec(code, env_args)
