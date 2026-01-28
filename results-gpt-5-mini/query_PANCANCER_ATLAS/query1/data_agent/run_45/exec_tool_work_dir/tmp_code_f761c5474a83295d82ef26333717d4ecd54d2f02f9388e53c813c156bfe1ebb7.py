code = """import json, re, math
import pandas as pd

# Load clinical LGG data and IGF2 expression data from storage file paths
with open(var_call_dT2QhpiZwggsr9UJnPdEMur1, 'r') as f:
    clin = json.load(f)
with open(var_call_FrKRnlntFTCccCh8YOT8qKKD, 'r') as f:
    expr = json.load(f)

# Build mapping from ParticipantBarcode (TCGA barcode) to histological_type
barcode_to_hist = {}
for rec in clin:
    hist = rec.get('histological_type')
    desc = rec.get('Patient_description', '')
    if not hist:
        continue
    # Exclude histology annotations enclosed in square brackets
    if '[' in hist or ']' in hist:
        continue
    m = re.search(r'(TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{4,6})', desc)
    if m:
        barcode = m.group(1)
        # Keep first mapping if duplicate
        if barcode not in barcode_to_hist:
            barcode_to_hist[barcode] = hist

# Aggregate log10(normalized_count + 1) by histology
hist_values = {}
for rec in expr:
    pb = rec.get('ParticipantBarcode')
    norm_raw = rec.get('normalized_count')
    if pb is None or norm_raw is None:
        continue
    # Only include if this participant is in our LGG mapping
    if pb not in barcode_to_hist:
        continue
    try:
        norm = float(norm_raw)
    except Exception:
        continue
    # Only include valid numeric expression values
    if math.isnan(norm):
        continue
    val = math.log10(norm + 1.0)
    hist = barcode_to_hist[pb]
    hist_values.setdefault(hist, []).append(val)

# Compute means and format with at least four decimal places
result = {}
for hist, vals in sorted(hist_values.items()):
    if len(vals) == 0:
        continue
    mean_val = sum(vals) / len(vals)
    # Format as string with 4 decimal places
    result[hist] = f"{mean_val:.4f}"

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mT1bjjVE8QMuRiOGjSjmS1Wq': ['clinical_info'], 'var_call_9JyoWp0xOjZoRu7qpTxE00dR': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_NYg9yHEFVuvR0isNzgaDSuzU': 'file_storage/call_NYg9yHEFVuvR0isNzgaDSuzU.json', 'var_call_CLzVg3YIgqG4UI22QdyyjvRW': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_oeDqHZhgenVofr9j4V6p3tk9': 'file_storage/call_oeDqHZhgenVofr9j4V6p3tk9.json', 'var_call_ixillOFNZOjQUKH4bA8SJj6y': [{'histological_type': 'Oligodendroglioma'}, {'histological_type': 'Astrocytoma'}, {'histological_type': 'Oligoastrocytoma'}], 'var_call_dT2QhpiZwggsr9UJnPdEMur1': 'file_storage/call_dT2QhpiZwggsr9UJnPdEMur1.json', 'var_call_2qdn2RQOhCBv0xehYigs5gpi': [{'cid': '0', 'name': 'ParticipantBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'SampleBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'AliquotBarcode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'SampleTypeLetterCode', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'SampleType', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'Symbol', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'Entrez', 'type': 'BIGINT', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '7', 'name': 'normalized_count', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_call_LionYAcFnwhSh6JCyD20EegC': [{'ParticipantBarcode': 'TCGA-AB-2908', 'Symbol': 'IGF2', 'normalized_count': '167.272646747735'}, {'ParticipantBarcode': 'TCGA-19-5960', 'Symbol': 'IGF2', 'normalized_count': '185.236'}, {'ParticipantBarcode': 'TCGA-21-1071', 'Symbol': 'IGF2', 'normalized_count': '80.6827'}, {'ParticipantBarcode': 'TCGA-30-1862', 'Symbol': 'IGF2', 'normalized_count': '13105.3695494317'}, {'ParticipantBarcode': 'TCGA-66-2795', 'Symbol': 'IGF2', 'normalized_count': '613.474'}], 'var_call_FrKRnlntFTCccCh8YOT8qKKD': 'file_storage/call_FrKRnlntFTCccCh8YOT8qKKD.json'}

exec(code, env_args)
