code = """import json
import re
import pandas as pd
import math

# Load previous tool results from storage
with open(var_call_M4kR9eXLPADUc96LRcUgX8Eg, 'r') as f:
    clinical = json.load(f)
with open(var_call_Cd7KTf5mF3IeP5HjCqCm07wB, 'r') as f:
    mutations = json.load(f)

# Extract barcode from Patient_description using regex
barcode_re = re.compile(r'(TCGA-[A-Za-z0-9\-]+)')

rows = []
for rec in clinical:
    desc = rec.get('Patient_description', '')
    hist = rec.get('histological_type')
    if not desc or not hist:
        continue
    m = barcode_re.search(desc)
    if not m:
        continue
    barcode = m.group(1)
    rows.append({'barcode': barcode, 'histological_type': hist})

# Create DataFrame and deduplicate by barcode (keep first)
df_clin = pd.DataFrame(rows).drop_duplicates(subset=['barcode']).reset_index(drop=True)

# Build set of patients with CDH1 PASS mutations
mutated_barcodes = set([m['ParticipantBarcode'] for m in mutations if m.get('ParticipantBarcode')])

# Filter clinical dataframe to those in BRCA cohort (already filtered by query) and known hist types
# Mark mutation status

df_clin['mutated'] = df_clin['barcode'].apply(lambda b: b in mutated_barcodes)

# Build contingency counts by histological_type
grouped = df_clin.groupby('histological_type')['mutated'].agg(lambda s: (s.sum(), (~s).sum()))
# grouped is a Series of tuples (mutated_count, not_mutated_count)
contingency = {}
for hist, (mut_ct, not_ct) in grouped.items():
    contingency[hist] = {'mutated': int(mut_ct), 'not_mutated': int(not_ct), 'total': int(mut_ct + not_ct)}

# Exclude histological categories with marginal totals <= 10
included = {h: v for h, v in contingency.items() if v['total'] > 10}

# If fewer than 2 categories remain, chi-square cannot be computed
if len(included) < 2:
    result = {
        'chi2': None,
        'degrees_of_freedom': 0,
        'included_histological_types': list(included.keys()),
        'contingency_table': included,
        'grand_total': sum(v['total'] for v in included.values()),
        'note': 'Not enough histological categories with total > 10 to compute chi-square.'
    }
else:
    # Build observed matrix rows x 2
    hist_types = sorted(included.keys())
    obs = []
    for h in hist_types:
        obs.append([included[h]['mutated'], included[h]['not_mutated']])
    # Convert to numeric
    grand_total = sum(sum(r) for r in obs)
    col_totals = [sum(r[i] for r in obs) for i in range(2)]
    row_totals = [sum(r) for r in obs]

    # Compute chi-square statistic
    chi2 = 0.0
    for i, r in enumerate(obs):
        for j, o in enumerate(r):
            e = row_totals[i] * col_totals[j] / grand_total if grand_total > 0 else 0
            if e > 0:
                chi2 += (o - e) ** 2 / e
    dof = (len(obs) - 1) * (2 - 1)

    result = {
        'chi2': chi2,
        'degrees_of_freedom': dof,
        'included_histological_types': hist_types,
        'contingency_table': included,
        'grand_total': grand_total
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jrzL1JAOF5mgtQdtHfOm1ruH': ['clinical_info'], 'var_call_jp7TjQrnDSOv9DsAozaptY6n': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_VmdJjDAWAqoMUXw0Wu03Aqsf': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_8DEV15gfyPIWWGDqMyvMbmLx': [], 'var_call_6wf2xpgXotISunrkNNzSnmO7': [], 'var_call_F76AvL4CXp3KEyh0Woeq5aHz': 'file_storage/call_F76AvL4CXp3KEyh0Woeq5aHz.json', 'var_call_M4kR9eXLPADUc96LRcUgX8Eg': 'file_storage/call_M4kR9eXLPADUc96LRcUgX8Eg.json', 'var_call_k8ep0oWpDFo4vGHLfcTI3AQF': [{'ParticipantBarcode': 'TCGA-EJ-5501'}, {'ParticipantBarcode': 'TCGA-EJ-5514'}, {'ParticipantBarcode': 'TCGA-EJ-5531'}, {'ParticipantBarcode': 'TCGA-EJ-7115'}, {'ParticipantBarcode': 'TCGA-EJ-7783'}, {'ParticipantBarcode': 'TCGA-EK-A2RC'}, {'ParticipantBarcode': 'TCGA-EK-A2RN'}, {'ParticipantBarcode': 'TCGA-EM-A2CK'}, {'ParticipantBarcode': 'TCGA-EM-A2OW'}, {'ParticipantBarcode': 'TCGA-EM-A2OZ'}, {'ParticipantBarcode': 'TCGA-EM-A3AL'}, {'ParticipantBarcode': 'TCGA-EM-A3AP'}, {'ParticipantBarcode': 'TCGA-EM-A3AQ'}, {'ParticipantBarcode': 'TCGA-EM-A4FF'}, {'ParticipantBarcode': 'TCGA-ER-A198'}, {'ParticipantBarcode': 'TCGA-ER-A19D'}, {'ParticipantBarcode': 'TCGA-ER-A19H'}, {'ParticipantBarcode': 'TCGA-ER-A3PL'}, {'ParticipantBarcode': 'TCGA-ET-A2N3'}, {'ParticipantBarcode': 'TCGA-ET-A3BP'}, {'ParticipantBarcode': 'TCGA-ET-A3BX'}, {'ParticipantBarcode': 'TCGA-ET-A3DO'}, {'ParticipantBarcode': 'TCGA-ET-A4KQ'}, {'ParticipantBarcode': 'TCGA-EV-5903'}, {'ParticipantBarcode': 'TCGA-EW-A1J1'}, {'ParticipantBarcode': 'TCGA-EW-A1PD'}, {'ParticipantBarcode': 'TCGA-F7-A50G'}, {'ParticipantBarcode': 'TCGA-FD-A3B8'}, {'ParticipantBarcode': 'TCGA-FD-A3SL'}, {'ParticipantBarcode': 'TCGA-FD-A3SN'}, {'ParticipantBarcode': 'TCGA-FD-A43U'}, {'ParticipantBarcode': 'TCGA-FD-A43Y'}, {'ParticipantBarcode': 'TCGA-FD-A5BS'}, {'ParticipantBarcode': 'TCGA-FG-7637'}, {'ParticipantBarcode': 'TCGA-FG-8186'}, {'ParticipantBarcode': 'TCGA-FG-8189'}, {'ParticipantBarcode': 'TCGA-FG-A4MU'}, {'ParticipantBarcode': 'TCGA-FI-A2D2'}, {'ParticipantBarcode': 'TCGA-FX-A48G'}, {'ParticipantBarcode': 'TCGA-FY-A40L'}, {'ParticipantBarcode': 'TCGA-G2-A2EJ'}, {'ParticipantBarcode': 'TCGA-G2-A2EL'}, {'ParticipantBarcode': 'TCGA-G3-A3CK'}, {'ParticipantBarcode': 'TCGA-G6-A8L8'}, {'ParticipantBarcode': 'TCGA-G7-A8LD'}, {'ParticipantBarcode': 'TCGA-G9-6333'}, {'ParticipantBarcode': 'TCGA-G9-6336'}, {'ParticipantBarcode': 'TCGA-G9-6339'}, {'ParticipantBarcode': 'TCGA-G9-6362'}, {'ParticipantBarcode': 'TCGA-GC-A3BM'}], 'var_call_Cd7KTf5mF3IeP5HjCqCm07wB': 'file_storage/call_Cd7KTf5mF3IeP5HjCqCm07wB.json'}

exec(code, env_args)
