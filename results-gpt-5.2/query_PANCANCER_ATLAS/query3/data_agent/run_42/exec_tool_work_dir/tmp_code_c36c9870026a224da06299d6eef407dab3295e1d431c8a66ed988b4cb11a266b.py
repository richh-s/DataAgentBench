code = """import json, re, pandas as pd
# load clinical records
path = var_call_WISY6FEdNFyV2mlpdtq2kkle
with open(path,'r') as f:
    clin = json.load(f)
df_clin = pd.DataFrame(clin)
# extract TCGA barcode from Patient_description
pat = re.compile(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})')
df_clin['participant_barcode'] = df_clin['Patient_description'].str.extract(pat, expand=False)
df_clin = df_clin.dropna(subset=['participant_barcode','histological_type'])
# load PASS CDH1 mutated participants
path_pass = var_call_igX7XOu4gv6T3bDbZixT3XER
with open(path_pass,'r') as f:
    mut_pass = json.load(f)
set_pass = set([r['participant_barcode'] for r in mut_pass])
# create mutation status for each clinical participant
# If multiple entries per participant in clinical, keep unique participants with hist type
# Some participants may have multiple rows; choose first histological_type
pt = df_clin[['participant_barcode','histological_type']].drop_duplicates('participant_barcode')
pt['CDH1_mut_PASS'] = pt['participant_barcode'].isin(set_pass).astype(int)
# contingency table
ct = pd.crosstab(pt['histological_type'], pt['CDH1_mut_PASS'])
# ensure both columns 0 and 1 exist
for c in [0,1]:
    if c not in ct.columns:
        ct[c]=0
ct = ct[[0,1]]
# filter out categories with row totals <=10
row_totals = ct.sum(axis=1)
ct_f = ct.loc[row_totals>10].copy()
# recompute col totals, grand total after filtering
col_tot = ct_f.sum(axis=0)
grand = col_tot.sum()
# exclude if any column total <=10 (marginal totals)
if (col_tot<=10).any() or grand==0 or ct_f.shape[0]==0:
    out = {'error':'Insufficient data after filtering marginal totals <=10','row_count':int(ct_f.shape[0]),'col_totals':{str(k):int(v) for k,v in col_tot.items()},'grand_total':int(grand)}
else:
    expected = pd.DataFrame(index=ct_f.index, columns=ct_f.columns, dtype=float)
    for r in ct_f.index:
        for c in ct_f.columns:
            expected.loc[r,c] = (ct_f.loc[r].sum()*col_tot[c])/grand
    chi2 = float((((ct_f-expected)**2)/expected).to_numpy().sum())
    dof = int((ct_f.shape[0]-1)*(ct_f.shape[1]-1))
    out = {
        'chi_square': chi2,
        'dof': dof,
        'grand_total': int(grand),
        'col_totals': {('CDH1_mut_PASS=0' if k==0 else 'CDH1_mut_PASS=1'): int(v) for k,v in col_tot.items()},
        'rows_used': int(ct_f.shape[0]),
        'contingency_table': {idx:{'no_mut':int(ct_f.loc[idx,0]),'mut':int(ct_f.loc[idx,1]),'row_total':int(ct_f.loc[idx].sum())} for idx in ct_f.index}
    }
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_igX7XOu4gv6T3bDbZixT3XER': 'file_storage/call_igX7XOu4gv6T3bDbZixT3XER.json', 'var_call_u2QUg0S9VZqAYAzk0XPbIxc3': 'file_storage/call_u2QUg0S9VZqAYAzk0XPbIxc3.json', 'var_call_CStvx11bUC6NySCOS6UdvpX8': [{'FILTER': 'PASS', 'n': '261'}, {'FILTER': 'wga', 'n': '38'}, {'FILTER': 'oxog', 'n': '6'}, {'FILTER': 'filterr', 'n': '5'}, {'FILTER': 'native_wga_mix', 'n': '4'}, {'FILTER': 'nonpreferredpair', 'n': '4'}], 'var_call_JhXzUKNuaBakE5aS2YW9BNp0': ['clinical_info'], 'var_call_JMCHzfssBoELlkGRbvREKO2c': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_lI39XfplxGw1RSyjl8BWTqld': ['Patient_description', 'days_to_birth', 'days_to_death', 'days_to_last_followup', 'days_to_initial_pathologic_diagnosis', 'age_at_initial_pathologic_diagnosis', 'icd_10', 'tissue_retrospective_collection_indicator', 'icd_o_3_histology', 'tissue_prospective_collection_indicator', 'history_of_neoadjuvant_treatment', 'icd_o_3_site', 'tumor_tissue_site', 'new_tumor_event_after_initial_treatment', 'radiation_therapy', 'race', 'prior_dx', 'ethnicity', 'informed_consent_verified', 'person_neoplasm_cancer_status', 'patient_id', 'year_of_initial_pathologic_diagnosis', 'histological_type', 'tissue_source_site', 'form_completion_date', 'pathologic_T', 'pathologic_M', 'clinical_M', 'pathologic_N', 'system_version', 'pathologic_stage', 'clinical_stage', 'clinical_T', 'clinical_N', 'extranodal_involvement', 'postoperative_rx_tx', 'primary_therapy_outcome_success', 'lymph_node_examined_count', 'primary_lymph_node_presentation_assessment', 'initial_pathologic_diagnosis_method', 'number_of_lymphnodes_positive_by_he', 'eastern_cancer_oncology_group', 'anatomic_neoplasm_subdivision', 'residual_tumor', 'histological_type_other', 'init_pathology_dx_method_other', 'karnofsky_performance_score', 'neoplasm_histologic_grade', 'height', 'weight', 'number_of_lymphnodes_positive_by_ihc', 'tobacco_smoking_history', 'number_pack_years_smoked', 'stopped_smoking_year', 'performance_status_scale_timing', 'laterality', 'targeted_molecular_therapy', 'year_of_tobacco_smoking_onset', 'anatomic_neoplasm_subdivision_other', 'patient_death_reason', 'tumor_tissue_site_other', 'menopause_status', 'margin_status', 'kras_gene_analysis_performed', 'venous_invasion', 'lymphatic_invasion', 'perineural_invasion_present', 'her2_immunohistochemistry_level_result', 'breast_carcinoma_progesterone_receptor_status', 'breast_carcinoma_surgical_procedure_name', 'breast_neoplasm_other_surgical_procedure_descriptive_text', 'axillary_lymph_node_stage_method_type', 'breast_carcinoma_estrogen_receptor_status', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi', 'lab_proc_her2_neu_immunohistochemistry_receptor_status', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type', 'additional_pharmaceutical_therapy', 'additional_radiation_therapy', 'lymphovascular_invasion_present', 'location_in_lung_parenchyma', 'pulmonary_function_test_performed', 'egfr_mutation_performed', 'diagnosis', 'eml4_alk_translocation_performed', 'days_to_new_tumor_event_after_initial_treatment', 'hemoglobin_result', 'serum_calcium_result', 'platelet_qualitative_result', 'number_of_lymphnodes_positive', 'white_cell_count_result', 'alcohol_history_documented', 'family_history_of_cancer', 'braf_gene_analysis_performed', 'city_of_procurement', 'surgical_approach', 'peritoneal_wash', 'total_pelv_lnr', 'total_aor_lnr', 'prior_glioma'], 'var_call_WISY6FEdNFyV2mlpdtq2kkle': 'file_storage/call_WISY6FEdNFyV2mlpdtq2kkle.json'}

exec(code, env_args)
