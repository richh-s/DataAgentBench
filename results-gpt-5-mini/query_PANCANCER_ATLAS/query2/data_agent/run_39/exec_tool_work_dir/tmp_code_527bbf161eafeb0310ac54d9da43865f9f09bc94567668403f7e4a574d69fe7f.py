code = """import json, re, pandas as pd

# Load files from storage
with open(var_call_jW9c281oFItWtateg7CYJ8v6, 'r') as f:
    clinical = json.load(f)
with open(var_call_B2tbV0oD8IejgNJqazs7ZjeK, 'r') as f:
    cdhs = json.load(f)

# helper to get patient id as first three segments of TCGA barcode
def patient_id(barcode):
    if not barcode or not isinstance(barcode, str):
        return None
    parts = barcode.split('-')
    if len(parts) >= 3:
        return '-'.join(parts[:3]).upper()
    return barcode.upper()

# extract clinical records: get barcode and histological_type
records = []
pat_re = re.compile(r'TCGA[-][A-Za-z0-9-]+', re.IGNORECASE)
for rec in clinical:
    desc = rec.get('Patient_description','')
    hist = rec.get('histological_type')
    if not desc or not hist:
        continue
    m = pat_re.search(desc)
    if not m:
        continue
    bc = m.group(0).upper()
    pid = patient_id(bc)
    if pid:
        records.append({'patient_barcode': bc, 'patient_id': pid, 'histological_type': hist.strip()})

df = pd.DataFrame(records)

# build set of CDH1-mutated patient IDs
cdh_patient_ids = set()
for d in cdhs:
    pb = d.get('ParticipantBarcode')
    if not pb:
        continue
    pid = patient_id(pb.upper())
    if pid:
        cdh_patient_ids.add(pid)

# Now, for each histological_type, compute total unique patients and number mutated
if df.empty:
    result = []
else:
    grouped = df.groupby('histological_type')
    rows = []
    for hist, g in grouped:
        unique_pids = set(g['patient_id'].unique())
        total = len(unique_pids)
        mutated = len([p for p in unique_pids if p in cdh_patient_ids])
        pct = round((mutated/total*100) if total>0 else 0.0, 2)
        rows.append({'histological_type': hist, 'total_alive_patients': int(total), 'mutated_patients': int(mutated), 'percent_mutated': pct})
    rows_sorted = sorted(rows, key=lambda x: (-x['percent_mutated'], -x['mutated_patients'], -x['total_alive_patients']))
    result = rows_sorted[:3]

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Rpcp0xB7n7YmXOWMpetNfMNd': [{'column_name': 'stopped_smoking_year'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'days_to_birth'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'Patient_description'}, {'column_name': 'prior_glioma'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}], 'var_call_pIdN2BxAeTwCpfyvPXumfvRf': [], 'var_call_dOUG1fLBdlHlQkAJQoMwlCaN': 'file_storage/call_dOUG1fLBdlHlQkAJQoMwlCaN.json', 'var_call_w6dmyPqPMeCUrCkVW3cSlvSr': 'file_storage/call_w6dmyPqPMeCUrCkVW3cSlvSr.json', 'var_call_jW9c281oFItWtateg7CYJ8v6': 'file_storage/call_jW9c281oFItWtateg7CYJ8v6.json', 'var_call_B2tbV0oD8IejgNJqazs7ZjeK': 'file_storage/call_B2tbV0oD8IejgNJqazs7ZjeK.json', 'var_call_SCWXnYMpnQxZpRVT7AJT0TdI': [], 'var_call_UWHbfbSkS2ZdYrJfIra3Lmpy': 'file_storage/call_UWHbfbSkS2ZdYrJfIra3Lmpy.json'}

exec(code, env_args)
