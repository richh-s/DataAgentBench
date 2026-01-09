code = """import json, re, math
import pandas as pd

# load clinical LGG histology
clin_src = var_call_vBjE5FkUTT2RTIfUF3v7KkOn
if isinstance(clin_src, str):
    with open(clin_src, 'r') as f:
        clin = json.load(f)
else:
    clin = clin_src

# parse TCGA barcode from Patient_description text
rows=[]
for r in clin:
    desc = r.get('participant_barcode')
    hist = r.get('histology')
    if not desc or not hist: 
        continue
    m = re.search(r'(TCGA-[A-Z0-9]{2}-[A-Z0-9]{4})', desc)
    if not m:
        continue
    rows.append({'participant_barcode': m.group(1), 'histology': hist})
clin_df = pd.DataFrame(rows).drop_duplicates(subset=['participant_barcode'])

# load expression IGF2
expr_src = var_call_hUjkgNfQ0KtKev86IDn248Z9
if isinstance(expr_src, str):
    with open(expr_src, 'r') as f:
        expr = json.load(f)
else:
    expr = expr_src
expr_df = pd.DataFrame(expr)
expr_df['normalized_count'] = pd.to_numeric(expr_df['normalized_count'], errors='coerce')
expr_df = expr_df.dropna(subset=['participant_barcode','normalized_count'])
# if multiple samples per participant, average log10(nc+1) per participant first
expr_df['log10_expr'] = (expr_df['normalized_count'] + 1.0).apply(lambda x: math.log10(x) if x> -1 else float('nan'))
expr_df = expr_df.dropna(subset=['log10_expr'])
per_pt = expr_df.groupby('participant_barcode', as_index=False)['log10_expr'].mean()

merged = clin_df.merge(per_pt, on='participant_barcode', how='inner')
res_df = merged.groupby('histology', as_index=False)['log10_expr'].mean().sort_values('histology')
res_df['avg_log10_igf2'] = res_df['log10_expr'].map(lambda v: f"{v:.4f}")
out = res_df[['histology','avg_log10_igf2']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_hUjkgNfQ0KtKev86IDn248Z9': 'file_storage/call_hUjkgNfQ0KtKev86IDn248Z9.json', 'var_call_AxIezdsdt3WuPh2yabqwyRrE': ['clinical_info'], 'var_call_4S3KFUjaRr5Mkr5MzQQkVSA6': [{'Patient_description': 'In the Ovarian serous cystadenocarcinoma dataset, patient TCGA-31-1953 (UUID 61feee94-3ac9-42fe-aaa3-dc6a3efe563c) is recorded as a FEMALE with vital status: Alive.', 'days_to_birth': '-19064.0', 'days_to_death': '[Not Applicable]', 'days_to_last_followup': '204.0', 'days_to_initial_pathologic_diagnosis': '0.0', 'age_at_initial_pathologic_diagnosis': '52.0', 'icd_10': 'C56.9', 'tissue_retrospective_collection_indicator': 'None', 'icd_o_3_histology': '8441/3', 'tissue_prospective_collection_indicator': 'None', 'history_of_neoadjuvant_treatment': 'No', 'icd_o_3_site': 'C56.9', 'tumor_tissue_site': 'Ovary', 'new_tumor_event_after_initial_treatment': 'None', 'radiation_therapy': 'NO', 'race': 'ASIAN', 'prior_dx': 'None', 'ethnicity': 'NOT HISPANIC OR LATINO', 'informed_consent_verified': 'YES', 'person_neoplasm_cancer_status': 'WITH TUMOR', 'patient_id': '1953', 'year_of_initial_pathologic_diagnosis': '2008.0', 'histological_type': 'Serous Cystadenocarcinoma', 'tissue_source_site': '31', 'form_completion_date': '2009-10-20', 'pathologic_T': '[Not Applicable]', 'pathologic_M': '[Not Applicable]', 'clinical_M': '[Not Applicable]', 'pathologic_N': '[Not Applicable]', 'system_version': 'None', 'pathologic_stage': '[Not Applicable]', 'clinical_stage': 'Stage IIIC', 'clinical_T': '[Not Applicable]', 'clinical_N': '[Not Applicable]', 'extranodal_involvement': '[Not Applicable]', 'postoperative_rx_tx': 'None', 'primary_therapy_outcome_success': 'None', 'lymph_node_examined_count': 'None', 'primary_lymph_node_presentation_assessment': 'None', 'initial_pathologic_diagnosis_method': 'Tumor resection', 'number_of_lymphnodes_positive_by_he': 'None', 'eastern_cancer_oncology_group': '1', 'anatomic_neoplasm_subdivision': 'Bilateral', 'residual_tumor': 'None', 'histological_type_other': 'None', 'init_pathology_dx_method_other': '[Not Applicable]', 'karnofsky_performance_score': 'None', 'neoplasm_histologic_grade': 'G3', 'height': 'None', 'weight': 'None', 'number_of_lymphnodes_positive_by_ihc': 'None', 'tobacco_smoking_history': 'None', 'number_pack_years_smoked': 'None', 'stopped_smoking_year': 'None', 'performance_status_scale_timing': 'Pre-Adjuvant Therapy', 'laterality': 'None', 'targeted_molecular_therapy': 'None', 'year_of_tobacco_smoking_onset': 'None', 'anatomic_neoplasm_subdivision_other': 'None', 'patient_death_reason': 'None', 'tumor_tissue_site_other': 'None', 'menopause_status': 'None', 'margin_status': 'None', 'kras_gene_analysis_performed': 'None', 'venous_invasion': 'NO', 'lymphatic_invasion': 'NO', 'perineural_invasion_present': 'None', 'her2_immunohistochemistry_level_result': 'None', 'breast_carcinoma_progesterone_receptor_status': 'None', 'breast_carcinoma_surgical_procedure_name': 'None', 'breast_neoplasm_other_surgical_procedure_descriptive_text': 'None', 'axillary_lymph_node_stage_method_type': 'None', 'breast_carcinoma_estrogen_receptor_status': 'None', 'cytokeratin_immunohistochemistry_staining_method_micrometastasi': 'None', 'lab_proc_her2_neu_immunohistochemistry_receptor_status': 'None', 'lab_procedure_her2_neu_in_situ_hybrid_outcome_type': 'None', 'additional_pharmaceutical_therapy': 'None', 'additional_radiation_therapy': 'None', 'lymphovascular_invasion_present': 'None', 'location_in_lung_parenchyma': 'None', 'pulmonary_function_test_performed': 'None', 'egfr_mutation_performed': 'None', 'diagnosis': 'None', 'eml4_alk_translocation_performed': 'None', 'days_to_new_tumor_event_after_initial_treatment': 'None', 'hemoglobin_result': 'None', 'serum_calcium_result': 'None', 'platelet_qualitative_result': 'None', 'number_of_lymphnodes_positive': 'None', 'white_cell_count_result': 'None', 'alcohol_history_documented': 'None', 'family_history_of_cancer': 'None', 'braf_gene_analysis_performed': 'None', 'city_of_procurement': 'None', 'surgical_approach': 'None', 'peritoneal_wash': 'None', 'total_pelv_lnr': 'None', 'total_aor_lnr': 'None', 'prior_glioma': 'None'}], 'var_call_zfR1QHWMMfpn0iK3QiMU8t24': {'n_cols': 99, 'candidate_columns': ['person_neoplasm_cancer_status', 'eastern_cancer_oncology_group', 'family_history_of_cancer']}, 'var_call_lFGlotw9v54Wrkc3IKcpy5uF': [{'histology': 'Infiltrating Ductal Carcinoma', 'n': '777'}, {'histology': 'Serous Cystadenocarcinoma', 'n': '584'}, {'histology': 'Untreated primary (de novo) GBM', 'n': '539'}, {'histology': 'Kidney Clear Cell Renal Carcinoma', 'n': '518'}, {'histology': 'Head and Neck Squamous Cell Carcinoma', 'n': '512'}, {'histology': 'Prostate Adenocarcinoma Acinar Type', 'n': '480'}, {'histology': 'Lung Squamous Cell Carcinoma- Not Otherwise Specified (NOS)', 'n': '470'}, {'histology': 'Muscle invasive urothelial carcinoma (pT2 or above)', 'n': '409'}, {'histology': 'Endometrioid endometrial adenocarcinoma', 'n': '401'}, {'histology': 'Colon Adenocarcinoma', 'n': '378'}, {'histology': 'Hepatocellular Carcinoma', 'n': '364'}, {'histology': 'Thyroid Papillary Carcinoma - Classical/usual', 'n': '356'}, {'histology': 'Lung Adenocarcinoma- Not Otherwise Specified (NOS)', 'n': '320'}, {'histology': 'Kidney Papillary Renal Cell Carcinoma', 'n': '286'}, {'histology': 'Cervical Squamous Cell Carcinoma', 'n': '254'}, {'histology': 'Infiltrating Lobular Carcinoma', 'n': '201'}, {'histology': 'Astrocytoma', 'n': '194'}, {'histology': 'Oligodendroglioma', 'n': '189'}, {'histology': 'Stomach  Adenocarcinoma  Not Otherwise Specified (NOS)', 'n': '162'}, {'histology': 'Pancreas-Adenocarcinoma Ductal Type', 'n': '153'}, {'histology': 'Pheochromocytoma', 'n': '147'}, {'histology': 'Rectal Adenocarcinoma', 'n': '140'}, {'histology': 'Oligoastrocytoma', 'n': '130'}, {'histology': 'Serous endometrial adenocarcinoma', 'n': '109'}, {'histology': 'Lung Adenocarcinoma Mixed Subtype', 'n': '107'}, {'histology': 'Thyroid Papillary Carcinoma - Follicular (>= 99% follicular patterned)', 'n': '102'}, {'histology': 'Leiomyosarcoma (LMS)', 'n': '101'}, {'histology': 'Esophagus Squamous Cell Carcinoma', 'n': '95'}, {'histology': 'Esophagus Adenocarcinoma  NOS', 'n': '88'}, {'histology': 'Adrenocortical carcinoma- Usual Type', 'n': '86'}], 'var_call_vBjE5FkUTT2RTIfUF3v7KkOn': 'file_storage/call_vBjE5FkUTT2RTIfUF3v7KkOn.json'}

exec(code, env_args)
