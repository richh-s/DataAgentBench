code = """import json, re, pandas as pd

# load clinical BRCA-like (breast site C50.9)
path = var_call_BnGXrCIwwtTpFqP8fogzsl8D
with open(path, 'r') as f:
    clin = json.load(f)

df = pd.DataFrame(clin)
# extract TCGA barcode from Patient_description text
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
df['ParticipantBarcode'] = df['participantbarcode'].apply(lambda x: pat.search(x).group(1) if isinstance(x,str) and pat.search(x) else None)
# alive if days_to_death is Not Applicable or null
alive_vals = {'[Not Applicable]', 'Not Applicable', 'NA', 'N/A', ''}
df['alive'] = df['days_to_death'].isna() | df['days_to_death'].isin(list(alive_vals))
# keep alive only and valid histology and barcode
alive_df = df[df['alive'] & df['ParticipantBarcode'].notna()].copy()

# load CDH1 mutated participants
mut_path = var_call_3Qd5kkKb2K17u50xUcfPBfJn
with open(mut_path, 'r') as f:
    muts = json.load(f)
mut_set = set([r['ParticipantBarcode'] for r in muts if r.get('ParticipantBarcode')])

alive_df['CDH1_mut'] = alive_df['ParticipantBarcode'].isin(mut_set)

# group by histological_type
agg = alive_df.groupby('histological_type').agg(
    alive_n=('ParticipantBarcode','nunique'),
    mutated_n=('CDH1_mut', lambda s: int(s.sum()))
).reset_index()
agg['pct_mutated'] = (agg['mutated_n'] / agg['alive_n'] * 100).round(2)

# require at least 5 alive patients to avoid tiny denominators
agg_filt = agg[agg['alive_n']>=5].sort_values(['pct_mutated','mutated_n','alive_n'], ascending=[False,False,False]).head(3)

result = agg_filt.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3Qd5kkKb2K17u50xUcfPBfJn': 'file_storage/call_3Qd5kkKb2K17u50xUcfPBfJn.json', 'var_call_Qx2ubRYcgfQZToAuwdRu7PVx': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_BkJQkreeDReuDWo2ToI4O3Q5': [], 'var_call_iKI7uhLNmshgm04EKyF2D3FA': [{'diagnosis': 'None', 'n': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'n': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'n': '490'}], 'var_call_qL3gtq9ysEiHMP66z7vS12fk': [{'site': 'C50.9', 'n': '1079'}, {'site': 'C64.9', 'n': '871'}, {'site': 'C71.9', 'n': '646'}, {'site': 'C56.9', 'n': '579'}, {'site': 'C34.1', 'n': '553'}, {'site': 'C54.1', 'n': '551'}, {'site': 'C73.9', 'n': '505'}, {'site': 'C61.9', 'n': '495'}, {'site': 'C71.0', 'n': '437'}, {'site': 'C22.0', 'n': '376'}, {'site': 'C34.3', 'n': '351'}, {'site': 'C53.9', 'n': '300'}, {'site': 'C67.9', 'n': '237'}, {'site': 'C16.3', 'n': '156'}, {'site': 'C74.9', 'n': '145'}, {'site': 'C25.0', 'n': '140'}, {'site': 'C62.9', 'n': '134'}, {'site': 'C02.9', 'n': '129'}, {'site': 'C15.5', 'n': '122'}, {'site': 'C32.9', 'n': '118'}, {'site': 'C48.0', 'n': '116'}, {'site': 'C16.0', 'n': '112'}, {'site': 'C18.7', 'n': '107'}, {'site': 'C18.2', 'n': '102'}, {'site': 'C16.2', 'n': '101'}, {'site': 'C18.9', 'n': '100'}, {'site': 'C77.3', 'n': '96'}, {'site': 'C74.0', 'n': '93'}, {'site': 'C38.4', 'n': '86'}, {'site': 'C37.9', 'n': '85'}], 'var_call_BnGXrCIwwtTpFqP8fogzsl8D': 'file_storage/call_BnGXrCIwwtTpFqP8fogzsl8D.json'}

exec(code, env_args)
