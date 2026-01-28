code = """import json
import pandas as pd
import math

# Load the stored query results from files
with open(var_call_unNwwMUOPz6F6oOWS2rQeaE5, 'r') as f:
    clinical = json.load(f)
with open(var_call_2PsEhI7biypyNTDVPBxoFnG2, 'r') as f:
    rna = json.load(f)

# Prepare clinical list: each has Patient_description and histological_type
# Filter clinical histological_type that are not enclosed in square brackets
import re

def is_valid_histology(h):
    if h is None:
        return False
    h = str(h).strip()
    if h == "":
        return False
    # exclude if entire annotation is enclosed in square brackets
    if re.match(r'^\[.*\]$', h):
        return False
    return True

# Build list of clinical records with patient_description and histology
clinical_records = []
for rec in clinical:
    pd_desc = rec.get('Patient_description')
    hist = rec.get('histological_type')
    if pd_desc and is_valid_histology(hist):
        clinical_records.append({'Patient_description': pd_desc, 'histological_type': hist})

# Convert RNA normalized_count to float where possible
rna_records = []
for rec in rna:
    pb = rec.get('ParticipantBarcode')
    nc = rec.get('normalized_count')
    try:
        nc_f = float(nc)
    except Exception:
        continue
    if pb:
        rna_records.append({'ParticipantBarcode': pb, 'normalized_count': nc_f})

# For each RNA record, try to find clinical LGG patient whose Patient_description contains the ParticipantBarcode
# Aggregate normalized_counts by histological_type
hist_counts = {}

for r in rna_records:
    pb = r['ParticipantBarcode']
    nc = r['normalized_count']
    matched = False
    for crec in clinical_records:
        if pb in crec['Patient_description']:
            hist = crec['histological_type']
            hist_counts.setdefault(hist, []).append(nc)
            matched = True
            break
    # If not matched, continue

# Compute average log10(normalized_count + 1) per histology
results = {}
for hist, counts in hist_counts.items():
    # filter valid numeric counts
    vals = []
    for c in counts:
        if c is None:
            continue
        try:
            v = float(c)
            if math.isnan(v):
                continue
            vals.append(math.log10(v + 1.0))
        except Exception:
            continue
    if len(vals) == 0:
        continue
    mean_val = sum(vals) / len(vals)
    # format with at least 4 decimals
    results[hist] = round(mean_val, 6)

# Sort results by histology name for consistent output
sorted_results = {k: results[k] for k in sorted(results.keys())}

import json
print("__RESULT__:")
print(json.dumps(sorted_results))"""

env_args = {'var_call_bc7RXletrC8qOmG6cX6iCoMX': ['clinical_info'], 'var_call_1UsWh85Z4nyymtSkCrB2XGa2': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_yeLL3kWKTGLGafRGxj5zrohU': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_t3u1EtJl7LYrOgTmzhzQMBb9': 'file_storage/call_t3u1EtJl7LYrOgTmzhzQMBb9.json', 'var_call_1h7dzUBRM2wVgFklfoDkFeyQ': 'file_storage/call_1h7dzUBRM2wVgFklfoDkFeyQ.json', 'var_call_2PsEhI7biypyNTDVPBxoFnG2': 'file_storage/call_2PsEhI7biypyNTDVPBxoFnG2.json', 'var_call_unNwwMUOPz6F6oOWS2rQeaE5': 'file_storage/call_unNwwMUOPz6F6oOWS2rQeaE5.json'}

exec(code, env_args)
