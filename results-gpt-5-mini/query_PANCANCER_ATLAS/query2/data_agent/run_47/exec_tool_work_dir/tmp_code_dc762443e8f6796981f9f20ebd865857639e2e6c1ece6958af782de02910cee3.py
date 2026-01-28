code = """import json
import re
import pandas as pd

# Load clinical data (may be file path or list)
clinical_var = var_call_DEhuV44hAKU1ycZWF25j9PRk
mut_var = var_call_Vi1MSRxkMmMFIu7MRWMTtqjI

def load_var(v):
    if isinstance(v, str):
        # assume file path to json
        with open(v, 'r') as f:
            return json.load(f)
    else:
        return v

clinical = load_var(clinical_var)
mutations = load_var(mut_var)

# Build mapping from participant barcode to histological_type for BRCA alive patients
# clinical records were filtered for Breast in the query, and represent alive rows (we used days_to_death IS NULL)
# But just in case, treat all provided clinical rows as BRCA alive

barcode_to_hist = {}
pattern = re.compile(r'TCGA[-A-Z0-9]+', re.IGNORECASE)
for rec in clinical:
    pd_desc = rec.get('Patient_description') or ''
    hist = rec.get('histological_type') or rec.get('histological_type')
    # try to extract TCGA barcode
    m = pattern.search(pd_desc)
    if m:
        barcode = m.group(0).upper()
        # normalize to first three segments TCGA-XX-XXXX or longer if present
        # keep as-is
        barcode_to_hist[barcode] = hist
    else:
        # try patient_id to construct barcode suffix if possible
        pid = rec.get('patient_id')
        if pid:
            pid = str(pid)
            # Many patient_id values are like A5EH or numeric; cannot reliably reconstruct full barcode
            # skip if no barcode
            pass

# Build set of mutated participant barcodes from mutations list
mutated_barcodes = set()
for rec in mutations:
    pb = rec.get('ParticipantBarcode')
    if pb:
        mutated_barcodes.add(pb.upper())

# Now compute per histological type counts among BRCA alive
# Need unique participants per hist type
hist_to_participants = {}
for barcode, hist in barcode_to_hist.items():
    if not hist:
        continue
    hist_to_participants.setdefault(hist, set()).add(barcode)

results = []
for hist, parts in hist_to_participants.items():
    total = len(parts)
    mutated = len(parts & mutated_barcodes)
    percent = (mutated / total * 100) if total > 0 else 0.0
    results.append({'histological_type': hist, 'total_patients': total, 'mutated_patients': mutated, 'percent_mutated': round(percent, 2)})

# Sort by percent descending, then by mutated count descending
results_sorted = sorted(results, key=lambda x: (-x['percent_mutated'], -x['mutated_patients']))

top3 = results_sorted[:3]

print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_iUQfzYNAvMO2NTkrqJi9n0OL': ['clinical_info'], 'var_call_coTtjiDkQbnvVczHiMr7D8Qt': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_nZGCimGA2p3KC1l2efQf10b9': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_AQQdg2MzfEnHYCs3QlIAm4vE': [], 'var_call_JpaRAb3Vd3CPu1ffJ8Hgc4rR': 'file_storage/call_JpaRAb3Vd3CPu1ffJ8Hgc4rR.json', 'var_call_DEhuV44hAKU1ycZWF25j9PRk': 'file_storage/call_DEhuV44hAKU1ycZWF25j9PRk.json', 'var_call_Vi1MSRxkMmMFIu7MRWMTtqjI': 'file_storage/call_Vi1MSRxkMmMFIu7MRWMTtqjI.json'}

exec(code, env_args)
