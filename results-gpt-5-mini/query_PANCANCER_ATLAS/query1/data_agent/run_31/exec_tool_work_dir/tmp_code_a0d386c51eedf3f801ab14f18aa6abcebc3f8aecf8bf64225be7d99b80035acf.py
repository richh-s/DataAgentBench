code = """import json, re, math
import pandas as pd
# load clinical LGG query results
fp_clin = var_call_S7BCQdsdew0EjltJNPKp5PUb
with open(fp_clin, 'r') as f:
    clin = json.load(f)
# load IGF2 expression rows
fp_rna = var_call_G9VFYpLZ3ET752f9v2CLIAA1
with open(fp_rna, 'r') as f:
    rna = json.load(f)
# parse TCGA barcodes from Patient_description
barcode_pattern = re.compile(r'TCGA-[A-Za-z0-9]{2}-[A-Za-z0-9]{3,4}')
barcode_to_hist = {}
for r in clin:
    pd_text = r.get('Patient_description','')
    hist = r.get('histological_type')
    if not pd_text or not hist:
        continue
    m = barcode_pattern.search(pd_text)
    if m:
        bc = m.group(0)
        # exclude histology annotations enclosed in square brackets
        if ('[' in str(hist)) or (']' in str(hist)):
            continue
        # store
        barcode_to_hist[bc] = hist
# Filter RNA rows for ParticipantBarcode in barcode_to_hist
rows = []
for rec in rna:
    pb = rec.get('ParticipantBarcode')
    if not pb:
        continue
    if pb in barcode_to_hist:
        nc = rec.get('normalized_count')
        try:
            val = float(nc)
        except Exception:
            continue
        # only include valid values (non-null, numeric)
        rows.append({'ParticipantBarcode': pb, 'normalized_count': val, 'histological_type': barcode_to_hist[pb]})
# if no rows, return empty
if len(rows)==0:
    result = {}
else:
    df = pd.DataFrame(rows)
    import numpy as np
    df['log10_expr'] = np.log10(df['normalized_count'] + 1)
    grouped = df.groupby('histological_type', sort=True)['log10_expr'].mean()
    # format to at least 4 decimal places
    result = {str(idx): float(f"{val:.4f}") for idx, val in grouped.items()}
# print result JSON
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1AGrZJVRb5MPbR4fZbpsCYJl': ['clinical_info'], 'var_call_ufgMFB1pA6yk7UW0qysCsJm4': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_ryBuUe9GPgTRL4T7LwuhZ6KU': 'file_storage/call_ryBuUe9GPgTRL4T7LwuhZ6KU.json', 'var_call_r4zzgFNGoWjCmx5GCPm5pPQv': {'keys': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'tumor_tissue_site_unique_sample': ['Brain', 'Omentum', 'Ovary', 'Peritoneum ovary'], 'patient_description_matches_sample': []}, 'var_call_pJLMKzKim29jGciJRTMSvSg4': 'file_storage/call_pJLMKzKim29jGciJRTMSvSg4.json', 'var_call_G9VFYpLZ3ET752f9v2CLIAA1': 'file_storage/call_G9VFYpLZ3ET752f9v2CLIAA1.json', 'var_call_aADFBH3XvqbfnZdpSFna8KDo': [{'histological_type': 'Glioblastoma Multiforme (GBM)'}, {'histological_type': 'Treated primary GBM'}, {'histological_type': 'Untreated primary (de novo) GBM'}], 'var_call_CS4fYvPOU9g5CSY0GLYYQYze': [], 'var_call_S7BCQdsdew0EjltJNPKp5PUb': 'file_storage/call_S7BCQdsdew0EjltJNPKp5PUb.json'}

exec(code, env_args)
