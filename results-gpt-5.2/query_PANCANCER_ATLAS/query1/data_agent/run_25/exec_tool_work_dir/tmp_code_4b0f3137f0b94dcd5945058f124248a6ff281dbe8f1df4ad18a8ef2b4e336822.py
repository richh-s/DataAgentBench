code = """import json, re, math, pandas as pd

def load_result(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

expr = load_result(var_call_QxKV8du6Xxxwv1l74PhiWd4q)
clin = load_result(var_call_ftQLWxZAE3qRaJAKpqbb77LJ)

def extract_barcode(s):
    if s is None:
        return None
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', str(s))
    return m.group(1) if m else None

expr_df = pd.DataFrame(expr)
expr_df['ParticipantBarcode'] = expr_df['ParticipantBarcode'].astype(str).map(lambda x: extract_barcode(x) or x)
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['ParticipantBarcode','normalized_count'])
expr_df = expr_df[expr_df['normalized_count'] >= 0]
expr_df['log10_expr'] = (expr_df['normalized_count'] + 1.0).map(lambda v: math.log10(v))

clin_df = pd.DataFrame(clin)
clin_df.columns = [c.lower() for c in clin_df.columns]
clin_df['barcode'] = clin_df['participantbarcode'].map(extract_barcode)
clin_df = clin_df.dropna(subset=['barcode','histology'])
clin_df['histology'] = clin_df['histology'].astype(str)
clin_df = clin_df[~clin_df['histology'].str.match(r'^\\s*\\[.*\\]\\s*$')]

merged = expr_df.merge(clin_df[['barcode','histology']], left_on='ParticipantBarcode', right_on='barcode', how='inner')
res = (merged.groupby('histology', as_index=False)
       .agg(n_patients=('ParticipantBarcode','nunique'), mean_log10_igf2=('log10_expr','mean'))
       .sort_values('histology'))

out_lines = []
for _, r in res.iterrows():
    out_lines.append(r['histology'] + ': ' + format(r['mean_log10_igf2'], '.4f'))
answer = '\\n'.join(out_lines)

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_QxKV8du6Xxxwv1l74PhiWd4q': 'file_storage/call_QxKV8du6Xxxwv1l74PhiWd4q.json', 'var_call_l8JX6ubRCAvmZe0cu1niFGVE': ['clinical_info'], 'var_call_8zdHwybkDuZ04Qeec777a0s1': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_TwmR1eZQ94y53xD48yNC1k9I': 'file_storage/call_TwmR1eZQ94y53xD48yNC1k9I.json', 'var_call_yNIgs3Pgm7Na9vtr6kf4v2UR': [], 'var_call_fFMV80d0nGWL2kyHOnZGq7Er': [{'diagnosis': 'Lung Adenocarcinoma'}, {'diagnosis': 'Lung Squamous Cell Carcinoma'}], 'var_call_lFBp2aUobJPHHICozLh694lA': 'file_storage/call_lFBp2aUobJPHHICozLh694lA.json', 'var_call_ftQLWxZAE3qRaJAKpqbb77LJ': 'file_storage/call_ftQLWxZAE3qRaJAKpqbb77LJ.json'}

exec(code, env_args)
