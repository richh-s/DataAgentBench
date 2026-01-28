code = """import json, re, math, pandas as pd

# load IGF2 expression rows (may be file path)
expr_src = var_call_ijsDuJxhIegoCRa7iXl1iTdF
if isinstance(expr_src, str):
    with open(expr_src, 'r') as f:
        expr_rows = json.load(f)
else:
    expr_rows = expr_src

clin_src = var_call_jI9NoidynSASmV5xhM81cfEl
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin_rows = json.load(f)
else:
    clin_rows = clin_src

# parse TCGA barcode from Patient_description text
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
parsed = []
for r in clin_rows:
    desc = r.get('participantbarcode') or r.get('ParticipantBarcode')
    hist = r.get('histology')
    if not desc or not hist:
        continue
    m = pat.search(desc)
    if not m:
        continue
    barcode = m.group(1)
    parsed.append({'ParticipantBarcode': barcode, 'histology': hist})

clin_df = pd.DataFrame(parsed).drop_duplicates(subset=['ParticipantBarcode'])
expr_df = pd.DataFrame(expr_rows)
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['normalized_count'])

merged = clin_df.merge(expr_df, on='ParticipantBarcode', how='inner')
# compute log10(normalized_count+1)
merged['log10_expr'] = (merged['normalized_count'] + 1).apply(lambda x: math.log10(x))

res = (merged.groupby('histology', as_index=False)
       .agg(avg_log10_igf2=('log10_expr','mean'), n=('log10_expr','size'))
       .sort_values('histology'))

# format with 4 decimals
out_lines = []
for _, row in res.iterrows():
    out_lines.append(f"{row['histology']}\t{row['avg_log10_igf2']:.4f}")
answer = "Histology\tAvg_log10(IGF2_normalized_count+1)\n" + "\n".join(out_lines)

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_ijsDuJxhIegoCRa7iXl1iTdF': 'file_storage/call_ijsDuJxhIegoCRa7iXl1iTdF.json', 'var_call_RJphhRS9T5wf7ucV9vcrq8qm': ['clinical_info'], 'var_call_vHXeFpF42IwDNvsEMCSJK7Ne': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_RRZuLSmm4HWhBZqvcjfSpHFa': [], 'var_call_S10Z296xcbLFLlfDXNhG3W3V': [{'diagnosis': 'None', 'n': '9757'}, {'diagnosis': 'Lung Adenocarcinoma', 'n': '514'}, {'diagnosis': 'Lung Squamous Cell Carcinoma', 'n': '490'}], 'var_call_wMHDNTv8SCKve2lG7JJCdChf': [{'tumor_tissue_site': 'Breast', 'n': '1087'}, {'tumor_tissue_site': 'Lung', 'n': '1004'}, {'tumor_tissue_site': 'Kidney', 'n': '869'}, {'tumor_tissue_site': 'Brain', 'n': '590'}, {'tumor_tissue_site': 'Ovary', 'n': '579'}, {'tumor_tissue_site': 'Head and Neck', 'n': '560'}, {'tumor_tissue_site': 'Endometrial', 'n': '530'}, {'tumor_tissue_site': 'Central nervous system', 'n': '513'}, {'tumor_tissue_site': 'Thyroid', 'n': '503'}, {'tumor_tissue_site': 'Prostate', 'n': '495'}, {'tumor_tissue_site': 'Colon', 'n': '442'}, {'tumor_tissue_site': 'Stomach', 'n': '440'}, {'tumor_tissue_site': 'Bladder', 'n': '412'}, {'tumor_tissue_site': 'Liver', 'n': '374'}, {'tumor_tissue_site': 'Cervical', 'n': '306'}, {'tumor_tissue_site': 'Extremities', 'n': '193'}, {'tumor_tissue_site': 'Pancreas', 'n': '184'}, {'tumor_tissue_site': 'Esophagus', 'n': '183'}, {'tumor_tissue_site': 'Trunk', 'n': '169'}, {'tumor_tissue_site': 'Rectum', 'n': '156'}, {'tumor_tissue_site': 'Adrenal gland', 'n': '146'}, {'tumor_tissue_site': 'Testes', 'n': '133'}, {'tumor_tissue_site': 'None', 'n': '100'}, {'tumor_tissue_site': 'Thymus', 'n': '97'}, {'tumor_tissue_site': 'Adrenal', 'n': '91'}, {'tumor_tissue_site': 'Pleura', 'n': '87'}, {'tumor_tissue_site': 'Retroperitoneum/Upper abdominal - Retroperitoneum', 'n': '69'}, {'tumor_tissue_site': 'Uterus', 'n': '57'}, {'tumor_tissue_site': 'Choroid', 'n': '56'}, {'tumor_tissue_site': 'Lower Extremity - Thigh/knee', 'n': '44'}], 'var_call_Qhyz68LC3c912B3OyPQiiHaK': [{'icd_o_3_site': 'C50.9', 'n': '1079'}, {'icd_o_3_site': 'C64.9', 'n': '871'}, {'icd_o_3_site': 'C71.9', 'n': '646'}, {'icd_o_3_site': 'C56.9', 'n': '579'}, {'icd_o_3_site': 'C34.1', 'n': '553'}, {'icd_o_3_site': 'C54.1', 'n': '551'}, {'icd_o_3_site': 'C73.9', 'n': '505'}, {'icd_o_3_site': 'C61.9', 'n': '495'}, {'icd_o_3_site': 'C71.0', 'n': '437'}, {'icd_o_3_site': 'C22.0', 'n': '376'}, {'icd_o_3_site': 'C34.3', 'n': '351'}, {'icd_o_3_site': 'C53.9', 'n': '300'}, {'icd_o_3_site': 'C67.9', 'n': '237'}, {'icd_o_3_site': 'C16.3', 'n': '156'}, {'icd_o_3_site': 'C74.9', 'n': '145'}, {'icd_o_3_site': 'C25.0', 'n': '140'}, {'icd_o_3_site': 'C62.9', 'n': '134'}, {'icd_o_3_site': 'C02.9', 'n': '129'}, {'icd_o_3_site': 'C15.5', 'n': '122'}, {'icd_o_3_site': 'C32.9', 'n': '118'}, {'icd_o_3_site': 'C48.0', 'n': '116'}, {'icd_o_3_site': 'C16.0', 'n': '112'}, {'icd_o_3_site': 'C18.7', 'n': '107'}, {'icd_o_3_site': 'C18.2', 'n': '102'}, {'icd_o_3_site': 'C16.2', 'n': '101'}, {'icd_o_3_site': 'C18.9', 'n': '100'}, {'icd_o_3_site': 'C77.3', 'n': '96'}, {'icd_o_3_site': 'C74.0', 'n': '93'}, {'icd_o_3_site': 'C38.4', 'n': '86'}, {'icd_o_3_site': 'C37.9', 'n': '85'}], 'var_call_qhA3oMGzRE13N2K0iXHpnlLI': [{'icd_o_3_histology': '8140/3', 'n': '1381'}, {'icd_o_3_histology': '8070/3', 'n': '1162'}, {'icd_o_3_histology': '8500/3', 'n': '929'}, {'icd_o_3_histology': '8441/3', 'n': '697'}, {'icd_o_3_histology': '8260/3', 'n': '669'}, {'icd_o_3_histology': '9440/3', 'n': '590'}, {'icd_o_3_histology': '8310/3', 'n': '509'}, {'icd_o_3_histology': '8720/3', 'n': '421'}, {'icd_o_3_histology': '8380/3', 'n': '402'}, {'icd_o_3_histology': '8170/3', 'n': '357'}, {'icd_o_3_histology': '8120/3', 'n': '341'}, {'icd_o_3_histology': '8550/3', 'n': '216'}, {'icd_o_3_histology': '8520/3', 'n': '199'}, {'icd_o_3_histology': '8480/3', 'n': '136'}, {'icd_o_3_histology': '9382/3', 'n': '131'}, {'icd_o_3_histology': '9401/3', 'n': '130'}, {'icd_o_3_histology': '8255/3', 'n': '117'}, {'icd_o_3_histology': '9450/3', 'n': '111'}, {'icd_o_3_histology': '8700/0', 'n': '110'}, {'icd_o_3_histology': '8340/3', 'n': '106'}, {'icd_o_3_histology': '8071/3', 'n': '105'}, {'icd_o_3_histology': '8890/3', 'n': '97'}, {'icd_o_3_histology': '8144/3', 'n': '87'}, {'icd_o_3_histology': '8370/3', 'n': '86'}, {'icd_o_3_histology': '8211/3', 'n': '83'}, {'icd_o_3_histology': '9451/3', 'n': '77'}, {'icd_o_3_histology': '8145/3', 'n': '68'}, {'icd_o_3_histology': '8130/3', 'n': '68'}, {'icd_o_3_histology': '9061/3', 'n': '65'}, {'icd_o_3_histology': '8072/3', 'n': '65'}], 'var_call_wRHJHUThCvY61gfE5dhSa659': 'file_storage/call_wRHJHUThCvY61gfE5dhSa659.json', 'var_call_jI9NoidynSASmV5xhM81cfEl': 'file_storage/call_jI9NoidynSASmV5xhM81cfEl.json'}

exec(code, env_args)
