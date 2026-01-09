code = """import json, pandas as pd

# Load CDH1-mutated participant list (may be file)
cdh1_src = var_call_Rj74yJxrRN7Ng6AlK69cfZTv
if isinstance(cdh1_src, str):
    with open(cdh1_src, 'r') as f:
        cdh1 = json.load(f)
else:
    cdh1 = cdh1_src

# Alive BRCA query returned only 1 row due to mismatched join key; need to parse barcode from Patient_description.
clin = var_call_iuNgUoKlebh5T4hzQ5HI5No9

cdh1_set = set([r['ParticipantBarcode'] for r in cdh1 if 'ParticipantBarcode' in r and r['ParticipantBarcode'] is not None])

# parse TCGA barcode pattern from participantbarcode field
import re
rows=[]
for r in clin:
    desc = r.get('participantbarcode') or r.get('ParticipantBarcode')
    hist = r.get('histological_type')
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc or '')
    bc = m.group(1) if m else None
    rows.append({'ParticipantBarcode': bc, 'histological_type': hist})

cdf = pd.DataFrame(rows)
if cdf.empty:
    out = []
else:
    cdf['is_cdh1_mut'] = cdf['ParticipantBarcode'].isin(cdh1_set)
    g = cdf.groupby('histological_type', dropna=False).agg(total_alive=('ParticipantBarcode','size'), cdh1_mut=('is_cdh1_mut','sum')).reset_index()
    g['pct_cdh1_mut'] = (g['cdh1_mut'] / g['total_alive'] * 100).round(2)
    g = g.sort_values(['pct_cdh1_mut','cdh1_mut','total_alive'], ascending=[False,False,False]).head(3)
    out = g.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Rj74yJxrRN7Ng6AlK69cfZTv': 'file_storage/call_Rj74yJxrRN7Ng6AlK69cfZTv.json', 'var_call_4axayB3cJepkPao27k2Wj4Kf': ['clinical_info'], 'var_call_EVoMIMxcC8aCHysOUw97BCVc': [{'column_name': 'Patient_description'}, {'column_name': 'days_to_birth'}, {'column_name': 'days_to_death'}, {'column_name': 'days_to_last_followup'}, {'column_name': 'days_to_initial_pathologic_diagnosis'}, {'column_name': 'age_at_initial_pathologic_diagnosis'}, {'column_name': 'icd_10'}, {'column_name': 'tissue_retrospective_collection_indicator'}, {'column_name': 'icd_o_3_histology'}, {'column_name': 'tissue_prospective_collection_indicator'}, {'column_name': 'history_of_neoadjuvant_treatment'}, {'column_name': 'icd_o_3_site'}, {'column_name': 'tumor_tissue_site'}, {'column_name': 'new_tumor_event_after_initial_treatment'}, {'column_name': 'radiation_therapy'}, {'column_name': 'race'}, {'column_name': 'prior_dx'}, {'column_name': 'ethnicity'}, {'column_name': 'informed_consent_verified'}, {'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'patient_id'}, {'column_name': 'year_of_initial_pathologic_diagnosis'}, {'column_name': 'histological_type'}, {'column_name': 'tissue_source_site'}, {'column_name': 'form_completion_date'}, {'column_name': 'pathologic_T'}, {'column_name': 'pathologic_M'}, {'column_name': 'clinical_M'}, {'column_name': 'pathologic_N'}, {'column_name': 'system_version'}, {'column_name': 'pathologic_stage'}, {'column_name': 'clinical_stage'}, {'column_name': 'clinical_T'}, {'column_name': 'clinical_N'}, {'column_name': 'extranodal_involvement'}, {'column_name': 'postoperative_rx_tx'}, {'column_name': 'primary_therapy_outcome_success'}, {'column_name': 'lymph_node_examined_count'}, {'column_name': 'primary_lymph_node_presentation_assessment'}, {'column_name': 'initial_pathologic_diagnosis_method'}, {'column_name': 'number_of_lymphnodes_positive_by_he'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'anatomic_neoplasm_subdivision'}, {'column_name': 'residual_tumor'}, {'column_name': 'histological_type_other'}, {'column_name': 'init_pathology_dx_method_other'}, {'column_name': 'karnofsky_performance_score'}, {'column_name': 'neoplasm_histologic_grade'}, {'column_name': 'height'}, {'column_name': 'weight'}, {'column_name': 'number_of_lymphnodes_positive_by_ihc'}, {'column_name': 'tobacco_smoking_history'}, {'column_name': 'number_pack_years_smoked'}, {'column_name': 'stopped_smoking_year'}, {'column_name': 'performance_status_scale_timing'}, {'column_name': 'laterality'}, {'column_name': 'targeted_molecular_therapy'}, {'column_name': 'year_of_tobacco_smoking_onset'}, {'column_name': 'anatomic_neoplasm_subdivision_other'}, {'column_name': 'patient_death_reason'}, {'column_name': 'tumor_tissue_site_other'}, {'column_name': 'menopause_status'}, {'column_name': 'margin_status'}, {'column_name': 'kras_gene_analysis_performed'}, {'column_name': 'venous_invasion'}, {'column_name': 'lymphatic_invasion'}, {'column_name': 'perineural_invasion_present'}, {'column_name': 'her2_immunohistochemistry_level_result'}, {'column_name': 'breast_carcinoma_progesterone_receptor_status'}, {'column_name': 'breast_carcinoma_surgical_procedure_name'}, {'column_name': 'breast_neoplasm_other_surgical_procedure_descriptive_text'}, {'column_name': 'axillary_lymph_node_stage_method_type'}, {'column_name': 'breast_carcinoma_estrogen_receptor_status'}, {'column_name': 'cytokeratin_immunohistochemistry_staining_method_micrometastasi'}, {'column_name': 'lab_proc_her2_neu_immunohistochemistry_receptor_status'}, {'column_name': 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type'}, {'column_name': 'additional_pharmaceutical_therapy'}, {'column_name': 'additional_radiation_therapy'}, {'column_name': 'lymphovascular_invasion_present'}, {'column_name': 'location_in_lung_parenchyma'}, {'column_name': 'pulmonary_function_test_performed'}, {'column_name': 'egfr_mutation_performed'}, {'column_name': 'diagnosis'}, {'column_name': 'eml4_alk_translocation_performed'}, {'column_name': 'days_to_new_tumor_event_after_initial_treatment'}, {'column_name': 'hemoglobin_result'}, {'column_name': 'serum_calcium_result'}, {'column_name': 'platelet_qualitative_result'}, {'column_name': 'number_of_lymphnodes_positive'}, {'column_name': 'white_cell_count_result'}, {'column_name': 'alcohol_history_documented'}, {'column_name': 'family_history_of_cancer'}, {'column_name': 'braf_gene_analysis_performed'}, {'column_name': 'city_of_procurement'}, {'column_name': 'surgical_approach'}, {'column_name': 'peritoneal_wash'}, {'column_name': 'total_pelv_lnr'}, {'column_name': 'total_aor_lnr'}, {'column_name': 'prior_glioma'}], 'var_call_YJm1yGbyHW0fpVsLVZ6BfoGI': [], 'var_call_dcUwf8tuWwawZNuyKS0u0pp9': [{'column_name': 'person_neoplasm_cancer_status'}, {'column_name': 'eastern_cancer_oncology_group'}, {'column_name': 'family_history_of_cancer'}], 'var_call_p0sgrca5vbMU7V70JRpfkafn': [], 'var_call_BDNZxEM0oAFOianZyQ90Tblp': [{'tumor_tissue_site': 'Breast', 'n': '1087'}, {'tumor_tissue_site': 'Lung', 'n': '1004'}, {'tumor_tissue_site': 'Kidney', 'n': '869'}, {'tumor_tissue_site': 'Brain', 'n': '590'}, {'tumor_tissue_site': 'Ovary', 'n': '579'}, {'tumor_tissue_site': 'Head and Neck', 'n': '560'}, {'tumor_tissue_site': 'Endometrial', 'n': '530'}, {'tumor_tissue_site': 'Central nervous system', 'n': '513'}, {'tumor_tissue_site': 'Thyroid', 'n': '503'}, {'tumor_tissue_site': 'Prostate', 'n': '495'}, {'tumor_tissue_site': 'Colon', 'n': '442'}, {'tumor_tissue_site': 'Stomach', 'n': '440'}, {'tumor_tissue_site': 'Bladder', 'n': '412'}, {'tumor_tissue_site': 'Liver', 'n': '374'}, {'tumor_tissue_site': 'Cervical', 'n': '306'}, {'tumor_tissue_site': 'Extremities', 'n': '193'}, {'tumor_tissue_site': 'Pancreas', 'n': '184'}, {'tumor_tissue_site': 'Esophagus', 'n': '183'}, {'tumor_tissue_site': 'Trunk', 'n': '169'}, {'tumor_tissue_site': 'Rectum', 'n': '156'}], 'var_call_iuNgUoKlebh5T4hzQ5HI5No9': [{'participantbarcode': 'Case 57a1604c-60b7-4b30-a75e-f70939532c5c, linked to barcode TCGA-BH-A0B2, corresponds to a FEMALE patient diagnosed with Breast invasive carcinoma, with vital status Alive.', 'histological_type': 'Infiltrating Ductal Carcinoma'}]}

exec(code, env_args)
